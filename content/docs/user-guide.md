---
title: "User Guide"
description: "How to create an integration for Apache Camel in a no-code way."
draft: false
date: "2023-06-19"
categories:
- User
---

On this guide we will learn how to create our first workflow using Kaoto in a no-code way. This means, we will not write any source code at this point.

# Starting Kaoto

The first step is to load the Kaoto application. Follow the [QuickStart](/quickstart) to know in which URL you can find it.

Now we want to make sure we are going to build a Kamelet Binding. Click on the top menú on the `+ New Route` button and select the `Kamelet Binding` option.

![](/images/docs/user-guide/1b-configuration.png "Select Kamelet Binding DSL")
![](/images/docs/user-guide/1c-configuration.png "Select Kamelet Binding DSL")

## Adding the first step

The initial page is an empty space with a placeholder with the title `ADD A STEP`.

![](/images/docs/user-guide/1-blank.png "Initial view on Kaoto")

We want to start a new integration by selecting the first step, which is going to be a timer. This timer is going to send a message to the following step. To select it, we either click on the placeholder or clicking on the book icon on the top left. Both options will open the catalog of steps.

![](/images/docs/user-guide/2-step-catalog.png "Step Catalog")

We have to search for the step called `timer-source` and drag and drop it into the placeholder with the title `ADD A STEP`.

![](/images/docs/user-guide/3-first-step.png)

Now that we have our first step in place, we need to configure it. When we click on the step we just dropped, a configuration tab will open on the right side of the editor with all the properties that can be configured. In our case, we want to fill a `Message` as `Hello Kaoto!` and the `Period` with `50000`. This means every `50000`ms a message with the content `Hello Kaoto!` will be sent to the rest of the workflow.

![](/images/docs/user-guide/4-configuration.png)

We can close both the configuration and step catalog at this point, if we want.

## Adding the second step

To add the following step, we have to click on the `+` button. This will open a mini-catalog. We want to log the message sent by the previous step, so we will select the `log-sink` step. This `log-sink` action is on the tab `END`, indicating that no more steps can be added after it.

![](/images/docs/user-guide/5-second-step.png)

Click on it and a new step will be added to your workflow. Note that now we still have a `+` button to add more steps if we wanted in between the timer and the log, but there is no `+` button to add steps before the starting step or after the ending step.

![](/images/docs/user-guide/6-final-step.png)

Your integration is now ready to be deployed. If you are curious on what source code has been, you can open the source code editor tab by clicking on the `</>` button.

![](/images/docs/user-guide/7-source-code.png)

## Running our integration

If you deployed Kaoto connected to a cluster, you will be able to start the integration using the `Deploy` button: the triangle button representing a “start”. We could afterwards stop the integration by clicking on the “stop” button.

