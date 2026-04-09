---
title: "Beans"
description: "Learn how to define and manage custom bean instances in your Apache Camel integrations using Kaoto"
date: 2026-04-02
weight: 6
---

## Overview

Beans allow you to define custom Java object instances that can be referenced and reused across your Apache Camel routes — such as a database connection pool, a custom processor, or a third-party client. If you completed the [Quickstart](../quickstart/), you can extend that integration by adding beans to it.

A bean has a **name** (its identifier within the integration), a **type** (the fully qualified Java class name), and optional configuration such as **properties**, **constructor arguments**, or a **factory method**. Once defined, a bean can be referenced from any step in your routes.

## Benefits

Using beans in your Camel integrations provides several key advantages:

- **Reusability** — Define once, reference multiple times across different routes without duplicating configuration
- **Centralized configuration** — Manage connection details, credentials, and settings in one place for easier maintenance
- **Type safety** — Leverage Java's type system with fully qualified class names for compile-time validation
- **Separation of concerns** — Keep infrastructure configuration separate from business logic in your routes
- **Testability** — Mock or replace beans easily during testing without modifying route definitions
- **Performance** — Share expensive resources like connection pools across multiple routes efficiently

### Common use cases

- **Data sources** — database connection pools (e.g., `PGSimpleDataSource`, `HikariDataSource`)
- **HTTP clients** — pre-configured REST or HTTP clients with base URLs and authentication
- **Custom processors** — Java classes implementing Camel's `Processor` interface for custom logic
- **Caches** — in-memory or distributed cache instances (e.g., Caffeine, Redis)
- **Serializers / Marshallers** — Jackson `ObjectMapper` or JAXB context beans
- **Business logic beans** — Custom Java classes containing business logic invoked via the Bean component or Bean EIP

### Bean Component and Bean EIP

Beans can also execute custom business logic in your routes:

- **Bean EIP** — The standard way to invoke bean methods as processing steps within a route. Use this for most scenarios where you need to execute business logic mid-route.
- **Bean Component** — Invokes beans using URI syntax (`uri: bean:beanName?method=methodName`). Use this when you need to dynamically construct the URI from runtime values such as headers or variables.

Both allow you to define business logic in Java classes and reference them as beans, keeping routes clean and logic reusable.

Kaoto offers two approaches for working with beans, covered in the scenarios below.

> [!TIP]
> **Configuration Best Practice**: The examples in this guide use Camel's [property placeholder syntax](https://camel.apache.org/manual/using-propertyplaceholder.html) like `{{db.password}}` for sensitive values. These properties are resolved at runtime from an `application.properties` file in your project. For example:
> ```properties
> db.password=your_actual_password
> ```
> For production deployments, use secret managers (e.g., Kubernetes Secrets) or platform-specific secret injection mechanisms.

---

## Scenario 1: Define a bean first, then reference it in a route step

This scenario demonstrates creating a PostgreSQL datasource bean for a book database, connecting it to a route, and running the complete integration.

### Prerequisites

Before starting, ensure you have:

- PostgreSQL installed and running locally
- A database named `bookstore` created
- Database credentials ready

Create the database and table:

