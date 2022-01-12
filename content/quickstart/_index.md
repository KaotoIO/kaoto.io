---
title: "QuickStart"
description: "Quickstart to test and start working with Kaoto, the Apache Camel orchestration tool."
draft: false
---

To start Kaoto you need to start both the frontend and the backend.

## Run Backend

There are several options to run the backend. The recommended quickstart way of running Kaoto is through Docker.

The only pre-requisite is to have [docker installed](https://docs.docker.com/get-docker/).

Then, you just have to run the kaotoio/backend image with the following command:

`docker run --rm -p 8080:8080 kaotoio/backend`

This will start the latest snapshot of the backend which will be reachable through the 8080 port.

You can test this worked by entering [http://localhost:8080/step](http://localhost:8080/step).

## Run Frontend

Once the backend is running, you can launch the frontend. This can be done by cloning the repository and running yarn.

You need to have installed the following:
* [Git](https://github.com/git-guides/install-git)
* [Node](https://nodejs.org/en/download/) >= 14
* [Yarn](https://classic.yarnpkg.com/lang/en/docs/install/) (3.x)

First checkout the source code:

`git clone https://github.com/KaotoIO/kaoto-ui.git`

Then install dependencies:

`yarn install`

Duplicate the `.env.example` file and name it `.env`.

Now you can run Kaoto:

`yarn start`

Open [http://localhost:1337](http://localhost:1337) to view it in the browser.

