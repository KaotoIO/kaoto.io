---
title: "Kaoto 2.11 release"
date: 2026-06-10
summary: Kaoto 2.11 is available.
authors: 
  - lordrip
  - igarashitm
  - PVinaches
  - djelinek
tags:
  - Kaoto
  - Release
  - Kaoto 2.11
---

## What's New?

This release brings significant enhancements to testing capabilities with Citrus framework integration, expanded DataMapper functionality for complex schema handling, and improved runtime management. Powered by Apache Camel 4.20.0, Kaoto continues to make visual integration design more powerful and intuitive.

### Citrus Testing Capabilities

Kaoto 2.11 introduces comprehensive Citrus framework integration, bringing automated testing capabilities directly into your visual integration design workflow. Build and manage Citrus tests alongside your Apache Camel routes, ensuring your integrations work correctly through behavior-driven testing.

**Visual Test Design**

- **Citrus Test Support** - Full integration with the Citrus testing framework, enabling you to create and manage automated tests directly within Kaoto's visual interface

{{< figure src="kaoto-extension.png" alt="Kaoto VS Code extension showing Citrus test integration" caption="Kaoto VS Code extension with Citrus testing support" class="image" >}}

- **Dedicated Test Icons** - Visual indicators for Citrus test actions make it easy to identify and distinguish test components from regular integration steps in your flows
- **Test Action Library** - Access to Citrus test actions (send, receive, echo, sleep, etc.) through Kaoto's component catalog, allowing you to build test scenarios visually

{{< figure src="test-icons.png" alt="Visual indicators for Citrus test actions in the component catalog" caption="Dedicated icons for Citrus test actions" class="image" >}}

**Test Configuration and Management**

- **Citrus Endpoint Configuration** - Specialized configuration fields for Citrus Endpoints, providing a streamlined interface for defining test endpoints with proper protocols and message formats
- **Standard Property Forms** - Configure test actions using Kaoto's familiar property forms, maintaining consistency with how you configure Camel components
- **YAML/XML Serialization** - Tests are serialized to standard Citrus YAML or XML format, making them portable and compatible with the broader Citrus ecosystem

{{< figure src="test-forms.png" alt="Configuration form for Citrus test actions" caption="Citrus test action configuration using Kaoto property forms" class="image" >}}

**Integrated Testing Workflow**

- **Side-by-Side Development** - Create tests in the same workspace as your integration routes, keeping test scenarios close to the code they validate
- **Visual Test Organization** - Manage test files through Kaoto's file explorer, with clear visual distinction between integration routes and test definitions
- **Test Execution** - Run Citrus tests directly from Kaoto's interface to validate your integration behavior during development

This feature bridges the gap between integration development and testing, allowing you to validate your Camel routes with behavior-driven testing capabilities while maintaining the visual approach that makes Kaoto powerful.

### Catalog and Runtime Management

Enhanced runtime and catalog management capabilities provide better control over your development environment, giving you the flexibility to choose how you execute and test your integrations.

**Multiple Execution Options**

Kaoto 2.11 introduces support for multiple executors, allowing you to choose the best runtime approach for your workflow:

- **Camel CLI (Default)** - The traditional and stable Camel JBang CLI executor provides reliable integration execution with full Camel JBang feature support. This is the recommended option for most users, offering proven stability and comprehensive Camel runtime capabilities
  
- **Camel Launcher (Experimental)** - A new experimental executor that offers an alternative execution approach. This feature is under active development and provides early access to upcoming runtime improvements. Perfect for users who want to explore new capabilities and provide feedback on future execution features

{{< figure src="settings.png" alt="Kaoto settings showing executor selection between Camel CLI and Camel Launcher" caption="Multiple executor options in Kaoto settings" class="image" >}}

**Why Multiple Executors Matter**

Different development scenarios benefit from different execution approaches. The Camel CLI excels at production-like testing with full JBang capabilities, while the experimental Camel Launcher explores new execution patterns that may offer performance or feature advantages in the future. Having both options ensures you can choose the right tool for your specific needs while maintaining backward compatibility.

**Centralized Configuration**

- **Settings-Based Catalog Versions** - Catalog versions are now read from settings, providing centralized version management across your workspace. This ensures consistency when working with multiple integration files and makes it easier to upgrade or switch between Camel versions
  
