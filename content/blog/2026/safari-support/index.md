---
title: "Kaoto playground now works in Safari"
date: 2026-11-02
summary: The Kaoto canvas renders correctly in Safari. Step toolbars, group containers, drag previews, and image exports all work as expected. Try the playground in your browser of choice.
authors:
  - lhein
  - pvinaches
tags:
  - Kaoto
  - Safari
  - Canvas
  - Visual Designer
  - Apache Camel
  - Browser Support
---

Building integration routes should feel smooth wherever you work. Until recently, Safari users hitting the [Kaoto online playground](/playground/) would see misplaced toolbars, broken drag previews, or blank image exports. With the 2.14 release, all of that is fixed. The canvas now renders correctly in Safari, and the playground is a first-class experience in every major browser.

## Under the hood

Safari is stricter than Chromium or Firefox about how HTML behaves inside an SVG `foreignObject`, which the canvas uses to embed step toolbars and group headers. That strictness meant toolbars appeared in the wrong position, group focus rings bled outside their boundaries, drag previews lost their background mid-move, and image exports were unreliable. The fixes moved layout responsibility back to SVG: drag-preview opacity and scale are now applied on the SVG layer, group focus rings are drawn as SVG shapes, and `StepToolbar` became a `StepToolbarOverlay` that lives entirely inside the SVG stacking context. The image export pipeline was tightened up at the same time to embed fonts reliably and enforce unique route IDs. Group backgrounds during drags are also preserved, and the animated canvas toolbar keeps the same rule in place: HTML inside `foreignObject` stays untransformed for Safari.

## Tell us if something looks off

Cross-browser rendering can surface edge cases that are hard to catch in isolation. If you notice anything that does not look right in Safari, please [open an issue](https://github.com/KaotoIO/kaoto/issues/new/choose) or join the conversation in the [GitHub discussions](https://github.com/orgs/KaotoIO/discussions). Screenshots and browser versions are a big help.

---

## Give it a try

- Kaoto online [playground](/playground/): open it in Safari and build a route end-to-end
- [VS Code extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto): the same canvas fixes, available in your editor

Safari is now a full citizen in the Kaoto ecosystem. 🐫