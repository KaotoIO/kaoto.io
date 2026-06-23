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

{{< image-sh src="datamapper-drag-name.gif" text="Drag and drop to create a field mapping" >}}

> [!TIP]
> Drag-and-drop is the fastest way to create simple field mappings. The DataMapper automatically generates the correct XPath expression for you.

---

## Container Mappings

When you drag a **container field** (a field that contains other fields, such as an XML element with child elements or a JSON object with properties) onto another container field, the DataMapper automatically maps their matching children — you don't need to connect each child field individually.

### How Container Mapping Works

1. **Drag a container field** from the source tree onto a matching container field in the target tree
2. The DataMapper **automatically pairs children** by name and creates individual mappings for each match
3. This works **recursively** — nested containers are also matched and mapped automatically
4. **Children that exist only on one side are skipped**

{{< image-sh src="datamapper-container-mapping.gif" text="Dragging a container field to automatically map matching children" >}}

For **XML schemas**, children are matched by element name and namespace. For **JSON schemas**, children are matched by property key. When mapping between XML and JSON, children are matched by name.

### Collection Mappings

When both the source and target fields are **collections** (marked with the collection icon), the DataMapper additionally wraps the mapping in a `for-each` loop that iterates over each item in the source collection.

{{< image-sh src="datamapper-collection-mappings.gif" text="Collection-to-collection mapping with for-each loop" >}}

### Mapping Line Styles

After creating a container mapping, you'll notice different line styles in the mapping view:

**Regular** — A solid gray line. A simple field-to-field mapping.

**Copy-of** — A double dark line. The source and target XML containers have identical structure (same name and namespace), so the DataMapper copies the entire subtree efficiently.

{{< image-sh src="datamapper-line-style-copy-of.png" text="Copy-of mapping shown as a double dark line" >}}

**Complete** — A dashed line with long dashes. All target children are mapped, and all nested containers among them use copy-of.

**Partial** — A dashed line with short dashes. Some target children are mapped, but not all have a matching source field, or nested containers are mapped field-by-field.

{{< image-sh src="datamapper-line-styles.png" text="Mapping line styles" >}}

> [!TIP]
> A partial mapping is not an error — it simply means some target fields don't have a corresponding source field. You can add individual mappings for the remaining fields manually.

### When Container Mapping Is Not Available

In some cases, the DataMapper will not allow a container-to-container mapping:

- **Mismatched field types**: A container field can only be mapped to another container field. Dragging a container onto a leaf field (or vice versa) will be rejected.
- **No compatible children**: If the source and target containers have no children with matching names, the mapping cannot be created.
- **JSON arrays**: JSON array wrapper fields cannot be mapped directly — expand the array and map its children instead.

> [!TIP]
> If a drop is rejected, try mapping the children individually instead of the parent container.

---

## XPath Expression Mapping

For more control over your mappings, you can type XPath expressions directly.

### Create a Mapping with XPath

1. **Double-click** on a target field to activate inline editing and type an XPath expression directly, without opening the 3-dot menu.

{{< image-sh src="datamapper-double-click-edit.gif" text="Double-click a target field to enter XPath directly" >}}

   Alternatively, you can click the 3-dot mapping context menu on the target field and click "Add Selector expression"
{{< image-sh src="datamapper-add-selector.png" text="Select 'Add selector expression'" >}}

2. **Enter your XPath expression**
{{< image-sh src="datamapper-input-xpath.png" text="Type the XPath expression" >}}

> [!NOTE]
> XPath expressions give you full control over data transformation, including string manipulation, calculations, and conditional logic. For complex expressions, consider using the [XPath Editor](../05-xpath-editor/).

---

## Comment on a Mapping

Once a mapping is created, you can also comment on it.

1. **Click the 3-dot menu** on the target field 

{{< image-sh src="datamapper-add-comment-dropdown.png" text="Add comment in dropdown" >}}

2. **Add your comment**

{{< image-sh src="datamapper-add-comment.png" text="Add comment" >}}

---

## Delete a Mapping

If you need to remove a mapping, click the trash icon <img src="datamapper-delete-mapping-btn.png" alt="Delete mapping icon" style="display: inline; height: 1.2em; vertical-align: middle;"> next to the target field and confirm the deletion.

{{< image-sh src="datamapper-delete-mapping.png" text="Delete mapping" >}}
{{< image-sh src="datamapper-delete-mapping-confirm.png" text="Confirm mapping deletion" >}}

> [!TIP]
> You can also delete a mapping by selecting the target field and pressing the **Delete** key on your keyboard.

> [!WARNING]
> Deleting a mapping is permanent and cannot be undone. Make sure you want to remove the mapping before confirming.

---

## Next Steps

Now that you can create and manage basic mappings:

1. **[Add conditional logic](../04-conditional-mappings/)** with if, choose-when-otherwise, and for-each
2. **[Use the XPath editor](../05-xpath-editor/)** for complex transformations with functions