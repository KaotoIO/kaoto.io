---
title: "Field Context Menu"
description: "Use the right-click field context menu to override types, substitute elements, and select choice members"
date: 2026-04-01
weight: 8
---

## Overview

Right-click any field node in the source or target tree to open the **field context menu**. This menu provides schema-level operations that change how a field is interpreted in your transformation — distinct from the `⋮` mapping context menu, which controls what XSLT instructions are generated.

The field context menu offers:

- **Field Override** — Change a field's type or substitute it with another element from its substitution group
- **Choice Support** — Select, change, or clear a member of an `xs:choice` field

> [!NOTE]
> **Behaviour differs between the source and target sides for choice and abstract fields.** On the **source side**, all candidates are visible as children by default — you can drag any of them freely without selecting first. Once you apply an override, substitution, or choice selection on the source side, only the selected member is shown (same as the target side). On the **target side**, candidates are hidden from the start until you make an explicit selection. When you reopen the DataMapper after editing an existing XSLT mapping, Kaoto automatically detects which selections were in use and restores them.

---

## Field Override

Field Override allows you to change how a schema field is interpreted in your transformation. The DataMapper supports two override modes, both accessed through the same **Field Override** modal:

- **Override Type** — Change a field's type to a compatible derived type (emits `xsi:type` in the generated XSLT)
- **Substitute Element** — Replace an element with one from its substitution group

> [!IMPORTANT]
> Field override options depend on your schema definitions. To enable type overrides, your schema must define type extensions using `xs:extension` or `xs:restriction`. For substitutions, your schema must define substitution groups. You can attach additional schema files that extend your base schema to unlock these capabilities.

### When to use Field Override

**Override Type:**
- The source data uses a derived type (e.g., `SpecialAddress` extends `Address`)
- You need to access additional fields defined in a subtype
- The actual runtime data differs from the base schema definition

**Substitute Element:**
- Working with XML Schema substitution groups
- Need to select a specific concrete element from a group of alternatives
- Handling polymorphic data structures

### The Field Override modal

Open it by right-clicking a field and selecting **"Override Field..."** from the context menu.

The modal has two sections:

- **Override Mode** — radio buttons to choose **Override Type** or **Substitute Element**
- **Selector** — a **typeahead** input listing compatible types or substitution candidates; start typing to filter the list

{{< image-sh src="datamapper-field-override-modal.png" text="Field Override modal with Override Type / Substitute Element radio buttons and typeahead selector" >}}

> [!TIP]
> When there are many candidates, type part of the name to narrow the list quickly.

### Extending schemas for Field Override

If the Field Override modal shows no available options, your schema may not define the necessary extensions or substitution groups. Attach additional schema files using the [schema attachment](../02-attaching-schemas/) process to unlock these capabilities.

> [!TIP]
> You can attach multiple schema files to the same DataMapper step — a base schema and one or more extension schemas that add derived types or substitution groups.

### Applying an Override Type

Override Type changes a field's type to a compatible type within the same type hierarchy. The generated XSLT includes an `xsi:type` attribute on the element to signal the derived type. Fields with an active override are marked with a special icon in the document tree.

**Steps:**

1. **Right-click on the field** you want to override
2. **Select "Override Field..."** from the menu
3. **Select the "Override Type" radio button** in the modal
4. **Choose a type** from the typeahead list of compatible derived types
5. Click **Save** — the field tree updates to show the new type's structure and an icon appears next to the field

{{< image-sh src="datamapper-field-override-type-selected.png" text="Override Type selected with typeahead list of compatible types" >}}

{{< image-sh src="datamapper-type-override-icon.png" text="Field with override type icon indicator" >}}

### Applying a Substitute Element

Substitute Element replaces a schema element with one of its designated substitution elements. Fields with an active substitution are marked with a special icon in the document tree.

**Steps:**

1. **Right-click on a field** that has available substitutions
2. **Select "Override Field..."** from the menu
3. **Select the "Substitute Element" radio button** in the modal
4. **Choose a substitute element** from the typeahead list
5. Click **Save** — the field updates to reflect the substituted element's name and structure

{{< image-sh src="datamapper-field-override-substitution-selected.png" text="Substitute Element selected with typeahead list of substitution group members" >}}

{{< image-sh src="datamapper-field-substitution-icon.png" text="Field with substitute element icon indicator" >}}

> [!NOTE]
> Override Type and Substitute Element are mutually exclusive on the same field. The modal disables the other radio button when an override is already active.

### Working with Abstract Elements

Abstract elements are special schema elements that cannot be used directly in XML instances — they must be substituted with a concrete implementation.

**Source side**

All substitution candidates are rendered as children of the abstract wrapper in the tree by default — you can drag any candidate directly onto a target field without making an explicit selection first. To narrow the tree to one candidate, right-click the abstract wrapper and use **"Select 'X' in 'Y'"** (inline) or **"Select Substitute…"** (modal) — the same actions as the target side. Once applied, only the selected candidate is shown.

