---
title: "Kaoto Documentation Revamp: Your Complete Guide to Visual Integration Design"
date: 2026-04-10
summary: We've completely revamped the Kaoto documentation to make it easier than ever to build Apache Camel integrations visually. Explore the new structure, comprehensive guides, and step-by-step tutorials.
authors:
  - pvinaches
  - lordrip
tags:
  - Kaoto
  - Documentation
  - Guide
---

## A Fresh Start for Kaoto Documentation

We're excited to announce a complete overhaul of the Kaoto documentation! Whether you're new to visual integration design or an experienced Apache Camel developer, our refreshed documentation provides everything you need to build powerful integrations with confidence.

The new documentation structure is designed to guide you from installation through advanced features, with clear explanations, practical examples, and visual aids at every step.

## What's New?

### Reorganized Structure for Better Navigation

The documentation is now organized into logical sections that match your learning journey:

1. **[Installation](/docs/installation/)** - Get Kaoto up and running in your environment
2. **[Quickstart](/docs/quickstart/)** - Build your first AI-powered integration in minutes
3. **[Designer](/docs/designer/)** - Master the visual designer interface and features
4. **[DataMapper](/docs/datamapper/)** - Transform and map data between different formats
5. **[REST](/docs/rest/)** - Work with REST APIs in your integrations

Each section builds on the previous one, creating a natural progression from beginner to advanced topics.

### Comprehensive Designer Guide

The **Designer** section has been completely restructured into focused, task-oriented guides:

#### [Managing Integrations](/docs/designer/01-managing-integrations/)

Learn the fundamentals of working with Kaoto integrations:

- **Understanding Resource Types** - Deep dive into Camel Routes, Kamelets, and Pipes, with clear guidance on when to use each type
- **Best Practices** - Why single integration per file is recommended and when to deviate from this pattern
- **Creating Integrations** - Step-by-step instructions for creating new integrations
- **The Flows List** - Your central control panel for managing integrations, with renaming, visibility control, and deletion
- **Advanced Entities** - RouteConfiguration, Intercept patterns, ErrorHandler, and OnException for sophisticated integration patterns

#### [Working with Nodes](/docs/designer/02-working-with-nodes/)

Master the essential operations for building your routes:

- Adding, replacing, and deleting steps
- Configuring components through intuitive forms
- Enabling and disabling components during development
- Generating documentation for your integrations
- Understanding the component catalog

#### [Reordering Nodes](/docs/designer/03-reordering-nodes/)

Efficiently reorganize your integration flows:

- Drag-and-drop operations (now production-ready!)
- Copy/paste functionality
- Move-before/after actions
- Working with complex nested structures

#### [Runtime Selector](/docs/designer/04-runtime-selector/)

Choose and configure the right Apache Camel runtime:

- Working with different Camel versions (Main, Quarkus, Spring Boot)
- Configuring custom catalog libraries

### Enhanced Quickstart Tutorial

The **[Quickstart](/docs/quickstart/)** guide now features a complete, real-world example that demonstrates Kaoto's capabilities:

**Build a Local Text Summarization Route** - Create a Camel route that:
- Monitors a folder for new text files
- Sends content to Ollama (running the Granite AI model)
- Outputs concise summaries

This hands-on tutorial introduces you to:
- Creating and configuring integrations
- Working with file components
- Integrating AI capabilities with OpenAI components
- Running and testing routes in VS Code

The tutorial includes detailed screenshots for every step, making it easy to follow along even if you're completely new to Kaoto.

### Expanded DataMapper Documentation

The **[DataMapper](/docs/datamapper/)** section now provides comprehensive coverage of this powerful feature:

- **Visual Data Mapping** - Drag-and-drop functionality for creating transformations
- **Schema Support** - Working with XML Schema (XSD) and JSON Schema files
- **Multiple Schema Files** - Handling complex schemas split across multiple files with `xs:import` and `xs:include`
- **JSON Support** - Complete guide to JSON source bodies and JSON target transformations
- **Conditional Mappings** - Creating `if`, `choose-when-otherwise`, and `for-each` mappings
- **XPath Expression Editor** - Advanced expression editing with function support
- **Collection Handling** - Merging multiple source collections into target fields

Each feature is explained with clear examples and visual demonstrations, including video tutorials for complex operations.

### REST API Integration Guide

The **[REST](/docs/rest/)** section covers both API-first and code-first approaches:

- **API-First Development** - Import OpenAPI specifications and generate Camel REST DSL definitions
- **Code-First Development** - Build REST APIs directly in Kaoto
- **REST Editor** - Visual configuration of REST endpoints, operations, and bindings

This section bridges the gap between API design and integration development, showing you how to leverage existing OpenAPI specifications in your Camel routes.

## Documentation Highlights

### Visual Learning

Every guide includes:
- **Screenshots** showing exactly what you'll see in the interface
- **Step-by-step instructions** with visual markers
- **Video tutorials** for complex operations
- **Before/after examples** to clarify the impact of each action

### Practical Tips and Best Practices

Throughout the documentation, you'll find:
- **💡 Tips** - Helpful hints and shortcuts
- **⚠️ Warnings** - Important considerations and common pitfalls
- **📝 Notes** - Additional context and technical details
- **Best Practice Recommendations** - Guidance on the recommended approach for common scenarios

### Clear Navigation

Each documentation page includes:
- **Table of contents** for quick navigation within the page
- **Next steps** section linking to related topics
- **Breadcrumb navigation** showing your location in the documentation hierarchy
- **Cross-references** to related features and concepts

## We Want Your Feedback

The documentation is a living resource that grows with the community. If you:
- Find something unclear or confusing
- Discover a missing topic or example
- Have suggestions for improvement
- Want to contribute documentation

Please join us in the [GitHub discussions](https://github.com/orgs/KaotoIO/discussions) or [create an issue](https://github.com/KaotoIO/kaoto/issues/new/choose).

## Explore the New Documentation

Ready to dive in? Visit the **[Kaoto Documentation](/docs/)** and start building powerful Apache Camel integrations with confidence.

Whether you're creating simple file processors or complex AI-powered workflows, the new documentation provides the guidance you need at every step of your journey.

## Give Kaoto a Try

* Start with the [Quickstart guide](/docs/quickstart/)
* Install the [VS Code extension](/docs/installation/)
* Try the [Kaoto showcase deployment](https://red.ht/kaoto)

Happy integrating! 🐫✨
