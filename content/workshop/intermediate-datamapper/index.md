---
title: "Transform Orders with DataMapper"
date: 2026-03-08T10:00:00+06:00
categories: ["intermediate"]
summary: "Build a real-world order dispatch integration and learn DataMapper by translating PurchaseOrder XML to ShipOrder format — without writing a single line of XSLT."
authors:
  - mmelko
---

## Introduction

You are an integration developer at **GlobalShip Warehousing**. Two core systems need to talk to each other — an Order Management System that outputs `PurchaseOrder` XML and a Legacy Shipping Platform that only accepts `ShipOrder` XML. Right now, a team manually converts between the two formats using hand-maintained XSLT files. Every time a new carrier or delivery type is added, someone edits raw XSLT. It breaks. It takes days.

Your task: **replace that manual process with a Camel integration built in Kaoto** — no XSLT editing required.

**What You'll Learn:**

- Polling a REST API on a schedule with the `timer` component
- Setting authentication headers and calling HTTP endpoints
- Splitting a JSON array and routing each item through a processing route
- Using **DataMapper** to translate between two XML schemas visually
- XPath expressions, constants, and `copy-of` mappings in DataMapper
- Dispatching results to a target system and acknowledging processed records
- Exporting and running the integration as a Quarkus application

**What You'll Build:**

A two-route Camel integration that polls the OMS for pending purchase orders, transforms each `PurchaseOrder` XML into the `ShipOrder` format required by the shipping platform, and dispatches the result — automatically, continuously.

```
Order Management System          Legacy Shipping Platform
─────────────────────────        ────────────────────────
GET  /oms/orders                 POST /lsp/ship-orders
GET  /oms/orders/{id}
     → PurchaseOrder XML    ──►       ShipOrder XML
```

You build the core integration end-to-end. Orders flow through. The mapping covers the essential fields. It works.

## Prerequisites

### Required Software

