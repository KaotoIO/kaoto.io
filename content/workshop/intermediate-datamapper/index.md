---
title: "Transform Orders with DataMapper"
date: 2026-10-01T10:00:00+06:00
categories: ["intermediate"]
summary: "Build a real-world order dispatch integration and learn DataMapper by translating PurchaseOrder XML to ShipOrder format — without writing a single line of XSLT."
authors:
  - mmelko
---

## Introduction

You are an integration developer at **GlobalShip Warehousing**. Two core systems need to talk to each other — an Order Management System that outputs `PurchaseOrder` XML and a Legacy Shipping Platform that only accepts `ShipOrder` XML. Right now, a team manually converts between the two formats using hand-maintained XSLT files. Every time a new carrier or delivery type is added, someone edits raw XSLT. It breaks. It takes days.

Your task: **replace that manual process with a Camel integration built in Kaoto** — no XSLT editing required.

The integration connects to these endpoints — all secured with Bearer token authentication:

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/oms/orders` | Fetch list of PENDING order IDs |
| `GET` | `/oms/orders/{id}` | Fetch PurchaseOrder XML for one order |
| `POST` | `/lsp/ship-orders` | Dispatch ShipOrder XML to the shipping platform |
| `POST` | `/oms/orders/{id}/ack` | Acknowledge the order as dispatched |

**What You'll Learn:**

- Using **DataMapper** to translate between two XML schemas visually — no XSLT editing
- XPath expressions, constants, `copy-of`, and `for-each` mappings in DataMapper
- Building a two-route Camel integration in Kaoto

**What You'll Build:**

A two-route Camel integration that polls the OMS for pending purchase orders, transforms each `PurchaseOrder` XML into the `ShipOrder` format required by the shipping platform, and dispatches the result — automatically, continuously.

## Prerequisites

Before starting this workshop, ensure you have the following installed and configured on your system:

### Required Software

- **Visual Studio Code** with the **Kaoto Extension** — [VS Code Marketplace](https://kaoto.io/docs/installation/)
- **Docker** or **Podman** — for running the mock server
- **Java Development Kit (JDK) 17 or later**
- **JBang** — [jbang.dev](https://www.jbang.dev/download/)

### Required Knowledge

This workshop assumes you have:

- **Basic understanding of integration concepts** — familiarity with REST APIs and XML
- **Basic command-line skills** — ability to run Docker or Podman commands
- **Familiarity with VS Code** — basic navigation and file management

> [!TIP]
> If you are new to Kaoto, complete the [Listen to a Folder](/workshop/beginner-file/) beginner workshop first. It introduces the Kaoto canvas, component configuration, and local route execution.

## Project Setup

Create a new directory for the workshop and open it in VS Code with the Kaoto extension installed.

The OMS and shipping platform are simulated by a mock server — start it before continuing:

**Docker:**
```bash
docker run -p 8080:8080 quay.io/mmelko/kaoto-workshop-mock
```

**Podman:**
```bash
podman run -p 8080:8080 quay.io/mmelko/kaoto-workshop-mock
```

Wait for the following output:

```
🏭  Kaoto Workshop Mock Server
   Warehouse dashboard : http://localhost:8080/
   Dispatch dashboard  : http://localhost:8080/dispatch
   API base            : http://localhost:8080/

