---
title: "Running Exported Projects"
description: "Run and deploy exported Camel Quarkus and Spring Boot projects from VS Code using the pre-configured launch and task configurations"
date: 2026-06-01
weight: 9
---

## Overview

When you export a Camel integration to a Maven project using Kaoto, the exported folder includes a `.vscode/` directory with pre-configured `tasks.json` and `launch.json` files. These give you ready-to-use **Run and Debug** launch configurations so you can run or deploy your project directly from VS Code without any manual setup.

Two runtimes are supported:

- **Camel Quarkus** — runs via `quarkus:dev`
- **Camel on Spring Boot** — runs via `spring-boot:run`

> [!NOTE]
> The `.vscode/` configurations are only written if the files do not already exist in the target folder, so any customizations you make are never overwritten on a subsequent export.

---

## Prerequisites

- **Java** 17 or later
- **Maven wrapper** (`./mvnw`) — included automatically in the exported project

---

## Running the project

Open the exported project folder in VS Code, then switch to the **Run and Debug** panel (`Ctrl+Shift+D` / `Cmd+Shift+D`). Click the configuration dropdown at the top of the panel to see the available launch configurations.

{{< image-sh src="run-and-debug-configurations.png" text="Run and Debug panel showing the available launch configurations for an exported Quarkus project" >}}

### Camel Quarkus

Select **Run (quarkus:dev)** and click the green play button (or press `F5`).

This triggers the `Run (quarkus:dev)` background task, which runs:

```bash
./mvnw quarkus:dev
```

The terminal opens automatically and streams the Quarkus dev-mode output. The task is marked as a background task — VS Code considers it started once the `Started` pattern appears in the output.

### Camel on Spring Boot

Select **Run (spring-boot:run)** and click the green play button (or press `F5`).

This triggers the `Run (spring-boot:run)` background task, which runs:

```bash
./mvnw spring-boot:run
```

The terminal opens automatically and streams the Spring Boot startup output.

---

## Deploying to OpenShift

Both runtimes also include a deploy configuration in the dropdown.

### Quarkus — Deploy on OpenShift

Select **Deploy on OpenShift (Quarkus)** and click play. This runs:

```bash
./mvnw package -Dquarkus.openshift.deploy=true
```

### Spring Boot — Deploy on OpenShift

Select **Deploy on OpenShift (Spring Boot)** and click play. This runs:

```bash
./mvnw package oc:build oc:apply
```

> [!NOTE]
> OpenShift deployment requires the OpenShift CLI (`oc`) and an active cluster login. Ensure you are logged in with `oc login` before triggering the deploy configuration.

---

## Next Steps

- **[Runtime Selector](../04-runtime-selector/)** — Choose the Camel runtime (Quarkus, Spring Boot, or Main) for your integration before exporting
- **[Executing Integrations](../05-executing-integrations/)** — Run integrations directly from VS Code without exporting to a Maven project
