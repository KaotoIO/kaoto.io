---
title: "Managing Integrations"
description: "Learn how to create, rename, delete, and organize flows in Kaoto"
date: 2026-03-31
weight: 1
---

## Overview

Managing integrations is a core part of working with Kaoto. This guide covers everything you need to know about creating, organizing, and managing integrations in your projects.

## Understanding Resource Types

Kaoto supports three main resource types for building integrations, each determined by its file extension:

### Camel Route (`.camel.yaml`)

In Apache Camel, a route is a set of processing steps that are applied to a message as it travels from a source to a destination. A route typically consists of a series of processing steps that are connected in a linear sequence.

**Key characteristics:**
- Supports multiple integrations per file (though single integration per file is recommended)
- Full access to all Camel components and patterns
- Ideal for complex integration scenarios

[Learn more about Apache Camel Routes](https://camel.apache.org/manual/routes.html)

### Kamelet (`.kamelet.yaml`)

Kamelets are reusable integration templates that encapsulate integration logic. Think of them as pre-built, configurable integration components that you can use across multiple projects.

**Key characteristics:**
- Single integration per file only
- Designed for reusability and sharing

[Learn more about Apache Camel Kamelets](https://camel.apache.org/camel-kamelets/next/index.html)

### Pipe (`.pipe.yaml`)

Pipes connect Kamelets together to create simple integration flows. They provide a declarative way to build integrations by connecting sources to sinks through Kamelets.

**Key characteristics:**
- Single integration per file only
- Simplified syntax for connecting Kamelets

[Learn more about Apache Camel Pipes](https://camel.apache.org/camel-k/latest/pipes/pipes.html)

---

## Working with Camel Routes

### Best Practice: Single Integration Per File

We strongly recommend organizing your Camel Routes with **one integration per file**. This approach provides several important benefits:

- **Better organization**: Each file has a clear, single purpose
- **Easier version control**: Changes to one integration don't affect others
- **Clearer file structure**: Project organization is more intuitive
- **Improved maintainability**: Easier to find, update, and test individual integrations
- **Better collaboration**: Reduces merge conflicts in team environments

**When to use multi-integration files:**
- Legacy code that already uses this pattern
- Tightly coupled integrations that must be deployed together
- Very simple integrations that are logically grouped

For most projects, stick with single integration per file as your default approach.

---

## Creating a New Integration

{{% create-integration-steps %}}

> [!TIP]
> The integration name doesn't need to match the file name.
> You can add multiple integrations to the same file using the same workflow.

## The Flows List

For Camel Routes, the **flows list** in the top toolbar is your central control panel for managing all integrations and entities in your current file. It provides quick access to:

- **1. Rename**: Edit integration names inline
- **2. Visibility control**: Show or hide integrations on the canvas
- **3. Delete**: Remove integrations from the file

{{< figure src="01-flow-list.png" alt="Flows list" caption="Flows list" class="image" >}}

### Renaming Integrations

To rename an existing integration:

1. Locate the integration in the flows list
2. Click on the pencil button
{{< figure src="01-rename-click-in-the-pencil.png" alt="Pencil button" caption="Pencil button" class="image" >}}
3. Type the new name
{{< figure src="01-rename-write-the-new-name.png" alt="The name gets editable" caption="The name gets editable" class="image" >}}
4. Press Enter or click in the accept button
5. Save the file

> [!TIP]
> The file name does NOT automatically update when you rename an integration.
> Only the integration ID inside the file changes.
> An unsaved changes indicator will appear until you save.

### Controlling Integration Visibility

When working with files containing multiple integrations, you can control which integrations are visible on the canvas:

1. Locate the integration in the flows list
2. Click the eye icon next to the integration name
{{< figure src="02-visibility-button.png" alt="Visibility button" caption="Visibility button" class="image" >}}
3. The integration toggles between visible and hidden on the canvas
{{< figure src="02-visibility-hidden-route.png" alt="Hidden flow" caption="Hidden flow" class="image" >}}

Hidden integrations remain in the file but don't clutter your canvas, making it easier to focus on specific integrations in complex files.

### Deleting Integrations

To delete an integration:

1. Locate the integration in the flows list
2. Click the delete icon next to the integration name
{{< figure src="03-delete-button.png" alt="Delete button" caption="Delete button" class="image" >}}
3. Confirm deletion in the dialog that appears
{{< figure src="03-delete-confirmation-modal.png" alt="Delete confirmation modal" caption="Delete confirmation modal" class="image" >}}
4. The integration content is removed from the file

> [!TIP]
> The file itself is NOT deleted, only the integration content is removed.
>
> For single-integration files, the file becomes empty after deletion.
>
> For multi-integration files, a new demo integration is created.

---

## Other Camel Entities in Kaoto

Beyond integrations, Kaoto supports additional Apache Camel entities for advanced integration patterns. All of these can be created via the **"Add new" dropdown** in the top toolbar.
{{< figure src="04-new-integration.png" alt="Add new dropdown" caption="Add new dropdown" class="image" >}}

### RouteConfiguration

RouteConfiguration defines reusable configuration that can be applied to multiple integrations, such as error handlers, interceptors, and other cross-cutting concerns.

**Use case**: Centralize common integration behaviors across your integration, reducing duplication and ensuring consistency.

[Learn more about RouteConfiguration](https://camel.apache.org/manual/route-configuration.html)

### Intercept, InterceptFrom, and InterceptSendToEndpoint

Intercept intercepts and processes all messages passing through the integration, regardless of their source or destination.

[Learn more about Intercept](https://camel.apache.org/components/next/eips/intercept.html)

#### Intercept

Intercept is a simple Intercept that intercepts all messages passing through the integration.

**Use case**: Implement global error handling, logging, or metrics collection across your integrations.

[Learn more about Intercept](https://camel.apache.org/components/next/eips/intercept.html#Intercept-Intercept)

#### InterceptSendToEndpoint

InterceptSendToEndpoint intercepts messages being sent to specific endpoints, allowing you to monitor or modify messages before they reach their destination.

**Use case**: Monitor, modify, or redirect messages going to particular destinations, useful for debugging or implementing conditional routing.

[Learn more about InterceptSendToEndpoint](https://camel.apache.org/components/next/eips/intercept.html#Intercept-InterceptSendToEndpoint)

#### InterceptFrom

InterceptFrom intercepts messages coming from specific endpoints, allowing you to process or validate messages before they enter your integration logic.

**Use case**: Process or validate messages from particular sources before integration processing begins, ensuring data quality and consistency.

[Learn more about InterceptFrom](https://camel.apache.org/components/next/eips/intercept.html#Intercept-InterceptFrom)

### ErrorHandler

ErrorHandler defines how errors are handled during message processing, including retry policies, dead letter channels, and error logging strategies.

**Use case**: Implement robust error handling strategies for your integrations, ensuring failures are handled gracefully and consistently.

[Learn more about ErrorHandler](https://camel.apache.org/manual/error-handler.html)

### OnException

OnException catches specific exceptions and defines custom handling logic for different error types, allowing you to respond differently based on the type of error encountered.

**Use case**: Handle different exceptions differently - for example, retry network errors automatically but log validation errors for manual review.

[Learn more about OnException](https://camel.apache.org/manual/exception-clause.html)

---

<!-- ## Next Steps

Now that you understand integration management, explore these related topics:

- **[Working with Nodes](../02-nodes)**: Learn how to add and configure components in your integrations
- **[Reordering Nodes](../03-reordering-nodes)**: Organize the flow of your integration logic
- **[Runtime Selector](../04-runtime-selector)**: Choose the right Camel runtime for your project -->