```sql
CREATE DATABASE bookstore;

\c bookstore

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(13),
    published_year INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Step 1 — Create the bean in the Beans Editor

1. Open a Camel integration file in Kaoto (or create a new one named `book-database.camel.yaml`)

2. Click the **Beans** tab at the top of the Kaoto editor to open the Beans Editor
{{< image-sh src="01-beans-tab.png" text="Beans tab" >}}

3. Click **Add new Beans** at the top of the bean list
{{< image-sh src="02-add-beans-button.png" text="Add new Beans button" >}}

4. In the **Details** form at the right, fill bean **name** and Java **type**:
   - **name** → `bookDataSource`
   - **type** → `org.postgresql.ds.PGSimpleDataSource`
{{< image-sh src="03-bean-name-type.png" text="Bean name and type" >}}

5. Lower in the **Details** form, add the connection details under **properties**. Click **Add a new property** button:
{{< image-sh src="04-bean-properties.png" text="Add Bean properties" >}}

6. Fill properties name and value as following:

   | Key | Value |
   | --- | ----- |
   | `serverName` | `localhost` |
   | `databaseName` | `bookstore` |
   | `user` |  `postgres` |
   | `password` | `{{db.password}}` |
   | `portNumber` | `5432` |

   {{< image-sh src="04-02-bean-properties-added.png" text="Bean properties added" >}}

This adds `beans` block

```yaml
- beans:
    - name: bookDataSource
      type: org.postgresql.ds.PGSimpleDataSource
      properties:
        serverName: localhost
        databaseName: bookstore
        user: postgres
        password: '{{db.password}}'
        portNumber: 5432
```

### Step 2 — Create a route using the bean

Now create a route that uses this datasource bean to insert book records:

1. Click the **Design** tab to return to the canvas

2. Kaoto creates a default timer-to-log route. Configure the **Timer** component:
   - **Timer Name** → `bookInsertTimer`
   - **Period** → `10000` (runs every 10 seconds)

3. Insert an **SQL** component between Timer and Log:
   - **Query** → `INSERT INTO books (title, author, isbn, published_year) VALUES ('Camel Integration Patterns', 'John Smith', '978-0321200686', 2003)`
   - **Data Source** → Select `#bookDataSource` from the dropdown

4. Update the **Log** step message:
   - **Message** → `Book inserted successfully: ${body}`

The generated structure looks like this:
{{< img-toggle src="./09-route.png" lang="yaml" >}}
- route:
    id: route-book-insert
    from:
      uri: timer
      parameters:
        timerName: bookInsertTimer
        period: "10000"
      steps:
        - to:
            uri: sql
            parameters:
              query: INSERT INTO books (title, author, isbn, published_year) VALUES ('Camel Integration Patterns', 'John Smith', '978-0321200686', 2003)
              dataSource: "#bookDataSource"
        - log:
            message: "Book inserted successfully: ${body}"
{{< /img-toggle >}}

### Step 3 — Run the integration

1. Ensure PostgreSQL is running and the `bookstore` database exists

2. In Kaoto, click the **Run** button in the toolbar
   {{< image-sh src="10-run-button.png" text="Run Button" >}}

3. The integration will start and begin inserting book records every 10 seconds
   {{< image-sh src="11-book-insert.png" text="Book inserted successfully" >}}

### Expected Output

When the integration runs successfully, you should see output similar to:

```text
INFO  [main] Apache Camel 4.18.1 (book-database) started in 156ms
INFO  [bookInsertTimer] Book inserted successfully: 1
INFO  [bookInsertTimer] Book inserted successfully: 1
```

### Verify the Data

Connect to your PostgreSQL database and query the books table:

```sql
SELECT * FROM books ORDER BY created_at DESC LIMIT 5;
```

You should see the newly inserted book records:

```text
 id |           title            |   author   |      isbn      | published_year |         created_at         
----+----------------------------+------------+----------------+----------------+----------------------------
  2 | Camel Integration Patterns | John Smith | 978-0321200686 |           2003 | 2026-04-03 14:59:57.165154
  1 | Camel Integration Patterns | John Smith | 978-0321200686 |           2003 | 2026-04-03 14:59:47.221565
```

### Complete Integration YAML

Here's the complete working integration combining the bean definition and route:

```yaml
- beans:
    - name: bookDataSource
      type: org.postgresql.ds.PGSimpleDataSource
      properties:
        serverName: localhost
        databaseName: bookstore
        user: postgres
        password: '{{db.password}}'
        portNumber: 5432

- route:
    id: route-book-insert
    from:
      uri: timer
      parameters:
        timerName: bookInsertTimer
        period: "10000"
      steps:
        - to:
            uri: sql
            parameters:
              query: INSERT INTO books (title, author, isbn, published_year) VALUES ('Camel Integration Patterns', 'John Smith', '978-0321200686', 2003)
              dataSource: "#bookDataSource"
        - log:
            message: "Book inserted successfully: ${body}"
```

