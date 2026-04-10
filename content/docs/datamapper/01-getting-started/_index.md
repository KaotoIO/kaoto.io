---
title: "Getting Started"
description: "Add DataMapper to your route and understand the interface"
date: 2026-04-01
weight: 1
---

## Overview

To use the DataMapper for creating data transformations, you need to add and configure a DataMapper step in your Camel route. This guide covers the essential steps to get started with the DataMapper interface.

---

## Adding a DataMapper step

Now let's add a DataMapper step to your Camel route. The DataMapper provides a visual interface for creating data transformations without writing XSLT code manually.

1. Add a **Kaoto DataMapper** step in your Camel route. When you `Append`, `Prepend` or `Replace` a step in the Kaoto Design view, you can find the **Kaoto DataMapper** step in the catalog.
{{< image-sh src="catalog-datamapper-tile.png" text="DataMapper Catalog Tile" >}}

2. Click the added **Kaoto DataMapper** step in the Kaoto Design to open the config form.
{{< image-sh src="kaoto-datamapper-step.png" text="Kaoto DataMapper step" >}}

3. In the config form, click the `Configure` button to open the visual DataMapper editor.
{{< image-sh src="datamapper-configure-button.png" text="DataMapper Configure button" >}}

4. This will open the visual DataMapper editor where you can create your data mappings.
{{< image-sh src="datamapper-blank.png" text="Blank DataMapper UI" >}}

---

## Understanding the Interface

The DataMapper editor is divided into two main sections that represent the data transformation flow:

{{< image-sh src="datamapper-source-target.png" text="Source and Target" >}}

### Source Section (Left Side)

The **Source** section represents where your data comes from - the input side of your mappings. This is where the DataMapper step reads the data from.

- **Body** - The incoming Camel Message Body (the main data payload)
- **Parameters** - Additional data from Camel Variables and Message Headers

Think of this as the "input" side of your transformation - the data you're reading from.

### Target Section (Right Side)

The **Target** section represents where your data goes to - the output side of your mappings. This is where the DataMapper step writes the transformed data.

- **Body** - The outgoing Camel Message Body (the transformed result)

Think of this as the "output" side of your transformation - the data structure you're creating.

> [!TIP]
> You can adjust the font size in the DataMapper interface to match your preference. Use the **+** and **-** magnifier icons in the toolbar to make the text larger or smaller for better readability.
> {{< image-sh src="datamapper-zoom.png" text="Zoom controls in DataMapper toolbar" >}}

---

## Working with Parameters

Parameters allow you to access Camel Variables and Message Headers in your mappings. This is useful when you need to combine data from multiple sources in your transformation.

### Add a Parameter

Follow the below steps to add a parameter.

1. Click the plus **+** button on the right side of the `Parameters` title.
{{< image-sh src="datamapper-add-parameter.png" text="Parameters" >}}

2. Now type the parameter name and click the check button on the right.
{{< image-sh src="datamapper-add-parameter-confirm.png" text="Add Parameter confirm" >}}

> [!TIP]
> When you have many parameters, you can improve readability by hiding them visually. Click the eye icon next to the Parameters section to toggle the visibility of the parameter list.
> {{< image-sh src="datamapper-hide-parameters.png" text="Hide parameters to improve readability" >}}

> [!NOTE]
> While Camel Exchange Properties are also mapped to parameters in the current `camel-xslt-saxon` implementation, after the [Camel Variables](https://camel.apache.org/manual/variables.html) have been introduced, it is no longer recommended to store application data in Camel Exchange Properties. We encourage to use [Camel Variables](https://camel.apache.org/manual/variables.html) instead.

### Delete a Parameter

To remove a parameter, click the trash icon next to it and confirm the deletion.

{{< image-sh src="datamapper-delete-param-trash.png" text="Click trash icon to delete parameter" >}}
{{< image-sh src="datamapper-delete-param-confirm.png" text="Confirm parameter deletion" >}}

> [!NOTE]
> If the parameter is used in any mappings, those mappings will become invalid after deletion. Review your mappings before removing parameters.

---

## Next Steps

Now that you understand the DataMapper interface, you can:

- **[Attach schemas](../02-attaching-schemas/)** to visualize your data structures
- **[Create mappings](../03-creating-mappings/)** between source and target fields
- **[Add conditional logic](../04-conditional-mappings/)** for complex transformations