---
title: "Stop copy-pasting your data filter: build a reusable Kamelet in Kaoto"
date: 2026-09-24
summary: Learn how to build a reusable Content Filter Kamelet in Kaoto and wire it into multiple routes to keep sensitive customer data out of analytics and partner feeds.
authors:
  - Shivam
tags:
  - Kaoto 2.12
  - Custom Kamelets
  - Canvas
  - Catalog
  - Apache Camel
  - UX
aliases:
  - /blog/custom-kamelets/
---

**What you'll learn**

- Why the Content Filter pattern belongs in a reusable Kamelet, not copy-pasted route steps
- How a multi-route Camel file makes the sensitive data leak obvious before you fix it
- How to **build** a custom action Kamelet in Kaoto with an **`allowlist`** property
- How each route configures its own allowlist in the step form — without duplicating filter logic

## The problem: when your data filter lives in two places, it breaks in one

Imagine a shipping integration. Orders arrive with everything fulfillment needs: customer name, email, address, SKU, amount. Downstream you also feed analytics **and** an external partner (for example a carrier status API). Those consumers must **not** see personally identifiable information (PII) — things like a customer's name, email address, or physical address.

Someone adds a few Camel steps on the analytics route to keep only safe fields. It works — until the partner export needs the same rule. Then someone pastes the steps again. Then a field is renamed (`customer_name` becomes `first_name` and `last_name`). Then one route is updated and the other isn't. The "policy" was never a policy; it was a snippet.

That snippet is the [Content Filter](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentFilter.html) pattern: remove data from a message so the receiver only sees what it should. **The filter is company policy.** Policy is exactly what you want as a reusable building block.

Apache Camel already has that building block: **Kamelets**. Kaoto makes the last mile pleasant — create the Kamelet in the editor, save it into the workspace, and the tile shows up in the catalog so you can wire it into routes visually.

## What we're building

A four-route integration in one YAML file that fans an incoming order out to fulfillment, analytics, and a partner export:

| Route | Role | Should see PII? |
|-------|------|-----------------|
| `order-ingest` | Creates a sample order and fans out | Yes (source of truth) |
| `order-fulfillment` | Warehouse / ops — needs contact data | **Yes** |
| `order-analytics` | Internal metrics — must not see PII | **No** |
| `order-partner-export` | Carrier / partner feed — must not see PII | **No** |

The build goes in three steps:

1. Start with all four routes **without** a filter (analytics and partner-export still log everything — the bug is visible).
2. **Build** a custom `content-filter-action` Kamelet in Kaoto with **one `allowlist` property**.
3. Place that Kamelet on analytics and partner-export, then set a **different allowlist on each route**.

## Step 1: Four routes, one file (no filter yet)

Create `orders.camel.yaml` (or any `*.camel.yaml` file Kaoto recognises). Paste the YAML below as-is. Notice that **analytics and partner-export do not call a Kamelet yet** — they log the full body, including PII.

```yaml
# Shared sample order (PII included on purpose)
- route:
    id: order-ingest
    description: Produce a sample order and fan out to fulfillment, analytics, and partner export
    from:
      uri: timer:orders
      parameters:
        period: "10000"
        repeatCount: "1"
      steps:
        - setBody:
            constant: >-
              {
                "order_id": "ORD-1001",
                "customer_name": "Ada Lovelace",
                "customer_email": "ada@example.com",
                "ship_to_address": "12 Analytical Engine Rd",
                "item_sku": "SKU-ABC-42",
                "quantity": 2,
                "amount": 149.99,
                "destination_country": "US",
                "shipping_priority": "NEXT_DAY",
                "status": "NEW"
              }
        - log:
            message: "Ingest accepted order ${body}"
        - multicast:
            parallelProcessing: false
            steps:
              - to:
                  uri: direct:fulfillment
              - to:
                  uri: direct:analytics
              - to:
                  uri: direct:partner-export

- route:
    id: order-fulfillment
    description: Ops path — needs PII to contact the customer
    from:
      uri: direct:fulfillment
      steps:
        - log:
            loggingLevel: INFO
            message: "FULFILLMENT (full payload): ${body}"

- route:
    id: order-analytics
    description: Analytics path — should not see PII (filter not applied yet)
    from:
      uri: direct:analytics
      steps:
        - log:
            loggingLevel: INFO
            message: "ANALYTICS (unfiltered — problem): ${body}"

- route:
    id: order-partner-export
    description: >-
      Partner / carrier export — functional downstream that only needs
      shipping facts, not customer identity (filter not applied yet)
    from:
      uri: direct:partner-export
      steps:
        - log:
            loggingLevel: INFO
            message: "PARTNER-EXPORT (unfiltered — problem): ${body}"
```

{{< figure src="canvas-with-no-content-filter-nodes.png" alt="Canvas with no content filter nodes yet" caption="Canvas with ingest → fulfillment / analytics / partner-export; no Content Filter nodes yet" class="image" >}}

