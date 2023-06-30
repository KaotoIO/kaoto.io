---
title: "Listen to a folder"
date: 2023-03-12T12:14:34+06:00
categories: ["beginner"]
image: "/images/workshop/beginner-file/front.png"
description: "Create a route that listens to a folder and outputs by log the modified files."
draft: false
kaoto: 1.0.0
goals: learn how to listen to changes in a folder using Apache Camel
---

## 1.- Log changes

The goals for this exercise are:

 - Start the flow with a `file-watch` step which watches a local folder like `/tmp/tutorial` and configure parameter `recursive` as `false`
 - Then `log` the detected change with an output like `Detected  ${header.CamelFileEventType} on file ${header.CamelFileName} at ${header.CamelFileLastModified}`
 
 **Make sure your folder (/tmp/tutorial) exists before running this integration.**
 
 **This integration will work better when run locally, as the folder must be in the same machine that it gets deployed.**

### Hints

 - To add new steps to the canvas, take a look at the [User Guide](/docs/user-guide/).
 - To configure a step and fill the configuration properties, click on the step icon of the canvas.
 - The first step you want to add is called `file-watch`. Don't confuse it with `file`
 - The second step is a `log`. There may be more than one `log` option, choose the one without the camel logo for simplicity.

### Solution

The following video showcases the solution.

{{< rawhtml >}} 

<video width=100% controls >
    <source src="/images/workshop/beginner-file/1-log-changes.webm" type="video/webm">
    Your browser does not support the video tag.
</video>

{{< /rawhtml >}}

At this point, the text editor should show the following code:

```
- from:
    uri: file-watch:/tmp/tutorial
    parameters:
      recursive: false
    steps:
    - log:
        message: Detected  ${header.CamelFileEventType} on file ${header.CamelFileName}
          at ${header.CamelFileLastModified}

```

If it doesn't look like that but you want to go to the following exercise, you can copy and paste that code on the text editor and click on the green tick button to synchronize.

## 2.- Add a filter

Now we want to add a `filter` between the `file-watch` and the `file` that copies the file in another folder everytime a file gets created.

This will require adding two steps:
 - A step `filter` that will open a branch of steps that will be executed only when `${header.CamelFileEventType} equals `'CREATE'`
 - A step `file` to create the new file in `/tmp/backup` or whatever folder you choose (different from the previous one)

 **Make sure your folder (/tmp/backup) exists before running this integration.**

### Hints

 - To create a new file, you have to use the step `file`
 - Configure the `directory name` of the `file` step as `/tmp/backup` (or whatever folder you are using)
 - The condition of the filter is configured in the `simple` text field as `${header.CamelFileEventType} == 'CREATE'`

### Solution

The following video showcases the solution.

{{< rawhtml >}} 

<video width=100% controls >
    <source src="/images/workshop/beginner-file/2-add-filter.webm" type="video/webm">
    Your browser does not support the video tag.
</video>

{{< /rawhtml >}}

At this point, the text editor should show the following code:

```
- from:
    uri: file-watch:/tmp/tutorial
    parameters:
      recursive: false
    steps:
    - filter:
        simple: ${header.CamelFileEventType} == 'CREATE'
        steps:
        - to:
            uri: file:/tmp/backup
    - log:
        message: Detected  ${header.CamelFileEventType} on file ${header.CamelFileName}
          at ${header.CamelFileLastModified}


```

If it doesn't look like that but you want to go to the following exercise, you can copy and paste that code on the text editor and click on the green tick button to synchronize.


## More information

More information about Apache Camel routes can be found on [the Apache Camel website](https://camel.apache.org/camel-k/1.11.x/languages/yaml.html)
