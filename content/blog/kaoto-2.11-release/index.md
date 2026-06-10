---
title: "Kaoto 2.11 release"
date: 2026-06-10
summary: Kaoto 2.11 is available.
authors: 
  - djelinek
  - igarashitm
  - PVinaches
  - lordrip
tags:
  - Kaoto
  - Release
  - Kaoto 2.11
---

## What's New?

This release brings significant enhancements to testing capabilities with Citrus framework integration, expanded DataMapper functionality for complex schema handling, and improved runtime management. Powered by Apache Camel 4.20.0, Kaoto continues to make visual integration design more powerful and intuitive.

### Citrus Testing Capabilities

Kaoto 2.11 introduces comprehensive Citrus framework integration for automated testing of your Apache Camel integrations:

- **Citrus Test Support** - Full integration with the Citrus testing framework, enabling you to create, manage, and execute automated tests directly within Kaoto
- **Visual Test Actions** - Dedicated icons for Citrus test actions, making it easy to identify and work with test components in your integration flows
- **Custom Test Fields** - Specialized configuration fields for Citrus Endpoints and MessageBody, streamlining test setup and configuration

This feature bridges the gap between integration development and testing, allowing you to validate your Camel routes with enterprise-grade testing capabilities.

VIDEO SHOWING CITRUS CAPABILITIES IN KAOTO


### Catalog and Runtime Management

Enhanced runtime and catalog management capabilities provide better control over your development environment:

- **Multiple Executors** - Support for both Camel CLI and experimental new feature Camel Launcher, giving you flexibility in how you run your integrations
- **Settings-Based Catalog Versions** - Catalog versions are now read from settings, providing centralized version management
- **Custom Run Arguments** - Users can now overwrite default run arguments for greater control over execution
- **Camel JBang 4.20.0** - Upgraded default Camel JBang version from 4.18.0 to 4.20.0

FIGURE OF SETTINGS PAGE


### DataMapper Enhancements

The DataMapper has received substantial improvements for handling complex data transformation scenarios:

**Advanced Schema Support**
- **Abstract Elements** - Full support for abstract element and abstract complexType definitions, enabling more flexible schema designs
- **Nillable Attributes** - Support for `xs:element nillable` attribute, properly handling nullable fields in XML schemas
- **Choice Improvements** - Enhanced `xs:choice` support with dedicated ChoiceSelectionService for better choice element handling
- **Circular Includes** - Support for circular `xs:include` references, allowing complex schema dependency graphs
- **Include Resolution** - Fixed `xs:include` resolution for same file names in different directories

**Literal and Expression Support**
- **Literal Deserialization** - DataMapper now supports literal value deserialization for direct value mapping
- **XSLT Comments** - Ability to add comments into generated XSLT for better documentation
- **Namespace Management** - Added `exclude-result-prefixes` to generated XSLT to prevent namespace leakage

**Field and Element Management**
- **Field Type Override UI** - Visual interface for overriding field types when needed
- **Element Substitution UI** - Dedicated UI for managing element substitution groups
- **Abstract Field Substitution** - Context menu support for substituting abstract fields with concrete implementations
- **Double-Click Editing** - Quick field editing via double-click for improved workflow
- **Choice Context Menu** - Specialized context menu for working with choice elements

**Collection and Container Handling**
- **Collection Semantics** - Members of collection choice now properly inherit collection semantics
- **For-Each Wrapping** - Collection choice mappings are automatically wrapped with for-each constructs
- **Container Auto Mapping** - Intelligent auto-mapping for container elements

**File Management**
- **Resource Existence Check** - New `isResourceExist` method in metadata API for validating resources
- **XSLT Recovery** - XSLT file recovery and rename functionality for better file management

**UI/UX Improvements**

The DataMapper interface has been refined for better usability:

- **Virtual Scrolling** - Improved performance when working with large schemas through virtual scrolling
- **Collapsed Collections** - Drag and drop now shows collections in collapsed state for cleaner visualization
- **Delete Key Support** - Delete data mapping usage by pressing the Delete key for faster workflow
- Allow to collapse the function list in XPath editor

### Canvas and Visual Editor Enhancements

Building integrations is now more intuitive with these canvas improvements:

- **Route AutoStartup Toggle** - Toggle switch in the title bar for controlling route autoStartup property

FIGURE OF A ROUTE

- **Space Bar Navigation** - Move the canvas by pressing and holding the Space bar for easier navigation
- **Container Selection Styles** - Visual styles for selected containers in NodeContainer for better feedback

FIGURE OR VIDEO OF CANVAS


### REST DSL and OpenAPI Support

- **Property Search Filter** - Search functionality in RestDslEditor for quickly finding properties

FIGURE OF REST DSL EDITOR

- **Accessible REST Editor** - REST DSL editor built with resizable split panels featuring improved accessibility
- **Improved OpenAPI Support** - Enhanced OpenAPI file handling with automatic detection of `*openapi.yml` files and flexible API URL imports without file extension restrictions

### Forms and Configuration

Configuration forms have been enhanced for better usability:

- **Custom Properties Configuration** - Support for key/value configuration format for endpoint properties in components like To, ToD, and other endpoint-based components, providing a more intuitive way to configure component parameters

FIGURE OF TOD AND ANOTHER COMPONENT


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

For a full list of changes please refer to the [changelog](https://github.com/KaotoIO/kaoto/releases/tag/2.11.0).

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