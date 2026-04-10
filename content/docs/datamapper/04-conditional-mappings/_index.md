---
title: "Conditional Mappings"
description: "Use if, choose-when-otherwise, and for-each logic for complex transformations"
date: 2026-04-01
weight: 4
---

## Overview

The DataMapper supports three types of conditional mappings to handle complex transformation logic:

- **`if`** - Execute mapping only when a condition is met
- **`choose-when-otherwise`** - Branch based on multiple conditions
- **`for-each`** - Iterate over collection fields (arrays)

---

## If Mapping

Create a mapping that only executes when a specific condition is true.

### Steps

1. **Click the 3-dot menu** on the target field and select **"wrap with if"**
{{< image-sh src="datamapper-if-if.png" text="Select wrap with if" >}}

2. **Configure the condition** - Drag source fields or type manually
{{< image-sh src="datamapper-if-condition.png" text="Define the if condition" >}}

3. **Create the mapping** for when the condition is true
{{< image-sh src="datamapper-if-mapping.png" text="Configure the conditional mapping" >}}

> [!TIP]
> You can drag source fields into the condition input to quickly build expressions like `$sourceField > 100` or `$status = 'active'`.

---

## Choose-When-Otherwise Mapping

Create branching logic with multiple conditions, similar to switch-case statements.

### Steps

1. **Click the 3-dot menu** and select **"wrap with choose-when-otherwise"**
{{< image-sh src="datamapper-choose-choose.png" text="Select choose-when-otherwise" >}}

2. **Configure when and otherwise conditions** - Similar to if mapping, configure the condition and create mappings for both when and otherwise branches
{{< image-sh src="datamapper-choose-otherwise-mapping.png" text="Configure when and otherwise mappings" >}}

3. **Add more when branches** (optional) - If you need multiple conditions, click the 3-dot menu on the choose field and select "Add when" to create additional when branches. Each branch can have its own condition and mappings.
{{< image-sh src="datamapper-choose-add-when.png" text="Add another when branch" >}}

> [!NOTE]
> The `otherwise` branch executes when none of the `when` conditions are satisfied, providing a default fallback.

---

## For-Each Mapping

When working with arrays or repeating elements, use for-each mappings to transform each item in the collection. Collection fields are identified by a layer icon <img src="datamapper-layer.png" alt="Layer icon" style="display: inline; height: 1.2em; vertical-align: middle;"> in the document tree.

### Steps

1. **Identify the target collection field** - Look for fields marked with the layer icon <img src="datamapper-layer.png" alt="Layer icon" style="display: inline; height: 1.2em; vertical-align: middle;">, indicating they contain multiple items

2. **Create the for-each mapping** - Click the 3-dot menu on the target collection field and select **"wrap with for-each"**
{{< image-sh src="datamapper-for-each-for-each.png" text="Select wrap with for-each" >}}

3. **Specify the source collection** - Choose which source collection to iterate over. This determines what data will be processed for each target item.
{{< image-sh src="datamapper-for-each-condition.png" text="Select source collection to iterate" >}}

4. **Map the collection item fields** - Create mappings for individual fields within each collection item. These mappings will be applied to every item in the collection.
{{< image-sh src="datamapper-for-each-mappings.png" text="Map fields for each collection item" >}}

> [!IMPORTANT]
> Inside a for-each mapping, field paths are relative to the collection item. For example, if iterating over `Items`, you reference `Name` instead of `Items/Name`.

---

## Multiple For-Each Mappings

Merge multiple source collections into a single target collection by adding multiple for-each mappings.

### Steps

1. **Create the first for-each mapping** as described above

2. **Add another for-each mapping** - Click "Add Conditional Mapping" in the placeholder below the first mapping, then select "Wrap with for-each"
{{< image-sh src="datamapper-wrap-with-for-each.png" text="Add second for-each mapping" >}}

3. **Configure the second collection mappings** - Select the second source collection to iterate over, then create field mappings for each item. This allows you to merge data from multiple collections into a single target array, combining items from different sources.
{{< image-sh src="datamapper-map-2nd-for-each-children.png" text="Configure second collection and map its fields" >}}

{{< video src="./dm_multiplemappings.mp4" subtitles="./dm_multiplemappings.vtt" >}}

> [!TIP]
> This technique is useful for merging data from multiple sources, such as combining orders from different systems into a single output array.

---

## Next Steps

Now that you understand conditional mappings:

1. **[Use the XPath editor](../05-xpath-editor/)** for complex expressions with functions
2. Return to the [DataMapper overview](../) to explore other features