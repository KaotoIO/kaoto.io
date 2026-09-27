---
title: "Conditional Mappings"
description: "Use if and choose-when-otherwise to apply branch logic in your mappings"
date: 2026-04-01
weight: 4
---

## Overview

Conditional mappings execute a mapping only when a specific condition is true. The DataMapper supports two types:

- **`if`** — Execute a mapping only when a condition is met
- **`choose-when-otherwise`** — Branch across multiple conditions and execute the first matching branch, like a switch-case statement

For iterating over collections, see [Loop Mappings](../05-loop-mappings/).

---

## If Mapping

Use `if` to wrap a target field: the entire field element is included in the output only when the condition is true.

### Steps

1. **Click the `⋮` menu** on the target field and select **"Wrap with Instruction" → "Wrap with if"**
{{< image-sh src="datamapper-if-if.png" text="Select wrap with if" >}}

2. **Configure the condition** — Drag source fields or type manually
{{< image-sh src="datamapper-if-condition.png" text="Define the if condition" >}}

3. **Create the mapping** for when the condition is true
{{< image-sh src="datamapper-if-mapping.png" text="Configure the conditional mapping" >}}

> [!TIP]
> You can drag source fields into the condition input to quickly build expressions like `$sourceField > 100` or `$status = 'active'`.

### Conditional value with Inner "if"

Use **Inner "if"** when the target field is always emitted but its *value* should depend on a condition. The field element appears in the output regardless; only the content written into it is gated.

**When to use Inner "if" instead of Wrap with "if":**

| Scenario | Use |
|---|---|
| Omit the field entirely when the condition is false | **Wrap with "if"** |
| Always emit the field, but write its value conditionally | **Inner "if"** |

#### Steps

1. **Click the `⋮` menu** on the target field and select **"Inner Instruction" → "Inner if"**

{{< image-sh src="datamapper-inner-if-menu.png" text="Inner Instruction flyout — click 'Inner if' to apply" >}}

2. **Set the condition** on the `if` node that appears inside the field row

3. **Map the value** onto the `if` node's child — this is the value written when the condition is true

{{< image-sh src="datamapper-inner-if-result.png" text="Resulting inner-if structure with condition and value mapping" >}}

> [!TIP]
> You can add a second **Inner "if"** on the same field to create an alternative branch: click the `⋮` menu on the existing `if` node and again select **"Inner Instruction" → "Inner if"**. The two `if` nodes become siblings inside the field, each writing its value when its own condition is true.

---

## Choose-When-Otherwise Mapping

Create branching logic with multiple conditions, similar to switch-case statements. Use `choose-when-otherwise` to wrap a target field: the field is emitted only through the branch whose condition matches.

### Steps

1. **Click the `⋮` menu** and select **"Wrap with Instruction" → "Wrap with choose-when-otherwise"**
{{< image-sh src="datamapper-choose-choose.png" text="Select choose-when-otherwise" >}}

2. **Map the `when` and `otherwise` branches** — set a condition on the `when` node, then add mappings for both branches. The `otherwise` branch runs automatically when no `when` condition matches.
{{< image-sh src="datamapper-choose-otherwise-mapping.png" text="Configure when and otherwise mappings" >}}

3. **Add more when branches** (optional) — Click the `⋮` menu on the `choose` node and select **"Add when"** to create additional `when` branches. Each branch can have its own condition and mappings.
{{< image-sh src="datamapper-choose-add-when.png" text="Add another when branch" >}}

> [!NOTE]
> The `otherwise` branch executes when none of the `when` conditions are satisfied, providing a default fallback.

### Conditional value with Inner "choose-when-otherwise"

Use **Inner "choose-when-otherwise"** when the target field is always emitted but its *value* should come from one of several branches. The field element is always present in the output; the `choose` structure determines which value expression is used.

> [!TIP]
> If the target field already has a value mapping (a `value-of` or dragged source field), the DataMapper automatically moves the existing mapping into the `when` branch and clones it into the `otherwise` branch when you apply Inner "choose-when-otherwise". You can then adjust each branch independently.

#### Steps

1. **Click the `⋮` menu** on the target field and select **"Inner Instruction" → "Inner choose-when-otherwise"**

{{< image-sh src="datamapper-inner-choose-menu.png" text="Inner Instruction flyout — click 'Inner choose-when-otherwise' to apply" >}}

2. **Set the `when` condition** — click the condition input on the `when` node and drag a source field or type an XPath expression

3. **Map the value for `when`** — drag a source field (or enter an XPath expression) onto the `when` node's child row

4. **Map the value for `otherwise`** — drag a source field or expression onto the `otherwise` node's child row

{{< image-sh src="datamapper-inner-choose-result.png" text="Resulting inner-choose-when-otherwise with value mappings on each branch" >}}

5. **Add more when branches** (optional) — click the `⋮` menu on the `choose` node and select **"Add when"**

---

## Next Steps

Now that you understand conditional mappings:

1. **[Loop Mappings](../05-loop-mappings/)** — iterate over collections with for-each and for-each-group
2. **[XPath Editor](../07-xpath-editor/)** — build complex expressions with functions