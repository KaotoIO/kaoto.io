---
title: "Create a multiple choice route in Apache Camel"
date: 2023-03-10T12:14:34+06:00
categories: ["intermediate"]
image: "/images/workshop/beginner-camel-choice/front.png"
description: "Create a route that uses content route based EIP."
draft: false
---

On this workshop we will learn how to create a multiple choice route in Apache Camel using mostly the graphical canvas. 

**We will be using Kaoto version `1.0.0`.**

The suggested way of following this workshop is to read the goals of each exercise and try to do it without looking at the solution. After finishing the exercise, you can check if the solution reached is the same as the solution suggested.

If you are having difficulties with an exercise, you can try to take a look at the `Hints`. If that's not enough, you can check on the `Solution` section how to do it.

Note that there may be more than one way of finishing the exercise.

## 1.- Create a simple choice 

We are going to start by creating a simple if-else code **using the graphical canvas**. We will have 5 steps in total:

![](/images/workshop/beginner-camel-choice/first.png "Create a simple choice")

 - A first step which will be a **timer** with `timer name` property filled as `tutorial`
 - A second step which will be a **set-body** that will generate randomly a zero or a one.
 - A third step which will be a **choice** step. This step will contain two branches:
    - A branch that detects if `${body} == 1`, leading to a **log** with a `message` configured as `"We got a one."`
    - A branch that will be fallback branch, leading to a **log** with a `message` configured as `"We got a ${body}."`

### Hints

#### A first step which will be a **timer** with `timer name` property filled as `tutorial`

 - To add new steps to the canvas, take a look at the [User Guide](/docs/user-guide/).
 - To configure a step and fill the configuration properties, click on the step icon of the canvas.
 
