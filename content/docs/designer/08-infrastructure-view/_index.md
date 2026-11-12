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
> Starting infrastructure services requires a container runtime — **Docker** or **Podman** — to be installed and running. If no container runtime is detected, Kaoto shows a clear error message instead of starting the service. On Linux with Podman, the Podman API socket must also be enabled — see [Running with Podman on Linux](#running-with-podman-on-linux).

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

## Running with Podman on Linux

> [!NOTE]
> This section only applies to **Linux + Podman**. On macOS and Windows, Podman runs inside a Podman machine (a VM) that already exposes a Docker-compatible API endpoint, so the Infrastructure view works there without any extra configuration.

`camel infra` starts services through [Testcontainers](https://java.testcontainers.org/), which talks to a **Docker-compatible API socket** rather than to the `docker` or `podman` CLI. Docker provides that socket out of the box, but on Linux Podman is daemonless, so nothing is listening on it by default. If you use Podman on Linux without the Podman service running, the service fails to start with an error like this:

```text
Could not find a valid Docker environment. Please check configuration. Attempted configurations were:
        UnixSocketClientProviderStrategy: failed with exception InvalidConfigurationException (Could not find unix domain socket). Root cause NoSuchFileException (/var/run/docker.sock)
        DockerDesktopClientProviderStrategy: failed with exception NullPointerException ...
```

Testcontainers is looking for `/var/run/docker.sock`, which does not exist. Fixing it takes two steps: run the Podman API service, then tell Testcontainers where its socket is.

### 1. Run the Podman API service

Pick one of the following options:

| Option | Command | Behaviour |
|--------|---------|-----------|
| **Systemd socket** (recommended) | `systemctl --user enable --now podman.socket` | Podman starts on demand when something connects to the socket and survives restarts. Nothing has to stay open in a terminal. |
| **Manual service** | `podman system service --time=0` | The `--time=0` flag disables the inactivity timeout. The command stays in the foreground, so the **terminal hangs** while the service is in use. Keep that terminal open, or append `&` to run it in the background of the current shell. |

Either way, you can check where the socket lives with:

```bash
podman info --format '{{.Host.RemoteSocket.Path}}'
```

For a rootless setup on Linux this is usually `/run/user/<uid>/podman/podman.sock`.

### 2. Point Testcontainers to the Podman socket

Create a `~/.testcontainers.properties` file in your home directory. Use the path printed above. The file does not expand shell variables, so write the resolved path (replace `1000` with your user id, `id -u`):

```properties
docker.host=unix:///run/user/1000/podman/podman.sock
```

Prefer this file over exporting `DOCKER_HOST`: VS Code launches `camel infra` with its own environment, which may not include variables from your shell profile, whereas the properties file is always read.

After that, starting a service from the Infrastructure view (or running `camel infra run <service>` from a terminal) works as it does with Docker.

For more details, for example on Ryuk (the Testcontainers cleanup container) or SELinux, see:

- [Using Podman instead of Docker](https://golang.testcontainers.org/system_requirements/using_podman/) in the Testcontainers documentation
- [Setup Testcontainers with Podman](https://podman-desktop.io/tutorial/testcontainers-with-podman) in the Podman Desktop tutorials

---

## Next Steps

- **[Executing Integrations](../05-executing-integrations/)** — Run your Camel routes locally from VS Code
- **[Custom Kamelets](../07-custom-kamelets/)** — Build reusable Kamelet components for your workspace
