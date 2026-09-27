---
title: "DataMapper Settings"
description: "Configure DataMapper output options such as the XML declaration"
date: 2026-09-25
weight: 9
---

## Overview

The **DataMapper Settings** modal lets you control how the generated XSLT stylesheet serialises its output. Open it by clicking the gear (⚙) icon in the **target body** header on the right side of the DataMapper canvas.

{{< image-sh src="dm-settings-modal.gif" text="DataMapper Settings modal — open via the gear icon in the target body header" >}}

---

## XML Declaration

When the target body document is an **XML Schema** type, the modal shows an **XML Declaration** section with an **"Omit XML declaration"** checkbox.

| Checkbox state | Effect on generated XSLT |
|---|---|
| Unchecked (default) | `<xsl:output>` does not set `omit-xml-declaration`, so the XML processor may emit `<?xml version="1.0" encoding="UTF-8"?>` |
| Checked | `<xsl:output omit-xml-declaration="yes"/>` is added to the stylesheet — the declaration is suppressed in the output |

> [!NOTE]
> The **"Omit XML declaration"** option is only enabled when the target body document type is XML Schema. When the target body is JSON or a primitive type, the checkbox is shown but greyed out because XML output declarations do not apply.

### When to omit the XML declaration

Omit the XML declaration when:
- The transformation output is embedded as a fragment inside another XML document
- A downstream system expects pure XML content without a processing declaration
- An HTTP response body must not start with `<?xml …?>`

Leave the checkbox unchecked (default) to let the XSLT processor follow its own default behaviour, which typically includes the declaration.

---

## Saving and Cancelling

Click **Save** to apply your changes. Click **Cancel** (or close the modal) to discard any changes made since the modal was opened.

---

## Next Steps

- **[Field Context Menu](../08-field-context-menu/)** — type overrides and abstract element substitution
- **[Creating Mappings](../03-creating-mappings/)** — return to the mapping workflow overview
