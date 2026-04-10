---
title: "DataMapper"
description: "Visual data transformation tool for mapping XML and JSON data structures in Apache Camel routes"
date: 2026-04-01
weight: 4
---

## Welcome to Kaoto DataMapper

The Kaoto DataMapper is a visual tool for creating data transformations in your Apache Camel routes. It provides a graphical interface to map data between XML and JSON structures using drag-and-drop operations, eliminating the need to write complex XSLT code manually.

{{< image-sh src="datamapper-done.png" text="Example of completed data mappings" >}}

Whether you're transforming XML to JSON, merging multiple data sources, or applying complex business logic to your data, the DataMapper helps you:

- **Map data visually** using drag-and-drop between source and target fields
- **Work with schemas** to visualize XML and JSON data structures
- **Create conditional logic** with if, choose-when-otherwise, and for-each mappings
- **Build complex transformations** using the XPath expression editor
- **Test and validate** your mappings in real-time

The DataMapper generates optimized XSLT 3.0 code that executes at runtime, giving you the power of XSLT without writing it manually.

---

## Getting Started

New to DataMapper? Start with **[Getting Started](./01-getting-started/)** to learn how to add a DataMapper step to your route and understand the interface. This guide introduces you to the Source and Target sections and shows you how to add parameters.

Once you have the DataMapper added, dive into **[Attaching Schemas](./02-attaching-schemas/)** to work with XML and JSON schemas. Learn how to attach schema files, choose root elements for XML, and understand JSON-specific characteristics.

After attaching your schemas, learn how to **[Create Mappings](./03-creating-mappings/)** between source and target fields using drag-and-drop or XPath expressions.

As your transformations grow more complex, explore **[Conditional Mappings](./04-conditional-mappings/)** to add logic with if statements, choose-when-otherwise, and for-each loops for processing collections.

When you need complex transformations, the **[XPath Editor](./05-xpath-editor/)** guide shows you how to use XPath functions with practical examples for string manipulation, conditionals, calculations, and more.