> [!TIP]
> This bean-based database infrastructure can later be referenced by REST endpoints for a complete book management API (e.g., `GET /books`, `POST /books`, `GET /books/{id}`). The datasource bean provides a reusable, centrally configured database connection that multiple routes and REST endpoints can share.

---

## Scenario 2: Start from the step, create the bean inline

This scenario demonstrates creating a bean directly from a component's configuration panel, useful when you're building a route and realize you need a new bean. We'll use the same book insertion example, but create the bean inline while configuring the SQL component.

### Step 1 — Add an SQL step to your route

1. Open a Camel integration file in Kaoto and click the **Design** tab at the top of the Kaoto editor

2. Kaoto creates a default timer-to-log route. Insert an **SQL** component between Timer and Log

3. In the SQL step configuration, you'll need to specify:
   - **Query** — `INSERT INTO books (title, author, isbn, published_year) VALUES ('Camel Integration Patterns', 'John Smith', '978-0321200686', 2003)`
   - **Data Source** — Reference to a datasource bean

4. Locate the **Data Source** field and click it
{{< image-sh src="12-data-source.png" text="Create a Data Source Bean" >}}

### Step 2 — Create the bean from the Data Source field

1. In the dropdown, click **Create new bean**
{{< image-sh src="13-create-new-bean-option.png" text="Create new bean option" >}}

2. A modal dialog opens — fill in:
   - **name** → `bookstoreDataSource`
   - **type** → `org.postgresql.ds.PGSimpleDataSource`
   {{< image-sh src="14-create-new-bean-modal.png" text="Create new bean modal" >}}

3. Add the connection details under **properties**:

   | Key | Value |
   | --- | ----- |
   | `serverName` | `localhost` |
   | `databaseName` | `bookstore` |
   | `user` | `postgres` |
   | `password` | `{{db.password}}` |
   | `portNumber` | `5432` |

   {{< image-sh src="15-create-new-bean-properties.png" text="DataSource Properties" >}}

4. Click **Create**
{{< image-sh src="16-create-new-bean-create.png" text="Create button" >}}

The bean is added to the beans list and the **Data Source** field is automatically set to reference it — in a single action.

{{< image-sh src="17-datasource-set.png" text="Data Source automatically set to bookstoreDataSource" >}}

This adds `beans` block
```yaml
- beans:
    - name: bookstoreDataSource
      type: org.postgresql.ds.PGSimpleDataSource
      properties:
        serverName: localhost
        databaseName: bookstore
        user: postgres
        password: '{{db.password}}'
        portNumber: 5432
```

---

## Editing a Bean

1. Click the **Beans** tab at the top of the Kaoto editor
   {{< image-sh src="01-beans-tab.png" text="Beans tab" >}}

2. In the Beans list at the left, click the row for the bean you want to edit — it shows all fields of the Bean at right
{{< image-sh src="18-bean-details.png" text="Bean Details" >}}

3. Modify the values as needed; changes are applied immediately
   {{< image-sh src="19-bean-properties.png" text="Bean Properties" >}}

To add a property, fill in a new key-value pair in the **properties** section. To remove a property, click the remove icon next to it.
{{< image-sh src="20-bean-properties-add.png" text="Add Bean Properties" >}}
{{< image-sh src="21-bean-properties-remove.png" text="Remove Bean Properties" >}}

---

## Deleting a Bean

1. Click the **Beans** tab at the top of the Kaoto editor

2. Click the **Delete** button (trash icon) on the right side of the bean row
{{< image-sh src="22-delete-bean.png" text="Delete button on a bean row" >}}

> [!WARNING]
> Deleting a bean that is still referenced by a route step leaves a dangling reference. Update or remove the affected step configurations before deleting the bean.
