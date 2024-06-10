---
title: "Create a Kamelet"
date: 2024-01-24T11:00:00+06:00
categories: ["intermediate"]
summary: "Learn how to create a Kamelet using Kaoto. We are going to create something similar to the Chuck Norris source, but generating cat facts"
---
## 1 - Create the Flow

The goals for this exercise are:

 - Create a Kamelet
 - Start the flow with a `timer`
 - Add another step that calls the cat facts service: `https://cat-fact.herokuapp.com/facts/random`
 - Add a `setBody` that extracts the `text` attribute of the response
 - End the flow with a `kamelet:sink`

### Hints

 - The `timer` component needs two configuration properties: `Timer name` and `Period`.
 - We want our Kamelet to be configurable to set the `period` in a configuration parameter. 
 - To call an external service, use the `https` component
 - To extract the attribute of the response, use a `setBody` with simple language and the expression `$.text`
 - The `kamelet:sink` is an end step.
 
### Solution

The following video showcases the solution.

{{< video src="1-create-kamelet.webm" controls="yes" >}}

At this point, the source editor should show the following code:

```yaml
apiVersion: camel.apache.org/v1
kind: Kamelet
metadata:
  annotations:
    camel.apache.org/catalog.version: main-SNAPSHOT
    camel.apache.org/kamelet.group: Users
    camel.apache.org/kamelet.icon: data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTkuMC4wLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgNjAgNjAiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDYwIDYwOyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+CjxwYXRoIGQ9Ik00OC4wMTQsNDIuODg5bC05LjU1My00Ljc3NkMzNy41NiwzNy42NjIsMzcsMzYuNzU2LDM3LDM1Ljc0OHYtMy4zODFjMC4yMjktMC4yOCwwLjQ3LTAuNTk5LDAuNzE5LTAuOTUxCgljMS4yMzktMS43NSwyLjIzMi0zLjY5OCwyLjk1NC01Ljc5OUM0Mi4wODQsMjQuOTcsNDMsMjMuNTc1LDQzLDIydi00YzAtMC45NjMtMC4zNi0xLjg5Ni0xLTIuNjI1di01LjMxOQoJYzAuMDU2LTAuNTUsMC4yNzYtMy44MjQtMi4wOTItNi41MjVDMzcuODU0LDEuMTg4LDM0LjUyMSwwLDMwLDBzLTcuODU0LDEuMTg4LTkuOTA4LDMuNTNDMTcuNzI0LDYuMjMxLDE3Ljk0NCw5LjUwNiwxOCwxMC4wNTYKCXY1LjMxOWMtMC42NCwwLjcyOS0xLDEuNjYyLTEsMi42MjV2NGMwLDEuMjE3LDAuNTUzLDIuMzUyLDEuNDk3LDMuMTA5YzAuOTE2LDMuNjI3LDIuODMzLDYuMzYsMy41MDMsNy4yMzd2My4zMDkKCWMwLDAuOTY4LTAuNTI4LDEuODU2LTEuMzc3LDIuMzJsLTguOTIxLDQuODY2QzguODAxLDQ0LjQyNCw3LDQ3LjQ1OCw3LDUwLjc2MlY1NGMwLDQuNzQ2LDE1LjA0NSw2LDIzLDZzMjMtMS4yNTQsMjMtNnYtMy4wNDMKCUM1Myw0Ny41MTksNTEuMDg5LDQ0LjQyNyw0OC4wMTQsNDIuODg5eiIvPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8L3N2Zz4K
    camel.apache.org/kamelet.support.level: Stable
    camel.apache.org/provider: Apache Software Foundation
  labels:
    camel.apache.org/kamelet.type: source
  name: kamelet-3113
spec:
  definition:
    description: Produces periodic events about random users!
    properties:
      period:
        default: 5000
        description: The time interval between two events
        title: Period
        type: integer
    title: kamelet-3113
    type: object
  dependencies:
    - camel:timer
    - camel:http
    - camel:kamelet
  template:
    from:
      steps:
        - to:
            parameters:
              httpUri: https://cat-fact.herokuapp.com/facts/random
            uri: https
        - setBody:
            expression:
              simple:
                expression: $.text
            id: setBody-1978
        - to: kamelet:sink
      id: from-7053
      parameters:
        period: "{{period}}"
        timerName: user
      uri: timer
  types:
    out:
      mediaType: application/json
```