### What you should see when it runs (before the fix)

**Fulfillment** correctly has identity fields:

```text
FULFILLMENT (full payload): {"order_id":"ORD-1001","customer_name":"Ada Lovelace","customer_email":"ada@example.com", ...}
```

**Analytics** and **partner-export** incorrectly have the same full payload:

```text
ANALYTICS (unfiltered — problem): {"order_id":"ORD-1001","customer_name":"Ada Lovelace","customer_email":"ada@example.com", ...}
PARTNER-EXPORT (unfiltered — problem): {"order_id":"ORD-1001","customer_name":"Ada Lovelace","customer_email":"ada@example.com", ...}
```

That's the teachable moment: two different consumers (metrics vs partner API), **one shared mistake** — no Content Filter yet.

{{< figure src="terminal-output-with-no-content-filter-nodes.png" alt="Terminal output with no content filter nodes yet" caption="Terminal output showing all fields — no Content Filter nodes connected yet" class="image" >}}

## Step 2: Build the custom Content Filter Kamelet in Kaoto

You're **not** going to paste a hard-coded allowlist into every route, and you're **not** going to clone `setBody` JSON on each route either. Instead, you'll create the Kamelet once in Kaoto (New → Kamelet, or your editor's create-Kamelet flow):

1. Set the name to `content-filter-action` and the type to **action** — not source (which produces messages) or sink (which consumes them), but action.
2. Add a single property: **`allowlist`** (string) — one control that each route will configure independently.
3. Give it a sensible default: the company baseline of safe shipping fields (no customer identity).
4. On the Kamelet canvas, wire `kamelet:source` → unmarshal JSON → `setBody` to keep only the fields named in `{{allowlist}}` → marshal JSON.
5. **Save** the Kamelet into the workspace (for example `content-filter-action.kamelet.yaml`). No IDE restart needed.

### Reference YAML

Use this as a check against **Source Code** view after building in Kaoto — or paste it directly if you're skipping the visual designer:

```yaml
metadata:
  name: content-filter-action
  labels:
    camel.apache.org/kamelet.type: action
  annotations: {}
spec:
  template:
    route:
      from:
        id: from-3051
        uri: kamelet:source
        parameters: {}
        steps:
          - unmarshal:
              id: unmarshal-1466
              json: {}
          - setBody:
              id: setBody-2579
              groovy:
                expression: >
                  def src = request.body

                  def allowed = '{{allowlist}}'.split(',')*.trim().findAll { it
                  } as Set

                  def out = new LinkedHashMap()

                  allowed.each { key ->
                    if (src.containsKey(key)) {
                      out.put(key, src[key])
                    }
                  }

                  return out
          - marshal:
              id: marshal-2137
              json:
                prettyPrint: true
  definition:
    description: "Strips PII from an order JSON body. Configure which safe fields
      each route may keep via the allowlist property (Content Filter EIP). Use
      via to: kamelet:content-filter-action."
    properties:
      allowlist:
        type: string
        title: Fields to keep
        description: Comma-separated field names from the safe set  (order_id, item_sku,
          quantity, amount, destination_country, shipping_priority,
          status). Do not include customer_* or address fields.
        default: order_id,item_sku,quantity,amount,destination_country,shipping_priority,status
```

Save if you edited source. Workspace Kamelets are picked up automatically when Kaoto refreshes the catalog tiles.

{{< figure src="canvas-with-content-filter-kamelet.png" alt="Canvas with content filter kamelet" caption="Canvas showing the Content Filter Kamelet and its configured properties in the form's Modified tab" class="image" >}}

### Alternative: one boolean property per field

If you'd rather give teams explicit toggles in the form (one checkbox per field), define properties such as `includeOrderId`, `includeAmount`, … (`type: boolean`, defaults `true`) and branch in Groovy with `if ({{includeOrderId}}) out.put('order_id', src['order_id'])`.

That approach makes it harder to accidentally request a PII field by typo, but it needs heavier logic to process all seven boolean properties. For this post we stick with a single **`allowlist`** string.

## Step 3: Wire the policy into your routes

This is the step that turns a Camel feature into a team practice.

### Open the integration in Kaoto

Open `orders.camel.yaml` in VS Code with the Kaoto extension. You should see all four routes on the canvas.

### Find the Kamelet in the catalog — no catalog rebuild needed

1. Confirm `content-filter-action.kamelet.yaml` is saved in the workspace.
2. On the **order-analytics** route, open the catalog (add step before the log).
3. Switch to the **Kamelets** tab and search for `content-filter` or `Content Filter`.

{{< figure src="catalog-modal-with-content-filter-tile.png" alt="Catalog modal with content filter tile" caption="Content Filter Kamelet tile on the catalog modal" class="image" >}}

