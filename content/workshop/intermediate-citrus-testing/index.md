---
title: "Test a Camel Route with Citrus"
date: 2026-06-10
categories: ["intermediate"]
summary: "Learn to write integration tests for an Apache Camel route using the Citrus testing framework. Start infrastructure automatically, send HTTP requests, verify logs, and validate Kafka messages — all with the help of Kaoto."
authors:
  - pvinaches
---

## Introduction

In this hands-on workshop, you will write an integration test for an Apache Camel route using the **Citrus testing framework**. Citrus lets you describe every test action in YAML, provision infrastructure on demand, and verify both log output and messaging endpoints without writing a single line of Java.

**What You'll Learn:**
- How to create a Citrus test in the Kaoto VSCode extension
- How to define reusable test payload variables in a Citrus YAML file
- How to start and stop Kafka test infrastructure with `camel-infra-run` and `camel-infra-stop`
- How to launch a Camel route during the test with `jbang-run`
- How to verify route logs with `jbang-verify`
- How to validate Kafka output with a `receive` action
- How to run the test from the Kaoto extension and inspect the result

**What You'll Test:**
A Camel route that exposes an HTTP endpoint, unmarshals incoming JSON, routes messages based on an `id` field, sets a custom header, logs the result, and publishes the processed message to a Kafka topic.

## Prerequisites

### Required Software