- **Custom Run Arguments** - Override default run arguments to fine-tune execution behavior. Add custom JVM options, enable specific Camel features, or configure runtime parameters without modifying your integration files

{{< figure src="run-arguments.png" alt="Custom run arguments configuration interface" caption="Override default run arguments for fine-tuned execution" class="image" >}}
  
- **Camel JBang 4.20.0** - Upgraded default Camel JBang version from 4.18.0 to 4.20.0, bringing the latest Camel features, performance improvements, and bug fixes to your development environment

### DataMapper Enhancements

The DataMapper has received substantial improvements for handling complex data transformation scenarios:

**Rendering Engine Re-invented**

Kaoto DataMapper rendering engine has been re-invented to be enterprise-grade — with virtual scrolling and browser-native rendering, you can flawlessly navigate through large data mappings with complex document schema structures.

---Video for complex mapping with scrolling

**Advanced Schema Support**
- **Field Override** - Support for overriding a document field or its type where it's compatible. Complex XML schema uses `Substitution Group` to allow element substitution, and `xs:extension`/`xs:restriction` to declare hierarchical type definitions. Kaoto DataMapper now offers to leverage this extensibility where the schema definition allows. Right-clicking on the document field offers override options
- **Abstract Elements** - An abstract element now shows its substitution candidates as children in the document tree, enabling direct mapping from/to the substituted fields
- **Choice Improvements** - Enhanced `xs:choice` support with dedicated context menu for choosing from choice options. Right-clicking on the document field offers choice options

---Video for choice improvements

- **Nillable Attributes** - Support for `xs:element nillable` attribute, properly handling nullable fields as declared in the XML schema
- **And more to come...** We continue working on improving complex document/mapping support. Further improvements to Abstract Elements support are on the way

**UI/UX Improvements**
- **Auto Mapping** - Several auto mapping options through Drag and Drop have been added:
  - Source collection field to target collection field: `for-each` mapping is automatically created
  - Container field to Container field: Automatically creates appropriate mappings, it either uses `xsl:copy-of` or creates mappings for individual children
- **Double-Click Editing** - If you're familiar with XPath, just double-click the target field and write the XPath expression right away

---Video for editing

- **Delete Key Support** - Delete data mapping item by pressing the Delete key for faster workflow
- Allow renaming XSLT file associated with Kaoto DataMapper step
- Allow to collapse the function list in XPath editor
- Highlight the selected field border, not only its title

**Other XSLT improvements**
- **XSLT Comments** - Ability to add comments into generated XSLT for better documentation. Once a comment is added, a comment icon appears on the mapping element — hover over it to see the comment in a tooltip
- Added `exclude-result-prefixes` to generated XSLT to prevent namespace leakage into transformed target XML instance

---Video for ccomments

### Canvas and Visual Editor Enhancements

Building integrations is now more intuitive with these canvas improvements:

- **Route AutoStartup Toggle** - Toggle switch in the title bar for controlling route autoStartup property

{{< figure src="autostartup-toggle.png" alt="Toggle switch in route title bar for controlling autoStartup property" caption="Route autoStartup toggle in the title bar" class="image" >}}

- **Space Bar Navigation** - Move the canvas by pressing and holding the Space bar for easier navigation
- **Container Selection Styles** - Visual styles for selected containers in NodeContainer for better feedback

{{< figure src="selection-colors.png" alt="Visual feedback when moving selected element highliting the possible drop zones" caption="Visual feedback when moving selected element highliting the possible drop zones" class="image" >}}

{{< figure src="selection-colors-container.png" alt="Visual feedback when moving selected containers highliting the possible drop zones" caption="Visual feedback when moving selected containers highliting the possible drop zones" class="image" >}}

### REST DSL and OpenAPI Support

- **Property Search Filter** - Search functionality in RestDslEditor for quickly finding properties

{{< figure src="rest-search.png" alt="Search functionality in REST DSL editor for filtering properties" caption="Property search filter in REST DSL editor" class="image" >}}

- **Accessible REST Editor** - REST DSL editor built with resizable split panels featuring improved accessibility
- **Improved OpenAPI Support** - Enhanced OpenAPI file handling with automatic detection of `*openapi.yml` files and flexible API URL imports without file extension restrictions