If it doesn't look like that but you still want to go to the following exercise, you can copy and paste that code to your source editor and save the changes. This will update the design editor as well.

---

## 2 - Configure title and description

The goals for this exercise are:

 - Give a proper description to the kamelet, like `Gets periodically Cat facts.` using the source code editor.
 - Give a proper `title` to the kamelet, like `Cat Source` using the source code editor.
 
### Hints

 - All these properties can be found on the `spec/definition` section of the yaml source code.
 - At the time of creating this workshop it wasn't possible to edit the `description` in the `Metadata` tab of the editor. We will however have that ability soon.
  
### Solution

The following video showcases the solution.

{{< video src="2-configure-metadata.webm" controls="yes" >}}

At this point, the source editor should show the following code:

```yaml
apiVersion: camel.apache.org/v1
kind: Kamelet
metadata:
  annotations:
    camel.apache.org/catalog.version: main-SNAPSHOT
    camel.apache.org/kamelet.group: Users
    camel.apache.org/kamelet.icon: data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTkuMC4wLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgNjAgNjAiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDYwIDYwOyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+CjxwYXRoIGQ9Ik00OC4wMTQsNDIuODg5bC05LjU1My00Ljc3NkMzNy41NiwzNy42NjIsMzcsMzYuNzU2LDM3LDM1Ljc0OHYtMy4zODFjMC4yMjktMC4yOCwwLjQ3LTAuNTk5LDAuNzE5LTAuOTUxCgljMS4yMzktMS43NSwyLjIzMi0zLjY5OCwyLjk1NC01Ljc5OUM0Mi4wODQsMjQuOTcsNDMsMjMuNTc1LDQzLDIydi00YzAtMC45NjMtMC4zNi0xLjg5Ni0xLTIuNjI1di01LjMxOQoJYzAuMDU2LTAuNTUsMC4yNzYtMy44MjQtMi4wOTItNi41MjVDMzcuODU0LDEuMTg4LDM0LjUyMSwwLDMwLDBzLTcuODU0LDEuMTg4LTkuOTA4LDMuNTNDMTcuNzI0LDYuMjMxLDE3Ljk0NCw5LjUwNiwxOCwxMC4wNTYKCXY1LjMxOWMtMC42NCwwLjcyOS0xLDEuNjYyLTEsMi42MjV2NGMwLDEuMjE3LDAuNTUzLDIuMzUyLDEuNDk3LDMuMTA5YzAuOTE2LDMuNjI3LDIuODMzLDYuMzYsMy41MDMsNy4yMzd2My4zMDkKCWMwLDAuOTY4LTAuNTI4LDEuODU2LTEuMzc3LDIuMzJsLTguOTIxLDQuODY2QzguODAxLDQ0LjQyNCw3LDQ3LjQ1OCw3LDUwLjc2MlY1NGMwLDQuNzQ2LDE1LjA0NSw2LDIzLDZzMjMtMS4yNTQsMjMtNnYtMy4wNDMKCUM1Myw0Ny41MTksNTEuMDg5LDQ0LjQyNyw0OC4wMTQsNDIuODg5eiIvPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8L3N2Zz4K
    camel.apache.org/kamelet.support.level: Stable
    camel.apache.org/provider: Apache Software Foundation
  labels:
    camel.apache.org/kamelet.type: source
  name: kamelet-3113
spec:
  definition:
    description: Gets periodically Cat facts
    properties:
      period:
        default: 5000
        description: The time interval between two events
        title: Period
        type: integer
    title: Cat Source
    type: object
  dependencies:
    - camel:timer
    - camel:http
    - camel:kamelet
  template:
    from:
      steps:
        - to:
            parameters:
              httpUri: https://cat-fact.herokuapp.com/facts/random
            uri: https
        - setBody:
            expression:
              simple:
                expression: $.text
            id: setBody-1978
        - to: kamelet:sink
      id: from-7053
      parameters:
        period: "{{period}}"
        timerName: user
      uri: timer
  types:
    out:
      mediaType: application/json
```

