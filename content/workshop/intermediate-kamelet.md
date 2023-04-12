---
title: "Create a Kamelet in Apache Camel"
date: 2023-03-11T12:14:34+06:00
categories: ["intermediate"]
image: "/images/workshop/intermediate-kamelet/front.png"
description: "Create a Kamelet using Kaoto."
draft: false
---

On this workshop we will learn how to create a Kamelet in Apache Camel using the graphical canvas. We are going to create something similar to the [Chuck Norris source](https://camel.apache.org/camel-kamelets/3.20.x/chuck-norris-source.html), but generating cat facts.

**We will be using Kaoto version `1.0.0`.**

The suggested way of following this workshop is to read the goals of each exercise and try to do it without looking at the solution. After finishing the exercise, you can check if the solution reached is the same as the solution suggested.

If you are having difficulties with an exercise, you can try to take a look at the `Hints`. If that's not enough, you can check on the `Solution` section how to do it.

Note that there may be more than one way of finishing the exercise.

## 1.- Make sure we are creating a Kamelet

We are going to start by making sure the `Settings` are properly configured.

### Hints

 - Look for the burguer (three dots) menu top right
 - At the end of the Settings window there is a `Type` that should be set to `Kamelet`.

### Solution

The following video showcases the solution.

{{< rawhtml >}} 

<video width=100% controls >
    <source src="/images/workshop/intermediate-kamelet/1-make-sure-kamelet.webm" type="video/webm">
    Your browser does not support the video tag.
</video>

{{< /rawhtml >}}

## 2.- Create the Flow

The goals for this exercise are:

 - Add a first step of `timer` type with a `period` of `10000`
 - Add another step that calls the cat facts service: `https://cat-fact.herokuapp.com/facts/random`
 - Add a `set-body` that extracts the `text` attribute of the response
 - End the flow with a `kamelet:sink`

### Hints

 - The `timer` component needs two configuration properties: `Timer name` and `Period`.
 - To call an external service, use the `https` component
 - To extract the attribute of the response, use a `set-body` with simple language and the following expression: `$.text`.
 - The `kamelet:sink` is an end step.
 
### Solution

At this point, the text editor should show the following code:

```

apiVersion: camel.apache.org/v1alpha1
kind: Kamelet
metadata:
  annotations:
    camel.apache.org/kamelet.icon: data:image/svg+xml;base64,PD94bWwgdmVy[...]
  labels:
    camel.apache.org/kamelet.type: source
  name: integration-source
spec:
  definition:
    title: null
    description: ''
    properties: {}
  dependencies:
  - camel:core
  - camel:timer
  - camel:https
  template:
    from:
      uri: timer:cats
      parameters:
        period: '10000'
      steps:
      - to:
          uri: https://cat-fact.herokuapp.com/facts/random
      - set-body:
          simple: $.text
      - to:
          uri: kamelet:sink

```

If it doesn't look like that but you want to go to the following exercise, you can copy and paste that code on the text editor and click on the green tick button to synchronize.

## 3.- Configure title and description

The goals for this exercise are:

 - Give a proper description to the kamelet, like `Gets periodically Cat facts.` using the Settings.
 - Give a proper `title` to the kamelet, like `Cat Source` using the source code editor.
 
### Hints

 - All these properties can be found on the `spec/definition` section of the yaml source code.
 - You can edit the `description` either on the source code or using the Settings menu.
 - The Settings menu is on the three dot hamburguer menu top right.
 
### Solution


At this point, the text editor should show the following code:

```

apiVersion: camel.apache.org/v1alpha1
kind: Kamelet
metadata:
  annotations:
    camel.apache.org/kamelet.icon: data:image/svg+xml;base64,PD94bWwgdmVy[...]
  labels:
    camel.apache.org/kamelet.type: source
  name: integration-source
spec:
  definition:
    title: Cat Source
    description: Gets periodically Cat facts.
    properties: {}
  dependencies:
  - camel:core
  - camel:timer
  - camel:https
  template:
    from:
      uri: timer:cats
      parameters:
        period: '10000'
      steps:
      - to:
          uri: https://cat-fact.herokuapp.com/facts/random
      - set-body:
          simple: ${body['text']}
      - to:
          uri: kamelet:sink

```

If it doesn't look like that but you want to go to the following exercise, you can copy and paste that code on the text editor and click on the green tick button to synchronize.

## 4.- Add Unmarshal

The goals for this exercise are:

 - Add an `unmarshal` step before `set-body` using the source code editor
 - The type of `unmarshal` will be `json` and use the `library` `Gson`
 
### Hints

 - You can add the `unmarshal` step on the graphical canvas, but (on version `1.0.0` you need the source code editor to properly configure it.
 - The proper expression to configure `unmarshal` on the source code is the following:
 
```
      - unmarshal:
          json:
            library: Gson
```
 
### Solution

At this point, the text editor should show the following code:

```

apiVersion: camel.apache.org/v1alpha1
kind: Kamelet
metadata:
  annotations:
    camel.apache.org/kamelet.icon: data:image/svg+xml;base64,PD94bWwgdmVy[...]
  labels:
    camel.apache.org/kamelet.type: source
  name: integration-source
spec:
  definition:
    title: Cat Source
    description: Gets periodically Cat facts.
    properties: {}
  dependencies:
  - camel:core
  - camel:timer
  - camel:https
  template:
    from:
      uri: timer:cats
      steps:
      - to:
          uri: https://cat-fact.herokuapp.com/facts/random
      - unmarshal:
          json:
            library: Gson
      - set-body:
          simple: ${body['text']}
      - to:
          uri: kamelet:sink
```

If it doesn't look like that but you want to go to the following exercise, you can copy and paste that code on the text editor and click on the green tick button to synchronize.


## 5.- Check the dependencies

Kaoto is able to automatically detect many of the dependencies needed for the Kamelet. Open the source code editor and look for the `dependencies` section. 

Goals for this exercise:
 
  - Add manually the `camel:gson` dependency
  
If instead of `camel:https` Kaoto is showing a `camel:http` that means you used the `http` component instead of the `https`.

Also note that Kaoto also detected this is a kamelet source, as it starts with a `timer` and ends with a `kamelet:sink`. Therefore, the name  of the kamelet in the source code, has a `-source` appended to it.
 
After this exercise, our kamelet will be ready to deploy.
 
### Solution

At this point, the text editor should show the following code:
```

apiVersion: camel.apache.org/v1alpha1
kind: Kamelet
metadata:
  annotations:
    camel.apache.org/kamelet.icon: data:image/svg+xml;base64,PD94bWwgdmVy[...]
  labels:
    camel.apache.org/kamelet.type: source
  name: integration-source
spec:
  definition:
    title: Cat Source
    description: Gets periodically Cat facts.
    properties: {}
  dependencies:
  - camel:core
  - camel:timer
  - camel:https
  - camel:gson
  template:
    from:
      uri: timer:cats
      steps:
      - to:
          uri: https://cat-fact.herokuapp.com/facts/random
      - unmarshal:
          json:
            library: Gson
      - set-body:
          simple: ${body['text']}
      - to:
          uri: kamelet:sink
```

### Hints

 - The source code editor can be shown by clicking on the `</>` top menu item.

## More information

More information about Apache Camel Kamelets can be found on [the Apache Camel website](https://camel.apache.org/camel-kamelets)
