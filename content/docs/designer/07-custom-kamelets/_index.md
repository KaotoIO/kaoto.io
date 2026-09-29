---
title: "Custom Kamelets"
description: "Build reusable custom Kamelets in Kaoto, publish them to the workspace catalog, and use them across routes with per-step configuration"
date: 2026-09-24
weight: 7
---

## Overview

Starting with Kaoto 2.12, **custom Kamelets you create and save in your workspace are automatically available as catalog tiles** — no catalog rebuild or IDE restart required. Once you save a `.kamelet.yaml` file, its tile appears in the Kaoto catalog so you can drop it onto any route and configure its properties through the standard configuration form, just like any built-in Kamelet.

This makes it practical to build **reusable, parameterized integration logic** once and wire it into many routes across your project.

---

## Kamelet Types

When you create a Kamelet in Kaoto you choose one of three types:

| Type | Role | Typical use |
|------|------|-------------|
| **source** | Produces messages | Custom trigger or inbound adapter |
| **sink** | Consumes messages | Custom outbound adapter or side-effect step |
| **action** | Sits mid-route and transforms or enriches the message | Filters, enrichers, converters, validators |

For logic that sits between existing route steps — such as a content filter or a data enricher — choose **action**.

---

## Creating a Custom Kamelet

1. Open the Kaoto view in VS Code and click **New File** in the integrations navigation bar.
2. Set the file name (e.g. `content-filter-action`) and choose the file type **Kamelet**.
3. In the **Definition** panel, set the Kamelet **type** (`source`, `sink`, or `action`) and add one or more **properties** — these become the configurable parameters exposed in the step form when the Kamelet is used in a route.
4. Build the internal route on the Kamelet canvas. An action Kamelet always starts from `kamelet:source`. Wire your processing steps after it.
5. **Save** the file as `<name>.kamelet.yaml` anywhere in your workspace.

Kaoto picks up the file automatically and the Kamelet tile appears in the catalog.

> [!TIP]
> The Kamelet name in `metadata.name` must match the file name prefix. For example, `content-filter-action.kamelet.yaml` must have `metadata.name: content-filter-action`.

---

## Defining Properties

Properties declared in `spec.definition.properties` become form fields in the route step configuration panel. Each property can have:

| Field | Purpose |
|-------|---------|
| `type` | Data type (`string`, `integer`, `boolean`, …) |
| `title` | Human-readable label shown in the form |
| `description` | Help text shown beneath the field |
| `default` | Value pre-filled when the step is first dropped |

**Example — a single `allowlist` property:**

```yaml
spec:
  definition:
    description: "Strips fields from a JSON body. Configure which fields to keep via the allowlist property."
    properties:
      allowlist:
        type: string
        title: Fields to keep
        description: Comma-separated field names to retain in the message body.
        default: order_id,item_sku,quantity,amount,status
```

Each route that uses this Kamelet can set its own value for `allowlist` without modifying the Kamelet definition.

---

## Using a Custom Kamelet in a Route

### Finding the Kamelet in the catalog

1. Open your Camel route file (e.g. `orders.camel.yaml`) in Kaoto.
2. Hover over a connection between steps and click **+**, or right-click a step and select **Prepend** / **Append**.
3. In the catalog modal, switch to the **Kamelets** tab and search by name.
4. Your workspace Kamelet tile appears alongside the built-in Kamelets — click it to insert it as a step.

### Configuring the step

After dropping the Kamelet onto the canvas, select the step to open its configuration form. The properties you defined in the Kamelet appear as form fields. Each route step stores its own property values independently — two routes can use the same Kamelet with completely different configurations.

The YAML generated for the step uses the `to: kamelet:<name>` syntax with a `parameters` block:

```yaml
- to:
    uri: kamelet:content-filter-action
    parameters:
      allowlist: order_id,item_sku,destination_country,status
```

---

## Live Property Refresh

Changes to a custom Kamelet's `spec.definition.properties` (for example, adding a new property or changing a default value) are reflected in the configuration forms of routes that already use that Kamelet — **without reopening the route file**.

---

## Catalog Behavior

| Scenario | Behavior |
|----------|----------|
| Kamelet file saved in workspace | Tile appears in catalog automatically |
| Kamelet file renamed or deleted | Tile is removed from catalog on next refresh |
| Property defaults updated in the Kamelet | Forms on existing route steps reflect the new defaults |
| Multiple routes using the same Kamelet | Each `to: kamelet:…` step stores its own parameter values |

---

## Example: Content Filter Action Kamelet

The following Kamelet implements the [Content Filter](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentFilter.html) enterprise integration pattern. It keeps only the fields listed in `allowlist` and removes everything else from the JSON body.

```yaml
metadata:
  name: content-filter-action
  labels:
    camel.apache.org/kamelet.type: action
spec:
  template:
    route:
      from:
        uri: kamelet:source
        steps:
          - unmarshal:
              json: {}
          - setBody:
              groovy:
                expression: >
                  def src = request.body
                  def allowed = '{{allowlist}}'.split(',')*.trim().findAll { it } as Set
                  def out = new LinkedHashMap()
                  allowed.each { key ->
                    if (src.containsKey(key)) { out.put(key, src[key]) }
                  }
                  return out
          - marshal:
              json:
                prettyPrint: true
  definition:
    description: "Strips PII from a JSON body. Configure which fields each route may keep via the allowlist property."
    properties:
      allowlist:
        type: string
        title: Fields to keep
        description: Comma-separated field names to retain. Do not include customer identity fields.
        default: order_id,item_sku,quantity,amount,destination_country,shipping_priority,status
```

Save this as `content-filter-action.kamelet.yaml`. Two routes can then use it with different allowlists:

```yaml
# Analytics route — default allowlist
- to:
    uri: kamelet:content-filter-action

# Partner export — narrower allowlist set in the step form
- to:
    uri: kamelet:content-filter-action
    parameters:
      allowlist: order_id,item_sku,quantity,destination_country,status
```

> [!TIP]
> For a step-by-step walkthrough of this example see the blog post
> [Stop copy-pasting your data filter: build a reusable Kamelet in Kaoto](/blog/2026/custom-kamelets/).

---

## Next Steps

- **[Working with Nodes](../02-working-with-nodes/)** — Add, replace, and configure steps including Kamelets
- **[Managing Integrations](../01-managing-integrations/)** — Create and organize `.kamelet.yaml` and `.camel.yaml` files
- **[Runtime Selector](../04-runtime-selector/)** — Configure the Camel catalog and runtime for your workspace
