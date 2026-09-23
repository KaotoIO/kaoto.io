---
title: "Kaoto 2.12 release"
date: 2026-09-23
summary: Kaoto 2.12 is available.
authors: 
  - djelinek
  - lhein
tags:
  - Kaoto
  - Release
  - Kaoto 2.12
aliases:
  - /blog/kaoto-2.12-release/
---

## What's New?

**This release delivers three headline themes:**

* a brand-new **Infrastructure view** for managing Camel infra services directly from VS Code
* a dramatically more powerful **DataMapper** with an enriched mapping context menu, full `xsl:variable` and `xsl:for-each-group` support, advanced schema handling (substitution groups, abstract types, `xs:choice` sequences, `xsi:type` generation), and an upgraded XPath editor with XSLT 3.0 / XPath 3.1 function completion
* and a set of **canvas and editor improvements** including custom Kamelet live refresh and `a2aSubTask` EIP support. 

*All powered by Apache Camel 4.22.1.*

## Infrastructure View (experimental)

A brand-new Infrastructure view has been added to the Kaoto sidebar. It integrates with `camel infra` to let you start, monitor, and stop Camel infrastructure services (databases, message brokers, and other backing services) without leaving VS Code.

**This feature is experimental and hidden by default**. To try it out, enable the `kaoto.infrastructure.enabled` setting in your VS Code settings.

{{< figure src="settings-experimental.png" alt="Settings page for enabling the experimental Camel Infa section" caption="Kaoto Settings for Experimental Infrastructure feature" class="image" >}}

**Start infrastructure services**

Click the **+** button in the Infrastructure view toolbar to pick a service from the list of all services available via camel infra. You can optionally specify a custom port before the service starts — leave it empty to use the service default.

* The extension detects when a **container runtime** (Docker or Podman) is not available and shows a clear error message instead of a cryptic failure
* If a service is **already running externally** (started outside VS Code), you are prompted to either use the existing instance or stop and restart it

**Monitor and manage running services**

Each running service is shown as a tree item with its name, port (if known), and a status indicator (`starting`, `running`, or `stopping`). While at least one service is running, the view automatically refreshes to keep status up to date.

* **Stop** — hover over a service and click the stop button; a confirmation dialog prevents accidental stops
* **Show logs** — opens the dedicated VS Code terminal for the service so you can inspect its output
* **Copy URL / Copy port** — one-click clipboard actions for quickly wiring a service address into your integration configuration

{{< figure src="infra-endpoints.png" alt="Infrastructure view showing a launched service" caption="The Infrastructure view of Kaoto" class="image" >}}

## DataMapper Enhancements

### Enhanced mapping context menu
* `Add copy selector` / `Add value selector ` / `Duplicate` mapping context menu - Mapping context menu now offers `Add value selector` to add `xsl:value-of`, `Add copy selector` to add `xsl:copy-of` and `Duplicate` to add multiple mappings on a collection target field
* `Wrap with Instruction` / `Inner Instruction`  mapping context menu - `Wrap with Instruction` and `Inner Instruction` sub categories are added to the mapping context menu, offering more flexible mapping instruction control
* **Double click short cut for adding a mapping** - if you double click the target field, input field is shown right away to quickly write down a mapping XPath expression

{{< figure src="dm-context-menu.png" alt="Showing the context menu for enhanced mappings" caption="Data Mapper with context menu for enhanced mappings" class="image" >}}

### XPath 3.1 & XSLT 3.0 Functions

The XPath expression editor has been significantly upgraded:

* **Function completion** — autocomplete suggestions for all XPath functions, including their signatures and descriptions, appear as you type
* **Hover help** — hovering over a recognised function name shows its documentation inline
* **XSLT 3.0 / XPath 3.1 function catalog** — a comprehensive catalog of function categories is now available, covering Math, Map, Array, Higher-Order functions, and XSLT-specific constructs

{{< figure src="dm-expression-editor.gif" alt="Showing the xpath expression editor in the Data Mapper" caption="Data Mapper with an open XPath expression editor" class="image" >}}

### Advanced Schema & Type Support
Several long-standing schema edge cases are now fully handled:

* `xs:sequence` inside `xs:choice` — you can now select a sequence branch within a choice field; Change/Clear context menu options, collection/cardinality inheritance, and nested choice clearing all work correctly
* `xsi:type` attribute generation — the XSLT output now emits `xsi:type` attributes when a SAFE type override is active, making the output self-documenting and allowing XML Schema validators to follow the type hierarchy without schema regeneration
* **Abstract type auto-detection** — XSLT-based auto-detection of wrapper field selections and substitutions, with automatic pruning of user-created fields that are no longer valid

