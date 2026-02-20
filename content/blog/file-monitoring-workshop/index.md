---
title: "Updated workshop: Listen to a Folder"
date: 2026-02-24
summary: Learn file system monitoring and event filtering with our beginner-friendly workshop
authors:
  - pvinaches
tags:
  - Kaoto Workshop
  - File Monitoring
  - Message Filter Pattern
  - Apache Camel
  - Beginner
---

We're excited to announce an updated **beginner-level workshop** that teaches you how to build a file monitoring integration using **Kaoto's visual designer** and **Apache Camel**!

## What's the Workshop About?

The [**Listen to a Folder**](/workshop/beginner-file) workshop guides you through creating an integration that monitors a directory for file system changes. You'll learn how to watch folders, filter events, and automatically back up files when they are created.

## What You'll Build

A file monitoring integration that demonstrates:

- **File System Monitoring** - Watching directories for CREATE, MODIFY, and DELETE events
- **Event Filtering** - Using the Message Filter pattern to process only specific events
- **Automatic Backup** - Copying newly created files to a backup directory
- **Event Logging** - Tracking all file system changes with detailed information

The complete integration monitors a folder, logs all file system events, filters for CREATE events, and automatically backs up newly created files to a separate directory.

## What You'll Learn

This hands-on workshop covers fundamental integration concepts:

- **File system monitoring** - Using the `file-watch` component to detect changes
- **Message headers** - Extracting metadata from Camel message headers
- **Message Filter pattern** - Conditionally processing messages based on criteria
- **Simple Expression Language** - Writing expressions to access message data
- **Local testing** - Running and debugging Camel routes with Kaoto

## Who Is This For?

This is a **beginner-level workshop** designed for developers who:

- Are new to Apache Camel and integration patterns
- Want to learn visual low-code development with Kaoto
- Need to understand file system integration
- Are looking for a gentle introduction to Enterprise Integration Patterns

## Let's Build it Together

Let us know what you think by joining us in the [GitHub discussions](https://github.com/orgs/KaotoIO/discussions).
Do you have an idea how to improve Kaoto? Would you love to see a useful feature implemented or simply ask a question? Please [create an issue](https://github.com/KaotoIO/kaoto/issues/new/choose).

## Get Started

* **Workshop**: [Listen to a Folder](/workshop/beginner-file)
* **Comprehensive Guide**: [Complete tutorial](/workshop/beginner-file/comprehensive-guide)
* **Kaoto quickstart**: [Getting started guide](/docs/quickstart/)
* **VS Code extension**: [Install from marketplace](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto)
* **Try Kaoto online**: [Showcase deployment](https://red.ht/kaoto)

Happy integrating! 🚀