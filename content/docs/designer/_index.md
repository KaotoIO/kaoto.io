---
title: "Designer"
description: "Learn how to use Kaoto's visual designer to build and manage Apache Camel integrations"
date: 2026-03-31
weight: 3
---

## Welcome to Kaoto Designer

Kaoto provides a powerful visual designer for building Apache Camel integrations without writing code. Whether you're creating simple file processors or complex AI-powered workflows, the designer helps you:

- **Create and manage integrations** visually using drag-and-drop components
- **Configure components** through intuitive forms instead of YAML syntax
- **Build routes** by connecting Camel components, Kamelets, and EIPs (Enterprise Integration Patterns)
- **Test and run** your integrations directly from VS Code

The designer supports all major Camel resource types including Routes, Kamelets, and Pipes, giving you the flexibility to build integrations that match your specific needs.

## Getting Started

New to Kaoto? Start with **[Managing Integrations](./01-managing-integrations/)** to learn how to create, organize, and work with your first integration. This guide covers everything from creating new integrations to understanding the different resource types available in Kaoto.

Once you have an integration created, dive into **[Working with Nodes](./02-working-with-nodes/)** to master the essential operations for building your routes. This guide shows you how to add, replace, delete, and configure steps in your integration, as well as how to enable or disable components during development and generate documentation for your work.

After building your first integration, learn how to **[Reordering Nodes](./03-reordering-nodes/)** to reorganize your routes efficiently. This guide covers drag-and-drop operations, copy/paste functionality, and move-before/after actions to help you structure your integrations exactly how you need them.

As your projects grow, you'll want to explore the **[Runtime Selector](./04-runtime-selector/)** to choose the right Apache Camel runtime for your needs. This guide explains how to work with different Camel versions including Main, Quarkus, and Spring Boot, and how to configure custom catalog libraries to match your project's requirements.

Ready to test your integrations? The **[Executing Integrations](./05-executing-integrations/)** guide shows you how to run and test your Camel routes directly from VS Code. Learn how to execute a single route for focused testing, run all routes in a folder for integration testing, or launch your entire workspace to verify end-to-end flows. This guide covers everything from starting and stopping routes to troubleshooting common execution issues and following best practices for development workflows.

Once you're comfortable with the basics, explore the other sections to master component configuration, node management, and advanced designer features.