🔑  Bearer token (all /oms/*, /lsp/*, /svc/* calls): kaoto-workshop
```

Open both monitoring dashboards and keep them visible alongside VS Code:

- **http://localhost:8080/** — Order backlog (OMS side)

{{< image-sh src="01-dashboard-oms.png" text="OMS dashboard — order backlog with PENDING orders" >}}

- **http://localhost:8080/dispatch** — Dispatch queue (LSP side)

{{< image-sh src="01-dashboard-lsp.png" text="LSP dispatch dashboard — empty queue before integration runs" >}}

The order backlog is already populated with pending orders. New ones arrive automatically every few seconds.

---

## Part 1 — Get the schemas

### Schemas

On the Order Management dashboard (http://localhost:8080/), click **⬇ Download schemas.zip**.

{{< image-sh src="12-download-schemas.png" text="OMS dashboard — Download schemas.zip link" >}}

Unzip into your project folder:

```
kaoto-workshop/
└── schemas/
    ├── PurchaseOrder.xsd   ← OMS output format
    ├── ShipOrder.xsd       ← LSP input format
    ├── AccountInfo.xsd     ← enrichment services
    ├── BillingInfo.xsd     ← (not used in this tutorial)
    ├── LogisticsInfo.xsd
    └── StockInfo.xsd
```

**✅ Checkpoint:** `kaoto-workshop/schemas/` contains 6 XSD files.

---

## Part 2 — Set up the project in VS Code

1. Open VS Code → **File → Open Folder** → select `kaoto-workshop/`.
2. Confirm the **Kaoto** icon appears in the Activity Bar.

Create a new Camel Route named `order-dispatch` using the Kaoto view. See [Creating a New Integration](/docs/designer/01-managing-integrations/) if you need a step-by-step guide.

{{< image-sh src="13-vscode.png" text="VS Code with Kaoto canvas open and schemas folder visible" >}}

**✅ Checkpoint:** The Kaoto canvas is open with a new route.

---

## Part 3 — Build the integration routes

The integration uses two routes:

- **Route 1 — Polling:** polls the OMS every 10 seconds, fetches the list of pending order IDs, and hands each ID off to Route 2.
- **Route 2 — Processing:** receives one order ID, fetches the full XML, transforms it, dispatches it to the LSP, and acknowledges the order.

Splitting into two routes keeps each one short and focused — enrichment steps can be added to Route 2 later without touching the polling logic.

> [!TIP]
> Already comfortable with Kaoto routes? Paste the following into your `order-dispatch.camel.yaml` to have the routes ready on the canvas — then read through the steps below to understand what each part does before moving to Part 4.
>
> ```yaml
> - route:
>     id: route-polling
>     from:
>       uri: timer
>       parameters:
>         period: "10000"
>         timerName: tick
>       steps:
>         - setHeader:
>             constant:
>               expression: Bearer kaoto-workshop
>             name: Authorization
>         - to:
>             uri: http
>             parameters:
>               httpMethod: GET
>               httpUri: localhost:8080/oms/orders
>         - unmarshal:
>             json: {}
>         - split:
>             simple:
>               expression: ${body}
>             steps:
>               - setHeader:
>                   name: orderId
>                   simple:
>                     expression: ${body}
>               - to:
>                   uri: direct
>                   parameters:
>                     name: process-order
> - route:
>     id: route-processing
>     from:
>       uri: direct
>       parameters:
>         name: process-order
>       steps:
>         - toD:
>             uri: http
>             parameters:
>               httpUri: localhost:8080/oms/orders/${header.orderId}
>               httpMethod: GET
>         - to:
>             uri: http
>             parameters:
>               httpUri: localhost:8080/lsp/ship-orders
>               httpMethod: POST
>         - toD:
>             uri: http
>             parameters:
>               httpUri: localhost:8080/oms/orders/${header.orderId}/ack
>               httpMethod: POST
> ```

---

### Route 1 — Polling

#### Step 4.1 — Polling trigger

The Kaoto canvas opens with a default route containing a timer. Replace the default timer configuration:

1. Click the default **Timer** step to open its properties panel.
2. Configure the properties — **Timer name** is in the **Required** tab, **Period** is in the **All** tab:

   | Property | Tab | Value |
   |----------|-----|-------|
   | **Timer name** | Required | `tick` |
   | **Period** | All | `10000` |

---

#### Step 4.2 — Fetch the order backlog

The OMS and LSP are secured systems — all API calls require a Bearer token. Set it once as an `Authorization` header at the beginning of Route 1 and it will be propagated to all subsequent steps, including Route 2.

1. Click **+** → search `setHeader` → select **Set Header**.

   | Property | Value |
   |----------|-------|
   | **Header name** | `Authorization` |
   | **Expression type** | `Constant` |
   | **Expression** | `Bearer kaoto-workshop` |

2. Click **+** → search `http` → select **HTTP**.

   | Property | Value |
   |----------|-------|
   | **URI** | `localhost:8080/oms/orders` |
   | **HTTP method** | `GET` |

3. Click **+** → search `unmarshal` → select **Unmarshal**.

   | Property | Value |
   |----------|-------|
   | **Data format** | `json` |

---

#### Step 4.3 — Fan out to Route 2

Split the JSON array so each order ID is processed individually, then hand it off to Route 2.

1. Click **+** → search `split` → select **Split**.

   | Property | Value |
   |----------|-------|
   | **Expression type** | `Simple` |
   | **Expression** | `${body}` |

2. Click **+** inside the split → search `setHeader` → select **Set Header**.

   | Property | Value |
   |----------|-------|
   | **Header name** | `orderId` |
   | **Expression type** | `Simple` |
   | **Expression** | `${body}` |

3. Click **+** inside the split → search `direct` → select **Direct**.

   | Property | Value |
   |----------|-------|
   | **Name** | `process-order` |

{{< img-toggle src="14-1-route1-complete.png" lang="yaml" >}}
- route:
    id: route-3822
    from:
      id: from-4170
      uri: timer
      parameters:
        period: "10000"
        timerName: tick
      steps:
        - setHeader:
            id: setHeader-2645
            constant:
              expression: Bearer kaoto-workshop
            name: Authorization
        - to:
            id: to-6056
            uri: http
            parameters:
              httpMethod: GET
              httpUri: localhost:8080/oms/orders
        - unmarshal:
            id: unmarshal-3896
            json: {}
        - split:
            id: split-1270
            simple:
              expression: ${body}
            steps:
              - setHeader:
                  id: setHeader-2808
                  name: orderId
                  simple:
                    expression: ${body}
              - to:
                  id: to-3006
                  uri: direct
                  parameters:
                    name: process-order
{{< /img-toggle >}}

**✅ Checkpoint (Route 1):** `timer → setHeader(Auth) → HTTP GET → unmarshal → split → [setHeader(orderId) → direct:process-order]`

---

### Route 2 — Processing

#### Step 4.4 — Fetch the PurchaseOrder XML

The `direct:process-order` step in Route 1 references a route that doesn't exist yet. Create it first:

1. In the properties panel of the **Direct** step in Route 1, click **Create route** — Kaoto scaffolds the second route automatically with `direct:process-order` as its source.

This route receives one order ID in the `orderId` header each time Route 1 fires.

2. Click **+** → search `http` → select **HTTP**.
3. In the properties panel, enable **Dynamic** — this switches the step from a static `to` to a dynamic `toD`, allowing the URI to be evaluated at runtime.
4. Configure the properties:

   | Property | Value |
   |----------|-------|
   | **URI** | `localhost:8080/oms/orders/${header.orderId}` |
   | **HTTP method** | `GET` |

The message body is now the raw `PurchaseOrder` XML.

---

> [!TIP]
> Route 2 uses three HTTP steps with similar configuration. Instead of searching and configuring each from scratch, you can right-click an existing HTTP step on the canvas → **Copy**, then right-click the target position → **Paste as next step**. See [Copy and Paste Nodes](/docs/designer/03-reordering-nodes/#copy-and-paste-nodes) for details.

#### Step 4.5 — Dispatch to the shipping platform

1. Click **+** → search `http` → select **HTTP**.

   | Property | Value |
   |----------|-------|
   | **URI** | `localhost:8080/lsp/ship-orders` |
   | **HTTP method** | `POST` |

---

#### Step 4.6 — Acknowledge the order

The dispatch succeeded — now tell the OMS. This step must come last: if the dispatch failed for any reason, the ACK is never sent and the order stays `PENDING` in the OMS — ready to be picked up and retried on the next poll.

1. Click **+** → search `http` → select **HTTP**.
2. Enable **Dynamic** in the properties panel.
3. Configure the properties:

   | Property | Value |
   |----------|-------|
   | **URI** | `localhost:8080/oms/orders/${header.orderId}/ack` |
   | **HTTP method** | `POST` |

The OMS dashboard moves the order from 🟡 PENDING to ✅ DISPATCHED.

{{< img-toggle src="14-4-route2-complete.png" lang="yaml" >}}
- route:
    id: route-1210
    from:
      uri: direct
      parameters:
        name: process-order
      steps:
        - toD:
            id: to-3707
            uri: http
            parameters:
              httpUri: localhost:8080/oms/orders/${header.orderId}
              httpMethod: GET
        - to:
            id: to-9723
            uri: http
            parameters:
              httpUri: localhost:8080/lsp/ship-orders
              httpMethod: POST
        - toD:
            id: to-9309
            uri: http
            parameters:
              httpUri: localhost:8080/oms/orders/${header.orderId}/ack
              httpMethod: POST
{{< /img-toggle >}}

**✅ Checkpoint (Route 2):** `direct:process-order → toD(fetch PurchaseOrder) → HTTP POST(ship-orders) → toD(ack)`

---

#### Step 4.7 — Add the DataMapper transformation

The route dispatches orders — but the LSP receives raw `PurchaseOrder` XML which it cannot process. The LSP speaks `ShipOrder`, a completely different format. We need to transform the message between the two steps.

Add a DataMapper step **between** the PurchaseOrder fetch and the POST to the shipping platform. On the canvas, look for the **+** icon on the arrow between those two steps — if you used the skeleton YAML, that is the arrow between the first `toD` (fetch) and the `to` (ship-orders) in `route-processing`:

1. Click the **+** on that arrow.
2. Search `DataMapper` → select it.
3. Click the DataMapper step to open its properties panel, then click **Configure** — the DataMapper editor opens in a new tab and the XSLT file is created alongside your route.

{{< image-sh src="datamapper-step.png" text="DataMapper step placed between the PurchaseOrder fetch and the ship-orders POST" >}}

> [!TIP]
> New to DataMapper? See the [DataMapper documentation](/docs/datamapper/) for a full overview before continuing.

---

## Part 4 — Map the fields in DataMapper

The OMS speaks `PurchaseOrder`. The LSP speaks `ShipOrder`. They have nothing structurally in common — different element names, different hierarchy, different namespaces. DataMapper is where you define the translation between them.

No XSLT editing. You drag, connect, and configure visually.

---

#### Step 5.1 — Load the schemas

**Source (OMS output):**
1. Click **+ Add source document** → select `schemas/PurchaseOrder.xsd` → root element: `PurchaseOrder`.

**Target (LSP input):**
1. Click **Set target schema** → select `schemas/ShipOrder.xsd` → root element: `ShipOrder`.

{{< image-sh src="15-1-load-schemas.png" text="Both schemas loaded — source tree on left, target tree on right" >}}

> [!TIP]
> For more information on loading and managing schemas, see [Attaching Schemas](/docs/datamapper/02-attaching-schemas/).

**✅ Checkpoint:** Source tree on the left, target tree on the right.

---

#### Step 5.2 — Order identification

The LSP needs its own order reference. Drag to connect fields, use **fx** for expressions.

> [!TIP]
> For more information on drag & drop mappings and the XPath editor, see [Creating Mappings](/docs/datamapper/03-creating-mappings/) and [XPath Editor](/docs/datamapper/05-xpath-editor/).

| Source | Target |
|--------|--------|
| `OrderHeader/OrderID` | `OrderIdentification/InternalOrderID` |
| `OrderHeader/OrderDate` | `OrderIdentification/PurchaseOrderDate` |

`PurchaseOrderNumber` is a derived field — the LSP wants it prefixed. Double-click `OrderIdentification/PurchaseOrderNumber` to open the input field, then click the **fx** button and enter the expression:

```xpath
concat('SO-', /*:PurchaseOrder/*:OrderHeader/*:OrderID)
```

> [!NOTE]
> The namespace prefix (`ns0:`, `ns1:`, etc.) depends on how the schema was loaded and may differ in your session. Using the wildcard prefix `*:` makes the expression work regardless of the prefix assigned.

{{< image-sh src="15-2-map-order-id.gif" text="Drag OrderID and OrderDate, then double-click PurchaseOrderNumber → fx to enter the concat expression" >}}

---

#### Step 5.3 — Processing metadata

The LSP requires status and audit fields on every incoming document. These are not in the PurchaseOrder — set them as fixed XPath string expressions.

Double-click each target field to open the input, then enter the value directly — string values must be wrapped in quotes:

| Target | Value |
|--------|-------|
| `OrderMetadata/ProcessingStatus` | `"PENDING"` |
| `OrderMetadata/SourceSystem` | `"Kaoto-DataMapper"` |
| `OrderMetadata/CreatedAt` | *(use **fx**)* `current-dateTime()` |

> [!NOTE]
> String values must be wrapped in quotes (`"PENDING"`). Numeric values like `9.99` in Step 5.8 do not need quotes — XPath treats them as numbers directly.

> [!TIP]
> For more information on setting constants, see [Creating Mappings](/docs/datamapper/03-creating-mappings/).

---

#### Step 5.4 — Customer identification

The OMS PurchaseOrder carries buyer information directly — drag each source field onto its target. No expressions needed, these are direct mappings.

| Source | Target |
|--------|--------|
| `Buyer/PartyID` | `CustomerInformation/CustomerID` |
| `Buyer/Name` | `CustomerInformation/FullName` |
| `Buyer/Email` | `CustomerInformation/Email` |


---

#### Step 5.5 — Delivery address

`ShippingAddress` in PurchaseOrder and `DeliveryAddress` in ShipOrder are structurally identical — same four fields, same types. Use the **copy-of** pattern to copy the entire block in a single rule instead of mapping fields one by one.

1. Click the `DeliveryAddress` target node → **Set mapping type → copy-of**.
2. Select `ShippingAddress` as the source.

{{< image-sh src="15-5-copy-of-delivery-address.gif" text="Set copy-of on DeliveryAddress" >}}

All four address fields (Street, City, PostalCode, Country) are covered by this single mapping rule.

---

#### Step 5.6 — Line items

Drag the `LineItem` source node onto the `ShipmentDetails/ShipmentItem` target node — DataMapper automatically creates a `for-each` loop that iterates over all items. Then map the individual fields inside:

| Source | Target |
|--------|--------|
| `LineItem/ProductID` | `ShipmentItem/SKU` |
| `LineItem/ProductName` | `ShipmentItem/ProductName` |
| `LineItem/Quantity` | `ShipmentItem/Quantity` |
| `LineItem/UnitPrice` | `ShipmentItem/UnitPrice` |
| `OrderHeader/TotalAmount` | `ShipmentDetails/TotalValue` |

> [!NOTE]
> `TotalValue` is mapped outside the `for-each` loop — it is a single value from the order header, not per line item.

---

#### Step 5.7 — Carrier assignment

`DeliveryMethod` is declared `abstract="true"` in the schema — the shipping platform cannot accept the abstract element, only a concrete subtype. Pick one now:

1. Right-click the `CarrierSelection/(abstract)` node in the target tree.
2. DataMapper shows a **type picker dropdown** — select `StandardDelivery`.
3. Set the one required sub-field:

| Target | Value |
|--------|-------|
| `StandardDelivery/MethodCode` | `"STD"` |

> [!NOTE]
> The abstract node appears as `(abstract)` in the target tree — it is a placeholder until you select a concrete subtype. Selecting a type here tells DataMapper which concrete element to output.

---

#### Step 5.8 — Shipping costs

One required field for now — the base cost.

| Target | Value |
|--------|-------|
| `ShippingCosts/BaseShippingCost` | `9.99` |

{{< image-sh src="15-8-mapping-complete.png" text="Complete DataMapper mapping — all fields connected" >}}

---

#### Step 5.9 — Save the mapping

DataMapper continuously updates the XSLT file as you work. Press **Ctrl/Cmd + S** to make sure the latest state is flushed to disk before closing the editor.

**✅ Checkpoint:** The generated XSLT file exists in the `kaoto-workshop/` folder. Its content should look like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- This file is generated by Kaoto DataMapper. Do not edit. -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="3.0"
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:fn="http://www.w3.org/2005/xpath-functions"
  xmlns:ns0="http://www.kaoto.io/shiporder"
  xmlns:ns1="http://www.kaoto.io/purchaseorder"
  exclude-result-prefixes="xs fn ns0 ns1">
  <xsl:output method="xml" indent="yes" omit-xml-declaration="yes"/>
  <xsl:template match="/">
    <ShipOrder xmlns="http://www.kaoto.io/shiporder">
      <OrderIdentification>
        <InternalOrderID><xsl:value-of select="/ns1:PurchaseOrder/ns1:OrderHeader/ns1:OrderID"/></InternalOrderID>
        <PurchaseOrderNumber><xsl:value-of select="concat('SO-',/ns1:PurchaseOrder/ns1:OrderHeader/ns1:OrderID)"/></PurchaseOrderNumber>
        <PurchaseOrderDate><xsl:value-of select="/ns1:PurchaseOrder/ns1:OrderHeader/ns1:OrderDate"/></PurchaseOrderDate>
      </OrderIdentification>
      <OrderMetadata>
        <CreatedAt><xsl:value-of select="current-dateTime()"/></CreatedAt>
        <ProcessingStatus><xsl:value-of select="'PENDING'"/></ProcessingStatus>
        <SourceSystem><xsl:value-of select="'Kaoto-Datamapper'"/></SourceSystem>
      </OrderMetadata>
      <CustomerInformation>
        <CustomerID><xsl:value-of select="/ns1:PurchaseOrder/ns1:Buyer/ns1:PartyID"/></CustomerID>
        <FullName><xsl:value-of select="/ns1:PurchaseOrder/ns1:Buyer/ns1:Name"/></FullName>
        <Email><xsl:value-of select="/ns1:PurchaseOrder/ns1:Buyer/ns1:Email"/></Email>
      </CustomerInformation>
      <DeliveryAddress>
        <xsl:copy-of select="/ns1:PurchaseOrder/ns1:ShippingAddress"/>
      </DeliveryAddress>
      <ShipmentDetails>
        <ShipmentItems>
          <xsl:for-each select="/ns1:PurchaseOrder/ns1:LineItems/ns1:LineItem">
            <ShipmentItem>
              <xsl:attribute name="lineNumber"><xsl:value-of select="@lineNumber"/></xsl:attribute>
              <SKU><xsl:value-of select="ns1:ProductID"/></SKU>
              <ProductName><xsl:value-of select="ns1:ProductName"/></ProductName>
              <Quantity><xsl:value-of select="ns1:Quantity"/></Quantity>
              <UnitPrice><xsl:value-of select="ns1:UnitPrice"/></UnitPrice>
            </ShipmentItem>
          </xsl:for-each>
        </ShipmentItems>
        <TotalValue><xsl:value-of select="/ns1:PurchaseOrder/ns1:OrderHeader/ns1:TotalAmount"/></TotalValue>
      </ShipmentDetails>
      <CarrierSelection>
        <StandardDelivery>
          <MethodCode><xsl:value-of select="'STD'"/></MethodCode>
        </StandardDelivery>
      </CarrierSelection>
      <ShippingCosts>
        <BaseShippingCost><xsl:value-of select="'9.99'"/></BaseShippingCost>
      </ShippingCosts>
    </ShipOrder>
  </xsl:template>
</xsl:stylesheet>
```

> [!NOTE]
> The namespace prefixes (`ns0:`, `ns1:`) in your generated file may differ — this is normal and depends on how the schemas were loaded.

---

## Part 5 — Run the integration

1. In the Kaoto **Integrations** view (left sidebar), locate the `order-dispatch` integration.
2. Click the **▶ Run** button next to it.

> [!TIP]
> For run options, executor settings, and stopping a running integration, see [Executing Integrations](/docs/designer/05-executing-integrations/).

Switch to your browser and watch both dashboards.

**Order Management dashboard** (http://localhost:8080/) — orders move through the pipeline:

🟡 PENDING → 🔵 PROCESSING → ✅ DISPATCHED

**Dispatch dashboard** (http://localhost:8080/dispatch) — the shipping platform starts receiving orders:

| Customer | Carrier | Container |
|----------|---------|-----------|
| John Smith ✅ | StandardDelivery | ⚠️ missing |
| Acme Corp ✅ | StandardDelivery | ⚠️ missing |

Customer names resolve correctly from the PurchaseOrder. Container type is blank — that field requires enrichment from the StockInfo service, covered in the next tutorial.

**✅ Checkpoint:** Orders are dispatched. The Dispatch dashboard is populated with correct customer names.

{{< image-sh src="17-run-kaoto.gif" text="Integration running — orders flowing through the pipeline" >}}

---

## What we built

The integration polls the OMS every 10 seconds, transforms each `PurchaseOrder` into `ShipOrder` format using a visual DataMapper mapping, and dispatches it to the shipping platform — automatically, continuously.

| ShipOrder field | Source |
|-----------------|--------|
| `InternalOrderID` | `PO/OrderHeader/OrderID` |
| `PurchaseOrderNumber` | `concat('SO-', OrderID)` |
| `ProcessingStatus` | `"PENDING"` |
| `SourceSystem` | `"Kaoto-DataMapper"` |
| `CreatedAt` | `current-dateTime()` |
| `CustomerID` | `PO/Buyer/PartyID` |
| `FullName` | `PO/Buyer/Name` |
| `Email` | `PO/Buyer/Email` |
| `DeliveryAddress` | `copy-of PO/ShippingAddress` |
| `ShipmentItems` | `for-each PO/LineItem` |
| `DeliveryMethod` | `StandardDelivery` |
| `BaseShippingCost` | Constant `9.99` |

---

## What's next

The core integration works — orders flow, fields are mapped, the shipping platform receives valid `ShipOrder` XML.

For now, explore what you've built: tweak a mapping in the DataMapper, add a different carrier type, or open the generated XSLT file to see what the visual mapping produced under the hood.

{{< image-sh src="whats-next.png" text="A dispatched order — mapped fields visible in the LSP dispatch detail" >}}

A follow-up tutorial is coming that takes this integration further — enriching each order with live data from four additional services, dynamic carrier selection, and exporting everything as a Quarkus application. Stay tuned.

---

## Troubleshooting

**401 Unauthorized**
All three HTTP steps need `Authorization: Bearer kaoto-workshop` — the orders list fetch, the individual order XML fetch, and the final POST to the shipping platform. Check each step in the properties panel.

**DataMapper schema tree is empty**
Open DataMapper, click **+ Add source document**, and select the XSD from the `schemas/` folder using the file browser — not a URL.

**Orders stay PENDING indefinitely**
A mapping error in the generated XSLT is the most common cause. Re-open DataMapper and check for unmapped required fields (marked red). Save again to regenerate the XSLT.

**`order-dispatch.xsl` is empty or missing**
Press **Ctrl/Cmd + S** explicitly inside the DataMapper editor window before closing it.

---

## Additional Resources

- [Kaoto Documentation](https://kaoto.io/docs/) — Kaoto user guide and reference
- [Apache Camel YAML DSL](https://camel.apache.org/components/4.0.x/others/yaml-dsl.html) — YAML DSL reference
- [Apache Camel Simple Language](https://camel.apache.org/components/4.0.x/languages/simple-language.html) — expression language reference
- [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/) — EIP reference

---

