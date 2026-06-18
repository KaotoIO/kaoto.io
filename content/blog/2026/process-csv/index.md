---
title: "New workshop: Process a CSV file"
date: 2026-02-04
summary: Learn to build a complete data processing pipeline with our new intermediate workshop
authors:
  - pvinaches
tags:
  - Kaoto Workshop
  - CSV Processing
  - Enterprise Integration Patterns
  - Kafka
  - PostgreSQL
  - Data Pipeline
  - Intermediate
---

We're excited to announce a new **intermediate-level workshop** that teaches you how to build a complete data processing pipeline using **Kaoto's visual designer** and **Apache Camel**!

## What's the Workshop About?

The [**Process a CSV file**](/workshop/intermediate-csv-processor) workshop guides you through building a real-world integration pipeline that processes healthcare patient data. You'll work with actual data from the Synthea patient dataset and learn how to combine multiple **Enterprise Integration Patterns (EIPs)** to create a robust, production-ready system.

## What You'll Build

A five-route integration pipeline that demonstrates:

- **CSV Ingestion** - Reading and parsing CSV files with automatic archiving
- **Data Validation** - Content-based routing to filter records by data quality
- **Database Integration** - Persisting valid records to PostgreSQL
- **Message Publishing** - Real-time monitoring with Apache Kafka
- **Error Handling** - Capturing and managing invalid records for review

The complete pipeline reads patient data from a CSV file, validates each record, stores valid data in a database, publishes to Kafka for monitoring, and captures invalid records in error files for later correction.

## What You'll Learn

This hands-on workshop covers essential integration patterns and technologies:

- **File polling and CSV data ingestion** - Automated file processing with idempotent consumers
- **Content-based routing** - Intelligent message routing based on data validation rules
- **Database integration** - Working with PostgreSQL using Camel Kamelets
- **Message publishing** - Publishing events to Apache Kafka topics
- **Error handling and data quality management** - Building resilient pipelines with proper error capture

## Who Is This For?

This is an **intermediate-level workshop** designed for developers who:

- Have basic understanding of integration concepts and data processing pipelines
- Are familiar with VSCode and command-line tools
- Want to learn how to build production-ready integration solutions
- Are interested in visual low-code development with Kaoto

## Let's Build it Together

Let us know what you think by joining us in the [GitHub discussions](https://github.com/orgs/KaotoIO/discussions).
Do you have an idea how to improve Kaoto? Would you love to see a useful feature implemented or simply ask a question? Please [create an issue](https://github.com/KaotoIO/kaoto/issues/new/choose).

## Get Started

* **Workshop**: [Process a CSV file](/workshop/intermediate-csv-processor)
* **Demo code**: [GitHub repository](https://github.com/KaotoIO/kaoto-examples/tree/main/csv-processor)
* **Kaoto quickstart**: [Getting started guide](/docs/quickstart/)
* **VS Code extension**: [Install from marketplace](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto)
* **Try Kaoto online**: [Showcase deployment](https://red.ht/kaoto)

Happy integrating! 🚀
