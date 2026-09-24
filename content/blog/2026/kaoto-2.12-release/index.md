---
title: "Kaoto 2.12 release"
date: 2026-09-23
summary: Kaoto 2.12 is available.
authors:
  - djelinek
  - lhein
  - mmelko
tags:
  - Kaoto
  - Release
  - Kaoto 2.12
aliases:
  - /blog/kaoto-2.12-release/
---

## What's New?

This release introduces an experimental Infrastructure view for managing Camel infrastructure services directly from VS Code, expands the DataMapper with more flexible mapping options and improved schema support, and improves working with custom Kamelets. Kaoto 2.12 includes support for [Apache Camel](https://camel.apache.org) 4.22.1.

### Infrastructure View (Experimental)

Kaoto 2.12 introduces an experimental Infrastructure view for starting, monitoring, and stopping databases, message brokers, and other Camel infrastructure services directly from VS Code using `camel infra`.

**This feature is experimental and hidden by default.** Enable `kaoto.infrastructure.enabled` in your VS Code settings to try it out.

{{< figure src="settings-experimental.png" alt="Settings page for enabling the experimental Infrastructure view" caption="Kaoto settings for the experimental Infrastructure view" class="image" >}}

- **Start Services** - Click the **+** button to choose a service and optionally set a custom port. Kaoto checks that Docker or Podman is available. If the service is already running outside VS Code, you can use the existing instance or stop and restart it.
- **Monitor Services** - View each service's status and port, with automatic refresh while services are running. Stop a service from the view with a confirmation dialog to prevent accidental stops.
- **View Logs** - Open a service's dedicated terminal to inspect its output.
- **Copy Connection Details** - Copy a service's URL or port to use in your integration configuration.

{{< figure src="infra-endpoints.png" alt="Infrastructure view showing a running service" caption="Manage running services in the Infrastructure view" class="image" >}}

### DataMapper Enhancements

The DataMapper adds more flexible mapping instructions, improved XPath editing, and expanded support for complex XML schemas.

**XPath 3.1 and XSLT 3.0 Functions**

The XPath expression editor provides more guidance when writing mapping expressions:

- **Function Completion** - Get function suggestions with signatures and descriptions as you type.
- **Hover Help** - Hover over a recognized function name to read its documentation.
- **Expanded Function Catalog** - Access XPath 3.1 and XSLT 3.0 functions, including math, map, array, and higher-order functions.

{{< figure src="dm-expression-editor.gif" alt="XPath expression editor in the DataMapper" caption="Write mapping expressions with the XPath expression editor" class="image" >}}

**Advanced Schema and Type Support**

- **Collection Abstract Fields** - Abstract and choice wrapper fields with `maxOccurs > 1` are now treated as collections, so substituted elements can be iterated correctly.

{{< figure src="dm-collection-abstract.gif" alt="DataMapper showing abstract fields with collection support" caption="Abstract and choice wrapper fields with maxOccurs > 1 as collections" class="image" >}}

- **Sequence Choices** - Select an `xs:sequence` branch within an `xs:choice` field. Change or clear selections from the context menu, with support for nested choices and inherited collection and cardinality constraints.

{{< figure src="dm-sequence-in-choice.gif" alt="DataMapper showing xs:sequence selection within xs:choice field" caption="Select an xs:sequence branch within an xs:choice field" class="image" >}}

- **Abstract Type Detection** - The DataMapper detects wrapper field selections and substitutions from XSLT and removes user-created fields that are no longer valid.
- **Type Overrides** - Generated XSLT now includes `xsi:type` attributes for compatible type overrides, allowing XML Schema validators to identify the selected type. The Field Override modal now uses a typeahead selector to search and filter available types as you type.

**Variables and Grouping**

- **Variables** - Use local and global `xsl:variable` definitions as mapping sources and reference them in XPath expressions.

{{< figure src="dm-variables.gif" alt="DataMapper Variables panel with local and global xsl:variable support" caption="Use xsl:variable definitions as mapping sources" class="image" >}}

- **Grouping and Sorting** - Create collection mappings with `xsl:for-each-group` and configure sorting with `xsl:sort`.

{{< figure src="dm-for-each-group.gif" alt="DataMapper configuring xsl:for-each-group mapping" caption="Configure grouping strategy and sort keys with xsl:for-each-group" class="image" >}}

**Enhanced Mapping Context Menu**

- **Value and Copy Selectors** - Add `xsl:value-of` and `xsl:copy-of` instructions from the mapping context menu, or use `Duplicate` to add multiple mappings to a collection target field.
- **Mapping Instructions** - Use the new `Wrap with Instruction` and `Inner Instruction` submenus to control how mapping instructions are nested.
- **Complex Field Expressions** - Primitive target fields can now use a full XPath expression as their value, not just a direct field reference.

{{< figure src="dm-context-menu.png" alt="DataMapper context menu showing mapping options" caption="New mapping options in the DataMapper context menu" class="image" >}}

**UX Improvements and Fixes**

- **XML Declaration Control** - A new settings modal lets you control whether the generated XSLT output includes an XML declaration header (`<?xml version="1.0"?>`).

{{< figure src="dm-settings-modal.gif" alt="DataMapper Settings modal with Omit XML declaration checkbox" caption="Control XML declaration output from the DataMapper settings" class="image" >}}

- **Field Info Popover** - Click any schema field to see its XSD type, cardinality, and description in a popover.

{{< figure src="dm-field-popover.png" alt="DataMapper source panel with field info popover showing type and cardinality" caption="View field type and cardinality details in a popover" class="image" >}}

- **Cleaner Mapping View** - Unconfigured wrapper children are hidden by default to reduce visual noise.
- Fixed field expansion state being lost when the first mapping was created
- Fixed mixed content (text + elements) rendering and `value-of`/`copy-of` consistency
- Fixed XSD type alias resolution (e.g. `xs:string` ↔ `xsd:string`) for field overrides
- Removed the XSLT catalog entry from the catalog dropdown to avoid confusion

### Custom Kamelet Improvements

Kaoto now treats your Kamelets like catalog citizens. Working with custom Kamelets is easier with these updates:

- **Workspace Kamelets** - Custom Kamelets in your workspace are automatically available in the catalog so you place it on any route and tune properties per step through configuration forms.
- **Live Property Refresh** - Changes to a custom Kamelet's properties now appear in the configuration forms of routes that use it, without reopening the route file.
- **Paste Support** - Pasting a Kamelet or Pipe now restores its complete definition, including beans, error handlers, and metadata.

{{< figure src="kamelet-catalog.png" alt="Shows a local Kamelet in the Kaoto Catalog" caption="Access and use your local Kamelets directly in your routes" class="image" >}}

### a2aSubTask EIP Support

The `a2aSubTask` (Agent-to-Agent Sub Task) EIP now appears as a step container on the canvas, like `aggregate`, `split`, and `saga`. You can add and manage its nested steps visually.

{{< figure src="a2asubtask.png" alt="Camel route with two a2aSubTask containers wrapping Elasticsearch and bean steps" caption="Organize route steps in A2A Sub Task containers" class="image" >}}

The route shown above is based on an example from the [Apache Camel documentation](https://camel.apache.org/components/4.22.x/others/a2a-consumer.html#_scoped_progress_updates_with_a2asubtask).

---

## Catalog Version

Kaoto 2.12 includes the **Apache Camel 4.22.1** catalog, providing components, EIPs, and Kamelet definitions for this Camel version.

For a full list of changes, please refer to the [change log](https://github.com/KaotoIO/kaoto/releases/tag/2.12.0).

---

## Let's Build it Together

Let us know what you think by joining us in the [GitHub discussions](https://github.com/orgs/KaotoIO/discussions).
Do you have an idea how to improve Kaoto? Would you love to see a useful feature implemented or simply ask a question? Please [create an issue](https://github.com/KaotoIO/kaoto/issues/new/choose).

## A big shoutout to our amazing contributors

Thank you to everyone who made this release possible!

Whether you are contributing code, reporting bugs, or sharing feedback in our [GitHub discussions](https://github.com/orgs/KaotoIO/discussions), your involvement is what keeps the Camel riding! 🐫🎉

### New Contributors

We're excited to welcome new contributors to the Kaoto community:

* [@AmIrRX0](https://github.com/AmIrRX0) made their first contribution in [#3840](https://github.com/KaotoIO/kaoto/pull/3840)
* [@atirna](https://github.com/atirna) made their first contribution in [#3787](https://github.com/KaotoIO/kaoto/pull/3787)
* [@AysajanE](https://github.com/AysajanE) made their first contribution in [#3478](https://github.com/KaotoIO/kaoto/pull/3478)
* [@brian-soltani](https://github.com/brian-soltani) made their first contribution in [#3591](https://github.com/KaotoIO/kaoto/pull/3591)
* [@chrisriv10](https://github.com/chrisriv10) made their first contribution in [#3827](https://github.com/KaotoIO/kaoto/pull/3827)
* [@ConsultingFuture4200](https://github.com/ConsultingFuture4200) made their first contribution in [#3540](https://github.com/KaotoIO/kaoto/pull/3540)
* [@etzel-mes](https://github.com/etzel-mes) made their first contribution in [#3469](https://github.com/KaotoIO/kaoto/pull/3469)
* [@Indo86](https://github.com/Indo86) made their first contribution in [#3941](https://github.com/KaotoIO/kaoto/pull/3941)
* [@Jinal-Sarvaiya](https://github.com/Jinal-Sarvaiya) made their first contribution in [#3483](https://github.com/KaotoIO/kaoto/pull/3483)
* [@MFA-G](https://github.com/MFA-G) made their first contribution in [#3758](https://github.com/KaotoIO/kaoto/pull/3758)
* [@nveces](https://github.com/nveces) made their first contribution in [#3276](https://github.com/KaotoIO/kaoto/pull/3276)
* [@plain-wind](https://github.com/plain-wind) made their first contribution in [#3831](https://github.com/KaotoIO/kaoto/pull/3831)
* [@snowyukitty](https://github.com/snowyukitty) made their first contribution in [#3576](https://github.com/KaotoIO/kaoto/pull/3576)
* [@soosoo34](https://github.com/soosoo34) made their first contribution in [#3587](https://github.com/KaotoIO/kaoto/pull/3587)
* [@UlikGames](https://github.com/UlikGames) made their first contribution in [#3595](https://github.com/KaotoIO/kaoto/pull/3595)


---

## Give it a try

* Kaoto [quickstart](/docs/quickstart/).
* Kaoto is available as a [VS Code extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto).
* Kaoto [showcase deployment](https://red.ht/kaoto).