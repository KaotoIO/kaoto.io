---
title: "Add Custom View"
description: "How to add a custom view to configure specific steps."
draft: false
date: "2021-01-10"
tags:
- Custom View
categories:
- Development
- Extension
- Frontend
image: "images/portfolio/screenshot-01.png"
---

Kaoto frontend is extendable allowing custom views when configuring steps.

## Implement Extension in Javascript

For each extension, you need to implement a React app that will be displayed when configuring and displaying the step. You can use one of the [example extension](https://github.com/KaotoIO/step-extension) as a guide.

## Add View Definition to repository

For each extension, you need to add a new file on your View Definition repository. You can use one of the [default View Definitions](https://github.com/KaotoIO/kaoto-viewdefinition-catalog).

```
name: Custom Details
id: detail-step
type: step
url: https://step-extension.netlify.app/remoteEntry.js
module: './Button'
scope: 'stepextension'
constraints: 
   -
      mandatory: true
      operation: CONTAINS_STEP_NAME
      parameter: twitter-search-source      
```

It is important that the url points to where you have deployed the extension implemented in the previous step.

The constraints will define when this extension will be shown. On the example, this extension will be shown when configuring the twitter-search-source kamelet.
