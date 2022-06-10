---
title: "Quickstart"
description: "Quickstart to test and start working with Kaoto, the low code and no code integration orchestration tool."
draft: false
---

To start Kaoto you need to start both the frontend and the backend. 

The recommended quickstart way of running Kaoto is through Docker. The only pre-requisite is to have [docker installed](https://docs.docker.com/get-docker/).

## Run Backend

You can run the kaotoio/backend image with the following command:

```bash
docker run --rm -d -p 8081:8081 --name kaoto-backend kaotoio/backend:0.2.0
```

This will start the latest snapshot of the backend which will be reachable through the 8081 port.

You can test this worked by entering [http://localhost:8081/step](http://localhost:8081/step).

## Run Frontend

Once the backend is running, you can launch the frontend with the following command:

```bash
docker run --rm -d -p 8080:80 -e KAOTO_API=http://localhost:8081 --name kaoto-frontend kaotoio/frontend:0.2.0
```

This will start the latest snapshot of the backend which will be reachable through the 8080 port.

Open [http://localhost:8080](http://localhost:8080) to use Kaoto.

## Upgrading Kaoto

If this is not your first time running Kaoto, you may need to refresh the version you have downloaded on your computer. 

The following commands will download the latest release:

```bash
docker pull kaotoio/backend:latest

docker pull kaotoio/frontend:latest
```

If you are an adventurer looking for the nightly version, you can also do:

```bash
docker pull kaotoio/frontend:nightly

docker pull kaotoio/backend:nightly
```

## Stop Kaoto

Always stop the containers when finishing using Kaoto, so you don't have containers dangling:

```bash
docker stop kaoto-backend

docker stop kaoto-frontend
```

