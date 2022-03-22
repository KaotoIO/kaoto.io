---
title: "About"
description: "Kaoto is the next generation orchestration designer to easily edit and deploy automations and integrations. Supports multiple Domain Specific Languages (DSL) like Kamelets and Apache Camel routes."
draft: false
---

Kaoto is an acronym for **Ka**mel **O**rchestration **To**ol. Kaoto is a low code and no code integration designer to edit and deploy.

The user interface have both a source code text editor and a drag and drop graphical space to edit workflows. When a change is done in one of them, the other gets updated automatically. This way users can work both no-code and low-code at the same time as an alternative to the traditional IDE.

![Kaoto in action](/images/about/low-code-kaoto.webp)

Kaoto supports by default Kamelets because of the simplicity of working with them as deployments of the integrations. 

Kaoto can load catalogs of building blocks from different sources. By default, Kaoto supports the official [Kamelet catalog](https://camel.apache.org/camel-kamelets). There is also a [growing support for Camel connectors](https://github.com/KaotoIO/camel-component-metadata).

![Catalog of steps](/images/about/step-replacement.webp)

Kaoto can support multiple Domain Specific Languages (DSL) as described in [the documentation](/docs/add_dsl).

Kaoto supports cloud-native Apache Camel deployments via Camel-K.
