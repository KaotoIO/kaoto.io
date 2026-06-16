---
title: "Feature of the Day: Link OpenAPI Specs to Your Routes"
date: 2026-06-19
summary: Turn your OpenAPI specification into a working REST API in seconds with Kaoto's API-first approach
authors:
  - pvinaches
tags:
  - Kaoto
  - Feature of the Day
  - REST DSL
  - OpenAPI
  - Apache Camel
---

## From OpenAPI Spec to Working API

Have an OpenAPI specification? Kaoto's API-first approach lets you link it directly to your Camel route - no manual endpoint creation needed. Apache Camel reads the spec at runtime and creates all your REST endpoints automatically.

Imagine you have an OpenAPI spec defining a `/books/{id}/fun-extract` endpoint that fetches book summaries from Project Gutenberg. With Kaoto, you simply link the OpenAPI file to your REST configuration, implement a direct route that handles the business logic (calling the external API, extracting the summary), and you're done. Your REST API is ready to serve requests. The OpenAPI specification remains the source of truth - any changes to the spec automatically update your endpoints at runtime.

This API-first approach is perfect for teams with strict API contracts or when you need runtime flexibility to update your API by changing the specification file. It bridges the gap between API design and integration development, letting you leverage existing OpenAPI specifications directly in your Camel routes.

### Learn More

Want to build this yourself? Our [REST DSL documentation](/docs/rest/) provides complete step-by-step tutorials for both API-first and code-first approaches:

- **[API-First Approach](/docs/rest/01_api_first/)** - Link OpenAPI specifications at runtime (includes the complete book summary API example)
- **[Code-First Approach](/docs/rest/02_code_first/)** - Generate endpoints from OpenAPI using the REST Import Wizard
- **[REST Editor](/docs/rest/03_rest_editor/)** - Create endpoints manually from scratch using the visual designer

Each guide includes detailed screenshots, configuration examples, and working code you can try immediately.

## Try It Yourself

* [Complete REST DSL Tutorial](/docs/rest/)
* [Install Kaoto VS Code Extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto)

Build your first REST API visually - available now in Kaoto 2.10 and later.

Happy integrating! 🚀