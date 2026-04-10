---
title: "Attaching Schemas"
description: "Work with XML and JSON schemas to visualize data structures"
date: 2026-04-01
weight: 2
---

## Overview

Schemas define the structure of your data and enable the visual tree representation in the DataMapper. The DataMapper supports both XML Schema (XSD) and JSON Schema files for Source Body, Target Body, and Parameters.

> [!NOTE]
> If the data is not structured and just a primitive value, you don't need to attach a schema file.

---

## Attaching a Schema

Follow these steps to attach a schema file to Source Body, Target Body, or Parameters:

1. **Place your schema file** (`.xsd` or `.json`) in the workspace directory
2. **Click "Attach a schema"** in the Source Body, Target Body, or Parameters section
{{< image-sh src="datamapper-attach-schema.png" text="Click to attach a schema" >}}
3. **Click the file button** in the modal
{{< image-sh src="datamapper-attach-schema-file-btn.png" text="Select schema file" >}}
4. **Select your schema file**
{{< image-sh src="datamapper-select-schema.png" text="Choose the schema file" >}}

> [!TIP]
> You can select and upload multiple schema files at once.
> {{< image-sh src="datamapper-attach-multiple.png" text="Selecting multiple schema files at once" >}}

5. **For XML schemas only:** Choose the root element - Select which top-level element to use if your schema defines multiple
{{< image-sh src="datamapper-select-root-element.png" text="Choose root element for XML schema" >}}
6. **Click Attach**
{{< image-sh src="datamapper-attach-schema-attach.png" text="Confirm schema attachment" >}}
7. The **document structure** appears as a tree - The schema is parsed and rendered as an expandable tree view, showing all elements, attributes, and their hierarchical relationships. You can now navigate through the structure and create mappings by dragging fields between source and target sections.
{{< image-sh src="datamapper-schema-attached.png" text="Schema rendered as a tree" >}}

---

## Detaching a Schema

To remove a schema from Source Body, Target Body, or Parameters, click the **Detach schema** button <img src="datamapper-detach-button.png" alt="Detach schema button" style="display: inline; height: 1.2em; vertical-align: middle;"> and confirm the action.

> [!IMPORTANT]
> Detaching a schema will remove all mappings associated with that schema. This action cannot be undone.

---

## Understanding JSON Field Labels

> [!NOTE]
> Kaoto DataMapper uses XSLT 3.0 [`json-to-xml()`](https://www.w3.org/TR/xslt-30/#func-json-to-xml) and [`xml-to-json()`](https://www.w3.org/TR/xslt-30/#func-xml-to-json) functions to support JSON mappings. The field labels reflect this internal representation.

JSON schemas use type-based labels since fields can be anonymous:

| Label | Meaning |
|-------|---------|
| `map` | Object field |
| `array` | Array field |
| `string` | String field |
| `number` | Number field |

### Field Label Examples

JSON schema fields are rendered with type-based labels in the tree view. Here's how different field types appear:

{{< image-sh src="datamapper-json-fields.png" text="JSON schema field types in the tree view" >}}

**Understanding the labels:**
- **Named fields** display as `type [@key = FieldName]` - For example, `string [@key = AccountId]` represents a string field named "AccountId"
- **Anonymous fields** show only the type - For example, `map` represents an unnamed object
- **Primitive types** like `string`, `number`, `boolean` indicate the data type
- **Complex types** like `map` (object) and `array` represent structured data

### Array Fields and Collections

> [!IMPORTANT]
> For `array` fields, the **children** are the collection items, not the array itself. Collection fields are marked with a layer icon <img src="datamapper-collection-field.png" alt="Collection icon" style="display: inline; height: 1.2em; vertical-align: middle;">. The `map` type field (child of the `array` field) is the actual collection field that you'll use in for-each mappings.

{{< image-sh src="datamapper-json-array-field.png" text="Array field with collection children" >}}

---

## JSON Parameter References

When using structured JSON parameters, they're internally converted to XML. Reference them with a `-x` suffix in XPath expressions:

- Parameter `Account` becomes `$Account-x`
- Parameter `Cart` becomes `$Cart-x`

{{< image-sh src="datamapper-json-mappings-all.png" text="Complete JSON mapping example showing -x suffix usage" >}}

> [!TIP]
> When creating mappings through drag and drop, Kaoto DataMapper automatically handles the `-x` suffix. You only need to remember this when editing XPath expressions manually.

---

## Next Steps

Now that you have schemas attached:

1. **[Create simple mappings](../03-creating-mappings/)** between source and target fields
2. **[Add conditional logic](../04-conditional-mappings/)** for complex transformations
3. **[Use the XPath editor](../05-xpath-editor/)** for advanced expressions