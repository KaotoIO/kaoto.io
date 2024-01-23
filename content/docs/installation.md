---
title: "Installation Guide"
description: "Guide on how to install and run Kaoto, the low-code and no-code editor for Apache Camel."
draft: false
date: "2023-06-19"
categories:
- User
---

## Using our testing instance

We have an [openly available testing instance](https://red.ht/kaoto).

As a suggestion, you can use some of our [workshops](/workshop) as guides.

Learn more about how to use Kaoto in the [Quickstart](/docs/quickstart)

## Using VS Code

Do you already use [Visual Studio Code](https://code.visualstudio.com/)? If you don't, you will need to install it first.

**For the best user experience and for additional supportive features, we suggest installing the [Extension Pack for Apache Camel](https://marketplace.visualstudio.com/items?itemName=redhat.apache-camel-extension-pack), which also includes the Kaoto VS Code extension.**

The [VS Code Kaoto extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto) is integrating Kaoto as an editor.

You can find specific information to get started on the [wiki page of the VS Code Kaoto project](https://github.com/KaotoIO/vscode-kaoto/wiki/Getting-started).

You can also watch this [video](https://www.youtube.com/watch?v=fWovZfyN54k&list=PLU-T8l-XOWOPjrXPojx2WDSegigcNzKs4&index=1&t=1s&pp=gAQBiAQB).

## Using Docker

The only pre-requisite is to have [docker installed](https://docs.docker.com/get-docker/).

```bash
docker pull quay.io/kaotoio/kaoto-app:main
docker run -p8081:8081 quay.io/kaotoio/kaoto-app:main
```

You can now access Kaoto on [http://localhost:8081](http://localhost:8081). If you specified a different port in the `-p` parameter above you need to adapt the URL.

Learn more about how to use Kaoto on the [Quickstart](/docs/quickstart)

Always stop the containers when finishing using Kaoto, so you don't have containers dangling:

```bash
docker stop kaoto-app
```
