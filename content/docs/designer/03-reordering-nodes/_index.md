---
title: "Reordering Nodes"
description: "Learn how to reorder nodes in the Kaoto canvas"
date: 2026-03-31
weight: 3
---

## Overview

Kaoto provides multiple ways to reorganize Apache Camel routes on the canvas. You can reorder steps using drag-and-drop, copy/paste nodes between routes, or use move-before/after operations for precise positioning.

Kaoto offers three primary methods for reordering nodes:

1. **[Drag and Drop](#drag-and-drop)**: Visually reorganize nodes by dragging them to new positions with real-time feedback
2. **[Copy/Paste](#copy-and-paste-nodes)**: Duplicate nodes within or across routes while preserving their configuration
3. **[Move Before/After](#move-beforeafter)**: Precisely reposition nodes using context menu actions

Each method serves different use cases and can be combined for efficient workflow design.

---

## Drag and Drop

Kaoto's drag-and-drop functionality allows you to reorganize Apache Camel routes directly on the canvas. You can reorder steps within a route, move steps across routes, and reorganize container structures with visual feedback guiding your operations.

For a comprehensive guide on drag-and-drop capabilities, including video demonstrations and detailed examples, see our [Drag and Drop blog post](https://kaoto.io/blog/drag-and-drop/).

---

## Copy and Paste Nodes

Copy and paste functionality allows you to duplicate nodes within the same route or across different routes while preserving their complete configuration. The paste options are context-aware, appearing only where the copied node can be validly inserted.

**How it works:**
- Right-click on any node to open the context menu
- Select **Copy** to copy the node to the clipboard
- Navigate to the desired location (same route or different route)
- Right-click on a compatible target position
- Select the appropriate **Paste** option based on the context

**Paste Options:**

The paste option label varies depending on where you're pasting. You may see up to three different paste options:

- **Paste as next step** – Pastes the copied step as the immediate next node in the sequence


<video controls src="01-paste-as-next-step.mp4" title="Paste as next step"></video>

- **Paste as child** – Available only on nodes that can contain children (e.g., [`from`](https://camel.apache.org/components/latest/eips/from-eip.html), [`doTry`](https://camel.apache.org/components/latest/eips/doTry-eip.html), [`multicast`](https://camel.apache.org/components/latest/eips/multicast-eip.html))


<video controls src="01-paste-as-child.mp4" title="Paste as child"></video>

- **Paste as special child** – Appears only when pasting into special processors like [`doTry`](https://camel.apache.org/components/latest/eips/doTry-eip.html) or [`choice`](https://camel.apache.org/components/latest/eips/choice-eip.html), and only if the copied content is a special node like [`when`](https://camel.apache.org/components/latest/eips/when-eip.html) or [`doCatch`](https://camel.apache.org/components/latest/eips/doCatch-eip.html)


<video controls src="01-paste-as-special-child.mp4" title="Paste as special child"></video>

> [!NOTE]
> You can copy any node, but paste options will only appear where it's contextually valid. If no paste option appears, the copied node cannot be inserted at that location.

**Use cases:**

- Duplicate commonly used processing steps across multiple routes
- Quickly replicate complex node configurations without manual reconfiguration
- Build similar routes faster by copying and modifying existing nodes
- Rebuild complete routes from scratch by copying and pasting them on the canvas (or simply duplicate the route)
- Copy error handling blocks (like [`doCatch`](https://camel.apache.org/components/latest/eips/doCatch-eip.html)) to standardize exception handling across routes

> [!TIP]
> Copied nodes retain all their property configurations, making it easy to create consistent processing patterns across your integrations.

---

## Move Before/After

The move-before/after functionality provides precise control over node positioning, ideal when you need exact placement without dragging. These operations are available through both the context menu and the floating toolbar that appears when you select a node.

**How it works:**
- Hover over the node you want to reposition (the floating toolbar will appear)
- Click **Move Before** or **Move After** buttons on the floating toolbar, or
- Right-click on the node and select **Move Before** or **Move After** from the context menu
- The node is repositioned relative to its previous position

**What you can move:**

Move-before/after works with all types of nodes, including:
- Regular step nodes (e.g., [`log`](https://camel.apache.org/components/latest/eips/log-eip.html), [`transform`](https://camel.apache.org/components/latest/eips/transform-eip.html))


<video controls src="02-move-regular-step-nodes.mp4" title="Move regular step nodes"></video>

- Container nodes (e.g., [`choice`](https://camel.apache.org/components/latest/eips/choice-eip.html), [`doTry`](https://camel.apache.org/components/latest/eips/doTry-eip.html))


<video controls src="02-move-container-nodes.mp4" title="Move container nodes"></video>

- Sub-containers within special processors:
  - [`when`](https://camel.apache.org/components/latest/eips/when-eip.html) branches inside [`choice`](https://camel.apache.org/components/latest/eips/choice-eip.html)
  - [`doCatch`](https://camel.apache.org/components/latest/eips/doCatch-eip.html) blocks inside [`doTry`](https://camel.apache.org/components/latest/eips/doTry-eip.html)
  - Other nested container structures

<video controls src="02-move-sub-containers-within-special-processors.mp4" title="Move sub-containers within special processors"></video>

**Use cases:**

- Precisely reorder nodes when drag-and-drop is less convenient
- Reposition nodes in complex routes with many steps
- Reorder conditional branches within a [`choice`](https://camel.apache.org/components/latest/eips/choice-eip.html) processor
- Reorganize exception handlers within a [`doTry`](https://camel.apache.org/components/latest/eips/doTry-eip.html) block
- Make fine adjustments to node order without visual dragging
- Quickly move nodes to specific positions in long sequences

> [!TIP]
> Move-before/after operations are particularly useful in routes with many nodes where scrolling and dragging might be cumbersome. Use the floating toolbar for quick access when a node is selected.

---

## Best Practices

To get the most out of Kaoto's node reordering capabilities:

1. **Choose the right method**: Use drag-and-drop for visual reorganization, copy/paste for duplication, and move-before/after for precise positioning
2. **Plan before you reorganize**: Think about the logical flow before moving or copying steps
3. **Use visual feedback**: When dragging, pay attention to the visual indicators showing valid drop zones and compatible targets
4. **Test after reorganizing**: Validate your routes after significant changes
5. **Leverage undo/redo**: Don't hesitate to experiment - you can always undo
6. **Combine methods**: Use drag-and-drop, copy/paste, and move operations together for efficient workflow design
7. **Save frequently**: While undo/redo is available, regular saves ensure you don't lose your work

---

## Next Steps

Now that you understand node reordering, explore these related topics:

<!-- - **[Working with Nodes](../02-nodes)**: Understand how to add and configure components in your integrations
- **[Runtime Selector](../04-runtime-selector)**: Choose the right Camel runtime for your project -->
