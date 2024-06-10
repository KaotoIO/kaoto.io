---
title: Version 2.0.0 TP3 released!
date: 2024-04-05T06:00:00+02:00
summary: We are happy to announce the release of Kaoto 2.0.0 TP3 (Tech Preview 3).
authors:
  - admin
tags:
  - Kaoto
  - Release
  - Kaoto 2.0 TP3
  - Tech Preview
---
**We are happy to announce the release of Kaoto 2.0.0 TP3 (Tech Preview 3).** 

Again we are getting closer to the final 2.0 release! TP3 marks the last tech preview release before we will release Kaoto 2.0. Again we spent time to add useful features and improvements to make Kaoto better. Below you will find a list of major things that have changed.

## New Features

#### Camel 4.4 support
We switched to using Apache Camel 4.4 in our models.

#### Kamelet Properties configuration
We extended the configuration form for Kamelets to allow users to add properties to their Kamelets.

#### Support for Error Handler and REST Configuration
Kaoto now supports global error handlers, route configuration error handlers as well as REST Configuration. At the moment we do not support creating those entities via the UI but you can already add them in the source code and Kaoto will recognize them and offer configuration options. 
We hope to finalize this feature for the 2.0 Final release.

## UX Improvements

#### Improved Expression configuration
We’ve converted the language drop down to a typeahead component which lets you type the expression language you want to use into the filter field. This way you will find your language of choice easily. 
Additionally we have slightly increased the size of the expression text field so you can better work with multiline expressions.

#### Context Menu Actions on Nodes
We simplified the names of the actions in the step context menu for your better understanding.

#### Configuration Form
When opening the configuration form for a step the form does no longer hide underlying nodes on the canvas but moves the nodes to the left. This is convenient when working with smaller resolutions / window sizes.
Another change you will recognize is that we added groups for the configuration form which will help you find a property more easily. We did also apply the sorting order for parameters as suggested by the Camel catalog.

## Bug Fixes

For a full list of changes please refer to the [change log.](https://github.com/KaotoIO/kaoto-next/releases/tag/2.0.0-TP3)

## Kaoto's Future Outlook
Our plan is to release the 2.0 version around mid of May 2024. At that point the development of Kaoto will not be complete by any means and we will continuously add new features and improvements. We aim at having monthly releases if possible. That way we can provide you with the latest features faster. 


## Give it a try!

* Kaoto [quickstart](/docs/quickstart/).
* Kaoto is available as a [VS Code extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto).
* Kaoto [showcase deployment](https://red.ht/kaoto).

## Let’s Build it Together

Let us know what you think by joining us in the [GitHub discussions](https://github.com/orgs/KaotoIO/discussions).
Do you have an idea how to improve Kaoto? Would you love to see a useful feature implemented or simply ask a question? Please [create an issue](https://github.com/KaotoIO/kaoto-next/issues/new/choose).

## A big shoutout to our amazing contributors
Thank you to everyone who made this release possible, whether by a code contribution, feedback, advocacy, or participating in an important discussion with us. ❤️

[@eerkmen](https://github.com/eerkmen) [@corners2wall](https://github.com/corners2wall) [@mkralik3](https://github.com/mkralik3) [@d4n1b](https://github.com/d4n1b) [@tplevko](https://github.com/tplevko) [@apupier](https://github.com/apupier) [@igarashitm](https://github.com/igarashitm) [@mmelko](https://github.com/mmelko) [@lordrip](https://github.com/lordrip) [@lhein](https://github.com/lhein) [@shivamG640](https://github.com/shivamG640) [@lburgazzoli](https://github.com/lburgazzoli) [@brunoNetId](https://github.com/brunoNetId) [@djelinek](https://github.com/djelinek) [@GuilhermeCamposo](https://github.com/GuilhermeCamposo) [@ibek](https://github.com/ibek) [@jcordes73](https://github.com/jcordes73) [@Mdenisco](https://github.com/Mdenisco) [@phantomjinx](https://github.com/phantomjinx) [@rstroop](https://github.com/rstroop) [@abkieling](https://github.com/abkieling) [@Shivam-Gu](https://github.com/Shivam-Gu) [@kumaradityaraj](https://github.com/kumaradityaraj) [@oscerd](https://github.com/oscerd) [@djelinek](https://github.com/djelinek) [@davsclaus](https://github.com/davsclaus) [@joshdreagan](https://github.com/joshdreagan)

Apologies in advance if we've missed anyone. 🙂