If it doesn't look like that but you still want to go to the following exercise, you can copy and paste that code to your source editor and save the changes. This will update the design editor as well.

---

## 3 - Add Unmarshal

The goals for this exercise are:

 - Add an `unmarshal` step before the `setBody` step
 - The data format type of `unmarshal` will be `json` and use the `Gson` library
 
### Solution

The following video showcases the solution.

{{< video src="3-configure-unmarshal.webm" controls="yes" >}}

At this point, the source editor should show the following code:

```yaml
apiVersion: camel.apache.org/v1
kind: Kamelet
metadata:
  annotations:
    camel.apache.org/catalog.version: main-SNAPSHOT
    camel.apache.org/kamelet.group: Users
    camel.apache.org/kamelet.icon: data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTkuMC4wLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgNjAgNjAiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDYwIDYwOyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+CjxwYXRoIGQ9Ik00OC4wMTQsNDIuODg5bC05LjU1My00Ljc3NkMzNy41NiwzNy42NjIsMzcsMzYuNzU2LDM3LDM1Ljc0OHYtMy4zODFjMC4yMjktMC4yOCwwLjQ3LTAuNTk5LDAuNzE5LTAuOTUxCgljMS4yMzktMS43NSwyLjIzMi0zLjY5OCwyLjk1NC01Ljc5OUM0Mi4wODQsMjQuOTcsNDMsMjMuNTc1LDQzLDIydi00YzAtMC45NjMtMC4zNi0xLjg5Ni0xLTIuNjI1di01LjMxOQoJYzAuMDU2LTAuNTUsMC4yNzYtMy44MjQtMi4wOTItNi41MjVDMzcuODU0LDEuMTg4LDM0LjUyMSwwLDMwLDBzLTcuODU0LDEuMTg4LTkuOTA4LDMuNTNDMTcuNzI0LDYuMjMxLDE3Ljk0NCw5LjUwNiwxOCwxMC4wNTYKCXY1LjMxOWMtMC42NCwwLjcyOS0xLDEuNjYyLTEsMi42MjV2NGMwLDEuMjE3LDAuNTUzLDIuMzUyLDEuNDk3LDMuMTA5YzAuOTE2LDMuNjI3LDIuODMzLDYuMzYsMy41MDMsNy4yMzd2My4zMDkKCWMwLDAuOTY4LTAuNTI4LDEuODU2LTEuMzc3LDIuMzJsLTguOTIxLDQuODY2QzguODAxLDQ0LjQyNCw3LDQ3LjQ1OCw3LDUwLjc2MlY1NGMwLDQuNzQ2LDE1LjA0NSw2LDIzLDZzMjMtMS4yNTQsMjMtNnYtMy4wNDMKCUM1Myw0Ny41MTksNTEuMDg5LDQ0LjQyNyw0OC4wMTQsNDIuODg5eiIvPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8L3N2Zz4K
    camel.apache.org/kamelet.support.level: Stable
    camel.apache.org/provider: Apache Software Foundation
  labels:
    camel.apache.org/kamelet.type: source
  name: kamelet-3113
spec:
  definition:
    description: Gets periodically Cat facts
    properties:
      period:
        default: 5000
        description: The time interval between two events
        title: Period
        type: integer
    title: Cat Source
    type: object
  dependencies:
    - camel:timer
    - camel:http
    - camel:kamelet
  template:
    from:
      steps:
        - to:
            parameters:
              httpUri: https://cat-fact.herokuapp.com/facts/random
            uri: https
        - unmarshal:
            id: unmarshal-1253
            json:
              library: Gson
        - setBody:
            expression:
              simple:
                expression: $.text
            id: setBody-1978
        - to: kamelet:sink
      id: from-7053
      parameters:
        period: "{{period}}"
        timerName: user
      uri: timer
  types:
    out:
      mediaType: application/json
```

If it doesn't look like that but you still want to go to the following exercise, you can copy and paste that code to your source editor and save the changes. This will update the design editor as well.

---

## 4 - Check the dependencies