- **Visual Studio Code** - Download from [code.visualstudio.com](https://code.visualstudio.com/)
- **Kaoto Extension for VSCode** - Install from the [VSCode Marketplace](https://kaoto.io/docs/installation/)
- **Podman Desktop** or **Docker Desktop** - For running containerized services
  - Podman: [podman.io/docs/installation](https://podman.io/docs/installation), first step needs an additional step after installing found in this [link](https://camel.apache.org/manual/test-infra.html#_container_runtime_support) 
  - Docker: [docs.docker.com/get-docker](https://docs.docker.com/get-docker/)
- **Java Development Kit (JDK) 17 or later** - Required for running Apache Camel
  - Download from [Adoptium](https://adoptium.net/) or your preferred JDK distribution
- **Apache Camel JBang** (Optional but recommended) - For easy infrastructure setup
  - Install via: `curl -Ls https://sh.jbang.dev | bash -s - trust add https://github.com/apache/camel`
  - Then: `jbang app install camel@apache/camel`

### Required Knowledge

- **Basic Apache Camel concepts** — routes, components, processors
- **Basic command-line skills** — navigating directories and running commands
- **Familiarity with VSCode** — basic navigation and file management

> [!TIP]
> If you haven't built a Camel route before, start with the [Listen to a Folder](/workshop/beginner-file) beginner workshop first.

## Project Setup

1. Install the [Kaoto extension for VSCode](https://kaoto.io/docs/installation/).
2. Clone or download the example project:

```bash
$ git clone https://github.com/KaotoIO/kaoto-examples.git
$ cd kaoto-examples/citrus-infra
```

## Description

This workshop walks you through understanding and executing a Citrus test for a Camel route. You will inspect the route, understand its behaviour, and then trace every action in the test file — from infrastructure startup to final cleanup.

**Test Scenarios Covered:**

| Payload | Expected log | Kafka message |
|---------|-------------|---------------|
| `{"id": 1, "message": "test data"}` | `Message processed successfully` | `Message processed successfully` |
| `{"id": 99, "message": "unknown test data"}` | `Message processed with unknown type` | _(not validated)_ |
| `{"message": "no id"}` (missing field) | `Message processed with unknown type` | _(not validated)_ |

---

## The Route Under Test

This is the Camel route you will be testing. Open `my-route.camel.yaml` in Kaoto to see it rendered as a visual graph.

{{< img-toggle src="./kaoto-flow.png" lang="yaml" >}}
- route:
    id: my-integration-route
    description: HTTP endpoint route that processes incoming JSON messages and
      routes them based on message ID, supporting both standard and alternative
      processing scenarios
    from:
      id: http-endpoint-input
      uri: platform-http:/test/route-input
      description: Platform HTTP endpoint listening on /test/route-input for incoming
        JSON requests
      steps:
        - unmarshal:
            id: unmarshal-json-request
            description: Deserialize incoming JSON payload into Java object using Jackson
              library
            json:
              library: Jackson
        - log:
            id: log-incoming-message
            description: Log the received message body for debugging and audit purposes
            message: "Received message: ${body}"
        - setHeader:
            id: set-processed-by-header
            description: Add custom header to track which integration service processed this
              message
            name: ProcessedBy
            constant: my-integration
        - choice:
            id: route-by-message-id
            description: Route message to appropriate handler based on the message ID field
            when:
              - id: check-alternative-scenario
                steps:
                  - setBody:
                      id: set-alternative-response
                      description: Set response body to indicate alternative scenario was processed
                      constant: Alternative scenario handled
                description: Route message to appropriate handler based on the message ID field
                simple:
                  expression: ${body[id]} == 2
              - id: check-standard-scenario
                steps:
                  - setBody:
                      id: set-standard-response
                      description: Set response body to indicate successful standard processing
                      constant: Message processed successfully
                description: Standard processing path for messages with ID equal to 1
                simple:
                  expression: ${body[id]} == 1
            otherwise:
              id: handle-unknown-message-type
              description: Fallback handler for messages with unrecognized ID values
              steps:
                - setBody:
                    id: set-unknown-response
                    description: Set response body indicating message was received but type was not
                      recognized
                    constant: Message processed with unknown type
        - log:
            id: log-final-output
            description: Log final response body and ProcessedBy header value for audit
              trail
            message: "Output: ${body} with header ProcessedBy=${header.ProcessedBy}"
        - to:
            id: send-to-kafka
            uri: kafka
            parameters:
              topic: "{{kafka.topic}}"
              brokers: "{{kafka.bootstrap.servers}}"
              clientId: "{{kafka.client.id}}"
            description: Send the processed response message to Kafka topic for downstream
              consumption
            disabled: false
{{< /img-toggle >}}

The route accepts HTTP POST requests on `/test/route-input` with a JSON body. It tags each message with a `ProcessedBy` header, branches on the `id` field to set the response body, logs the result, and publishes it to a Kafka topic.

> [!TIP]
> The Kafka broker address is read from `application.properties` via `{{kafka.bootstrap.servers}}`. At test time, Citrus overrides this value with the address of the container it starts: the route itself requires no changes.
>
> Create an `application.properties` file in the `citrus-infra/` directory with the following content:
>
> ```properties
> kafka.bootstrap.servers=localhost:9092
> kafka.topic=my-topic
> kafka.client.id=camel-route-client
> ```

---

## Part 1: Creating the Test File with Kaoto

### Goal

Use the Kaoto extension to scaffold the Citrus test file directly from VSCode.

### Step-by-Step Instructions

#### Step 1: Open the Kaoto Extension

Open the Kaoto panel in VSCode. You will see a **New Citrus test** button in the toolbar.

{{< image-sh src="kaoto-extension.png" text="Kaoto extension panel showing the New Citrus test button" >}}

Click **New Citrus test**.

#### Step 2: Select the Destination Folder and Name the File

When prompted, select the `test/` folder inside `citrus-infra/` as the destination. Then enter `my-integration` as the test file name.

Kaoto will create `test/my-integration.citrus.yaml` with a starter template ready to edit. It will also automatically generate `test/citrus-application.properties` — this file is required for the test to run but you don't need to modify it.

**✅ Checkpoint:** The files `test/my-integration.citrus.yaml` and `test/citrus-application.properties` exist in your project.

---

## Part 2: Adding Test Variables

### Goal

Add the test payload variables to the Citrus test file using Kaoto's canvas.

### Step-by-Step Instructions

#### Step 1: Open the Test File in Kaoto

Open `test/my-integration.citrus.yaml` in VSCode. Kaoto will render it as a visual canvas. Click on the **my-integration** node in the canvas to open its configuration panel.

#### Step 2: Navigate to the All Tab

In the configuration panel, click the **All** tab. This exposes every field of the test definition, including the `variables` section.

{{< image-sh src="citrus-test-variables.png" text="Kaoto All tab showing the variables section" >}}

#### Step 3: Add the Variables

The template already contains a first variable entry. Replace its content with:

| Field | Value |
|-------|-------|
| `name` | `test.payload` |
| `value` | `{"id": 1, "message": "test data"}` |

Click **+** again to add each of the remaining variables:

| `name` | `value` |
|--------|---------|
| `test.payload.unknown` | `{"id": 99, "message": "unknown test data"}` |
| `test.payload.missing.field` | `{"message": "no id"}` |

Variables are declared once at the top and referenced throughout the test with the `${variableName}` syntax. This keeps test data in one place and makes it easy to update.

#### Step 4: Save the File

Save the file with **Ctrl+S** (or **Cmd+S** on macOS). Kaoto will write the variables to `test/my-integration.citrus.yaml`.

**✅ Checkpoint:** All three variables are defined and saved in `test/my-integration.citrus.yaml`.

---

## Part 3: Adding Infrastructure Components

### Goal

Add the Kafka infrastructure startup and teardown actions to the test using Kaoto's canvas.

### Step-by-Step Instructions

#### Step 1: Replace the Echo Component with camel-infra-run

The template includes a placeholder `echo` component as the first action. Hover over it in the canvas and click the **Replace** icon that appears. In the search box, type `camel-infra-run` and select it.

Click on the `camel-infra-run` component, open the **All** tab, and enter `kafka` in the **service** field.

This action starts a Kafka container via Podman or Docker. Once the container is healthy, Citrus automatically exports its bootstrap address as the environment variable `CITRUS_CAMEL_INFRA_KAFKA_BOOTSTRAP_SERVERS`.

> [!NOTE]
> Your container runtime (Podman or Docker) must be running before executing the test.

#### Step 2: Add a doFinally Action

Click **Add step** at the end of the actions list and search for `dofinally`. Select it to append a `doFinally` block. This action runs its nested steps regardless of whether the test passes or fails, guaranteeing cleanup even on test errors.

#### Step 3: Add Steps Inside doFinally

Inside the `doFinally` block, click **Add step** and search for `camel-infra-stop`. Select it. Click on the `camel-infra-stop` component, open the **All** tab, and enter `kafka` in the **service** field.

Click **Add step** again inside the same `doFinally` block and add an `echo` action. Click on it, open the **All** tab, and enter `Tests completed` in the **message** field.

{{< img-toggle src="./first-components.png" lang="yaml" >}}
  name: my-integration.citrus
  author: Citrus
  status: FINAL
  description: Sample test in YAML
  variables:
    - name: test.payload
      value: "'{\"id\": 1, \"message\": \"test data\"}'"
    - name: test.payload.unknown
      value: "'{\"id\": 99, \"message\": \"unknown test data\"}'"
    - name: test.payload.missing.field
      value: "'{\"message\": \"no id\"}'"
  actions:
    - camel:
        infra:
          run:
            service: kafka
    - doFinally:
        actions:
          - camel:
              infra:
                stop:
                  service: kafka
          - echo:
              message: Tests completed
{{< /img-toggle >}}

#### Step 4: Create the jbang.properties File

Create a new file named `jbang.properties` inside the `test/` folder with the following content:

```properties
run.deps=org.citrusframework:citrus-camel:4.10.1,\
         org.citrusframework:citrus-testcontainers:4.10.1,\
         org.apache.camel:camel-test-infra-kafka:4.20.0,\
         org.citrusframework:citrus-kafka:4.10.1
```

JBang reads this file automatically when running the test and downloads the listed dependencies. They provide the Camel JBang actions, container lifecycle management, the Kafka container image, and the Citrus Kafka consumer endpoint.

**✅ Checkpoint:** The canvas shows `camel-infra-run` as the first action and a `doFinally` block containing `camel-infra-stop` and `echo` at the end, all configured, and `test/jbang.properties` exists with the required dependencies.

---

## Part 4: Adding the jbang-run and Delay Components

### Goal

Start the Camel route as part of the test using the `jbang-run` action, and add a short `delay` after it so Kafka has time to become ready before the first HTTP request is sent.

### Step-by-Step Instructions

#### Step 1: Add the jbang-run Component

Hover over the arrow between the `camel-infra-run` node and the `doFinally` block. A **+** icon will appear. Click it and search for `jbang-run`. Select it to insert the action between them.

Repeat the same process on the arrow that appears after `jbang-run`: hover over it, click **+**, and this time search for `delay`. Select it.

#### Step 2: Configure jbang-run — Integration File

Click on the `jbang-run` node to open its configuration panel. Navigate to the **All** tab.

You will see an **Integration** row with a pencil (✏️) icon on the right. Click the pencil to expand the integration entry form.

{{< image-sh src="jbang-run-pencil.png" text="Kaoto All tab for jbang-run showing the Integration row with the pencil icon" >}}

Fill in the fields:

| Field | Value |
|-------|-------|
| **File** | `../my-route.camel.yaml` |
| **Name** | `my-route` |

This tells Citrus which Camel route file to run and assigns it an internal name so it can be stopped cleanly later.

#### Step 3: Configure jbang-run — System Properties

Still in the `jbang-run` **All** tab, scroll down and expand the **Advanced** section. Locate **SystemProperties** and click **+** inside the **Properties** group to add a new entry.

{{< image-sh src="jbang-run-systemproperties.png" text="Kaoto Advanced section for jbang-run showing SystemProperties with the kafka.bootstrap.servers property configured" >}}

| Field | Value |
|-------|-------|
| **Name** | `kafka.bootstrap.servers` |
| **Value** | `${CITRUS_CAMEL_INFRA_KAFKA_BOOTSTRAP_SERVERS}` |

This overrides the `kafka.bootstrap.servers` property at runtime with the address of the Kafka container that Citrus started in the previous action. The route picks it up automatically without any code change.

#### Step 4: Configure the Delay Component

Click on the `delay` node. In its configuration panel, set the **Milliseconds** field to `2000`.

This 2-second pause gives the Camel route time to start up and connect to Kafka before the test begins sending HTTP requests.

**✅ Checkpoint:** The canvas shows `camel-infra-run` → `jbang-run` (with the integration file and system property configured) → `delay` (2000 ms) → `doFinally`.

{{< img-toggle src="./kaoto-next.png" lang="yaml" >}}
name: my-integration.citrus
author: Citrus
status: FINAL
description: Sample test in YAML
variables:
  - name: test.payload
    value: "'{\"id\": 1, \"message\": \"test data\"}'"
  - name: test.payload.unknown
    value: "'{\"id\": 99, \"message\": \"unknown test data\"}'"
  - name: test.payload.missing.field
    value: "'{\"message\": \"no id\"}'"
actions:
  - camel:
      infra:
        run:
          service: kafka
  - camel:
      jbang:
        run:
          integration:
            file: ../my-route.camel.yaml
            name: my-route
            systemProperties:
              properties:
                - name: kafka.bootstrap.servers
                  value: ${CITRUS_CAMEL_INFRA_KAFKA_BOOTSTRAP_SERVERS}
  - delay:
      milliseconds: "2000"
  - doFinally:
      actions:
        - camel:
            infra:
              stop:
                service: kafka
        - echo:
            message: Tests completed
{{< /img-toggle >}}

---

## Part 5: Validating the Choice Outputs

### Goal

Add the test actions that verify each route branch produces the expected log output, and validate the Kafka message for the standard scenario.

### Step-by-Step Instructions

#### Step 1: Add the Standard Scenario Actions

After the `delay` action and before `doFinally`, add these components in order:

1. `send`
2. `jbang-verify`
3. `receive`
4. `echo`

Configure them with the following values:

**send**

| Field | Value |
|-------|-------|
| **Endpoint** | `http://localhost:8080/test/route-input` |

In **Message** → **Body** → **Data**, add `${test.payload}`.

In **Headers**, add one entry:

| Field | Value |
|-------|-------|
| **Name** | `Content-Type` |
| **Value** | `application/json` |

**jbang-verify**

| Field | Value |
|-------|-------|
| **Integration** | `my-route` |
| **LogMessage** | `Output: Message processed successfully with header ProcessedBy=my-integration` |

**receive**

| Field | Value |
|-------|-------|
| **Endpoint** | `kafka:my-topic?server=${CITRUS_CAMEL_INFRA_KAFKA_BOOTSTRAP_SERVERS}` |

In **Message** → **Body** → **Data**, enter `Message processed successfully`.

**echo**

| Field | Value |
|-------|-------|
| **Message** | `✓ Standard scenario (ID=1) log and Kafka message validated` |

{{< img-toggle src="./kaoto-next.png" lang="yaml" >}}
name: my-integration.citrus
{{</ img-toggle >}}

#### Step 2: Add the Remaining Choice Scenarios After the img-toggle

After the `img-toggle`, add the actions for the other two route branches. For each one, add these components in order:

1. `send`
2. `jbang-verify`
3. `echo`

Use the same fields as in the standard scenario, but replace the values with the following ones.

**Unknown scenario**

**send**

| Field | Value |
|-------|-------|
| **Endpoint** | `http://localhost:8080/test/route-input` |

In **Message** → **Body** → **Data**, add `${test.payload.unknown}`.

In **Headers**, add one entry:

| Field | Value |
|-------|-------|
| **Name** | `Content-Type` |
| **Value** | `application/json` |

**jbang-verify**

| Field | Value |
|-------|-------|
| **Integration** | `my-route` |
| **LogMessage** | `Output: Message processed with unknown type with header ProcessedBy=my-integration` |

**echo**

| Field | Value |
|-------|-------|
| **Message** | `✓ Unknown scenario (ID=99) log validated` |

**Missing field scenario**

**send**

| Field | Value |
|-------|-------|
| **Endpoint** | `http://localhost:8080/test/route-input` |

In **Message** → **Body** → **Data**, add `${test.payload.missing.field}`.

In **Headers**, add one entry:

| Field | Value |
|-------|-------|
| **Name** | `Content-Type` |
| **Value** | `application/json` |

**jbang-verify**

| Field | Value |
|-------|-------|
| **Integration** | `my-route` |
| **LogMessage** | `Output: Message processed with unknown type with header ProcessedBy=my-integration` |

**echo**

| Field | Value |
|-------|-------|
| **Message** | `✓ Missing field scenario (No ID) log validated` |

All of these actions must be inserted before the `doFinally` block.

**✅ Checkpoint:** The test now covers all three route outcomes: the standard scenario validates both the log and Kafka output, and the other two scenarios validate the expected log entry.

{{< img-toggle src="./kaoto-next.png" lang="yaml" >}}
name: my-integration.citrus
{{</ img-toggle >}}

## Part 6: Running the Test

### Goal

Run the Citrus test directly from the Kaoto extension and confirm it passed.

### Step-by-Step Instructions

#### Step 1: Start the Test from the Kaoto Extension

In the Kaoto extension, locate the `test/` folder that contains `my-integration.citrus.yaml`. When you hover over the test file, Kaoto shows a **Play** button.

Make sure Docker Desktop or Podman Desktop is already running, then click **Play** and wait for the test to complete.

#### Step 2: Watch the Terminal Output

Kaoto opens a terminal and starts the Citrus test run for you.

At the beginning of the run, the output will start with lines similar to these:

```text
Reading Citrus application properties file: ./citrus-application.properties
2026-06-26 14:26:35.846  INFO 95584 --- [           main] framework.main.TestRunConfiguration : Setting application property citrus.camel.jbang.dump.integration.output=true
2026-06-26 14:26:35.848  INFO 95584 --- [           main] framework.main.TestRunConfiguration : Setting application property citrus.camel.jbang.version=4.20.0
2026-06-26 14:26:35.987  INFO 95584 --- [           main] rk.junit.jupiter.JUnitJupiterEngine : Reset test sources for a fresh test run
2026-06-26 14:26:35.987  INFO 95584 --- [           main] rk.junit.jupiter.JUnitJupiterEngine : Adding test source my-integration.citrus
```

When the test finishes successfully, the output will end with lines similar to these:

```text
2026-06-26 14:26:52.668  INFO 95584 --- [           main] rusframework.report.LoggingReporter : CITRUS TEST RESULTS
2026-06-26 14:26:52.668  INFO 95584 --- [           main] rusframework.report.LoggingReporter :
2026-06-26 14:26:52.669  INFO 95584 --- [           main] rusframework.report.LoggingReporter : SUCCESS ( 16397 ms) my-integration.citrus
2026-06-26 14:26:52.669  INFO 95584 --- [           main] rusframework.report.LoggingReporter :
2026-06-26 14:26:52.669  INFO 95584 --- [           main] rusframework.report.LoggingReporter : TOTAL:          1
2026-06-26 14:26:52.669  INFO 95584 --- [           main] rusframework.report.LoggingReporter : PASSED:         1 (100.0%)
2026-06-26 14:26:52.670  INFO 95584 --- [           main] rusframework.report.LoggingReporter : FAILED:         0 (0.0%)
2026-06-26 14:26:52.671  INFO 95584 --- [           main] rusframework.report.LoggingReporter : TIME:           16397 ms
2026-06-26 14:26:52.671  INFO 95584 --- [           main] rusframework.report.LoggingReporter :
2026-06-26 14:26:52.671  INFO 95584 --- [           main] rusframework.report.LoggingReporter : ------------------------------------------------------------------------
2026-06-26 14:26:52.678  INFO 95584 --- [           main] k.report.AbstractOutputFileReporter : Generated test report: .citrus-jbang/citrus-reports/citrus-test-results.html

Tests finished after 16643 ms
Total tests run: 1, Passes: 1, Failures: 0, Skips: 0
 *  Press any key to close the terminal.
```

#### Step 3: Confirm the Result in the Kaoto Extension

After the run completes, Kaoto shows the test result next to the test file:

- a green check mark if the test passed
- a red cross if the test failed

**✅ Checkpoint:** You've successfully run the full Citrus test suite.

---


## Additional Resources

### Documentation

- [Kaoto Documentation](https://kaoto.io/docs/) — Kaoto user guide and tutorials
- [Citrus Documentation](https://citrusframework.org/citrus/reference/html/) — Complete Citrus reference

### Example Code

- [Kaoto Examples Repository](https://github.com/KaotoIO/kaoto-examples/tree/main/citrus-infra) — Complete working example used in this workshop

### Community

- [Kaoto GitHub](https://github.com/KaotoIO/kaoto) — Report issues and contribute
- [Apache Camel Community](https://camel.apache.org/community/) — Get help and connect with other users
