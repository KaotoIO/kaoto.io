---
title: "Quickstart Guide"
description: "How to create an integration for Apache Camel in a no-code / low-code way."
date: 2024-09-13
---

On this guide you will learn how to create your first route using Kaoto in a no-code way. This means, you will not write any source code at this point.

## Getting Kaoto

The first step is to install the Kaoto VS Code extension. Follow the [Installation Guide](/docs/installation) to find out more about how to do it. Once done with the installation tasks you should launch VS Code. Make sure you have created and selected a workspace folder where your integration will be stored. If you did not select a workspace, many commands will not show up as expected or behave differently.

## Switching to the Kaoto View

<div style="display: flex; align-items: center;">
  <img src="kaoto-view.png" alt="Switch to the Kaoto View" style="margin-right: 20px;" />
  <p>We have introduced a new view for Kaoto to make it very straight forward and easy to work with your integrations. To switch to the Kaoto view, click on the Kaoto Camel icon in the left sidebar of VS Code. This view allows you to create and manage your integrations. It will also help you keeping track of what is inside your integrations files, helps you launching the integrations locally or on a Kubernetes cluster and it also offers a collection of useful links to resources on the web which can accelerate your integration work further.</p>
</div>

## Creating a New Camel Route

With the `Kaoto` view (the Kaoto Camel icon) on the left sidebar open you will see the `Integration` section on top. When moving the mouse to the right side of the `Integrations` headline you will see some small icons, one of the is a file with a plus sign. Click on it, select `New Camel Route` and follow the instructions to create your first Camel Route.

Once done, the new file will be created and the Kaoto editor should appear as shown in the video below. If the editor does not appear, revisit the earlier steps to ensure you followed all instructions correctly.

<video controls width="600">
  <source src="create-integration.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

At this point, you have successfully created your first working Camel Route, which can be tested immediately.

## Running the Camel Route

Testing your integration is easy and straigth forward. In the `Integrations` section hover over the file name of your integration and this will reveal some useful buttons. One of these buttons is a Camel icon with a green play button. Click it to launch your integration locally using [Camel JBang](https://camel.apache.org/manual/camel-jbang.html). Please check the below video which will show you how to launch the integration and possible actions to interact with a running integration.

<video controls width="600">
  <source src="launch-integration.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

As you can see in the video your integration is launched in Dev Mode and changes to the integration via the Kaoto editor or the source code will be reloaded whenever you save. This will help you prototyping faster.
