---
title: "XPath Editor"
description: "Create complex transformations with the XPath expression editor"
date: 2026-04-01
weight: 7
---

## Overview

The XPath Editor is a full-featured code editor for writing XPath expressions. Every target field also has an inline expression input for quick edits, but the XPath Editor is the right tool when:

- The expression is **too long or complex to read and write comfortably in the inline input**
- You want to **browse the function catalog** — the left panel lists all available XPath 3.1 functions organised by category, so you don't need to memorise them; drag one into the editor to insert it with its parameter placeholders
- You want **auto-completion and hover help** — as you type, the editor suggests matching functions and shows their full signature and description on hover

---

## Opening the XPath Editor

To edit or create complex XPath expressions, click the **fx** button on any target field that has a mapping. This opens the XPath Editor where you can build your expression.

{{< image-sh src="datamapper-edit-xpath.png" text="Click fx button to open XPath Editor" >}}

---

## Building XPath Expressions

The XPath Editor interface provides two main areas: a palette on the left with fields and functions, and an expression editor on the right.

{{< image-sh src="datamapper-xpath-editor.png" text="XPath Editor interface" >}}

### Adding Fields

You can add source fields to your expression by:
- **Typing directly** — Enter field paths manually using XPath syntax
- **Drag and drop** — Drag fields from the **Fields** tab and drop them into the editor

{{< image-sh src="datamapper-xpath-dnd-fields.png" text="Drag and drop fields into the expression" >}}

### Using XPath Functions

The XPath Editor ships a full **XSLT 3.0 / XPath 3.1** function catalog organized into 15 categories:

| Category | Examples |
|---|---|
| **String** | `concat()`, `string-join()`, `upper-case()`, `lower-case()`, `normalize-space()`, `replace()` |
| **Substring Matching** | `starts-with()`, `ends-with()`, `contains()`, `substring()`, `substring-before()`, `substring-after()` |
| **Pattern Matching** | `matches()`, `tokenize()`, `analyze-string()` |
| **Numeric** | `sum()`, `avg()`, `min()`, `max()`, `round()`, `floor()`, `ceiling()`, `format-number()` |
| **Date and Time** | `current-date()`, `current-time()`, `current-dateTime()`, `format-date()`, `format-time()` |
| **Boolean** | `boolean()`, `not()`, `true()`, `false()` |
| **QName** | `QName()`, `local-name()`, `namespace-uri()`, `prefix-from-QName()` |
| **Node** | `name()`, `node-name()`, `root()`, `path()`, `has-children()`, `innermost()`, `outermost()` |
| **Sequence** | `count()`, `empty()`, `exists()`, `distinct-values()`, `index-of()`, `reverse()`, `subsequence()` |
| **Context** | `position()`, `last()`, `current()`, `current-group()`, `current-grouping-key()` |
| **Math** | `math:pi()`, `math:exp()`, `math:log()`, `math:sin()`, `math:cos()`, `math:pow()`, `math:sqrt()` |
| **Map** | `map:merge()`, `map:get()`, `map:put()`, `map:keys()`, `map:contains()`, `map:remove()` |
| **Array** | `array:size()`, `array:get()`, `array:put()`, `array:append()`, `array:join()`, `array:flatten()` |
| **Higher-Order** | `fn:apply()`, `fn:filter()`, `fn:fold-left()`, `fn:fold-right()`, `fn:for-each()`, `fn:for-each-pair()` |
| **XSLT** | `key()`, `element-available()`, `function-available()`, `current-output-uri()`, `unparsed-text()` |

To browse and use functions:

1. **Switch to the Functions tab** in the left palette

{{< image-sh src="datamapper-xpath-functions.png" text="Browse available XPath functions" >}}

The tab has a **"Filter functions…"** input at the top — type part of a function name to narrow the list across all categories instantly.

> [!TIP]
> You can also collapse function categories by clicking the chevron next to the category header.
> {{< image-sh src="datamapper-xpath-functions-collapse.png" text="Click chevron to collapse a category" >}}

2. **Drag the function** you need and drop it into the editor

{{< image-sh src="datamapper-xpath-functions-dnd.png" text="Drag and drop functions" >}}

3. **Fill in the function parameters** with field references or literal values

### Saving Your Expression

Once you've built your XPath expression, click the **Close** button to apply it to the mapping.

{{< image-sh src="datamapper-xpath-close.png" text="Close editor to save expression" >}}

The mapping will now appear in the tree view with your custom XPath expression.

{{< image-sh src="datamapper-xpath-done.png" text="Completed XPath mapping" >}}

> [!TIP]
> Start with simple expressions and test them before adding complexity. You can always reopen the XPath Editor to refine your expression.

---

## Auto-Completion

The expression editor supports **IntelliSense-style auto-completion** for XPath functions. As you type a function name, a suggestion list appears automatically. You can also trigger it explicitly by pressing **Ctrl+Space**.

{{< image-sh src="datamapper-xpath-completion.png" text="Function Completion" >}}

Each suggestion shows:
- The **function name** as the completion label
- The **full function signature** (parameters and return type) as detail text
- A **description** of what the function does

Selecting a suggestion inserts the function name followed by an argument placeholder so the cursor lands inside the parentheses, ready for you to type or drag in a field reference.

> [!TIP]
> Auto-completion works for all 15 function categories in the XPath 3.1 catalog. It also completes XPath **keywords** such as `return`, `satisfies`, `instance of`, and `treat as`.

---

## Hover Help

Hovering the cursor over any function name in the expression editor shows a **tooltip** with:
- The complete function **signature** (parameter names, types, and return type)
- A **description** of the function's behaviour

{{< image-sh src="datamapper-xpath-hover.png" text="Function Hover Help" >}}

This is useful when you remember a function name but need a quick reminder of the argument order or expected types without leaving the editor.

---

## Next Steps

- **[Variables](../06-variables/)** — define `xsl:variable` values that can be referenced in XPath expressions
- **[Field Context Menu](../08-field-context-menu/)** — advanced schema-level operations such as type overrides and abstract element substitution