#### A second step which will be a **set-body** that will generate randomly a zero or a one.

 - You can generate random numbers using the simple language function [random](https://camel.apache.org/components/3.20.x/languages/simple-language.html#_variables).
 - The simple expression `${random(2))}` will generate a random number between zero (included) and two (not included). 
 - When configuring the `set-body`, we can use the `expression syntax` `Simple` and then the `expression` used will be `${random(2)}`. 
 
#### A third step which will be a **choice** step.

 - To configure the different choices, we click on the `choice` step which will open a tab with two buttons: ` + When` and `+ Otherwise`
 - We have to click once on each button to create an `if` and an `else`.
 - If we add more than one `when` (if condition), we can remove them using the trash icon.
 - We have to fill the condition `${body} == 1` on the `when` and click `Apply`.
 - We can now add steps on the canvas as before, just clicking on the placeholder.
 - We add a `log` step. Kaoto offers two `log` steps to add: the camel component and the EIP. For simplicity, we will choose the EIP (the one without the Camel logo).
 - We have to fill the `message` property as described on the goals.

### Solution

The following video showcases the solution.

{{< rawhtml >}} 

<video width=100% controls >
    <source src="/images/workshop/beginner-camel-choice/1-create-simple-choice.mp4" type="video/mp4">
    Your browser does not support the video tag.  
</video>

{{< /rawhtml >}}

At this point, the text editor should show the following code:

```
- from:
    uri: timer:tutorial
    steps:
    - set-body:
        simple: ${random(2)}
    - choice:
        when:
        - simple: ${body} == 1
          steps:
          - log:
              message: We got a one.
        otherwise:
          steps:
          - log:
              message: We got a ${body}
```

If it doesn't look like that but you want to go to the following exercise, you can copy and paste that code on the text editor and click on the green tick button to synchronize.

## 2.- Set Header instead of Body

On this exercise we are going to modify the previously created route to replace the `set-body` with a `set-header`.

The goals for this exercise are:

 - Modify the route so instead of setting the body, we will use a header called `myChoice` for the decision.

### Hints

 - To replace an existing component, select it from the step catalog and drag and drop on top of it.
 - Note that you have to use the proper type of step: `START`, `MIDDLE` or `END`.
 
### Solution

The following video showcases the solution.

{{< rawhtml >}} 

<video width=100% controls >
    <source src="/images/workshop/beginner-camel-choice/2-set-header.webm" type="video/mp4">
    Your browser does not support the video tag.
</video>

{{< /rawhtml >}}

At this point, the text editor should show the following code:

```
- from:
    uri: timer:tutorial
    steps:
    - set-header:
        simple: ${random(2)}
        name: myChoice
    - choice:
        when:
        - simple: ${header.myChoice} == 1
          steps:
          - log:
              message: We got a one.
        otherwise:
          steps:
          - log:
              message: We got a ${body}
```

If it doesn't look like that but you want to go to the following exercise, you can copy and paste that code on the text editor and click on the green tick button to synchronize.

## 3.- Connect to an external service

On this exercise we are going to modify the previously created route to add a more complex route. We are going to modify the `when` branch to send a request to an API.

The goals for this exercise are:

 - Modify the route so when the generated random number is `0` it calls the service `https://dog-api.kinduff.com/api/facts` to display a random dog fact on the log
 - Modify the route so when the generated random number is `1` it calls the service `https://cat-fact.herokuapp.com/facts/random` to display a random cat fact on the log
 - Move the log out of the `choice` branches
 - Change the log to just display the `${body}` of the message

Note: these two services are testing services that we don't control. Make sure they run properly before attempting to use them to prevent any weird errors.

### Hints

 - To call an external service, you can use the `https` component.
 - You just need to configure the `HTTP Uri` with the proper value.
 - To remove a step from a flow branch, there is a `-` button that appears when you hover over the step.
 - You can add steps after the `choice` by clicking on the `+` button near it.
 
### Solution

The following video showcases the solution.

{{< rawhtml >}} 

<video width=100% controls >
    <source src="/images/workshop/beginner-camel-choice/3-connect-external-service.webm" type="video/mp4">
    Your browser does not support the video tag.
</video>

{{< /rawhtml >}}

At this point, the text editor should show the following code:

```

- from:
    uri: timer:tutorial
    steps:
    - set-header:
        simple: ${random(2)}
        name: myChoice
    - choice:
        when:
        - simple: ${header.myChoice} == 1
          steps:
          - to:
              uri: https://cat-fact.herokuapp.com/facts/random
        otherwise:
          steps:
          - to:
              uri: https://dog-api.kinduff.com/api/facts
    - log:
        message: ${body}
```

If it doesn't look like that but you want to go to the following exercise, you can copy and paste that code on the text editor and click on the green tick button to synchronize.

## Deployment

At this point, if you deploy the existing integration, the log should show something like this:

```

2023-04-11 12:37:17.107  INFO 69161 --- [           main] el.impl.engine.AbstractCamelContext : Apache Camel 3.20.3 (maria-test) started in 1s19ms (build:98ms init:709ms start:212ms JVM-uptime:2s)
2023-04-11 12:37:18.990  INFO 69161 --- [imer://tutorial] maria-test.camel.yaml:17            : {"facts":["Dogs are all direct descendants of wolves."],"success":true}
2023-04-11 12:37:19.865  INFO 69161 --- [imer://tutorial] maria-test.camel.yaml:17            : {"status":{"verified":null,"sentCount":0},"_id":"61d36272403b4002d3798703","user":"61b8566766b26cede617b4ef","text":"35342r54235233.","type":"cat","deleted":false,"createdAt":"2022-01-03T20:54:10.612Z","updatedAt":"2022-01-03T20:54:10.612Z","__v":0}
2023-04-11 12:37:20.216  INFO 69161 --- [imer://tutorial] maria-test.camel.yaml:17            : {"status":{"verified":null,"sentCount":0},"_id":"64328a14b831d40018499dfc","user":"642fee0fd56bfe7a06ce6788","text":"Something interesting and amazing about cats.","type":"cat","deleted":false,"createdAt":"2023-04-09T09:49:08.850Z","updatedAt":"2023-04-09T09:49:08.850Z","__v":0}
2023-04-11 12:37:21.874  INFO 69161 --- [imer://tutorial] maria-test.camel.yaml:17            : {"status":{"verified":null,"sentCount":0},"_id":"640977e892271493a95639ad","user":"640027109444b2a501a06ba8","text":"Cat it the best animal in the world< pero no todo el mundo piensa asi.","type":"cat","deleted":false,"createdAt":"2023-03-09T06:08:40.401Z","updatedAt":"2023-03-09T06:08:40.401Z","__v":0}
2023-04-11 12:37:22.143  INFO 69161 --- [imer://tutorial] maria-test.camel.yaml:17            : {"facts":["During the Middle Ages, Great Danes and Mastiffs were sometimes suited with armor and spiked collars to enter a battle or to defend supply caravans."],"success":true}
2023-04-11 12:37:23.142  INFO 69161 --- [imer://tutorial] maria-test.camel.yaml:17            : {"facts":["One of the most famous Labrador Retrievers was \"Endal,\" an assistance dog recognized as the most decorated dog in the world."],"success":true}
2023-04-11 12:37:24.140  INFO 69161 --- [imer://tutorial] maria-test.camel.yaml:17            : {"facts":["Americans love dogs! 44% of U.S. households have a dog, which equates to 55.3 million homes"],"success":true}
2023-04-11 12:37:25.586  INFO 69161 --- [imer://tutorial] maria-test.camel.yaml:17            : {"status":{"verified":null,"sentCount":0},"_id":"6433e407c8f25e1d24c35557","user
```

## More information

More information about Apache Camel routes can be found on [the Apache Camel website](https://camel.apache.org/camel-k/1.11.x/languages/yaml.html)
