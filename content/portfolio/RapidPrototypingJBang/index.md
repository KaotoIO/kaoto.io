---
title: "Rapid Prototyping with Camel JBang and Kaoto"
date: 2024-01-29T12:00:00+06:00
categories: ["jbang","visual editor", "no-code", "testing"]
summary: "Use live reload of your integration via Camel JBang to speed up development"
---
On the following video we can see how to run your integration using Camel JBang dev mode.

{{< video src="RapidPrototypingJBang.webm" controls="yes" >}}

Please make sure you have the [Camel JBang CLI](https://camel.apache.org/manual/camel-jbang.html) installed before you start.

First we create a new route by selecting "New" in the top menu bar. Make sure that "Camel Route" is selected. This will already spawn a small integration which start with a **timer** and ends with a **log**. The timer is going to send a message to the following log step periodically. The log step will just log the message sent from the previous step. 

Now hit the **Copy to Clipboard** button in the top menu above your route visualization. This will copy the integration source code to your clipboard. We will use that in the next step.

Finally we are going to run the integration in *dev mode* from the clipboard. For this we open a console and enter the following command:

```bash
camel run clipboard.yaml --dev
```

We are using the [Run from Clipboard](https://camel.apache.org/manual/camel-jbang.html#_run_from_clipboard) functionality of the Camel JBang CLI. This means whenever something is copied to your clipboard, it will automatically reloading in the Camel JBang CLI as the current integration. 

You should by now see an output in the console repeating every second. You can now click on the **log** step to open up the configuration form in Kaoto. Now scroll to the **Message** property and change it to whatever you like to show up in the console. Finally hit again the **Copy to Clipboard** button and watch the console reloading the integration and then your new message will show up.

**Please note, this is risky! For a more secure approach see [Dev Mode with Live Reload](https://camel.apache.org/manual/camel-jbang.html#_dev_mode_with_live_reload)**.