**Target side**

An abstract element initially shows only the wrapper node; candidates are **hidden until you make a selection**. There are two ways to select a concrete implementation:

<!-- MEDIA PLACEHOLDER: Screenshot showing an abstract element wrapper node in the **target** tree before any substitute is selected — wrapper row visible with "Select Substitute…" in the right-click menu, no candidate children below it. -->

*Inline quick-select* — Right-click the abstract element wrapper. If the substitution group is small, the context menu lists each candidate directly with a **"Select 'X' in 'Y'"** entry that applies the selection in one click without opening a modal.

{{< image-sh src="datamapper-abstract-context-menu.png" text="Inline quick-select via context menu" >}}

*Select Substitute modal* — Right-click the abstract element and choose **"Select Substitute…"** to open the selection modal with the full candidate list. Type to filter, then click **Confirm**.

<!-- MEDIA PLACEHOLDER: Screenshot showing the WrapperSelectionModal open for an abstract field, with the list of concrete substitute candidates including type badges and child-field previews. -->

{{< image-sh src="datamapper-abstract-field-override.png" text="Selecting concrete implementation via the Select Substitute modal" >}}

Once selected, only the chosen implementation's fields appear in the tree. The generated XSLT references the substitution element by name.

> [!TIP]
> To change the selected substitute, right-click the currently selected field and choose **"Select Substitute…"** again, or choose **"Clear substitution"** to return to the unselected state.

### Abstract elements in repeating fields

When the abstract field has `maxOccurs>1`, each instance in a collection mapping can independently reference a different substitute. Duplicate a collection mapping instance (using **Duplicate** from the `⋮` menu) to create a second instance and assign it a different substitute.

### Identifying overridden fields

Fields with active overrides are easy to identify in the document tree:

- **Override Type** — Marked with an override type icon
- **Substitute Element** — Marked with a substitution icon

### Resetting a Field Override

To restore the original schema-defined field:

1. **Right-click on the overridden field** (marked with an icon)
2. **Select "Reset Override"** from the context menu
3. The field returns to its original type or element and the icon is removed

{{< image-sh src="datamapper-reset-override.png" text="Reset Override option in context menu" >}}

> [!NOTE]
> Resetting a field override may invalidate mappings that reference fields only available in the overridden type.

---

## Choice Support

### Understanding xs:choice in schemas

XML Schema `xs:choice` defines a set of mutually exclusive element options.

On the **source side**, all choice members are visible as children by default — you can drag any member's fields directly without selecting first. To narrow the tree to one member, right-click the choice wrapper and use **"Select 'X' in 'Y'"** (inline) or **"Select Member…"** (modal) — the same actions as the target side. Once applied, only the selected member is shown.

On the **target side**, a choice wrapper initially shows only the wrapper node; member fields are **hidden until you make a selection**.

| `maxOccurs` | Behaviour |
|---|---|
| `1` (default) | One member is active at a time; a document-level selection applies to the whole mapping |
| `>1` | Multiple instances can appear; each collection instance can independently select a different member |

> [!NOTE]
> `xs:sequence` branches inside `xs:choice` are fully supported. A sequence branch appears as a single selectable entry in the member list, described by its child fields (e.g., `(street | city | postCode)`).

### Selecting a choice member (target side)

On the target side, right-click the choice wrapper to make or change a selection.

**Inline quick-select** — when a member is already selected and visible, right-click it and select **"Select 'X' in 'Y'"** to switch to a different member in one click.

**Select Member modal** — right-click the choice wrapper and choose **"Select Member…"** to open the selection modal. Type to filter, choose a member, then click **Confirm**. The selected member's fields become visible; other members are hidden.

{{< image-sh src="datamapper-choice-selection.png" text="Choice member selection modal" >}}

> [!TIP]
> The member list dissolves any abstract members within the choice into their concrete substitution candidates, so you pick a concrete type directly in one step.

### Choice members in repeating fields

When a choice field has `maxOccurs>1`, each collection instance independently selects a member. Use **Duplicate** from the `⋮` menu to create a second collection instance and assign it a different choice member.

### Working with nested choices

The DataMapper supports nested `xs:choice` elements. When multiple nested choices are selected, an indicator (e.g., `×2`) appears next to the field showing how many choice wrapper levels have been collapsed.

{{< image-sh src="datamapper-choice-nested-indicator.png" text="Nested choice indicator showing collapsed wrapper levels" >}}

### Clearing a selection

To return a choice field to its unselected state:

1. **Right-click on the choice field** (or the currently selected member)
2. **Select "Clear selection"**
3. The member fields are hidden again and the field returns to its unselected state

---

## Next Steps

- **[DataMapper Settings](../09-settings/)** — control XML declaration output for XML target documents
- **[Loop Mappings](../05-loop-mappings/)** — abstract and choice elements also work inside `for-each` and `for-each-group` collection scopes
