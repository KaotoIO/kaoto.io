---
title: "Listen to a Folder"
date: 2026-03-09T10:00:00+06:00
categories: ["beginner"]
summary: "Learn to build a file monitoring integration using Kaoto's visual designer and Apache Camel. Monitor directories, filter events, and back up files automatically."
authors:
  - pvinaches
---
## Introduction

In this hands-on workshop, you will build a file monitoring integration using **Kaoto's visual designer** and **Apache Camel**. You'll learn how to watch a directory for file system changes, filter events based on conditions, and automatically back up files when they are created.

**What You'll Learn:**
- File system monitoring with the `file-watch` component
- Extracting metadata from Camel message headers
- Filtering events using the Message Filter pattern
- Copying files to backup locations
- Testing and debugging Camel routes locally
- Using Apache Camel's Simple Expression Language

**What You'll Build:**
A Camel route that monitors a directory for file changes, filters CREATE events, backs up newly created files to a separate directory, and logs all file system events to the console.

## Prerequisites

Before starting this workshop, ensure you have the following installed and configured on your system:

### Required Software

- **Visual Studio Code** - Download from [code.visualstudio.com](https://code.visualstudio.com/)
- **Kaoto Extension for VSCode** - Install from the [VSCode Marketplace](https://kaoto.io/docs/installation/)
- **Java Development Kit (JDK) 17 or later** - Required for running Apache Camel
  - Download from [Adoptium](https://adoptium.net/) or your preferred JDK distribution
- **Apache Camel JBang** - For easy infrastructure setup
  - **Installation:** Visit [jbang.dev](https://www.jbang.dev/download/) for platform-specific instructions
  - **macOS/Linux:** `curl -Ls https://sh.jbang.dev | bash -s - trust add https://github.com/apache/camel`
  - **Windows:** Follow the installation instructions at [jbang.dev](https://www.jbang.dev/download/) (includes installers for Chocolatey, Scoop, or manual installation)
  - **After installation:** `jbang app install camel@apache/camel`

> [!NOTE]
> **JBang is the only hard requirement.** The Kaoto extension will automatically install Trusts, Camel CLI, and Camel plugins as needed during extension installation.

### Required Knowledge

This workshop assumes you have:

- **Basic understanding of integration concepts** - Familiarity with data processing
- **Basic command-line skills** - Ability to navigate directories and run commands
- **Familiarity with VSCode** - Basic navigation and file management

### What You'll Set Up During the Workshop

The following will be configured as part of the workshop steps:

- Test directories for file monitoring
- Backup directory for file copies
- Camel integration route

> [!TIP]
> If you're new to Kaoto or Apache Camel, this beginner workshop is the perfect starting point. It introduces core concepts progressively.

## Project Setup

1. Install the [Kaoto extension for VSCode](https://kaoto.io/docs/installation/).
2. Create a new directory for the workshop:

```bash
$ mkdir file-monitor-workshop
$ cd file-monitor-workshop
```

> [!NOTE]
> **Windows users:** This workshop was created in a Unix-based environment. While the commands shown should work in PowerShell, Command Prompt, and Git Bash, you may need to make adjustments accordingly. For example, if using Command Prompt, use `md` instead of `mkdir`, and adjust file paths to use Windows-style paths (e.g., `C:\tmp\tutorial\` instead of `/tmp/tutorial/`).

## Description

This workshop guides you through building a file monitoring integration using **Apache Camel** and **Kaoto**. You will create a route that demonstrates the **File Integration Pattern** and **Message Filter Pattern**, two fundamental Enterprise Integration Patterns (EIPs).

**The Route Flow:**

```
File System Events → File Watch → Filter (CREATE only) → Copy to Backup
                                                       ↓
                                                    Log All Events
```

The route continuously monitors a directory, processes each file system event, filters for CREATE events to trigger backups, and logs all events for visibility.

## Part 1: Log Changes

### Goal

Create a route that watches a folder and logs file system events (CREATE, MODIFY, DELETE) with detailed information about each change.

### Step-by-Step Instructions

#### Step 1: Create a New Route

1. Open VSCode and navigate to your `file-monitor-workshop` directory
2. Click the **Kaoto** icon in the left sidebar
3. Click the **Camel File...** button to create a new integration

{{< image-sh src="kaoto-ext-start.webp" text="Creating a new route in Kaoto" >}}

4. If the **Camel File...** button is not showing, click on the second icon next to **Integrations** (a file with a + sign).
5. In the dialog that appears:
   - Select **Camel Route** as the file type
   - Select **YAML** as the Camel DSL
   - Choose your workshop folder as the saving location
   - Name the file `file-monitor`

A new route will appear in the Kaoto visual designer with a default timer component, a SetBody step and Log processor.

{{< image-sh src="new-route.webp" text="New route created" >}}

6. Select **Camel Main 4.16.0** from the options that appear when clicking the Camel version selector. This tutorial was created using this version and other versions have not been tested in this context. If chosen other Camel versions, they may present slight variations in component availability and presentation.

{{< image-sh src="top-panel.webp" text="Camel version selector" >}}

#### Step 2: Configure the File Watcher

The first component needs to monitor the test directory for file changes.

1. **Hover** over the timer component in the visual designer
2. Click the **Replace** icon (circular arrow) that appears

{{< image-sh src="replace-timer.webp" text="Replace timer component" >}}

3. In the search box, type `file-watch` and select the **File Watch** component

{{< image-sh src="search-file-watch.webp" text="Search for file-watch component" >}}

4. Click on the File Watch component to open its properties panel on the right
5. Navigate to the **All** tab at the top of the properties panel
6. Configure the following properties:

   | Property | Value | What it does |
   |----------|-------|--------------|
   | **path** | `/tmp/tutorial/` | Directory to monitor for changes |
   | **recursive** | `false` | Don't watch subdirectories |
   | **auto create** | `true` | Creates the directory automatically. True by default |

{{< image-sh src="file-watch-form.webp" text="File watch configuration form" >}}

7. **Save** the file using `Ctrl/Cmd + S` or by clicking **File** → **Save** in the VS Code menu bar

> [!IMPORTANT]
> Use the `file-watch` component, not the `file` component. The `file-watch` component monitors for file system events, while `file` is for reading file contents.

#### Step 3: Add Log Processor

Now we'll add a log step to output information about detected changes.

1. **Hover** over the second component (SetBody) in the route
2. Click the **Delete** icon
3. Click on the Log processor to open its properties
4. Configure the message property in **Required** tab:

   | Property | Value |
   |----------|-------|
   | **message** | `Detected ${header.CamelFileEventType} on file ${header.CamelFileName} at ${header.CamelFileLastModified}` |

5. **Save** the changes

> **💡 Understanding Camel Headers:** The `file-watch` component populates message headers with metadata about file events:
> - `CamelFileEventType`: Type of event (CREATE, MODIFY, DELETE)
> - `CamelFileName`: Name of the affected file
> - `CamelFileLastModified`: Timestamp of last modification

#### Step 4: Review Your Route

You can find the source code by clicking in the </> icon on the top right of the visual designer.

{{< image-sh src="source-code-icon.webp" text="Source code icon" >}}

Your completed route should look like this in the visual designer. The YAML source should be similar to:

{{< img-toggle src="./partial-route.webp" lang="yaml" >}}
- route:
    id: route-2573
    from:
      id: from-3280
      uri: file-watch
      parameters:
        path: /tmp/tutorial/
        recursive: false
      steps:
        - log:
            message: Detected ${header.CamelFileEventType} on file ${header.CamelFileName}
              at ${header.CamelFileLastModified}
{{< /img-toggle >}}

> [!TIP]
> If your YAML doesn't match exactly, you can copy and paste this code into the source editor. Kaoto will automatically update the visual designer.

#### Step 5: Test Your Route

Before continuing, you can test this basic route to see it in action:

1. In the Kaoto extension panel, click the **Play** button (▶️) next to your folder or Integrations
2. A new terminal will open showing Camel JBang starting the route
3. In a new terminal window, create a test file:

```bash
$ echo "test content" > /tmp/tutorial/test.txt
```

4. Watch the Camel terminal for log output showing the CREATE event

```bash
INFO 40740 --- [elFileWatchPoll] file-monitor.camel.yaml:10               : Detected CREATE on file test.txt at 1774260948651
```

5. Press `Ctrl + C` in the Camel terminal to stop the route when done

> **💡 Testing incrementally:** It's good practice to test your route after each major addition. This helps catch issues early and builds understanding step-by-step.

**✅ Checkpoint:** You've completed Part 1! The route will now monitor the folder and log all file system events.

---

## Part 2: Add a Filter

### Goal

Enhance the route to filter events and only back up files when they are created (not modified or deleted). This introduces the **Message Filter Pattern**.

### Step-by-Step Instructions

#### Step 1: Add Filter Processor

We'll insert a filter between the file-watch and log components.

1. **Hover** over the arrow between file-watch and log

{{< image-sh src="hover-arrow.webp" text="Hover over arrow to add component" >}}

2. Click the **+** icon that appears on the arrow
3. Search for `filter` and select the **Filter** processor
4. Click on the Filter component to open its properties
5. Configure the filter expression in **Required** tab:

   | Property | Value | What it does |
   |----------|-------|--------------|
   | **Expression language** | **Simple** | The expression language to use |
   | **Expression** | `${header.CamelFileEventType} == 'CREATE'` | Condition to evaluate |

{{< image-sh src="filter-form.webp" text="Filter configuration form" >}}

6. **Save** the changes

> **💡 Understanding the Filter:** The filter creates a conditional branch. Steps inside the filter only execute when the condition is true. In this case, only CREATE events will pass through.

#### Step 2: Add File Component Inside Filter

Now we'll add a file component inside the filter to copy created files.

1. Click **inside the filter placeholder** (the dotted box area)

{{< image-sh src="filter-placeholder.webp" text="Filter placeholder for adding components" >}}

2. This will add a new component inside the filter branch
3. Search for `file` and select the **File** component
4. Click on the File component to open its properties
5. Configure in **Required** tab:

   | Property | Value | What it does |
   |----------|-------|--------------|
   | **directoryName** | `/tmp/backup/` | Destination folder for file copies |
   | **auto create** | `true` | Creates the directory automatically. True by default |

6. **Save** the changes

> [!IMPORTANT]
> The file component must be placed **inside** the filter. Use the "Insert into" context menu or click inside the filter placeholder to ensure proper nesting.

#### Step 3: Review Your Route

Your completed route should look like this in the visual designer. The YAML source should be similar to:

{{< img-toggle src="./partial-route2.webp" lang="yaml" >}}
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

**✅ Checkpoint:** You've completed Part 2! The route now backs up files only when they are created, while still logging all events.

---

## Part 3: Testing Your Route

### Goal

Launch the route locally and verify it works correctly by creating, modifying, and deleting test files.

### Step-by-Step Instructions

#### Step 1: Launch the Route

1. In the VSCode file explorer, locate your `file-monitor-workshop` folder
2. In the Kaoto extension panel, find the folder containing your YAML route file
3. Click the **Play** button (▶️) next to Integrations or next to the folder name

{{< image-sh src="play-route.webp" text="Play button location" >}}
{{< image-sh src="play-route2.webp" text="Play button location alternative view" >}}

4. A new terminal will open in VSCode
5. Watch the terminal output as Camel JBang starts the route

You should see output similar to:

```
INFO  [route-2573] Apache Camel 4.16.0 (file-monitor) started in ...
```

> **💡 What's happening:** The Kaoto extension uses Camel JBang to run your route locally, making it easy to test without complex setup.

#### Step 2: Test the Integration

With the route running, test it by creating files in the monitored directory:

1. Open a new terminal window
2. Create a test file:

```bash
$ echo "test content" > /tmp/tutorial/test1.txt
```

3. Watch the Camel terminal for log output showing the CREATE event

```bash
INFO 43481 --- [elFileWatchPoll] file-monitor.camel.yaml:10               : Detected CREATE on file test1.txt at 1774260948651
```

4. Verify the file was copied to `/tmp/backup/`
5. Try modifying the file:

```bash
$ echo "modified" >> /tmp/tutorial/test1.txt
```

6. Watch for the MODIFY event in the logs (file won't be copied again)

```bash
INFO 43481 --- [elFileWatchPoll] file-monitor.camel.yaml:20               : Detected MODIFY on file test1.txt at 1774261092994
```

7. Try deleting the file:

```bash
$ rm /tmp/tutorial/test1.txt
```

8. Watch for the DELETE event in the logs

```bash
INFO 43481 --- [elFileWatchPoll] file-monitor.camel.yaml:20               : Detected DELETE on file test1.txt at 1774261151985
```

#### Step 3: Stop the Route

To stop the running integration:

1. Go to the terminal where Camel is running
2. Press `Ctrl + C`

**✅ Checkpoint:** You've completed the workshop! You now understand file monitoring, filtering, and local testing with Kaoto.

## Key Concepts Covered

### Apache Camel Components

**Components** are the building blocks of Camel routes. They represent endpoints that can send or receive messages.

| Component | Purpose | Used In |
|-----------|---------|---------|
| **file-watch** | Monitors directories for file events | Part 1 |
| **file** | Reads from or writes to files | Part 2 |

### Apache Camel Processors

**Processors** transform or manipulate messages as they flow through a route.

| Processor | Purpose | Used In |
|-----------|---------|---------|
| **log** | Outputs messages to console | Part 1 |
| **filter** | Conditionally executes steps | Part 2 |

### Simple Expression Language

Camel's **Simple Expression Language** is used for accessing message data and performing operations.

| Expression | What it accesses | Example |
|------------|------------------|---------|
| `${header.name}` | Message header | `${header.CamelFileEventType}` |
| `${header.CamelFileEventType}` | File event type | CREATE, MODIFY, DELETE |
| `${header.CamelFileName}` | File name | test1.txt |
| `${header.CamelFileLastModified}` | Last modified timestamp | 2024-01-24T12:30:00 |

### Enterprise Integration Patterns

This workshop demonstrates the **Message Filter Pattern**:

**Message Filter** - Selectively processes messages based on criteria. In this workshop, we filter file events to process only CREATE events for backup purposes.

## Best Practices

### Route Design

1. **Start simple**: Begin with basic routes, add complexity gradually
2. **Use meaningful names**: Name components and routes clearly
3. **Add descriptions**: Use the description property to document components
4. **Test incrementally**: Test after each major change

### Component Selection

1. **Choose the right component**: Understand component vs. processor differences
2. **Read documentation**: Reference Apache Camel docs for details
3. **Configure properly**: Fill all required parameters
4. **Use appropriate expressions**: Match expression language to use case

### Testing Strategy

1. **Verify prerequisites**: Check installations before testing
2. **Create test data**: Prepare files and directories
3. **Monitor output**: Watch terminal for errors and results
4. **Iterate quickly**: Make small changes and retest

### Troubleshooting

1. **Check prerequisites**: Verify Extension Pack and JBang installed
2. **Verify paths**: Ensure directories exist and are accessible
3. **Review configuration**: Double-check parameter values
4. **Read error messages**: Camel provides detailed error information

## Additional Resources

### Documentation

- [Kaoto Documentation](https://kaoto.io/docs/) - Kaoto user guide and tutorials
- [Apache Camel Documentation](https://camel.apache.org/docs/) - Complete Camel reference
- [Apache Camel YAML DSL](https://camel.apache.org/components/4.14.x/others/yaml-dsl.html) - YAML DSL reference
- [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/) - EIP reference

### Community

- [Kaoto GitHub](https://github.com/KaotoIO/kaoto) - Report issues and contribute
- [Apache Camel Community](https://camel.apache.org/community/) - Get help and connect with other users