### Forms and Configuration

Configuration forms have been enhanced for better usability:

- **Custom Properties Configuration** - Support for key/value configuration format for endpoint properties in components like To, ToD, and other endpoint-based components, providing a more intuitive way to configure component parameters

{{< figure src="toD.png" alt="ToD component showing key/value configuration format for endpoint properties" caption="Custom properties configuration in ToD component" class="image" >}}

{{< figure src="kamelet-comp.png" alt="Kamelet component showing key/value configuration format for parameters" caption="Custom properties configuration in Kamelet component" class="image" >}}

---

## Bug Fixes

### DataMapper Fixes

**Visual and Layout Issues**
- Fixed after/before icons dependency on layout
- Resolved parent node collapse when choice node chevron is clicked
- Fixed grabbing icon showing after schema is attached
- Reduced dragged item size to improve usability
- Restored panel headers (Source and Target)
- Fixed tree node indentation for non-expandable children
- Corrected abstract field indentation
- Removed vertical scrollbar in XPath editor when content fits

**Mapping and Field Management**
- Consolidated mapping action capability checks into actions
- Fixed InstructionItem targeted field item removal
- Corrected primitive document content and document root rendering
- Synchronized mapping lines on window resize when editor changes size
- Avoided state update in useDataMapperDeleteHotKey hook
- Fixed mapping refresh timing
- Skipped rendering nested choice node if both are selected
- Synchronized param lines on add with no attached schema in SourcePanel
- Show delete button for target node added by "Add Mapping"
- Show inner choice members in nested choice context menu

**Schema and Substitution**
- Implemented substitution field logic (S.1, S.2, S.3)
- Restricted dragged container to be dropped into compatible sub-containers
- Use solid line for primitive params without schema
- Sort substitution group members deterministically

**UI and Interaction**
- Changed the pencil icon for launching XPath Editor
- Fixed export mapping dropdown item close on modal open

### Canvas and Visualization Fixes
- Fixed route alignment when created from an empty canvas
- Restricted container drag area to header only

### OpenAPI and File Handling

- Fixed JSON OpenAPI files detection and file validation

### UI and Responsiveness

- Fixed responsiveness navigation

---

## Catalog Version

Kaoto 2.11 includes support for:

- **Camel Main** - 4.20.0, 4.18.2, 4.14.5, 4.10.7
- **Camel extensions for Quarkus** - 3.35.0, 3.33.1, 3.27.4, 3.20.4 
- **Camel Spring Boot** - 4.20.0, 4.18.2, 4.14.7, 4.10.9
- **Citrus** - 4.10.0, 4.10.1

---

## Let's Build it Together

Let us know what you think by joining us in the [GitHub discussions](https://github.com/orgs/KaotoIO/discussions).
Do you have an idea how to improve Kaoto? Would you love to see a useful feature implemented or simply ask a question? Please [create an issue](https://github.com/KaotoIO/kaoto/issues/new/choose).

---

## A big shoutout to our amazing contributors

Thank you to everyone who made this release possible!

Whether you are contributing code, reporting bugs, or sharing feedback in our [GitHub discussions](https://github.com/KaotoIO/kaoto/discussions), your involvement is what keeps the Camel riding! 🐫🎉

### New Contributors

We're excited to welcome new contributors to the Kaoto community:

* [@matheusandre1](https://github.com/matheusandre1) made their first contribution in [#3079](https://github.com/KaotoIO/kaoto/pull/3079)
* [@pvillant](https://github.com/pvillant) made their first contribution in [#3128](https://github.com/KaotoIO/kaoto/pull/3128)
* [@filip-stanojkovic](https://github.com/filip-stanojkovic) made their first contribution in [#3255](https://github.com/KaotoIO/kaoto/pull/3255)
* [@akagifreeez](https://github.com/akagifreeez) made their first contribution in [#3273](https://github.com/KaotoIO/kaoto/pull/3273)
* [@rukman7](https://github.com/rukman7) made their first contribution in [#3283](https://github.com/KaotoIO/kaoto/pull/3283)

---

## Give it a try

* Kaoto [quickstart](/docs/quickstart/).
* Kaoto is available as a [VS Code extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto).
* Kaoto [showcase deployment](https://red.ht/kaoto).