---
title: "Kaoto Infrastructure view: manage Camel dev services from VS Code"
date: 2026-10-08
summary: Kaoto 2.12 shipped a new experimental Infrastructure view for starting, monitoring, and stopping Camel backing services directly from VS Code. It is hidden by default while we gather feedback — here is how to enable it and what it can do.
authors:
  - djelinek
tags:
  - Kaoto
  - Kaoto 2.12
  - Apache Camel
  - VS Code
  - Experimental
  - Camel Infra
  - Camel CLI
  - Dev Services
---

Kaoto 2.12 introduced a new **Infrastructure view** — a sidebar panel that lets you start, monitor, and stop Camel infrastructure services (databases, message brokers, and other backing services) without leaving VS Code. The feature shipped in **2.12** and is present in **2.13**.

{{< image-sh src="infrastructure-view.png" text="The Infrastructure view in the Kaoto sidebar" >}}

Because it is experimental, the view is hidden by default behind a single VS Code setting. This post walks you through enabling it and shows what it can do — and we would love to hear your feedback.

---

## Why it exists

Every non-trivial Camel integration depends on something external: a database, a message broker, a cache. While developing locally, that usually means opening a terminal, running a `docker run` or `podman run` command, waiting for the service to be ready, copying the connection URL into your config, and repeating this every time you restart your machine.

The Infrastructure view moves all of that into Kaoto. One click to start a service, live status in the sidebar, one-click copy of the connection URL into your clipboard.

---

## Enabling the view

The feature is marked **experimental** and hidden by default — that is why you may not have noticed it. Experimental does not mean broken: the view is fully functional and usable today. We keep it opt-in while we gather feedback and decide what to add next.

To turn it on:

1. Open **VS Code Settings** (`Ctrl+,` / `Cmd+,`) and search for `kaoto.infrastructure.enabled`.
2. Check the **Kaoto › Infrastructure: Enabled** checkbox.
3. The **Infrastructure** panel appears in the Kaoto sidebar.

{{< image-sh src="infrastructure-settings.png" text="One setting is all it takes to unlock the Infrastructure view" >}}

---

## Starting a service

Once the view is visible, click the **+** button in the toolbar. Kaoto queries [`camel infra`](https://camel.apache.org/manual/camel-jbang-dev-services.html) — the dev services capability built into Camel JBang — and shows you the list of available services.

Pick one, optionally enter a custom port (leave it empty to use the service default), and the service starts. It appears immediately in the tree with a `starting` badge that flips to `running` once the container is ready.

A couple of guardrails worth knowing:

- **No container runtime?** If Docker or Podman is not running, Kaoto shows a clear error message instead of a cryptic failure.
- **Already running externally?** If the service is already up (started outside VS Code), a dialog lets you choose: **Use Existing** to keep it as-is and register it in the view, or **Stop and Restart** to take over management.

---

## Watching and managing running services

Each running service shows its name, port, and a live status indicator. The view refreshes automatically while services are running so the status stays accurate.

{{< image-sh src="infrastructure-view-service.png" text="Running services in the Infrastructure view with their port and live status" >}}

Hover over a service for inline actions:

- **Stop** — stops the service with a confirmation dialog to prevent accidental stops
- **Show logs** — opens the dedicated VS Code terminal for the service

Right-click for clipboard shortcuts:

- **Copy URL** — copies the service address (`host:port`) to the clipboard, when available
- **Copy port** — just the port number

---

## We want your feedback

This feature is marked **experimental** for a reason: we shipped it to get real-world signal on how developers actually want to manage infrastructure from their editor. Your feedback now directly shapes where it goes next.

Things we are particularly interested in:

- Which services do you start most often?
- Is the start / stop / log flow what you expected, or did something feel off?
- What is missing that would make this part of your daily workflow?

Join the conversation in [GitHub Discussions](https://github.com/orgs/KaotoIO/discussions) or [open an issue](https://github.com/KaotoIO/kaoto/issues/new/choose) if you hit a rough edge.

---

## Give it a try

- Install or update the [Kaoto VS Code extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto) — the Infrastructure view is available from version **2.12** onwards
- Enable `kaoto.infrastructure.enabled` in your VS Code settings
- Read the full **[Infrastructure view documentation](/docs/designer/08-infrastructure-view/)** for a detailed reference
- Start a service and let us know what you think 🐫
