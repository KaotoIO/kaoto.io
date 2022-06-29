---
title: "Add a Custom View"
description: "How to add a custom view for specific steps."
draft: false
date: "2022-01-10"
tags:
- Custom View
categories:
- Development
- Extension
- Frontend
image: "/images/step-extension.png"
---

Kaoto's frontend is extendable, allowing you to create custom views. You
can configure Kaoto to show a specific view instead of the generic form to configure properties in a step. 
We call these custom views **Step Extensions**.

Kaoto has an **Step Extension API** to interact with the main application. This API can
be used to control deployments remotely, or to do some kind of data transformation 
with the output of a particular step.

There are two main changes when adding a new step extension:

1. The Step Extension itself, which is a remote application implemented by you.
2. The View Definition catalog, that lists all available views and extensions.


## Implementing a Step Extension

A Step Extension is a web application that uses Webpack 4.x or later.

This can even be in the form of built static files. In fact, this is
how we are able to host our [example](https://step-extension.netlify.app/) on 
Netlify. You can use the [example extension](https://github.com/KaotoIO/step-extension) as a template.

Or maybe you already have an external application that you'd like to have
embedded within Kaoto. Then you can [skip to the View Definition section directly](#view-definition-catalog).

### Under the Hood

As we are using [module federation](https://webpack.js.org/concepts/module-federation/), your
application need to use Webpack 4.x or later. Webpack can be used with other tools like Rollup. 
Or you can use it just for module federation if you choose to.

If you're not familiar with the concept of module federation, don't worry. 
The important thing to know is that it gives you the flexibility to
deploy your application independently, so Kaoto don't need to be
restarted. 

Dependency alignment is not needed with module federation. You can specify 
whether you want to share a particular version of a framework, like React, 
or if you want to use your own.

### Enabling Module Federation in Your App

One of the biggest benefits of using module federation is that it works just
like any other `import`. This means **you don't have to make any alterations
to an existing code base**. It's simply a matter of configuring it.

When you enable module federation, your `webpack.config.js` file will look 
something like this:

```js
const HtmlWebPackPlugin = require("html-webpack-plugin");
const ModuleFederationPlugin = require("webpack/lib/container/ModuleFederationPlugin");
const deps = require("./package.json").dependencies;

module.exports = {
  devServer: {
    port: 3000,
    historyApiFallback: true,
  },
  output: {
    publicPath: "http://localhost:3000/",
  },
  resolve: {
    extensions: [".tsx", ".ts", ".jsx", ".js", ".json"],
  },
  plugins: [
    new ModuleFederationPlugin({
      name: "funapp",
      filename: "remoteEntry.js",
      exposes: {
        "./FunComponent": "./src/FunComponent",
      },
      shared: {
        ...deps,
        react: {
          singleton: true,
          requiredVersion: deps.react,
        },
        "react-dom": {
          singleton: true,
          requiredVersion: deps["react-dom"],
        }, },
    }),
    new HtmlWebPackPlugin({
      template: "./src/index.html",
    }),
  ],
};
```

Some important things to note is the `ModuleFederationPlugin`, which comes 
built into Webpack. In it, you have a few properties that are relevant:

- `name`: The name of your application. This cannot conflict with another 
Step Extension `name` in the catalog.
- `filename`: This is the name of your remote entry file, which is usually 
  `remoteEntry.js`.
- `exposes`: The files this application will expose to Kaoto. Typically, 
  this will be a single component. In this example, we are sharing a component 
  called `FunComponent`.
- `shared`: Any libraries you want to share with Kaoto.

There are other options we won't go into, but these are the basics.


You can learn more about the [Step Extension API here](/docs/step-extension-api).

## View Definition Catalog

Kaoto uses a repository of configuration files to determine what 
views should the frontend use and when. To make Kaoto aware of your Step Extension, 
you need to add a configuration file with your extension.
 
First, you will have to fork 
[the catalog being used by default](https://github.com/KaotoIO/kaoto-viewdefinition-catalog)
to be able to include your configuration file while you develop it.

Then you will need to
[configure your backend to use your forked View Definition catalog](https://github.com/KaotoIO/kaoto-backend/blob/main/api/src/main/resources/application.yaml#L8).


```yaml {linenos=inline,hl_lines=[6]}
repository:
  step:
    [...]
  viewdefinition:
    jar:
      - "https://github.com/YourUser/YourRepository/archive/refs/heads/main.zip"
```

Now you need to create a configuration file for your step extension. You can use 
one of the [existing files as template](https://github.com/KaotoIO/kaoto-viewdefinition-catalog).

For example:

```yaml {linenos=inline,hl_lines=[4,5,6],linenostart=1}
name: Fun Component
id: detail-step
type: step
url: http://localhost:8080
module: './FunComponent'
scope: 'funapp'
constraints: 
   -
      mandatory: true
      operation: CONTAINS_STEP_NAME
      parameter: twitter-search-source      
```

Most of these properties are simply mapping to the `ModuleFederationPlugin` 
properties we've just defined above:

- `name` is what will appear as the label of the new tab of the component
- `url` is where your application is running
- `module` here corresponds to the `exposes` object, or the components 
  you're exposing.
- `scope` MUST match the `name` of your application that we defined earlier
- `constraints` defines when the extension will be shown. In this
   example, the extension will be shown when configuring the
   `twitter-search-source` step. It will appear as a new "Fun Component"
   tab when you click on it in the Visualization.

It is important that the `url` points to where you have deployed the extension
implemented in the previous step.

## Putting it All Together

You should now have an application that has Webpack Module Federation 
enabled, with a defined component that you want to stream to Kaoto. 
Start Kaoto as usual, ensuring that it is pointing to the correct View 
Definition catalog.

You can now proceed to the [Step Extension API](/docs/step-extension-api)
documentation to make your extension more interesting.

