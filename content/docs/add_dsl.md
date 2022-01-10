---
title: "Add a new DSL"
description: "How to add a new Domain Specific Language to Kaoto."
draft: false
date: "2021-01-01"
tags:
- DSL
categories:
- Development
- Extension
- Backend
image: "images/portfolio/screenshot-03.png"
---

Kaoto frontend is agnostic of the DSL (Domain Specific Language) used, so to add suport for a new DSL we just have to implement the specific endpoints on the [API](https://kaotoio.github.io/kaoto-backend/api/index.html).

## Implementation in Java

You can use the [kamelet-support](https://github.com/KaotoIO/kaoto-backend/tree/main/kamelet-support) project as an example.

You need to create a new Java Maven project that [will be added as dependency on the API project](https://github.com/KaotoIO/kaoto-backend/blob/main/api/pom.xml#L88-L92). You will need to add the [model, catalog and services-interfaces dependencies](https://github.com/KaotoIO/kaoto-backend/blob/main/api/pom.xml#L88-L92) in your project.

Your project has to provide implementations for the following services:


### DeploymentGeneratorService

This service will translate from the JSON list of steps used by the frontend to visualize graphically the workflow to the Custom Resource Definition (CRD) to deploy on Kubernetes.

Your implementation must be `@ApplicationScoped`:

```
@ApplicationScoped
public class KameletBindingDeploymentGeneratorService
        implements DeploymentGeneratorService {

```

The `identifier()` should return a unique string that will be useful to correlate the generated CRD with the type of workflow we are generating.


```
    public String identifier() {
        return "KameletBinding";
    }
    
```

The `getKinds()` must return what steps are this CRD compatible with.

```

    @Override
    public List<String> getKinds() {
        return Arrays.asList(new String[]{CAMEL_CONNECTOR, KAMELET});
    }

```

Then, we need to implement the `parse(...)` function that will return the CRD content based on the list of steps.

```
    @Override
    public String parse(final String name, final List<Step> steps) {
        if (!appliesTo(steps)) {
            return "";
        }
         ...
    }

```

Finally, the `appliesTo(...)` function will be used to decide if this service can be applied to the list of steps.


### StepParserService

This service will do the reverse operation as DeploymentGeneratorService: given a CRD, return the list of steps associated to it. As the previous one, it must have the `@ApplicationScoped` annotation.

```
@ApplicationScoped
public class KameletBindingStepParserService
        implements StepParserService<Step> {
```

You may want to inject a catalog step.

```
    private StepCatalog catalog;

    @Inject
    public void setCatalog(final StepCatalog catalog) {
        this.catalog = catalog;
    }
```

The `parse(...)` function will return the list of steps given a string.

```

    @Override
    public List<Step> parse(final String input) {
        if (!appliesTo(input)) {
            throw new IllegalArgumentException(
                    "Wrong format provided. This is not parseable by us");
        }

        ...
    }

```

And the `appliesTo(...)` function will also check that the CRD provided is valid for this service.

```
    @Override
    public boolean appliesTo(final String yaml) {
        return yaml.contains("kind: KameletBinding");
    }
```



### StepCatalogParser (Optional)

Your DSL probably has specific steps that needs to be added to the catalog. To add those steps to the general catalog, you have to provide an `@ApplicationScoped` implementation of the `StepCatalogParser`:


```
@ApplicationScoped
public final class KameletParseCatalog implements StepCatalogParser {

    private KameletParseCatalog() {

    }

    @Override
    public ParseCatalog<Step> getParser(final String url, final String tag) {
        ParseCatalog<Step> parseCatalog = new GitParseCatalog<>(url, tag);
        parseCatalog.setFileVisitor(new KameletFileProcessor());
        return parseCatalog;
    }


    @Override
    public ParseCatalog<Step> getParser(final String url) {
        ParseCatalog<Step> parseCatalog = new JarParseCatalog<>(url);
        parseCatalog.setFileVisitor(new KameletFileProcessor());
        return parseCatalog;
    }
}
```

Both GitParseCatalog and JarParseCatalog are helper classes that will access the git repository or zip file defined and use a FileVisitor to process the files encountered on them. You don't have to use them in your implementation. The only requirement is to return a [ParseCatalog](https://github.com/KaotoIO/kaoto-backend/blob/main/metadata/src/main/java/io/kaoto/backend/metadata/ParseCatalog.java) that will be called when warming up the catalog steps.

On this case, the [KameletFileProcessor](https://github.com/KaotoIO/kaoto-backend/blob/main/kamelet-support/src/main/java/io/kaoto/backend/metadata/parser/step/kamelet/KameletFileProcessor.java) is an auxiliary class that extends [YamlProcessFile](https://github.com/KaotoIO/kaoto-backend/blob/main/metadata/src/main/java/io/kaoto/backend/metadata/parser/YamlProcessFile.java) to process Kamelet metadata definitions. You can use any FileProcessor that you find suitable to your usecase.

If you don't require any FileProcessor, you can leave that property empty. The only mandatory implementation detail about the ParseCatalog instance returned by your StepCatalogParser is that the returned ParseCatalog `parse()` function returns a list of Steps. You can implement your own ParseCatalog class.

It may be you are using your own kind of steps, specific for your DSL.

#### How to define my custom Step

As described on the [documentation](https://kaotoio.github.io/kaoto-backend/#step), a Step is composed of the following properties:

* **kind** Kind of step which will help correlate the step with the type of workflow it supports. Examples: Steps of kind `kamelet` can be used on Kamelet Bindings. Make sure your `Kind` is unique or compatible with the services that use the same `Kind`.
* **ID** Unique identifier for this step in our whole Kaoto environment.
* **title** Human-readable title of this step. Useful for the frontend.
* **description** Human-readable description of what this step does. This will help users identify what steps they want to use for their usecase.
* **group** Group that identifies and classifies inside the steps world. This can help classify the steps.
* **icon** Base64 icon image for this step. Useful to quickly visually identify steps.
* **UUID** Volatile UUID to mark the relationship between a viewDefinition and a step. Kaoto will fill this property automatically.
* **name** Used only for Camel Connectors. Defines the name of the connector. 
* **type** Type of step: START, MIDDLE, END. This helps the most basic validation of steps: validates the position of the step in the general workflow.
* **parameters** List of configurable parameters for this step.
  | Property         | Description |
  |--------------|-----------|------------|
  |label |Human-readable label for this property.|
  |description| Human-readable description of this parameter.|
  |id| Unique identifier of this parameter.|
  |path| Used only for Camel connectors. Defines if a parameter should be placed on the uri path.|
  |type| Type of parameter: string, integer, boolean,...|
  |value| Actual value of the property, once the user fills it.|
  |defaultValue| Default value to use if `value` is empty.|
  