> **Expected:** The tile appears without regenerating a Camel catalog archive. Workspace Kamelets are merged in automatically when Kaoto refreshes its catalog tiles.

### Apply it where PII must not leave

**Fulfillment** stays as a plain `log` step — ops still need contact data.

**Analytics** and **partner-export** each get the **same** Kamelet tile inserted before their log step. The difference is the `allowlist` value you set on each:

1. Insert **Content Filter** on `order-analytics`.
2. Open the step's configuration form — you'll see a single **Fields to keep** / `allowlist` control.
3. Leave analytics on the default (full safe set), or edit the comma-separated list as needed.
4. Insert **Content Filter** on `order-partner-export`.
5. On **that** step's form, set a narrower allowlist — for example, drop `amount` and `shipping_priority`.

You're editing the allowlist **per route usage**, through the Kamelet parameter — not by duplicating filter YAML into each route.

After wiring, the source looks like this:

```yaml
- route:
    id: order-analytics
    description: Analytics
    from:
      uri: direct:analytics
      steps:
        - to:
            uri: kamelet:content-filter-action
            id: to-4189
        - log:
            loggingLevel: INFO
            message: "ANALYTICS: ${body}"
- route:
    id: order-partner-export
    description: Partner
    from:
      uri: direct:partner-export
      steps:
        - to:
            uri: kamelet:content-filter-action
            id: content-filter-kamelet-on-order-partner-export
            parameters:
              allowlist: order_id,item_sku,quantity,destination_country,status
        - log:
            loggingLevel: INFO
            message: "PARTNER-EXPORT: ${body}"
```

Same tile, two `allowlist` values. Fulfillment still has no filter.

{{< figure src="config-form-content-filter-node-on-order-partner-export.png" alt="Config form of content filter node on order-partner-export" caption="Config form (Modified tab) of the Content Filter node on the order-partner-export route" class="image" >}}

### What you should see after the fix

```text
FULFILLMENT (full payload): {"order_id":"ORD-1001","customer_name":"Ada Lovelace","customer_email":"ada@example.com", ...}
ANALYTICS (filtered): {"order_id":"ORD-1001","item_sku":"SKU-ABC-42","quantity":2,"amount":149.99,"destination_country":"US","shipping_priority":"NEXT_DAY","status":"NEW"}
PARTNER-EXPORT (filtered): {"order_id":"ORD-1001","item_sku":"SKU-ABC-42","quantity":2,"destination_country":"US","status":"NEW"}
```

{{< figure src="terminal-output-with-content-filter-nodes.png" alt="Terminal output with content filter nodes" caption="Terminal output after adding Content Filter nodes — PII is gone from analytics and partner-export" class="image" >}}

Partner-export has no `amount` or `shipping_priority` — configured on that step only, without touching the analytics route.

### Two ways to change policy

| Change | Where | Effect |
|--------|--------|--------|
| **Per-route allowlist** | Kaoto form / `parameters.allowlist` on that `to: kamelet:...` step | Only that consumer's field set changes |
| **Baseline default** | Kamelet definition `properties.allowlist.default` | What every new usage starts with before you edit the form |

To change what **one** consumer receives, edit that step's `allowlist` in Kaoto. To change the **starting default** for all new usages, update the property default in the Kamelet editor, save, and re-open the step form.

## Takeaways

1. **Show the leak first** — a multi-route file makes it obvious that analytics and partner-export share the same problem.
2. **Build the Content Filter as a Kamelet of type `action`** — actions sit mid-route and transform the message, which is exactly what a filter does. One template, many call sites, zero duplication.
3. **Kaoto closes the loop** — save the Kamelet → catalog tile appears → drop it onto routes → edit each `allowlist` in the form.
4. **Keep PII out of allowlists by convention** — the property description and code review are your guardrails.

The same approach works beyond data filtering. Anywhere you catch yourself copy-pasting the same transformation, enrichment, or validation logic across routes — currency conversion, audit stamping, schema validation, payload size trimming — a custom action Kamelet is the right fix. Define the logic once, expose the variable parts as properties, and let each route configure its own values through the Kaoto form.

## Further reading

- Enterprise Integration Patterns — [Content Filter](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentFilter.html)
- [Apache Camel Kamelets](https://camel.apache.org/camel-kamelets/next/)
- [Kaoto documentation](/docs/)

## Let's build it together

Let us know what you think by joining us in the [GitHub discussions](https://github.com/orgs/KaotoIO/discussions).
Do you have an idea for improving Kaoto's Kamelet support? Would you love to see a useful feature implemented or simply ask a question? Please [create an issue](https://github.com/KaotoIO/kaoto/issues/new/choose).

## Give it a try

- Kaoto online [editor](https://kaotoio.github.io/kaoto/#/)
- Kaoto is available as a [VS Code extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto)

Happy integrating! 🚀
