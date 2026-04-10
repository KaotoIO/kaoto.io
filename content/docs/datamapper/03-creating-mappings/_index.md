---
title: "Creating Mappings"
description: "Build simple field-to-field mappings using drag-and-drop or XPath"
date: 2026-04-01
weight: 3
---

## Overview

Once you have schemas attached, you can create mappings between source and target fields. The DataMapper offers two primary methods: drag-and-drop for quick mappings and XPath expressions for more control.

---

## Drag and Drop Mapping

The easiest way to create a mapping is by dragging a source field onto a target field. A line will be drawn between the fields to visualize the connection.

### Example: Map the Name Field

{{< video src="./datamapper-drag-name.mp4" >}}

> [!TIP]
> Drag-and-drop is the fastest way to create simple field mappings. The DataMapper automatically generates the correct XPath expression for you.

---

## XPath Expression Mapping

For more control over your mappings, you can type XPath expressions directly.

### Create a Mapping with XPath

1. **Click the 3-dot menu** on the target field
{{< image-sh src="datamapper-add-selector.png" text="Select 'Add selector expression'" >}}

2. **Enter your XPath expression**
{{< image-sh src="datamapper-type-xpath.png" text="Type the XPath expression" >}}

> [!NOTE]
> XPath expressions give you full control over data transformation, including string manipulation, calculations, and conditional logic. For complex expressions, consider using the [XPath Editor](../05-xpath-editor/).

---

## Delete a Mapping

If you need to remove a mapping, click the trash icon <img src="datamapper-delete-mapping-btn.png" alt="Delete mapping icon" style="display: inline; height: 1.2em; vertical-align: middle;"> next to the target field and confirm the deletion.

{{< image-sh src="datamapper-delete-mapping.png" text="Delete mapping" >}}
{{< image-sh src="datamapper-delete-mapping-confirm.png" text="Confirm mapping deletion" >}}

> [!WARNING]
> Deleting a mapping is permanent and cannot be undone. Make sure you want to remove the mapping before confirming.

---

## Next Steps

Now that you can create and manage basic mappings:

1. **[Add conditional logic](../04-conditional-mappings/)** with if, choose-when-otherwise, and for-each
2. **[Use the XPath editor](../05-xpath-editor/)** for complex transformations with functions