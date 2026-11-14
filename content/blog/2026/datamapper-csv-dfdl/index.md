---
title: "Mapping CSV data with the Kaoto DataMapper"
date: 2026-11-13
summary: The DataMapper works with XML and JSON, but you can map CSV too. Describe the CSV with a DFDL schema, let camel-dfdl turn it into XML, and map it visually.
authors:
  - igarashitm
tags:
  - Kaoto
  - DataMapper
  - CSV
  - DFDL
  - camel-dfdl
aliases:
  - /blog/datamapper-csv-dfdl/
---

The Kaoto DataMapper maps between XML and JSON documents. A lot of real integrations start with something else, though, and CSV is probably the most common example. This post shows how to map CSV data with the DataMapper today, using the [`camel-dfdl`](https://camel.apache.org/components/next/dataformats/dfdl-dataformat.html) data format to bridge the gap.

If you would rather skip the walkthrough and run the result, the finished project is in [kaoto-examples](https://github.com/KaotoIO/kaoto-examples/tree/main/csv-dfdl-datamapper).

## The idea

The DataMapper needs a schema for each side of the mapping, and it understands XML Schema and JSON Schema. [DFDL](https://daffodil.apache.org/) (Data Format Description Language) is a standard for describing text and binary formats, and a DFDL schema is an XML Schema extended with `dfdl:` annotations that describe how the data is laid out on the wire. Because it is still an XML Schema, the DataMapper can load it, and because `camel-dfdl` uses [Apache Daffodil](https://daffodil.apache.org/) to turn the structured text into XML using that same schema, the data and the schema always agree.

So the route looks like this:

```
CSV  →  unmarshal (camel-dfdl)  →  XML  →  DataMapper  →  XML / JSON
```

This is the same approach that can be used for other structured text formats, such as X12 or HL7. See the links at the end of this post.

## Why not use an existing CSV DFDL schema?

There is a generic [CSV schema](https://github.com/DFDLSchemas/CSV) in the DFDLSchemas project. It works, but it is deliberately generic. Every line becomes a `record` with a list of anonymous `item` elements:

```xml
<record>
  <item>smith</item>
  <item>robert</item>
  <item>brandon</item>
  <item>1988-03-24</item>
</record>
```

Even when your CSV has a header line, the column names are lost. This is what you get when you attach this schema to a DataMapper document: the column values are all in a repeatable `item` field, and the header line in a generic `title`.

{{< image-sh src="generic-csv.png" text="Generic CSV DFDL schema is attached to the source body" >}}

You can still map from it. Since the columns are only distinguished by their position, you refer to them as `item[1]`, `item[2]` and so on, and you have to keep track of which column each position stands for. If the layout can vary, for example when columns are optional or come in a different order, you can combine those positions with a `choose` / `when` / `otherwise` condition to decide what to map in each case.

That has its place. For a CSV with only a few columns it is manageable, and it can even be an advantage when the column specification is not strictly defined and you need to react to the data at mapping time. But for a large CSV with a well-defined structure it quickly becomes a nightmare: dozens of positional references, none of them self-explanatory, and every one of them breaks silently if a column is added or moved. For a well-structured CSV we want the columns to have names, which is what the rest of this post does.

## Step 1: Describe your CSV with a DFDL schema

Here is our sample CSV file, `orders.csv`:

```csv
orderId,customer,product,quantity,unitPrice
A-1001,Acme Corp,Widget,3,9.99
A-1002,Acme Corp,Gadget,1,24.50
A-1003,Acme Corp,Gizmo,10,2.75
```

Creating the schema means turning the header into elements. Each column becomes a named element, and the whole file becomes a list of records:

```xml
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
           xmlns:dfdl="http://www.ogf.org/dfdl/dfdl-1.0/">

  <xs:annotation>
    <xs:appinfo source="http://www.ogf.org/dfdl/">
      <dfdl:format representation="text" encoding="UTF-8" lengthKind="delimited" ... />
    </xs:appinfo>
  </xs:annotation>

  <xs:element name="orders">
    <xs:complexType>
      <xs:sequence dfdl:separator="%NL;" dfdl:separatorPosition="postfix">
        <xs:element name="header">
          <xs:complexType>
            <xs:sequence dfdl:separator=",">
              <xs:element name="title" type="xs:string" maxOccurs="unbounded"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name="order" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence dfdl:separator=",">
              <xs:element name="orderId" type="xs:string"/>
              <xs:element name="customer" type="xs:string"/>
              <xs:element name="product" type="xs:string"/>
              <xs:element name="quantity" type="xs:int"/>
              <xs:element name="unitPrice" type="xs:decimal"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

A few things are worth pointing out:

- The outer `xs:sequence` separates the lines of the file: `dfdl:separator="%NL;"`, with the separator after each line.
- The header line is consumed by the `header` element, so it does not end up as a data row. Its content is generic (`title`), and the real column names live in the `order` element.
- Columns are matched to elements by position, not by name. The header names are not checked against the elements of `order`. If a CSV file has its columns in a different order, the values silently end up in the wrong elements, so reorder the elements in `order` to match the file.
- The inner `xs:sequence` of `order` separates the columns with `dfdl:separator=","`. Change this if your file uses a different delimiter.
- This schema does not handle quoted fields. A value that contains the separator, such as `"Acme, Inc"`, is split into extra fields and the row fails to parse. Use it only for CSV files whose values contain no separators.
- Each column is an `xs:element` with a name and a type. Declaring `quantity` as `xs:int` and `unitPrice` as `xs:decimal` means the DataMapper knows they are numbers.
- The `dfdl:format` annotation on the schema sets the defaults for everything else, such as the encoding and how numbers are represented. DFDL requires many properties to be defined, so the example spells them all out. The complete schema is in the [example project](https://github.com/KaotoIO/kaoto-examples/tree/main/csv-dfdl-datamapper/orders.dfdl.xsd).

## Step 2: Try it with Camel

Before involving the DataMapper, check that the schema works. This route reads the CSV and unmarshals it with `camel-dfdl`:

{{< img-toggle src="./csv-to-xml-canvas.png" lang="yaml" >}}
- route:
    id: csv-to-xml
    from:
      uri: timer
      parameters:
        timerName: once
        repeatCount: "1"
      steps:
        - setBody:
            expression:
              constant:
                expression: resource:classpath:orders.csv
        - unmarshal:
            dfdl:
              schemaUri: orders.dfdl.xsd
        - log:
            message: ${body}
{{< /img-toggle >}}

Run it in Kaoto. Click the `Run: Workspace` button:

{{< image-sh src="csv-to-xml-run.png" text="Run csv-to-xml Camel route from Kaoto" >}}

The log shows the CSV as XML, with the column names as element names and the values typed according to the schema:

```xml
<orders>
  <header>
    <title>orderId</title><title>customer</title><title>product</title>
    <title>quantity</title><title>unitPrice</title>
  </header>
  <order>
    <orderId>A-1001</orderId>
    <customer>Acme Corp</customer>
    <product>Widget</product>
    <quantity>3</quantity>
    <unitPrice>9.99</unitPrice>
  </order>
  ...
</orders>
```

## Step 3: Map it with the DataMapper

Now add a DataMapper step after the `unmarshal` step.

{{< image-sh src="add-datamapper.png" text="Add DataMapper step" >}}

For this example, imagine the CSV is a batch order from a single customer, and the target is one invoice for the whole batch, described by a plain XML Schema, `invoice.xsd`. It has the customer, one `line` per CSV row, and a `grandTotal` after the lines:

```xml
<invoice>
  <billTo/>
  <line>
    <orderId/>
    <description/>
    <quantity/>
    <unitPrice/>
    <lineTotal/>
  </line>
  <grandTotal/>
</invoice>
```

1. Open the DataMapper step and attach `orders.dfdl.xsd` as the **Source Body** schema. The DataMapper accepts it like any other `.xsd`, and ignores the `dfdl:` annotations.
2. Attach `invoice.xsd` as the **Target Body** schema.
3. Create the mappings. Because the source fields are named after the CSV columns, this is a normal visual mapping:
   - Use a `for-each` on `order` to produce one `line` per CSV row. Inside it, map `orderId`, `quantity` and `unitPrice` straight across, and build `description` from the product and quantity with `concat(product, ' x ', quantity)`.
   - The CSV repeats the customer on every row, so map the `customer` of the first `order` to `billTo`.
   - `lineTotal` and `grandTotal` have no counterpart in the CSV, so compute them in the XPath editor. For `lineTotal`, multiply `xs:decimal(quantity)` and `xs:decimal(unitPrice)` within the `for-each`. For `grandTotal`, add up the same product over all the orders: `sum(/orders/order/(xs:decimal(quantity) * xs:decimal(unitPrice)))`. The values read from the XML are untyped, and XPath would otherwise multiply them as floating-point numbers, which can show rounding artifacts such as `2.3999999999999995` instead of `2.4`. Casting them to `xs:decimal` keeps the amounts exact.

{{< image-sh src="datamapper-done.png" text="Configured data mappings" >}}

{{< image-sh src="xpath-editor-grandTotal.png" text="Editing grandTotal expression in XPath Editor" >}}

The route now has the shape setBody (CSV) → Unmarshal (XML) → DataMapper:

{{< img-toggle src="./csv-to-xml-datamapper-canvas.png" lang="yaml" >}}
- route:
    id: csv-to-xml
    from:
      uri: timer
      parameters:
        timerName: once
        repeatCount: "1"
      steps:
        - setBody:
            expression:
              constant:
                expression: resource:classpath:orders.csv
        - unmarshal:
            dfdl:
              schemaUri: orders.dfdl.xsd
        - step:
            id: kaoto-datamapper-3148ebc4
            steps:
              - to:
                  id: kaoto-datamapper-xslt-6547
                  uri: xslt-saxon:kaoto-datamapper-3148ebc4.xsl
                  parameters:
                    failOnNullBody: false
        - log:
            message: ${body}
{{< /img-toggle >}}

The DataMapper generates the XSLT behind the scenes. Each `order` element in the CSV becomes a `line` of the invoice, and the `grandTotal` adds them up.

Running the route again gives one invoice for the whole batch:

```xml
<invoice>
   <billTo>Acme Corp</billTo>
   <line>
      <orderId>A-1001</orderId>
      <description>Widget x 3</description>
      <quantity>3</quantity>
      <unitPrice>9.99</unitPrice>
      <lineTotal>29.97</lineTotal>
   </line>
   ...
   <grandTotal>81.97</grandTotal>
</invoice>
```

## What's next

Writing the DFDL schema by hand is fine for a CSV with a handful of columns, like the one in this post. Real-world CSV files often have dozens or even hundreds of columns, and typing out one element per column is tedious and easy to get wrong, and it has to be repeated for every CSV layout you want to map. We are planning to automate it, and the work is tracked in [kaoto#4475](https://github.com/KaotoIO/kaoto/issues/4475):

1. **Upload a CSV file** in the DataMapper. A header line is enough; you do not need the whole file.
2. **Generate the DFDL schema** from it. Each column in the header becomes a named field, and the rows are represented as an array of that field set, exactly as in the schema above.
3. **Add the `camel-dfdl` step automatically** inside the DataMapper step, so the CSV is converted to XML before the mapping and back again afterwards, without you having to configure it.

These features are planned and are **not available yet**. Until then, the manual approach in this post works with the DataMapper as it is today. Stay tuned!

## Let's build it together

CSV support in the DataMapper is tracked in [kaoto#4475](https://github.com/KaotoIO/kaoto/issues/4475). Any kind of feedback is always more than welcome.

Join the conversation in the [GitHub discussions](https://github.com/orgs/KaotoIO/discussions) or [create an issue](https://github.com/KaotoIO/kaoto/issues/new/choose).

---

## Give it a try

- The [CSV DFDL DataMapper example](https://github.com/KaotoIO/kaoto-examples/tree/main/csv-dfdl-datamapper) in kaoto-examples: the finished project from this post, ready to run with Camel JBang
- Kaoto is available as a [VS Code extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto), where you can open the example and explore the DataMapper mapping

## See also

The same `camel-dfdl` and DataMapper combination works for other structured text formats. These proof-of-concept projects are good places to start:

- [X12 837](https://github.com/igarashitm/camel-x12-837-poc): converts X12 837 EDI messages to and from XML with DFDL, and maps them with the DataMapper
- [HL7](https://github.com/igarashitm/camel-hl7-xml-poc): converts HL7 messages to XML and back, and transforms them with the DataMapper
