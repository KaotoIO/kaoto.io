---
title: "Quickstart"
description: "Quickstart to test and start working with Kaoto, the low code and no code integration orchestration tool."
draft: false
---

To start Kaoto you need to start both the frontend and the backend. 

The recommended quickstart way of running Kaoto is through Docker. The only pre-requisite is to have [docker installed](https://docs.docker.com/get-docker/).

```bash
docker run --rm  -p 8081:8081  --name kaoto quay.io/kaotoio/standalone:test
```

You can now access Kaoto on [http://localhost:8081](http://localhost:8081)


Always stop the containers when finishing using Kaoto, so you don't have containers dangling:

```bash
docker stop kaoto
```

