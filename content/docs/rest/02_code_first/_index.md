---
title: "Code-First Approach"
description: "Use Kaoto's REST Import Wizard to generate endpoints and build routes visually"
date: 2026-03-31
weight: 2
---

## Introduction

The code-first approach uses Kaoto's REST Import Wizard to import OpenAPI specifications and automatically generate REST endpoints with route stubs. Unlike the API-first approach (which links the spec at runtime), the wizard creates explicit endpoint definitions in your route file. Once generated, the OpenAPI file is no longer needed - all endpoints are defined in your route file. You then implement the route logic visually using Kaoto's component catalog and Design view.

## Import OpenAPI Specification with Kaoto

### Step 1: Configure in the REST Import Wizard

1. In the Kaoto extension, click in Import next to OpenAPI and it will open the REST Import Wizard.

{{< image-sh src="rest-import-button.png" text="Kaoto's REST Import Wizard button" >}}

2. In the Kaoto Import Wizard, select **Upload file** as the source
3. Click **Choose file** and select the `book-summary-api.openapi.yaml` file

4. The wizard will parse the file and show all discovered operations

{{< image-sh src="rest-import-wizard-1.png" text="Kaoto parses the OpenAPI file and shows operations" >}}

You should see the `GET /books/{id}/fun-extract` operation listed.

5. Configure the following options (both should be checked):

- ☑ **Create REST DSL operations** - Generates REST endpoint definitions
- ☑ **Create routes with direct endpoints** - Generates route stubs for each operation

{{< image-sh src="rest-import-generation.png" text="Configure REST DSL and route generation options" >}}

6. Choose the folder to save the information and then give a name to the route.

{{< image-sh src="rest-import-wizard-2.png" text="Configure how Kaoto generates the routes" >}}


### Step 2: Review Generated Structure in Kaoto

After importing, Kaoto generates and displays in the Design view:

1. **REST DSL definition** - Complete endpoint with parameters and responses
2. **Direct route stub** - A placeholder route ready for implementation

The generated structure looks like this:

