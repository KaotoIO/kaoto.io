---
title: "About"
description: "Kaoto is the next generation orchestration designer to easily edit and deploy automations and integrations as an alternative to the traditional IDE. Kaoto supports multiple Domain Specific Languages (DSL) like Kamelets and Apache Camel routes."
draft: false
---

Kaoto is an acronym for **Ka**mel **O**rchestration **To**ol. Kaoto is a low code and no code integration designer to edit and deploy based on [Apache Camel](https://camel.apache.org/). It is designed to be extendable and flexible and adaptable to different usecases. [You can find statistics and history of Kaoto here](/timeline).

The user interface have both a source code editor and a drag and drop graphical space to edit workflows. When a change is done in one of them, the other gets updated automatically. This way users can choose to work both no-code or low-code.

![Kaoto in action](/images/about/low-code-kaoto.webp)

Kaoto can load catalogs of building blocks from different sources. By default, Kaoto supports the official [Kamelet catalog](https://camel.apache.org/camel-kamelets). There is also a [growing support for Camel connectors](https://github.com/KaotoIO/camel-component-metadata). You can configure your own catalog of steps (using the official Kamelet catalog or using your own).

![Catalog of steps](/images/about/step-replacement.webp)

You can also extend the user interface. Each step can have its own [extension](https://kaoto.io/docs/add_custom_view/) to configure its properties. This is not also useful when you add your own steps, but also it can help you adapt Kaoto to different kinds of users, hiding or extending certain details important for your usecase.

Although focused on Apache Camel, Kaoto can support multiple Domain Specific Languages (DSL) as described in [the documentation](/docs/add_dsl). The Kaoto team is also working on full [support for cloud-native Apache Camel deployments via Camel-K](https://github.com/KaotoIO/kaoto-backend/issues/10).