| Requirement | Version |
|-------------|---------|
| **VS Code** | latest stable |
| **Docker Desktop** | any recent |
| **Java** | 17+ |
| **JBang** | latest ([jbang.dev](https://www.jbang.dev/download/)) |

### Required Knowledge

This workshop assumes you have:

- **Basic understanding of integration concepts** — familiarity with REST APIs and XML
- **Basic command-line skills** — ability to run Docker and Maven commands
- **Familiarity with VS Code** — basic navigation and file management

> [!TIP]
> If you are new to Kaoto, complete the [Listen to a Folder](/workshop/beginner-file/) beginner workshop first. It introduces the Kaoto canvas, component configuration, and local route execution.

## Project Setup

1. Install the [Kaoto extension for VS Code](https://kaoto.io/docs/installation/) if you haven't already.
2. Create a new directory for the workshop:

```bash
mkdir kaoto-workshop
cd kaoto-workshop
```

> [!NOTE]
> **Windows users:** Use `md kaoto-workshop` in Command Prompt, or use PowerShell / Git Bash where `mkdir` works as shown.

---

## Part 1.1 — Start the systems

The OMS and the shipping platform are simulated by a single mock server. It generates a live stream of incoming purchase orders and accepts your ShipOrder output — exactly as the real systems would.

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

Open both monitoring dashboards in your browser and keep them visible alongside VS Code:

- **http://localhost:8080/** — Order backlog (OMS side)

{{< image-sh src="01-dashboard-oms.png" text="OMS dashboard — order backlog with PENDING orders" >}}

- **http://localhost:8080/dispatch** — Dispatch queue (LSP side)

{{< image-sh src="01-dashboard-lsp.png" text="LSP dispatch dashboard — empty queue before integration runs" >}}

The order backlog is already populated with pending orders. New ones arrive automatically every few seconds — the OMS is always running.

**✅ Checkpoint:** Both dashboards are open. The order backlog shows orders with status 🟡 PENDING.

---

## Part 1.2 — Get the API contracts

Both systems publish their XML schemas and expose a documented REST API. Before building anything, read the contract — it tells you exactly what data is available and where to send the result.

### Schemas

On the Order Management dashboard (http://localhost:8080/), click **⬇ Download schemas.zip**.

{{< image-sh src="12-download-schemas.png" text="OMS dashboard — Download schemas.zip link" >}}

Unzip into your project folder:

```
kaoto-workshop/
└── schemas/
    ├── PurchaseOrder.xsd   ← OMS output format
    ├── ShipOrder.xsd       ← LSP input format
    ├── AccountInfo.xsd     ← customer enrichment service
    ├── BillingInfo.xsd     ← billing enrichment service
    ├── LogisticsInfo.xsd   ← logistics enrichment service
    └── StockInfo.xsd       ← stock enrichment service
```

### API endpoints

All endpoints require the Bearer token shown at server startup.

**Order Management System (OMS) — source**

| Method | Endpoint | Returns |
|--------|----------|---------|
| `GET` | `/oms/orders` | `application/json` — array of PENDING order IDs |
| `GET` | `/oms/orders/{id}` | `application/xml` — PurchaseOrder XML |
| `POST` | `/oms/orders/{id}/ack` | `application/json` — `{"ok":true}` |

**Legacy Shipping Platform (LSP) — target**

| Method | Endpoint | Body / Returns |
|--------|----------|----------------|
| `POST` | `/lsp/ship-orders` | ShipOrder XML → `{"trackingId":"TRK-..."}`, HTTP 202 |

**Enrichment services**

| Method | Endpoint | Returns |
|--------|----------|---------|
| `GET` | `/svc/accounts/{partyId}` | `application/xml` — AccountInfo XML |
| `GET` | `/svc/billing/{orderId}` | `application/xml` — BillingInfo XML |
| `GET` | `/svc/logistics/{orderId}` | `application/xml` — LogisticsInfo XML |
| `GET` | `/svc/stock/{orderId}` | `application/xml` — StockInfo XML |

> [!TIP]
> You can open any `GET` endpoint directly in the browser. The Warehouse dashboard sidebar links to the enrichment services as a quick reference.

**✅ Checkpoint:** `kaoto-workshop/schemas/` contains 6 XSD files. You know what endpoints to call and what they return.

---

## Part 1.3 — Set up the project in VS Code

1. Install the [Kaoto extension for VS Code](https://kaoto.io/docs/installation/) if you haven't already.
2. Open VS Code → **File → Open Folder** → select `kaoto-workshop/`.
3. Confirm the **Kaoto** icon appears in the Activity Bar.

Create a new Camel Route named `order-dispatch` using the Kaoto view. See [Creating a New Integration](/docs/designer/01-managing-integrations/) if you need a step-by-step guide.

{{< image-sh src="13-vscode.png" text="VS Code with Kaoto canvas open and schemas folder visible" >}}

**✅ Checkpoint:** The `schemas/` folder is visible in the VS Code Explorer and the Kaoto canvas is open with a new route.

---

## Part 1.4 — Build the integration routes

The integration uses two routes:

- **Route 1 — Polling:** polls the OMS every 10 seconds, fetches the list of pending order IDs, and hands each ID off to Route 2.
- **Route 2 — Processing:** receives one order ID, fetches the full XML, transforms it, dispatches it to the LSP, and acknowledges the order.

Splitting into two routes keeps each one short and focused — enrichment steps can be added to Route 2 later without touching the polling logic.

> [!TIP]
> Already comfortable with Kaoto routes? Paste the following into your `order-dispatch.camel.yaml` to have the routes ready on the canvas — then read through the steps below to understand what each part does before moving to Part 1.5.
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

#### Step 1.4.1 — Polling trigger

The Kaoto canvas opens with a default route. Delete it and start fresh — see [Deleting Integrations](/docs/designer/01-managing-integrations/#deleting-integrations) if needed.

1. Delete the default route from the canvas.
2. Click **+ Add route** → click **+ Add step** → search `timer` → select **Timer**.
3. Configure the properties — **Timer name** is in the **Required** tab, **Period** is in the **All** tab:

   | Property | Tab | Value |
   |----------|-----|-------|
   | **Timer name** | Required | `tick` |
   | **Period** | All | `10000` |

---

#### Step 1.4.2 — Fetch the order backlog

All `/oms/*`, `/lsp/*`, and `/svc/*` endpoints require the Bearer token from Part 1.1. Set it once as a message header here — it will be available to all subsequent steps including Route 2.

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

#### Step 1.4.3 — Fan out to Route 2

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

{{< image-sh src="14-1-route1-complete.png" text="Route 1 complete: timer → setHeader → HTTP GET → unmarshal → split → direct" >}}

**✅ Checkpoint (Route 1):** `timer → setHeader(Auth) → HTTP GET → unmarshal → split → [setHeader(orderId) → direct:process-order]`

---

### Route 2 — Processing

#### Step 1.4.4 — Fetch the PurchaseOrder XML

The `direct:process-order` step in Route 1 references a route that doesn't exist yet. Create it first:

1. In the properties panel of the **Direct** step in Route 1, click **Create route** — Kaoto scaffolds the second route automatically with `direct:process-order` as its source.
   Alternatively, click **+ Add route** on the canvas and set the **from** component to **Direct** with name `process-order`.

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

#### Step 1.4.5 — Dispatch to the shipping platform

1. Click **+** → search `http` → select **HTTP**.

   | Property | Value |
   |----------|-------|
   | **URI** | `localhost:8080/lsp/ship-orders` |
   | **HTTP method** | `POST` |

---

#### Step 1.4.6 — Acknowledge the order

The dispatch succeeded — now tell the OMS. This step must come last: if the dispatch failed for any reason, the ACK is never sent and the order stays `PENDING` in the OMS — ready to be picked up and retried on the next poll.

1. Click **+** → search `http` → select **HTTP**.
2. Enable **Dynamic** in the properties panel.
3. Configure the properties:

   | Property | Value |
   |----------|-------|
   | **URI** | `localhost:8080/oms/orders/${header.orderId}/ack` |
   | **HTTP method** | `POST` |

The OMS dashboard moves the order from 🟡 PENDING to ✅ DISPATCHED.

{{< image-sh src="14-4-route2-complete.png" text="Route 2 complete: direct → fetch PO → HTTP POST → ack" >}}

**✅ Checkpoint (Route 2):** `direct:process-order → toD(fetch PurchaseOrder) → HTTP POST(ship-orders) → toD(ack)`

---

#### Step 1.4.7 — Add the DataMapper transformation

The route dispatches orders — but the LSP receives raw `PurchaseOrder` XML which it cannot process. The LSP speaks `ShipOrder`, a completely different format. We need to transform the message between the two steps.

Add a DataMapper step **between** the PurchaseOrder fetch and the POST to the shipping platform. On the canvas, look for the **+** icon on the arrow between those two steps — if you used the skeleton YAML, that is the arrow between the first `toD` (fetch) and the `to` (ship-orders) in `route-processing`:

1. Click the **+** on that arrow.
2. Search `DataMapper` → select it.
3. Click **Open DataMapper** — the editor opens in a new tab. Kaoto automatically creates the XSLT file alongside your route.

> [!TIP]
> New to DataMapper? See the [DataMapper documentation](/docs/datamapper/) for a full overview before continuing.

---

## Part 1.5 — Map the fields in DataMapper

The OMS speaks `PurchaseOrder`. The LSP speaks `ShipOrder`. They have nothing structurally in common — different element names, different hierarchy, different namespaces. DataMapper is where you define the translation between them.

No XSLT editing. You drag, connect, and configure visually.

---

#### Step 1.5.1 — Load the schemas

**Source (OMS output):**
1. Click **+ Add source document** → select `schemas/PurchaseOrder.xsd` → root element: `PurchaseOrder`.

**Target (LSP input):**
1. Click **Set target schema** → select `schemas/ShipOrder.xsd` → root element: `ShipOrder`.

{{< image-sh src="15-1-load-schemas.png" text="Both schemas loaded — source tree on left, target tree on right" >}}

> For more information on loading and managing schemas, see [Attaching Schemas](/docs/datamapper/02-attaching-schemas/).

**✅ Checkpoint:** Source tree on the left, target tree on the right.

---

#### Step 1.5.2 — Order identification

The LSP needs its own order reference. Drag to connect fields, use **fx** for expressions.

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

#### Step 1.5.3 — Processing metadata

The LSP requires status and audit fields on every incoming document. These are not in the PurchaseOrder — set them as constants.

Click the target field → **constant** → enter the value.

| Target | Value |
|--------|-------|
| `OrderMetadata/ProcessingStatus` | `"PENDING"` |
| `OrderMetadata/SourceSystem` | `"Kaoto-DataMapper"` |
| `OrderMetadata/CreatedAt` | *(use **fx**)* `current-dateTime()` |

> [!NOTE]
> String constants must be wrapped in quotes (`"PENDING"`). Numeric values like `9.99` in Step 1.5.8 do not need quotes.

> For more information on setting constants, see [Creating Mappings](/docs/datamapper/03-creating-mappings/).

---

#### Step 1.5.4 — Customer identification

The OMS PurchaseOrder carries buyer information directly — map it straight from the source document.

| Source | Target |
|--------|--------|
| `Buyer/PartyID` | `CustomerInformation/CustomerID` |
| `Buyer/Name` | `CustomerInformation/FullName` |
| `Buyer/Email` | `CustomerInformation/Email` |


---

#### Step 1.5.5 — Delivery address

`ShippingAddress` in PurchaseOrder and `DeliveryAddress` in ShipOrder are structurally identical — same four fields, same types. Use the **copy-of** pattern to copy the entire block in a single rule instead of mapping fields one by one.

1. Click the `DeliveryAddress` target node → **Set mapping type → copy-of**.
2. Select `ShippingAddress` as the source.

{{< image-sh src="15-5-copy-of-delivery-address.gif" text="Set copy-of on DeliveryAddress" >}}

All four address fields (Street, City, PostalCode, Country) are covered by this single mapping rule.

---

#### Step 1.5.6 — Line items

Drag the `LineItem` source node onto the `ShipmentDetails/ShipmentItem` target node — DataMapper automatically creates a `for-each` loop that iterates over all items. Then map the individual fields inside:

| Source | Target |
|--------|--------|
| `LineItem/ProductID` | `ShipmentItem/SKU` |
| `LineItem/ProductName` | `ShipmentItem/ProductName` |
| `LineItem/Quantity` | `ShipmentItem/Quantity` |
| `LineItem/UnitPrice` | `ShipmentItem/UnitPrice` |
| `OrderHeader/TotalAmount` | `ShipmentDetails/TotalValue` |

---

#### Step 1.5.7 — Carrier assignment

`DeliveryMethod` is declared `abstract="true"` in the schema — the shipping platform cannot accept the abstract element, only a concrete subtype. Pick one now:

1. Right-click the `CarrierSelection/(abstract)` node in the target tree.
2. DataMapper shows a **type picker dropdown** — select `StandardDelivery`.
3. Set the one required sub-field:

| Target | Value |
|--------|-------|
| `StandardDelivery/MethodCode` | `"STD"` |

> [!NOTE]
> The abstract node appears as `(abstract)` in the target tree — it is a placeholder until you select a concrete subtype. This is DataMapper's visual equivalent of `xsl:choose` in raw XSLT.

---

#### Step 1.5.8 — Shipping costs

One required field for now — the base cost.

| Target | Value |
|--------|-------|
| `ShippingCosts/BaseShippingCost` | `9.99` |

{{< image-sh src="15-8-mapping-complete.png" text="Complete DataMapper mapping — all fields connected" >}}

---

#### Step 1.5.9 — Save the mapping

DataMapper continuously updates the XSLT file as you work. Press **Ctrl/Cmd + S** to make sure the latest state is flushed to disk before closing the editor.

**✅ Checkpoint:** The generated XSLT file exists in the `kaoto-workshop/` folder and is non-empty.

---

## Part 1.6 — Run the integration

1. In the Kaoto **Integrations** view (left sidebar), locate the `order-dispatch` integration.
2. Click the **▶ Run** button next to it.

> For run options, executor settings, and stopping a running integration, see [Executing Integrations](/docs/designer/05-executing-integrations/).

Switch to your browser and watch both dashboards.

**Order Management dashboard** (http://localhost:8080/) — orders move through the pipeline:

🟡 PENDING → 🔵 PROCESSING → ✅ DISPATCHED

**Dispatch dashboard** (http://localhost:8080/dispatch) — the shipping platform starts receiving orders:

| Customer | Carrier | Container |
|----------|---------|-----------|
| John Smith ✅ | StandardDelivery | ⚠️ missing |
| Acme Corp ✅ | StandardDelivery | ⚠️ missing |

Customer names resolve correctly from the PurchaseOrder. Container type is blank — that field requires the StockInfo service available in Part 2.

**✅ Checkpoint:** Orders are dispatched. The Dispatch dashboard is populated with correct customer names.

{{< image-sh src="17-run-kaoto.gif" text="Integration running — orders flowing through the pipeline" >}}

---

## What we built

The integration polls the OMS every 10 seconds, transforms each `PurchaseOrder` into `ShipOrder` format using a visual DataMapper mapping, and dispatches it to the shipping platform — automatically, continuously.

| ShipOrder field | Source |
|-----------------|--------|
| `InternalOrderID` | `PO/OrderHeader/OrderID` |
| `PurchaseOrderNumber` | `concat('SO-', OrderID)` |
| `ProcessingStatus` | Constant `PENDING` |
| `SourceSystem` | Constant `Kaoto-DataMapper` |
| `CreatedAt` | `current-dateTime()` |
| `CustomerID` | `PO/Buyer/PartyID` |
| `FullName` | `PO/Buyer/Name` |
| `Email` | `PO/Buyer/Email` |
| `DeliveryAddress` | `copy-of PO/ShippingAddress` |
| `ShipmentItems` | `for-each PO/LineItems` |
| `DeliveryMethod` | `StandardDelivery` |
| `BaseShippingCost` | Constant `9.99` |

---

## What's next

The core integration works. A natural next step is to make it production-grade by enriching each order with data from additional internal services — live customer lookups, dynamic carrier selection, shipping cost calculation, and container type from stock. International customs handling can also be layered in, triggered automatically by the delivery country.

For now, explore what you've built: add a second carrier type in the DataMapper, tweak the polling interval, or inspect the generated XSLT in the `order-dispatch.xsl` file to see exactly what the visual mapping produced.

Once you're ready to go further, the next tutorial covers enrichment with multiple services, advanced DataMapper patterns, and exporting the finished integration as a Quarkus application.

{{< image-sh src="whats-next.png" text="A dispatched order — mapped fields visible in the LSP dispatch detail" >}}

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

