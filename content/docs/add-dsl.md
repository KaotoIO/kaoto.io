---
title: "Add a New DSL"
description: "How to add a new Domain Specific Language to Kaoto."
draft: false
date: "2021-01-01"
tags:
- DSL
categories:
- Development
- Extension
- Backend
---

Kaoto's frontend is agnostic of the DSL (Domain Specific Language) used, so to add support for a new DSL we just have to implement the specific endpoints on the [API](https://kaotoio.github.io/kaoto-backend/api/index.html).

To properly deploy the workflows, Kaoto is expecting the integration to be deployed via a [CustomResourceDefinition (CRD)](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) as [Camel-K](https://camel.apache.org/camel-k/) does. You can use other kinds of source code and build integrations with them, but they won't be deployable via Kaoto.

## Implementation

You can use the [kamelet-support](https://github.com/KaotoIO/kaoto-backend/tree/main/kamelet-support) project as an example.

You need to create a new Java Maven project that [will be added as dependency on the API project](https://github.com/KaotoIO/kaoto-backend/blob/main/api/pom.xml#L88-L92). You will need to add the [model, catalog and services-interfaces dependencies](https://github.com/KaotoIO/kaoto-backend/blob/main/kamelet-support/pom.xml#L14-L28) in your project.

Your project has to provide implementations for one or more the following services:


### DeploymentGeneratorService

This service will translate from the JSON list of steps used by the frontend to visualize graphically the workflow to the source code. By implementing this service, you give Kaoto the ability to "translate" from graphical to source code.

![From steps to code](/images/docs/kaoto-backend-overview-crd.svg "From steps to code")

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

The `getKinds()` must return what steps are this CRD compatible with. Kaoto will try to apply all DeploymentGeneratorServices on all the calls unless we explicitly ask for a specific source code output. The `getKinds` function is a quick check to know if we should apply this implementation when Kaoto is requested to output source codes.

```

    @Override
    public List<String> getKinds() {
        return Arrays.asList(new String[]{CAMEL_CONNECTOR, KAMELET});
    }

```

Then, we need to implement the `parse(...)` function that will return the CRD content based on the list of steps and a map of metadata.

```
    @Override
    public String parse(List<Step> steps, Map<String, Object> metadata) {
        if (!appliesTo(steps)) {
            return ""; //someone tried to apply this service to the wrong list of steps
        }
         ...
    }

```

Finally, the `appliesTo(...)` function will be used to decide if this service can be applied to the list of steps. Note that this `appliesTo` function is the one that decides if you will be able to generate the source code or not. If this function returns `true`, the function `parse` must return valid source code. 


### StepParserService

This service will do the reverse operation as DeploymentGeneratorService: given a CRD, return the list of steps associated to it. By implementing this service, you give Kaoto the ability to "translate" from the source code to graphic editing.

![From code to steps](/images/docs/kaoto-backend-overview-steps.svg "From code to steps")

As the previous one, it must have the `@ApplicationScoped` annotation. 

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
    public ParseResult<Step> deepParse(String input);
        if (!appliesTo(input)) {
            throw new IllegalArgumentException(
                    "Wrong format provided. This is not parseable by us");
        }

        ...
    }

```

The `ParseResult<T>` class is an auxiliary class that returns both a list of steps and some metadata that may be helpful to decorate the source code. For example, the name of the integration, or some dependencies.

```
    class ParseResult<T> {
        private List<T> steps;
        private Map<String, Object> metadata;
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

 Note that this `appliesTo` function is the one that decides if you will be able to parse the source code or not. If this function returns `true`, the function `parse` must return a valid list of steps. 


### StepCatalogParser (Optional)

Your DSL may have specific steps that needs to be added to the catalog. To add those steps to the general catalog, you have to provide an `@ApplicationScoped` implementation of the `StepCatalogParser`:


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

On this case, the [KameletFileProcessor](https://github.com/KaotoIO/kaoto-backend/blob/main/kamelet-support/src/main/java/io/kaoto/backend/metadata/parser/step/kamelet/KameletFileProcessor.java) is an auxiliary class that extends [YamlProcessFile](https://github.com/KaotoIO/kaoto-backend/blob/main/metadata/src/main/java/io/kaoto/backend/metadata/parser/YamlProcessFile.java) to process Kamelet metadata definitions. You can use any FileProcessor that you find suitable to your use-case.

If you don't require any FileProcessor, you can leave that property empty. The only mandatory implementation detail about the ParseCatalog instance returned by your StepCatalogParser is that the returned ParseCatalog `parse()` function returns a list of Steps. You can implement your own ParseCatalog class.

It may be you are using your own kind of steps, specific for your DSL.
