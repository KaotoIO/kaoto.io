---
title: Kaoto 2.7 released
date: 2025-09-03T00:00:00+06:00
summary: Kaoto 2.7 is available.
authors:
  - admin
tags:
  - Kaoto
  - Release
  - Kaoto 2.7
---
## What's new?

It has been quite some time since the last Kaoto release. We have been busy improving Kaoto with more usability features and the addition of JSON support for our Data Mapper.

Please take a look below to learn about the exciting new things we added to this version.

## Features & Improvements

### Data Mapper JSON Support (Tech Preview)

<p align="center"><img src="./datamapper-json.png" alt="DataMapper JSON Support" /></p>

Building on the XML support introduced earlier, the Data Mapper now enables you to:

* serialize and deserialize JSON data structures for visual mapping
* attach JSON schemas to visualize data structures in a tree view
* create mappings between JSON and XML formats
* choose root elements when working with schemas containing multiple root elements

#### JSON Support Demo

<video controls preload="metadata" playsinline style="max-width:100%;height:auto;">
<source src="./dm_json.mp4" type="video/mp4">
Your browser does not support the video tag.
<a href="./dm_json.mp4">Download the video</a>.
</video>

#### Choose XML Root Element Demo

<video controls preload="metadata" playsinline style="max-width:100%;height:auto;">
<source src="./dm_chooserootelement.mp4" type="video/mp4">
Your browser does not support the video tag.
<a href="./dm_chooserootelement.mp4">Download the video</a>.
</video>

You can find more detailed information about the Data Mapper in our online [user manual](/docs/manual/04_datamapper/).

### Improved Maven Support

If you are using the Kaoto VS Code extension and you work in a Maven project then this little improvement might delight you. Whenever you add a new component endpoint to your route, upon saving your `pom.xml` file gets updated with the required dependency.

<p align="center"><img src="./dep-update.gif" alt="showcasing the dependency update" /></p>

### Drag & Drop Support

In earlier releases we already introduced the drag & drop support partially and you had to enable it in the settings. With this release we consider it good enough to enable it by default.

You can now reorder steps directly on the canvas by dragging them into the right positions. Additionally we enabled the support for dragging between different containers and finally we also improved the visual feedback for the drag & drop operation.

<video controls preload="metadata" playsinline style="max-width:100%;height:auto;">
<source src="./drag-n-drop-simple.mp4" type="video/mp4">
Your browser does not support the video tag.
<a href="./drag-n-drop-simple.mp4">Download the video</a>.
</video>

### Copy & Paste Support

We have added support for copying and pasting steps and containers via the right-click context menu in the graphical editor.

<video controls preload="metadata" playsinline style="max-width:100%;height:auto;">
<source src="./copy-paste.mp4" type="video/mp4">
Your browser does not support the video tag.
<a href="./copy-paste.mp4">Download the video</a>.
</video>

### Quick Duplicate

There are sometimes repetetive tasks that require you to create several steps of the same kind just with different configurations. We have added the __Duplicate__ feature to ease the pain. With a single click you can now duplicate existing steps and even containers.

<video controls preload="metadata" playsinline style="max-width:100%;height:auto;">
<source src="./duplicate.mp4" type="video/mp4">
Your browser does not support the video tag.
<a href="./duplicate.mp4">Download the video</a>.
</video>

### Undo / Redo Support

Did you delete something by mistake? This is no longer an issue due to the added support for Undo and Redo in the graphical editor. This way you can now navigate your design changes and recover from accidental modifications easily.

<video controls preload="metadata" playsinline style="max-width:100%;height:auto;">
<source src="./undo-redo.mp4" type="video/mp4">
Your browser does not support the video tag.
<a href="./undo-redo.mp4">Download the video</a>.
</video>

### Form and UI Enhancements

* intelligent form suggestions
* form suggestions help you to complete configurations faster
* *simple* expression language suggestions for easier expression authoring
* `application.properties` suggestions with metadata-driven completions

<video controls preload="metadata" playsinline style="max-width:100%;height:auto;">
<source src="./suggestions-property-placeholders.mp4" type="video/mp4">
Your browser does not support the video tag.
<a href="./suggestions-property-placeholders.mp4">Download the video</a>.
</video>

### Other Enhancements

* Switch between `to`, `toD`, and `poll` variants directly in the form

<p align="center"><img src="./endpoint-switch.png" alt="showcasing the endpoint type selector" /></p>

* Preserve expressions when switching between different languages
* Improved parameter handling with URI parsing enhancements

## Bug Fixes

For a full list of changes please refer to the [change log.](https://github.com/KaotoIO/kaoto/releases/tag/2.7.0)

## Let’s Build it Together

Let us know what you think by joining us in the [GitHub discussions](https://github.com/orgs/KaotoIO/discussions).
Do you have an idea how to improve Kaoto? Would you love to see a useful feature implemented or simply ask a question? Please [create an issue](https://github.com/KaotoIO/kaoto/issues/new/choose).

## A big shoutout to our amazing contributors

Thank you to everyone who made this release possible, whether by a code contribution, feedback, advocacy, or participating in an important discussion with us. ❤️

## Give it a try

* Kaoto [quickstart](/docs/quickstart/).
* Kaoto is available as a [VS Code extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto).
* Kaoto [showcase deployment](https://red.ht/kaoto).
