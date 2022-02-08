---
title: "QuickStart"
description: "Quickstart to test and start working with Kaoto, the low code and no code integration orchestration tool."
draft: false
---

To start Kaoto you need to start both the frontend and the backend. 

The recommended quickstart way of running Kaoto is through Docker. The only pre-requisite is to have [docker installed](https://docs.docker.com/get-docker/).

## Run Backend

You can run the kaotoio/backend image with the following command:

`docker run --rm -p 8081:8081 kaotoio/backend`

This will start the latest snapshot of the backend which will be reachable through the 8081 port.

You can test this worked by entering [http://localhost:8081/step](http://localhost:8081/step).

## Run Frontend

Once the backend is running, you can launch the frontend with the following command:

`docker run --rm -p 8080:8080 kaotoio/frontend`

This will start the latest snapshot of the backend which will be reachable through the 8080 port.

Open [http://localhost:8080](http://localhost:8080) to use Kaoto.
