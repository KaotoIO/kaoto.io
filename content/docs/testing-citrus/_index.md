---
title: "Testing with Citrus"
description: "Write and run automated integration tests for Apache Camel routes using Citrus and Kaoto"
date: 2026-10-05
weight: 8
---

## Overview

Automated testing is a critical part of developing robust integration routes. The **Citrus Framework** provides powerful, declarative testing capabilities that integrate seamlessly with Apache Camel integrations.

This guide demonstrates how to write and run automated tests for Camel integrations using the Citrus YAML DSL and the Kaoto VS Code extension. We will test the file-monitoring route created in the **[Listen to a Folder Workshop](../../workshop/beginner-file/)**, which watches a directory for new files and automatically copies them to a backup folder.

## Prerequisites

Before starting, ensure you have:

- **VS Code** installed on your system - [Follow the installation guide](https://code.visualstudio.com/download)
- **Kaoto VS Code extension** - See the [installation guide](../installation/) for setup instructions
- **JBang** - Required for running tests with `camel-cli-run`. See the [installation guide](../installation/) for setup instructions

> [!NOTE]
> The Kaoto VS Code extension automatically installs Camel CLI for you. However, **JBang remains a hard requirement** and must be installed manually before running `camel-cli-run` tests.

## The Route Under Test

The route under test is the completed file-monitoring integration built during the **[Listen to a Folder Workshop](../../workshop/beginner-file/)**. You can refer to that workshop for detailed step-by-step instructions on designing this flow.

Save the following Camel route definition as `file-copier.camel.yaml` in your workspace folder:

{{< img-toggle src="./kaoto-file-copier-route-diagram.webp" lang="yaml" >}}
- route:
    id: route-2573
    from:
      id: from-3280
      uri: file-watch
      parameters:
        path: /tmp/tutorial/
        recursive: false
      steps:
        - filter:
            id: filter-2413
            steps:
              - to:
                  id: to-2610
                  uri: file
                  parameters:
                    directoryName: /tmp/backup/
            simple:
              expression: ${header.CamelFileEventType} == 'CREATE'
        - log:
            message: Detected ${header.CamelFileEventType} on file ${header.CamelFileName}
              at ${header.CamelFileLastModified}
{{< /img-toggle >}}

This route watches the `/tmp/tutorial/` folder for system changes. When a file is created, the route filters the `CREATE` event, copies the file to `/tmp/backup/`, and logs the event detail to the console.

> [!NOTE]
> **Windows users:** The paths `/tmp/tutorial/` and `/tmp/backup/` used throughout this guide are Unix-style. If you are on Windows, replace them with equivalent Windows paths (e.g., `C:/tmp/tutorial/` and `C:/tmp/backup/`). You must keep the paths **consistent** across all locations: the route's `path` and `directoryName` parameters above, the Groovy file-creation script, the Groovy assertion script, and the Groovy cleanup script.

## Creating the Citrus Test

The following Citrus test was created with **Citrus 5.0.0**. The Kaoto VS Code extension includes built-in tooling to visually scaffold Citrus test cases for your integrations.

### Step 1: Scaffold the Test Workspace

1. Open VS Code and click the **Kaoto** icon in your left sidebar to display the extension panels.
2. Locate the **TESTS** panel.
3. Click the **"New Citrus Test..."** button:

{{< image-sh src="kaoto-tests-panel-new-citrus-test-button.png" text="New Citrus Test button in the TESTS panel" >}}

4. Select your workspace or destination folder from the system prompt menu.
5. Provide a name for the test file (without extension), for example `file-copier`:

{{< image-sh src="kaoto-new-citrus-test-name-prompt.png" text="Provide a name for the new test file" >}}

The extension automatically creates a dedicated test workspace for you:
- **`test/file-copier.citrus.yaml`**: The main declarative test file where your test scenarios are declared.
- **`test/citrus-application.properties`**: A configuration properties file.

> [!IMPORTANT]
> **The Naming Convention:** Citrus integration tests must use the `.citrus.yaml` file suffix (e.g., `file-copier.citrus.yaml`). This suffix tells the test runner and Citrus JBang to treat the file as a Citrus integration test.

---

### Step 2: Design the Test Visually in Kaoto

When you open `test/file-copier.citrus.yaml`, Kaoto renders it inside the visual designer with a default template showing a sample test.

{{< image-sh src="kaoto-citrus-default-test-template-canvas.png" text="Sample Citrus test structure on the canvas" >}}

We will modify this test template step-by-step using the visual interface:

1. **Configure Test Metadata and Variables:** Click on the top header bar of the Citrus flow (**"Sample test in YAML"**) on your canvas to open its properties panel on the right.
   - Go to the **Variables** tab and delete the default `message` variable.
   - Go to the **Metadata** (or **All**) tab and change the **Description** field to: `Verify that creating a file in /tmp/tutorial/ correctly copies it to /tmp/backup/`
   - Save the file (`Ctrl/Cmd + S`) to apply the changes. This will also update the canvas header to match your new test name. Saving is recommended after each change.
2. **Switch the Default Action:** Hover over the default `echo` action node on the canvas and click the **Replace** (circular arrow) icon.
3. **Choose Camel Run Action:** In the component catalog, search for `run` and choose the second option, **Run (`camel-cli-run`)**:

{{< image-sh src="kaoto-add-camel-cli-run-component.png" text="Add camel-cli-run component" >}}

> [!NOTE]
> To help you organize your test scenarios, Kaoto groups Citrus components into three intuitive categories:
> - **Test Actions**: Individual steps that do the actual work during your test (such as starting your Camel route, pausing the flow, or running script assertions).
> - **Test Containers**: Logic wrappers that group actions together to control how they run (like loops, conditional execution, or retries).
> - **Test Endpoints**: Connectors that let your test talk to external systems (such as databases, HTTP servers, or message brokers like Kafka).

4. **Configure Camel Run Properties:** Click the `Run` node on the canvas to open its properties panel. Under the **All** tab, fill in the integration name and file path relative to the `test/` folder:
   - **Integration Name:** `file-copier`
   - **File:** `../file-copier.camel.yaml`

   > [!NOTE]
   > **How it works (`camel-cli-run`):** This action starts your Camel integration route under test as a background subprocess. JBang automatically resolves dependencies and keeps the route running for the duration of the test.

5. **Add Sleep Action:** Click **"Add step"** (+), search for `sleep`, and add the **Sleep** action. Click the node, and under properties, configure the pause duration:
   - **Time:** `2000` (milliseconds)

   > [!NOTE]
   > **How it works (`sleep`):** Because integration routes run asynchronously, sleep actions are used to give the Camel route time to fully initialize and bind to endpoints before assertions are performed.

6. **Add Groovy Action to Simulate File Creation:** Click **"Add step"** (+), search for `groovy`, and add the **Groovy** action. Click the node and, in the `script` properties text box, paste the code to write our test file:
   ```groovy
   new File('/tmp/tutorial/test-doc.txt').write('Hello, Citrus!')
   ```

   > [!NOTE]
   > **How it works (`groovy`):** Citrus can execute customized Groovy scripts directly inside the test context. This is highly useful for interacting with local directories (like writing an input file to trigger file-monitoring).

7. **Add a second Sleep Action:** Click **"Add step"** (+), add another **Sleep** action, and configure it for `2000` milliseconds to allow the integration route time to detect and process the file.

8. **Add Groovy Action to Assert File Copying:** Click **"Add step"** (+), add another **Groovy** action, and paste the assertion script inside the `script` text box to verify that the file was copied successfully:
   ```groovy
   def backupFile = new File('/tmp/backup/test-doc.txt')
   assert backupFile.exists() : "Backup file was not created!"
   assert backupFile.text == 'Hello, Citrus!' : "Backup file content mismatch!"
   ```

   > [!NOTE]
   > **How it works (assertions):** Here, another Groovy action acts as a validation script. It checks if the backup file was successfully created in the `/tmp/backup/` directory, and asserts that its contents match the original test string.

9. **Add Camel Verify Action:** Click **"Add step"** (+), search for `verify`, and add the **Verify (`camel-cli-verify`)** component:

{{< image-sh src="kaoto-add-camel-cli-verify-component.png" text="Add camel-cli-verify component" >}}

Select the `Verify` node and configure its properties under the form panel:
- **Integration:** `file-copier`
- **Log Message:** `Detected CREATE on file test-doc.txt`

   > [!NOTE]
   > **How it works (`camel-cli-verify`):** This action scans the standard console log of the running integration to verify that the route correctly processed the file and logged the corresponding log line.

10. **Add `doFinally` Cleanup Container:** To ensure tests are reproducible and leave a clean environment even when a previous step fails, click **"Add step"** (+), search for `doFinally`, and add the **Do Finally (`doFinally`)** container. Inside it, add a **Groovy** action and paste the cleanup code in the `script` text box:
   ```groovy
   new File('/tmp/tutorial/test-doc.txt').delete()
   new File('/tmp/backup/test-doc.txt').delete()
   ```

   > [!NOTE]
   > **How it works (`doFinally`):** Actions placed inside a `doFinally` container always execute at the end of the test, regardless of whether earlier steps passed or failed. This guarantees temporary files are cleaned up even if the test encounters an error.

---

### Step 3: Review Your Test Source

By clicking the code icon (`</>`) on the top right of the visual editor, you can view the underlying Citrus YAML DSL. Your completed `test/file-copier.citrus.yaml` file should look exactly like this:

{{< img-toggle src="./kaoto-completed-citrus-test-yaml.png" lang="yaml" >}}
name: file-copier.citrus
author: Citrus
status: FINAL
description: Verify that creating a file in /tmp/tutorial/ correctly copies it
  to /tmp/backup/
variables: []
actions:
  - camel:
      cli:
        run:
          integration:
            file: ../file-copier.camel.yaml
            name: file-copier
  - sleep:
      milliseconds: "2000"
  - groovy:
      script:
        script: new File('/tmp/tutorial/test-doc.txt').write('Hello, Citrus!')
  - sleep:
      milliseconds: "2000"
  - groovy:
      script:
        script: >-
          def backupFile = new File('/tmp/backup/test-doc.txt')

          assert backupFile.exists() : "Backup file was not created!"

          assert backupFile.text == 'Hello, Citrus!' : "Backup file content
          mismatch!"
  - camel:
      cli:
        verify:
          integration: file-copier
          logMessage: Detected CREATE on file test-doc.txt
  - doFinally:
      actions:
        - groovy:
            script:
              script: |-
                new File('/tmp/tutorial/test-doc.txt').delete()
                new File('/tmp/backup/test-doc.txt').delete()
{{< /img-toggle >}}

---

## Running the Test

Once your test file is ready, run it directly from Kaoto using the **play button** in the **TESTS** panel. Locate `file-copier.citrus.yaml` in the panel and click the **Run** (▶) icon next to it:

{{< image-sh src="kaoto-citrus-test-play-button.png" text="Run Citrus test using the Kaoto play button in the TESTS panel" >}}

Kaoto launches the test using **Citrus 5.0.0** in the background. The integrated output panel streams the test execution logs in real time.

## Expected Output

When the test finishes, the output panel displays the full Citrus test results. A successful run looks like this:

{{< image-sh src="kaoto-citrus-test-run-results.png" text="Citrus test run results showing a passing test" >}}

## Additional resources

For complete Citrus documentation, visit [citrusframework.org](https://citrusframework.org/).