### Variables & Grouping
* `xsl:variable` support — `xsl:variable` is now fully supported. variables defined inside the mapping context as well as the global level variables can now be used as source document nodes, mapped and referenced just like body or parameter fields
* `xsl:for-each-group` support — `xsl:for-each-group` is now fully supported including `xsl:sort`. It allows to create complex collection mapping with grouping and sort functionality enabled

## Custom Kamelet Improvements
Several quality-of-life fixes land for users who author and use custom Kamelets:

* **Live property refresh** — editing a custom Kamelet file on disk now immediately reflects new or changed properties in the config form of any route that uses it, without having to close and reopen the route file. Previously the stale cached definition was returned on every subsequent selection
* **Workspace Kamelets surfaced via VS Code API** — the extension now feeds workspace-local Kamelet files into the dynamic catalog pipeline through the editor channel API, so custom Kamelets are available to the catalog and form resolution without any manual configuration
* **Paste support for Kamelet templates** — copying and pasting a Kamelet or Pipe now correctly applies the pasted definition and rebuilds all child entities (beans, error handler, metadata) instead of leaving a blank canvas

## a2aSubTask EIP Support
The `a2aSubTask` (Agent-to-Agent Sub Task) EIP now renders correctly as a **step container** on the canvas, consistent with other container EIPs such as `aggregate`, `split`, and `saga`. Nested steps inside `a2aSubTask` can be added and managed visually.

## Catalog Version

This release ships with the **Apache Camel 4.22.1** catalog (`@kaoto/camel-catalog 0.10.4`), bringing the latest components, EIPs, and Kamelet definitions from the Apache Camel community.

For a full list of changes please refer to the [change log](https://github.com/KaotoIO/kaoto/releases/tag/2.12.0).

## Let's Build it Together

Let us know what you think by joining us in the [GitHub discussions](https://github.com/orgs/KaotoIO/discussions).
Do you have an idea how to improve Kaoto? Would you love to see a useful feature implemented or simply ask a question? Please [create an issue](https://github.com/KaotoIO/kaoto/issues/new/choose).

## A big shoutout to our amazing contributors

Thank you to everyone who made this release possible!

Whether you are contributing code, reporting bugs, or sharing feedback in our [GitHub discussions](https://github.com/KaotoIO/kaoto/discussions), your involvement is what keeps the Camel riding! 🐫🎉

### New Contributors

We're excited to welcome new contributors to the Kaoto community:

* [@AmIrRX0](https://github.com/AmIrRX0) made their first contribution in [#3840](https://github.com/KaotoIO/kaoto/pull/3840)
* [@AysajanE](https://github.com/AysajanE) made their first contribution in [#3478](https://github.com/KaotoIO/kaoto/pull/3478)
* [@ConsultingFuture4200](https://github.com/ConsultingFuture4200) made their first contribution in [#3540](https://github.com/KaotoIO/kaoto/pull/3540)
* [@Indo86](https://github.com/Indo86) made their first contribution in [#3941](https://github.com/KaotoIO/kaoto/pull/3941)
* [@Jinal-Sarvaiya](https://github.com/Jinal-Sarvaiya) made their first contribution in [#3483](https://github.com/KaotoIO/kaoto/pull/3483)
* [@MFA-G](https://github.com/MFA-G) made their first contribution in [#3758](https://github.com/KaotoIO/kaoto/pull/3758)
* [@UlikGames](https://github.com/UlikGames) made their first contribution in [#3595](https://github.com/KaotoIO/kaoto/pull/3595)
* [@atirna](https://github.com/atirna) made their first contribution in [#3787](https://github.com/KaotoIO/kaoto/pull/3787)
* [@brian-soltani](https://github.com/brian-soltani) made their first contribution in [#3591](https://github.com/KaotoIO/kaoto/pull/3591)
* [@chrisriv10](https://github.com/chrisriv10) made their first contribution in [#3827](https://github.com/KaotoIO/kaoto/pull/3827)
* [@etzel-mes](https://github.com/etzel-mes) made their first contribution in [#3469](https://github.com/KaotoIO/kaoto/pull/3469)
* [@nveces](https://github.com/nveces) made their first contribution in [#3276](https://github.com/KaotoIO/kaoto/pull/3276)
* [@plain-wind](https://github.com/plain-wind) made their first contribution in [#3831](https://github.com/KaotoIO/kaoto/pull/3831)
* [@snowyukitty](https://github.com/snowyukitty) made their first contribution in [#3576](https://github.com/KaotoIO/kaoto/pull/3576)
* [@soosoo34](https://github.com/soosoo34) made their first contribution in [#3587](https://github.com/KaotoIO/kaoto/pull/3587)


---

## Give it a try

* Kaoto [quickstart](/docs/quickstart/).
* Kaoto is available as a [VS Code extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto).
* Kaoto [showcase deployment](https://red.ht/kaoto).