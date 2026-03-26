---
title: "REST DSL"
description: "Build REST APIs with Apache Camel using different approaches in Kaoto"
date: 2026-03-31
weight: 5
---

## Overview

The REST DSL (Domain Specific Language) in Apache Camel provides a powerful way to define REST APIs. Kaoto offers multiple approaches to work with REST DSL, each suited for different workflows and preferences.

This guide demonstrates two distinct approaches to building REST APIs with Kaoto:

1. **[API-First Approach](01_api_first/)** - Link OpenAPI specifications at runtime
2. **[Code-First Approach](02_code_first/)** - Generate endpoints from OpenAPI using the REST Import Wizard or **[create endpoints manually from scratch using the visual REST Editor](03_rest_editor/)**

Each approach builds a REST API that fetches books from Project Gutenberg via RapidAPI and generates AI-powered summaries using the Apache Camel OpenAI component. 


## Prerequisites

Before starting any of the approaches, ensure you have:

- **VS Code** installed - [Download here](https://code.visualstudio.com/download)
- **Kaoto VS Code extension** - See the [installation guide](../installation/)
- **RapidAPI account and API key** - Sign up at [RapidAPI](https://rapidapi.com/) and subscribe to the [Project Gutenberg Free Books API](https://rapidapi.com/help-lQ_hVT8W5/api/project-gutenberg-free-books-api1)
- **Camel catalog** - This documentation was created with Camel version 4.18.0, though other versions and distributions are available

### Additional Prerequisites for Code-First and REST Editor

- **Ollama** installed and running - [Installation guide](https://ollama.com/download)
- **Granite 4 model** pulled in Ollama - Run `ollama pull granite4:tiny-h` ([Granite 4 on Ollama](https://ollama.com/library/granite4))

## Shared Resources

The API-first and code-first approaches use the same OpenAPI specification:

**[Download book-summary-api.openapi.yaml](./book-summary-api.openapi.yaml)**

Save this file to your workspace folder before starting the API-first or code-first examples. The REST Editor approach creates endpoints from scratch without OpenAPI.

## Comparison of Approaches

| Aspect | API-First | Code-First |
|--------|-----------|----------------|-------------|
| **Workflow** | Link OpenAPI spec | Generate + Visual design |
| **OpenAPI Usage** | Runtime link (required) | Import wizard (not needed at runtime) or create from scratch |
| **Best For** | API contract enforcement | Learning, prototyping |
| **UI Interaction** | Minimal | Moderate |
| **Examples** | `/books/{id}/fun-extract` | `/books/{id}/fun-extract` + `/books/popular` |

## Choose Your Approach

### [1. API-First Approach](01_api_first/)

**Best for**: Teams with strict API contracts, when the OpenAPI spec is the source of truth, or when you need runtime flexibility to update the API by changing the spec.

**What you'll build**: A REST endpoint that fetches book summaries from Project Gutenberg by linking an OpenAPI specification.

**Key characteristic**: The OpenAPI file must be present at runtime - Camel reads it to create endpoints. The OpenAPI file is the source of truth.

---

### [2. Code-First Approach](02_code_first/)

**Best for**: Rapid prototyping without OpenAPI available.

**What you'll build**: The same REST endpoint as API-First, but with added AI-powered fun extracts using OpenAI, generated from the OpenAPI spec.

**Key characteristic**: OpenAPI can be used only during development - endpoints are generated into your route file or create from scratch. The Camel route file is the source of truth.

## Key Concepts

### REST DSL

Camel's domain-specific language for defining REST APIs. It provides a declarative way to specify REST endpoints, their operations, and how they map to Camel routes.

[Learn more about Apache Camel REST DSL](https://camel.apache.org/manual/rest-dsl.html)

### OpenAPI Specification

A standard format for describing REST APIs. Kaoto can import OpenAPI specifications to automatically generate REST DSL definitions.

[Learn more about OpenAPI and Camel](https://camel.apache.org/components/latest/others/openapi-java.html)

### Direct Routes

Reusable route components that can be called from REST endpoints. They separate the REST API definition from the implementation logic, providing synchronous in-memory communication between routes.

[Learn more about Camel Direct Component](https://camel.apache.org/components/latest/direct-component.html)

### REST Configuration

Global settings that apply to all REST endpoints in your integration, such as the HTTP component, port, CORS settings, and binding mode.

[Learn more about REST Configuration](https://camel.apache.org/manual/rest-dsl.html#_rest_configuration)