{{< img-toggle src="imported-route.png" lang="yaml" >}}
- rest:
    id: rest-1774958475751
    get:
      - id: getBookFunExtract
        path: /books/{id}/fun-extract
        routeId: route-getBookFunExtract
        to: direct:getBookFunExtract
        description: Fetches a book from Project Gutenberg and generates an AI extract using OpenAI
        produces: application/json
        param:
          - name: id
            type: path
            required: true
            description: Project Gutenberg book ID (e.g., 11 for Alice's Adventures in Wonderland)
            dataType: integer
        responseMessage:
          - code: "200"
            message: Book fun extract generated successfully
            contentType: application/json
          - code: "404"
            message: Book not found in Project Gutenberg
          - code: "500"
            message: Server error during processing
- route:
    id: route-getBookFunExtract
    from:
      uri: direct:getBookFunExtract
      id: direct-from-getBookFunExtract
      steps:
        - setBody:
            constant: Operation getBookFunExtract not yet implemented
{{< /img-toggle >}}

Your route file now contains the REST endpoint definition, and the direct route stub.

## Implement the Route Visually in Kaoto

Now you'll implement the logic by reusing the route from the API-first approach and adding OpenAI integration.

> [!NOTE]
> This section assumes you've completed the [API-First Approach](../01_api_first/) documentation example. If not, complete that first or refer to it for the Gutenberg API integration steps.

### Step 3: Copy Route from API-First Implementation

1. Open the route file from the API-first documentation example (e.g., `book-api.camel.yaml`)
2. In Kaoto's Design view, locate the `route-getBookFunExtract` route
3. Right-click on the **route** (not on individual steps) and select **Copy**

{{< image-sh src="copy-route.png" text="Copy the complete route from API-first implementation" >}}

### Step 4: Paste Route into Code-First Route

1. Switch back to your code-first route file
2. In the Design view, find the `route-getBookFunExtract` route
3. Right-click on the Design canvas itself (not on the setBody step) and select **Paste**. This pastes the complete route from the API-first route.

{{< image-sh src="paste-route.png" text="Paste the complete route into the code-first route file" >}}

### Step 5: Drag and Drop Steps to Reorder

1. In the Design view, locate the `removeHeaders` step
2. Click and drag the `removeHeaders` step
3. Drop it directly after the `direct` component (at the beginning of the route)
4. Do the same with the other components.

The new route structure after drag and drop:

{{< img-toggle src="after-drag-and-drop.png" lang="yaml" >}}
- route:
    id: route-getBookFunExtract
    from:
      uri: direct:getBookFunExtract
      id: direct-from-getBookFunExtract
      steps:
        - removeHeaders:
            id: removeHeaders-4268-1881
            pattern: CamelHttp*
        - setHeader:
            id: setHeader-3265-3267
            name: x-rapidapi-host
            constant:
              expression: project-gutenberg-free-books-api1.p.rapidapi.com
        - setHeader:
            id: setHeader-2139-3021
            simple:
              expression: "{{gutenberg.api.key}}"
            name: x-rapidapi-key
        - toD:
            id: toD-4177-4046
            uri: https://project-gutenberg-free-books-api1.p.rapidapi.com/books/${header.id}?bridgeEndpoint=true
            parameters: {}
        - setBody:
            id: setBody-2130-2169
            jsonpath:
              expression: $.results[0].summary
        - log:
            message: '"Book summary: ${body}"'
        - setBody:
            constant: Operation getBookFunExtract not yet implemented
{{< /img-toggle >}}

### Step 6: Delete Placeholder and Extra Steps

1. Delete the placeholder `setBody` step at the end (the one with "Operation getBookFunExtract not yet implemented")
2. Delete any remaining copied `direct` component

Your route now has the complete Gutenberg API integration in the correct order.

### Step 7: Add OpenAI Integration from Catalog

Now add the AI-powered fun extract generation:

1. Hover over the arrow after the `setBody` step (the one that extracts `$.results[0].summary`)
2. Click the **+** button that appears
3. In the catalog search, type `openai`
4. Select **OpenAI** component
5. Configure in Kaoto's form:

| Property | Value |
|----------|-------|
| **Operation** | chat-completion |
| **Api Key** | OLLAMA-LOCAL-KEY |
| **Base Url** | http://localhost:11434/v1 |
| **Model** | granite4:tiny-h |
| **System Message** | Summarize this text into a couple of short sentences and give it a funny twist |

This sends the book summary to your local Ollama instance running the Granite 4 model for AI-powered fun extracts.

> [!TIP]
> For more details on configuring OpenAI in Kaoto, refer to the [Quickstart guide](../../quickstart/).

The OpenAI component is now inserted between `setBody` and `log`, completing your route.

## Complete Route

Your final route should look like this:
{{< img-toggle src="./complete-route.png" lang="yaml" >}}
- rest:
    id: rest-1775038763756
    get:
      - id: getBookFunExtract
        path: /books/{id}/fun-extract
        routeId: route-getBookFunExtract
        to: direct:getBookFunExtract
        description: Fetches a book from Project Gutenberg and generates an AI extract
          using OpenAI
        produces: application/json
        param:
          - name: id
            type: path
            required: true
            description: Project Gutenberg book ID (e.g., 11 for Alice's Adventures in
              Wonderland)
            dataType: integer
        responseMessage:
          - code: "200"
            message: Book fun extract generated successfully
            contentType: application/json
          - code: "404"
            message: Book not found in Project Gutenberg
          - code: "500"
            message: Server error during processing
- route:
    id: route-getBookFunExtract
    from:
      uri: direct:getBookFunExtract
      id: direct-from-getBookFunExtract
      steps:
        - removeHeaders:
            id: removeHeaders-4268-1881
            pattern: CamelHttp*
        - setHeader:
            id: setHeader-3265-3267
            name: x-rapidapi-host
            constant:
              expression: project-gutenberg-free-books-api1.p.rapidapi.com
        - setHeader:
            id: setHeader-2139-3021
            simple:
              expression: "{{gutenberg.api.key}}"
            name: x-rapidapi-key
        - toD:
            id: toD-4177-4046
            uri: https://project-gutenberg-free-books-api1.p.rapidapi.com/books/${header.id}?bridgeEndpoint=true
            parameters: {}
        - setBody:
            id: setBody-2130-2169
            jsonpath:
              expression: $.results[0].summary
        - to:
            id: to-3162
            uri: openai
            parameters:
              operation: chat-completion
              apiKey: OLLAMA-LOCAL-KEY
              baseUrl: http://localhost:11434/v1
              model: granite4:tiny-h
              systemMessage: Summarize this text into a couple of short sentences and give it
                a funny twist
        - log:
            message: '"Book summary: ${body}"'
{{< /img-toggle >}}

## Testing in Kaoto

### Run the Integration

1. Make sure Ollama is running with the Granite 4 model
2. In Kaoto's toolbar, click the **Run** button. Make sure your application.properties and the new route are in the same folder.
3. Kaoto will start your integration using JBang
4. Watch the Design view to see your routes activate

### Test the Endpoint

Open a terminal and run:

```bash
curl http://localhost:8080/books/1342/fun-extract
```

You should receive an AI-generated fun extract of "Pride and Prejudice" (book ID 1342).

### Try Different Books

```bash
# Frankenstein
curl http://localhost:8080/books/84/fun-extract

# The Adventures of Sherlock Holmes
curl http://localhost:8080/books/1661/fun-extract
```

Each request will return a unique AI-generated fun extract!

## Key Concepts

### Apache Camel REST DSL

The REST DSL in Apache Camel provides a declarative way to define REST APIs. It allows you to specify REST endpoints, their operations, parameters, and responses in a structured format.

[Learn more about Apache Camel REST DSL](https://camel.apache.org/manual/rest-dsl.html)

### Kaoto REST Import Wizard

Kaoto's REST Import Wizard automates:
1. Parsing OpenAPI specifications
2. Generating explicit REST DSL endpoint definitions (not just linking)
3. Creating direct route stubs ready for implementation

Unlike API-first (which links the spec at runtime), the wizard creates the actual endpoint definitions in your route file. Once generated, the OpenAPI file is no longer needed.

[Learn more about OpenAPI and Camel](https://camel.apache.org/components/latest/others/openapi-java.html)

### Direct Component

The Direct component provides synchronous, in-memory communication between routes, allowing you to separate REST endpoint definitions from their implementation logic.

[Learn more about Camel Direct Component](https://camel.apache.org/components/latest/direct-component.html)

### Combining Multiple APIs

This documentation example demonstrates combining two external APIs:
1. **Project Gutenberg API** (via RapidAPI) - Fetches book data
2. **OpenAI API** (via Ollama) - Generates AI summaries

Camel makes it easy to orchestrate multiple services in a single route.

## Summary

This documentation demonstrated:

1. ✅ Using Kaoto's REST Import Wizard to generate REST endpoints from OpenAPI (no runtime dependency on OpenAPI file)
2. ✅ Building a route visually using Kaoto's Design and component catalog
3. ✅ Configuring components using Kaoto's forms
4. ✅ Connecting to external APIs (Gutenberg and OpenAI) visually
5. ✅ Running and testing the integration using Kaoto's tools

## Next Steps

- **[Extending with REST Editor](../03_rest_editor/)** - Learn how to add new endpoints from scratch using the REST Editor
