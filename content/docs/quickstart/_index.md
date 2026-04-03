---
title: "Quickstart"
description: "Build a local text summarization route using Kaoto, Apache Camel, and Ollama AI"
date: 2026-03-25
weight: 2
---

## Overview

In this quickstart guide, you'll build a Camel route that automatically summarizes text files using a local AI model. The route will monitor a folder for new text files, send their content to Ollama (running the Granite AI model), and output concise summaries.

## Prerequisites

Before starting, ensure you have:

- **VS Code** installed on your system - [Follow the installation guide](https://code.visualstudio.com/download)
- **Kaoto VS Code extension** - See the [installation guide](../installation/) for setup instructions
- **Ollama** installed and running - Follow the [Ollama installation guide](https://ollama.com/download) to set it up
- **Granite 4 model** pulled in Ollama - Run `ollama pull granite4:tiny-h` in your terminal (https://ollama.com/library/granite4)

## Create and Run Your First Route

{{% create-integration-steps %}}

### Run the Simple Route

1. Click the **"Run: Workspace"** button in the Integrations panel
{{< image-sh src="02-run-workspace-button.png" text="Run workspace button" >}}

2. The route will start executing, check the terminal output - you should see "Hello Camel from route1" printed every second
{{< image-sh src="02-run-workspace-output.png" text="Run workspace output" >}}

3. To stop the route, you can click on the **"Terminate"** button
{{< image-sh src="02-run-workspace-terminate.png" text="Stop the route" >}}


## Add AI Summarization
For this route, we're gonna use Apache Camel 4.18 (or newer), make sure to select that version in the **Runtime selector**
{{< image-sh src="03-select-camel-4-18.png" text="Select Camel 4.18 or newer" >}}

For starters, instead of automatically producing empty messages with the **timer** component, we're gonna use a **file** component for reading text files from a directory where we're gonna place the text to summarize

### Add the File Component
1. Hover over the **timer** node and click the replace button
{{< image-sh src="03-replace-timer.png" text="Replace timer" >}}

2. In the component catalog, search for **"file"** and select it
{{< image-sh src="03-pick-file-component.png" text="Pick file component" >}}

3. You'll end up having something like this, notice how hovering over the exclamation mark tell us that we're missing the **`directoryName`** configuration
{{< image-sh src="03-missing-directory-name.png" text="Missing directoryName" >}}

4. Click on the **file** component, and fill the **directoryName** field with **./input**
{{< image-sh src="03-configuring-directory-name.png" text="Configuring directoryName" >}}

5. Click on the **All** toggle, and search for the **`noop`** property and enable it
{{< image-sh src="03-enabling-noop-property.png" text="Noop property" >}}

6. Search for the **`idempotent`** property and enable it
{{< image-sh src="03-enabling-idempotent-property.png" text="Idempotent property" >}}

7. Hover over the **setBody** node and click the delete button
{{< image-sh src="03-delete-setBody-node.png" text="Delete setBody" >}}

8. Switch to the File explorer
{{< image-sh src="03-file-explorer.png" text="Navigate to file explorer" >}}

9. Create a new folder called **`input`** with a **`story.txt`** file inside where we're gonna write the text to summarize.
{{< image-sh src="03-folder-structure.png" text="Folder structure" >}}

> [!TIP]
> For a text example, we're gonna visit [the wonderful Project Gutenberg](https://www.gutenberg.org/) and use a paragraph from [the Alice's Adventures in Wonderland by Lewis Carroll book](https://www.gutenberg.org/ebooks/11)
>
> First, she dreamed of little Alice herself, and once again the tiny
> hands were clasped upon her knee, and the bright eager eyes were
> looking up into hers—she could hear the very tones of her voice, and
> see that queer little toss of her head to keep back the wandering hair
> that _would_ always get into her eyes—and still as she listened, or
> seemed to listen, the whole place around her became alive with the
> strange creatures of her little sister’s dream.
>
> The long grass rustled at her feet as the White Rabbit hurried by—the
> frightened Mouse splashed his way through the neighbouring pool—she
> could hear the rattle of the teacups as the March Hare and his friends
> shared their never-ending meal, and the shrill voice of the Queen
> ordering off her unfortunate guests to execution—once more the pig-baby
> was sneezing on the Duchess’s knee, while plates and dishes crashed
> around it—once more the shriek of the Gryphon, the squeaking of the
> Lizard’s slate-pencil, and the choking of the suppressed guinea-pigs,
> filled the air, mixed up with the distant sobs of the miserable Mock
> Turtle.

10. Navigate back to the Kaoto perspective and run the route, you should get a similar output like this.
Notice how we can see the text as the route output.

{{< img-toggle src="./03-result.png" lang="yaml" >}}
- route:
    from:
      uri: file
      parameters:
        directoryName: ./input
        idempotent: true
        noop: true
      steps:
        - log: ${body}
      id: from-6531
    id: route-1905
{{< /img-toggle >}}

11. We can stop the route now. In the next step, we're gonna add the **`open ai`** component to perform the summary
{{< image-sh src="03-stop-route.png" text="Stop route" >}}


### Add the Open AI Component
For the summary process, we're gonna use the **`Open AI`** component to leverage our local Ollama instance with the Granite model

1. Hover in the edge between the **`file`** and **`log`** components, and click on the **Add step** button
{{< image-sh src="04-add-openai-component.png" text="Add Open AI component" >}}

2. In the component catalog, search for **`openai`**
{{< image-sh src="04-pick-openai-component.png" text="Pick Open AI component" >}}

3. Once the **`openai`** component is added, click on it and pick the **All** view to configure the follow options:
{{< image-sh src="04-openai-all-configuration.png" text="Select all configuration" >}}

| Property           | Value                                                                          |
| ---                | ---                                                                            |
| **Operation**      | chat-completion                                                                |
| **Api Key**        | OLLAMA-LOCAL-KEY                                                               |
| **Base Url**       | http://localhost:11434/v1                                                      |
| **Model**          | granite4:tiny-h                                                                |
| **System Message** | Summarize this text into a couple of short sentences and give it a funny twist |

> [!TIP]
> For running Ollama locally, a **Api Key** is not really needed, so we can fill this field with any string, or the actual "OLLAMA-LOCAL-KEY" string

> [!TIP]
> After editing the option, you can click on the **Modified** toggle to see what has changed
> {{< image-sh src="04-modified-properties.png" text="Modified properties" >}}

> [!WARNING]
> For the next step, make sure to run `ollama run granite4:tiny-h` in your terminal beforehand

4. Time of truth, let's run the route and see the summary. If everything went well, you should get a similar output like this:
```text
2026-03-26 13:09:37.293  INFO 592754 --- [ file://./input] demo.camel.yaml:19                       : Once upon a time in Wonderland, Alice dreamt that her childhood fascination turned into a reality where she met her favorite characters from "Alice in Wonderland," but this time it's all around her, filling her ears and eyes! Oh, and let's not forget about the sneezing pig-baby and execution-ordered rabbit. Truly an unforgettable experience!

(Note: This is a lighthearted reimagining of the original text.)
```
{{< img-toggle src="./04-result.png" lang="yaml" >}}
- route:
    from:
      uri: file
      parameters:
        directoryName: ./input
        idempotent: true
        noop: true
      steps:
        - to:
            id: to-2057
            uri: openai
            parameters:
              operation: chat-completion
              baseUrl: http://localhost:11434/v1
              systemMessage: Summarize this text into a couple of short sentences and give it
                a funny twist
              apiKey: OLLAMA-LOCAL-KEY
              model: granite4:tiny-h
        - log: ${body}
      id: from-6531
    id: route-1905
{{< /img-toggle >}}
