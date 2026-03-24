---
title: "Installation"
description: "Complete guide on how to install and run Kaoto, the visual designer for Apache Camel integrations"
date: 2026-03-24
weight: 1
---

## Overview

Kaoto is a visual designer for Apache Camel that helps you create, edit, and deploy integration flows with ease. This guide covers multiple installation options to get you started quickly.

## Installation Options

Choose the installation method that best fits your needs:

- **[VS Code Extension](#using-vs-code)** - Recommended for local development and testing
- **[Online Testing Instance](#using-our-online-testing-instance)** - Try Kaoto without installing anything
- **[Podman](#using-podman)** - Run Kaoto in a containerized environment

---

## Using our Online Testing Instance

The fastest way to try Kaoto is through our [openly available testing instance](https://red.ht/kaoto).

**Perfect for:**
- Quick evaluation and testing
- Following our [workshops](/workshop) as guides
- Learning Kaoto basics without local setup

**Next steps:**
- Learn more about how to use Kaoto in the [Quickstart](/docs/quickstart)
- Explore our [workshops](/workshop) for hands-on tutorials

---

## Using VS Code

The VS Code extension provides the most complete Kaoto experience with local development capabilities.

### Requirements

Before installing the Kaoto extension, ensure you have:

#### Required Software

- **[Visual Studio Code](https://code.visualstudio.com/)** - The code editor
- **[JBang](https://www.jbang.dev/download/)** - Required for running Camel integrations locally
  - **macOS/Linux:**
    ```bash
    curl -Ls https://sh.jbang.dev | bash -s - trust add https://github.com/apache/camel
    ```
  - **Windows:** [Installation instructions](https://www.jbang.dev/download/)
  - **Verify installation:**
    ```bash
    jbang version
    ```

> [!NOTE]
> **JBang is the only hard requirement.** The Kaoto extension will automatically install Camel CLI, and other required dependencies as needed during extension installation and first use.

### Install the Kaoto VS Code Extension

> [!NOTE]
> The Kaoto extension provides all the required functionality to create and run your integrations locally as a standalone extension.

**Installation Steps:**

1. Open **Visual Studio Code**
2. Open the **Extensions** view on the left side panel (or press `Ctrl+Shift+X` / `Cmd+Shift+X`)
3. Type `Kaoto` in the search field
4. Click the **Install** button on the **Kaoto** extension

{{< figure src="kaoto-install.png" alt="Install Kaoto Extension" caption="Install Kaoto Extension in VS Code" class="image" >}}

**What you get:**
- Visual designer for Apache Camel routes
- Integrated catalog of Camel components and patterns
- Local route execution with Camel JBang
- YAML and XML DSL support
- Real-time validation and error checking

---

## Using Podman

Run Kaoto in a containerized environment using Podman.

### Requirements

- **[Podman](https://podman.io/docs/installation)** installed and running

### Installation Steps

1. **Pull the Kaoto image:**
   ```bash
   podman pull quay.io/kaotoio/kaoto-app:main
   ```

2. **Run the container:**
   ```bash
   podman run -p 8080:8080 quay.io/kaotoio/kaoto-app:main
   ```

3. **Access Kaoto:**
   - Open your browser and navigate to [http://localhost:8080](http://localhost:8080)
   - If you used a different port in the `-p` parameter, adjust the URL accordingly

---

## Verifying Your Installation

After installation, verify that Kaoto is working correctly:

### For VS Code Extension

1. Open VS Code
2. Click the Kaoto icon in the left sidebar
3. Create a new Camel route file
4. You should see the visual designer interface

### For Podman

1. Access [http://localhost:8080](http://localhost:8080)
2. You should see the Kaoto web interface
3. Try creating a simple route to test functionality

### For Online Instance

1. Visit [https://red.ht/kaoto](https://red.ht/kaoto)
2. The Kaoto interface should load in your browser
3. Try exploring the catalog and creating a test route

---

## Troubleshooting

### Common Issues

**VS Code Extension not appearing:**
- Ensure VS Code is up to date
- Restart VS Code after installation
- Check the Extensions view to confirm installation

**JBang not found:**
- Verify JBang is installed: `jbang version`
- Ensure your PATH includes JBang binaries

**Podman container won't start:**
- Verify Podman is running: `podman ps`
- Check if port 8080 is already in use
- Review Podman logs: `podman logs kaoto-app`

**Java version issues:**
- Verify Java 17 or later is installed: `java -version`
- Set JAVA_HOME environment variable if needed

### Getting Help

If you encounter issues:

1. Check the [Kaoto documentation](https://kaoto.io/docs/)
2. Visit the [GitHub Issues page](https://github.com/KaotoIO/kaoto/issues)
3. Join the [Zulip Chat](https://camel.zulipchat.com/#narrow/stream/441302-kaoto)
4. Ask in the [Discussion Forums](https://github.com/orgs/KaotoIO/discussions)

---

## Next Steps

Now that you have Kaoto installed, here's what to do next:

1. **[Quickstart Guide](/docs/quickstart)** - Create your first integration in minutes
2. **[Workshops](/workshop)** - Follow hands-on tutorials
3. **[Documentation](/docs/)** - Explore all available documentation sections

---

## Additional Resources

### Kaoto Resources
- **[VS Code Kaoto Extension on Marketplace](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto)** - Download and reviews
- **[Kaoto GitHub](https://github.com/KaotoIO/kaoto)** - Main project source code
- **[VS Code Kaoto GitHub Repository](https://github.com/KaotoIO/vscode-kaoto)** - Extension source code
- **[Kaoto Examples](https://github.com/KaotoIO/kaoto-examples)** - Sample integrations and use cases

### Apache Camel Resources
- **[Apache Camel Documentation](https://camel.apache.org/docs/)** - Learn about Apache Camel
- **[Camel JBang Documentation](https://camel.apache.org/manual/camel-jbang.html)** - JBang integration guide

### Community
- **[Community Resources](/contribute)** - Get involved with the Kaoto community
- **[Zulip Chat](https://camel.zulipchat.com/#narrow/stream/441302-kaoto)** - Real-time chat support
- **[Discussion Forums](https://github.com/orgs/KaotoIO/discussions)** - Community discussions