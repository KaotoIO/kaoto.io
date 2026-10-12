---
title: "Infrastructure View"
description: "Start, monitor, and stop Camel infrastructure services such as databases and message brokers directly from VS Code using the Kaoto Infrastructure view"
date: 2026-10-08
weight: 8
---

## Overview

The **Infrastructure view** is a Kaoto sidebar panel that integrates with `camel infra` to let you start, monitor, and stop backing services — databases, message brokers, and other infrastructure your integration depends on — without leaving VS Code.

> [!NOTE]
> The view is hidden by default and must be enabled in your VS Code settings before it appears.

---

## Enabling the Infrastructure view

1. Open **VS Code Settings** (`Ctrl+,` / `Cmd+,`) and search for `kaoto.infrastructure.enabled`.
2. Check the **Kaoto › Infrastructure: Enabled** checkbox.
3. The **Infrastructure** panel appears in the Kaoto sidebar.

{{< image-sh src="infrastructure-settings.png" text="Enabling the Infrastructure view in VS Code Settings" >}}

---

## Starting a service

1. In the **Infrastructure** panel, click the **+** button in the toolbar.
2. A list of all services available via `camel infra` appears — select the one you want to start.
3. An input box prompts for a custom port. Leave it empty to use the service default, or enter a port number between 1 and 65535.
4. The service starts and appears as a tree item in the view with a `starting` status indicator, which changes to `running` once the service is ready.

> [!NOTE]
> Starting infrastructure services requires a container runtime — **Docker** or **Podman** — to be installed and running. If no container runtime is detected, Kaoto shows a clear error message instead of starting the service.

### Service already running

If the service you selected is already running outside VS Code, a dialog gives you two choices:

| Option | Behaviour |
|--------|-----------|
| **Use Existing** | Keeps the externally-started instance and registers it in the view |
| **Stop and Restart** | Stops the external instance and starts a fresh one managed by Kaoto |

---

## Managing running services

Each running service is displayed as a tree item showing its name, port (if known), and a live status indicator (`starting`, `running`, or `stopping`). While at least one service is running, the view refreshes automatically to keep status up to date.

{{< image-sh src="infrastructure-view.png" text="Infrastructure view showing running Camel infra services" >}}

Hover over a service item to reveal its inline action buttons:

| Action | Description |
|--------|-------------|
| **Stop** | Stops the service; a confirmation dialog prevents accidental stops |
| **Show logs** | Opens the dedicated VS Code terminal for the service so you can inspect its output |

Right-click a service item for additional options:

| Action | Description |
|--------|-------------|
| **Copy URL** | Copies the service address (`host:port`) to the clipboard, when available |
| **Copy port** | Copies just the port number to the clipboard |

---

## Next Steps

- **[Executing Integrations](../05-executing-integrations/)** — Run your Camel routes locally from VS Code
- **[Custom Kamelets](../07-custom-kamelets/)** — Build reusable Kamelet components for your workspace
