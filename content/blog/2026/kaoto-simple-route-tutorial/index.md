---
title: "Build an HTTP-to-Kafka Route with Kaoto"
date: 2026-06-10
authors: ["pvinaches"]
categories: ["Tooling", "Tutorial"]
keywords: ["apache camel", "kaoto", "kafka", "content-based router", "camel jbang", "visual designer"]
preview: "Use Kaoto's visual designer to build a Camel route that receives JSON over HTTP, routes messages by content, and publishes results to Kafka — without writing YAML by hand."
---

Most Camel tutorials start with a text editor. This one starts with a canvas.

**Kaoto** is a visual designer for Apache Camel that lets you drag, drop, and configure routes without touching a YAML file directly. You still get the full power of Camel under the hood but building it differently.

In this tutorial you will wire together an HTTP endpoint, a JSON deserializer, a content-based router, and a Kafka producer. Then, the integration runs with Camel JBang through the Kaoto extension. No need to add a Maven project nor a framework setup.

## Prerequisites

- **Visual Studio Code** with the [Kaoto extension](https://kaoto.io/docs/installation/) installed
- **Apache Camel JBang** — `jbang app install camel@apache/camel`
- A running **Kafka** broker — the quickest way is `camel infra run kafka`

## Project Setup

Create a new folder and open it in VSCode:

```bash
mkdir http-kafka-route
cd http-kafka-route
```

Create an `application-dev.properties` file with your Kafka connection details:

```properties
kafka.bootstrap.servers=localhost:9092
kafka.topic=my-topic
kafka.client.id=camel-route-client
```

## Step 1: Create a New Route

1. Open VSCode and navigate to your `http-kafka-route` folder
2. Click the **Kaoto** icon in the left sidebar
3. Click the **Camel File...** button to create a new integration
4. In the dialog, select **Camel Route** as the file type, **YAML** as the DSL, and name the file `my-route`
5. Select **Camel Main 4.20.0** from the version selector at the top of the designer

A new route appears with a default timer component, a SetBody step, and a Log processor.

## Step 2: Expose an HTTP Endpoint

The route should wake up when an HTTP request arrives, not on a timer. Replace the default consumer:

1. **Hover** over the timer component and click the **Replace** icon (circular arrow)
2. Search for `platform-http` and select the **Platform HTTP** component
3. Open its properties and set **path** to `/test/route-input`
4. **Save** with `Ctrl/Cmd + S`

`platform-http` exposes the endpoint through the embedded HTTP server that Camel JBang starts automatically.

## Step 3: Deserialize the Incoming JSON

Incoming requests arrive as a raw string. Before we can branch on the `id` field, the body needs to be parsed into a map that Camel expressions can navigate.

1. **Hover** over the **SetBody** step and click the **Replace** icon
2. Search for `unmarshal` and select the **Unmarshal** processor
3. In the **Required** tab, set **Data Format Type** to `JSON`
4. In the **All** tab, set **Library** to `Jackson`
5. **Save** the changes

After this step, `${body[id]}` in a Simple expression will read the `id` field directly from the deserialized body.

## Step 4: Stamp the Message with a Tracking Header

Before the route branches, it is useful to record which integration processed the message. This header travels with the message all the way to Kafka and makes debugging straightforward.

1. **Hover** over the arrow after Unmarshal and click the **+** icon
2. Search for `setHeader` and select the **Set Header** processor
3. Configure:

   | Property | Value |
   |----------|-------|
   | **Header name** | `ProcessedBy` |
   | **Expression language** | `Constant` |
   | **Expression** | `my-integration` |

4. **Save** the changes

## Step 5: Branch on the `id` Field

The Content-Based Router pattern routes each message to exactly one branch based on its content. Add a Choice processor and configure three outcomes.

1. **Hover** over the arrow after Set Header and click the **+** icon
2. Search for `choice` and select the **Choice** processor
3. The Choice component appears with a `when` branch and an `otherwise` branch

**First `when` branch — `id == 1`:**

1. Click the **When** branch to open its properties
2. Set **Expression language** to `Simple` and **Expression** to `${body[id]} == 1`
3. Click **inside the When branch** placeholder and add a **Set Body** processor with **Expression language** `Constant` and **Expression** `Message processed successfully`

**Second `when` branch — `id == 2`:**

1. Click the **+** icon on the Choice component to add another `when` clause
2. Set the expression to `${body[id]} == 2`
3. Add a **Set Body** inside it with constant `Alternative scenario handled`

**`otherwise` branch:**

1. Click inside the **Otherwise** placeholder and add a **Set Body** processor
2. Set the constant to `Message processed with unknown type`

The `otherwise` branch acts as a safe fallback for any input that doesn't match a known `id`.

4. **Save** the changes

## Step 6: Log the Result

Log the final body and the `ProcessedBy` header so you can see what each branch produced without inspecting Kafka directly.

1. The default **Log** processor at the end of the route is already in place — click it to open its properties
2. Set **message** to `Output: ${body} with header ProcessedBy=${header.ProcessedBy}`
3. **Save** the changes

## Step 7: Publish to Kafka

With the message processed and logged, the last step is to forward it to Kafka. The `{{...}}` placeholders are resolved at runtime from your `application-dev.properties` file, so the same route works in any environment by swapping a single properties file.

1. **Hover** over the arrow after Log and click the **+** icon
2. Search for `kafka` and select the **Kafka** component
3. Configure:

   | Property | Value |
   |----------|-------|
   | **topic** | `{{kafka.topic}}` |
   | **brokers** | `{{kafka.bootstrap.servers}}` |
   | **clientId** | `{{kafka.client.id}}` |

4. **Save** the changes

## Step 8: Run and Test

1. In the Kaoto extension panel, click the **Play** button (▶️) next to your folder
2. A terminal opens and Camel JBang starts the route
3. In a second terminal, send a test request:

```bash
curl -s -X POST http://localhost:8080/test/route-input \
    -H "Content-Type: application/json" \
    -d '{"id": 1, "message": "hello"}'
```

The Camel terminal will show the log output with the branch result and the `ProcessedBy` header value. Try `"id": 2` to hit the second branch, or omit the field entirely to trigger the `otherwise` fallback.

## Next Step: Testing it with Citrus

Running `curl` manually covers the happy path, but it doesn't verify all three branches consistently or assert the Kafka messages. The natural next step is an automated test.

The [**Test a Camel Route with Citrus**](https://kaoto.io/workshop/intermediate-citrus-testing) workshop walks you through writing a Citrus YAML test that starts Kafka automatically, launches the route, sends HTTP requests for each scenario, and asserts both the log output and the Kafka messages — no Java required.

- **Workshop**: [Test a Camel Route with Citrus](https://kaoto.io/workshop/intermediate-citrus-testing)
- **Demo code**: [GitHub repository](https://github.com/KaotoIO/kaoto-examples/tree/main/citrus-infra)
- **Kaoto quickstart**: [Getting started guide](https://kaoto.io/docs/quickstart/)
- **VS Code extension**: [Install from marketplace](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto)

Have questions or feedback? Reach us on the [Kaoto GitHub Discussions](https://github.com/KaotoIO/kaoto/discussions) or stop by the [Kaoto Zulip chat](https://camel.zulipchat.com/#narrow/stream/441,302-kaoto).