We are aiming let Kaoto automatically detect dependencies needed for the Kamelet to work properly. However at this time we still have to add a dependency ourselves. Open the source code editor and look for the `dependencies` section. 

Goal for this exercise:
 
  - Add the `camel:gson` dependency required by our `unmarshal` step

After this exercise, your new kamelet will be ready to be deployed.
 
### Solution

The following video showcases the solution.

{{< video src="4-add-dependency.webm" controls="yes" >}}

At this point, the source editor should show the following code:

```yaml
apiVersion: camel.apache.org/v1
kind: Kamelet
metadata:
  annotations:
    camel.apache.org/catalog.version: main-SNAPSHOT
    camel.apache.org/kamelet.group: Users
    camel.apache.org/kamelet.icon: data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTkuMC4wLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgNjAgNjAiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDYwIDYwOyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+CjxwYXRoIGQ9Ik00OC4wMTQsNDIuODg5bC05LjU1My00Ljc3NkMzNy41NiwzNy42NjIsMzcsMzYuNzU2LDM3LDM1Ljc0OHYtMy4zODFjMC4yMjktMC4yOCwwLjQ3LTAuNTk5LDAuNzE5LTAuOTUxCgljMS4yMzktMS43NSwyLjIzMi0zLjY5OCwyLjk1NC01Ljc5OUM0Mi4wODQsMjQuOTcsNDMsMjMuNTc1LDQzLDIydi00YzAtMC45NjMtMC4zNi0xLjg5Ni0xLTIuNjI1di01LjMxOQoJYzAuMDU2LTAuNTUsMC4yNzYtMy44MjQtMi4wOTItNi41MjVDMzcuODU0LDEuMTg4LDM0LjUyMSwwLDMwLDBzLTcuODU0LDEuMTg4LTkuOTA4LDMuNTNDMTcuNzI0LDYuMjMxLDE3Ljk0NCw5LjUwNiwxOCwxMC4wNTYKCXY1LjMxOWMtMC42NCwwLjcyOS0xLDEuNjYyLTEsMi42MjV2NGMwLDEuMjE3LDAuNTUzLDIuMzUyLDEuNDk3LDMuMTA5YzAuOTE2LDMuNjI3LDIuODMzLDYuMzYsMy41MDMsNy4yMzd2My4zMDkKCWMwLDAuOTY4LTAuNTI4LDEuODU2LTEuMzc3LDIuMzJsLTguOTIxLDQuODY2QzguODAxLDQ0LjQyNCw3LDQ3LjQ1OCw3LDUwLjc2MlY1NGMwLDQuNzQ2LDE1LjA0NSw2LDIzLDZzMjMtMS4yNTQsMjMtNnYtMy4wNDMKCUM1Myw0Ny41MTksNTEuMDg5LDQ0LjQyNyw0OC4wMTQsNDIuODg5eiIvPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8L3N2Zz4K
    camel.apache.org/kamelet.support.level: Stable
    camel.apache.org/provider: Apache Software Foundation
  labels:
    camel.apache.org/kamelet.type: source
  name: kamelet-3113
spec:
  definition:
    description: Gets periodically Cat facts
    properties:
      period:
        default: 5000
        description: The time interval between two events
        title: Period
        type: integer
    title: Cat Source
    type: object
  dependencies:
    - camel:timer
    - camel:http
    - camel:kamelet
    - camel:gson
  template:
    from:
      steps:
        - to:
            parameters:
              httpUri: https://cat-fact.herokuapp.com/facts/random
            uri: https
        - unmarshal:
            id: unmarshal-1253
            json:
              library: Gson
        - setBody:
            expression:
              simple:
                expression: $.text
            id: setBody-1978
        - to: kamelet:sink
      id: from-7053
      parameters:
        period: "{{period}}"
        timerName: user
      uri: timer
  types:
    out:
      mediaType: application/json
```

### Hints

 - The source code editor can be shown by right clicking the file in the `Explorer` view and selecting `Open with` -> `Text Editor`.

## More information

More information about Apache Camel Kamelets can be found on [the Apache Camel website](https://camel.apache.org/camel-kamelets)
