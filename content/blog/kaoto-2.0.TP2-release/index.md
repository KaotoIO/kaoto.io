---
title: Version 2.0.0 TP2 released!
date: 2024-02-29T11:00:00+02:00
summary: We are happy to announce the release of Kaoto 2.0.0 TP2 (Tech Preview 2).
authors:
  - admin
tags:
  - Kaoto
  - Release
  - Kaoto 2.0 TP2
  - Tech Preview
---
**We are happy to announce the release of Kaoto 2.0.0 TP2 (Tech Preview 2).** 

We strive to make Kaoto a top choice when it comes to working with [Apache Camel](https://camel.apache.org/) integrations. To achieve that we continuously add new features and enhancements to make the integration developer's life easier and closely collaborate with the [Apache Camel](https://camel.apache.org/) project.

## New Features

#### Camel routes configuration
We added root containers for Camel Routes and Kamelets, so you can configure their behavior.

#### Support for Kamelet Beans
Added support for Kamelet Beans using the Form.

#### Kamelet configuration
Included a custom form to configure the most common aspects of a Kamelet easily.

#### Dropdown placeholders
Users can now enter placeholders in drop-down boxes, enhancing flexibility in defining component configurations.


## UX Improvements

#### Sticky Configuration Form header
We’ve made the form title sticky to ensure a better experience while scrolling through options.

#### Sticky Catalog filter controls
Now the catalog’s filter sticks to the top, so the selected filter is always visible.

#### Catalog filter counts
When searching for a component or a pattern, we included the result count from other categories as well, so we can see what’s available at a glance

#### Sorted Patterns and Components parameters
For ease of navigation, patterns parameters,  and component parameters are now sorted by the Catalog index.

#### Consistent Field Spacing
We've improved field spacing across different components for a cleaner and more consistent look.

## Bug Fixes

* The form scroll bar is outside of the form, to avoid colliding with the form controls
* Empty objects `{}` are not persisted in the source code
* Fix typos in the Bean and OnException definitions upstream ([CAMEL-20462](https://issues.apache.org/jira/browse/CAMEL-20462))

For a full list of changes please refer to the [change log](https://github.com/KaotoIO/kaoto-next/releases/tag/2.0.0-TP2).

## Give it a try!

* Kaoto [quickstart](/docs/quickstart/).
* Kaoto is available as a [VS Code extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto).
* Kaoto [showcase deployment](https://red.ht/kaoto).

## Let’s Build it Together

Let us know what you think by joining us in the [GitHub discussions](https://github.com/orgs/KaotoIO/discussions).
Do you have an idea how to improve Kaoto? Would you love to see a useful feature implemented or simply ask a question? Please [create an issue](https://github.com/KaotoIO/kaoto-next/issues/new/choose)

## A big shoutout to our amazing contributors
Thank you to everyone who made this release possible, whether by a code contribution, feedback, advocacy, or participating in an important discussion with us. ❤️

[@eerkmen](https://github.com/eerkmen) [@corners2wall](https://github.com/corners2wall) [@mkralik3](https://github.com/mkralik3) [@d4n1b](https://github.com/d4n1b) [@tplevko](https://github.com/tplevko) [@apupier](https://github.com/apupier) [@igarashitm](https://github.com/igarashitm) [@mmelko](https://github.com/mmelko) [@lordrip](https://github.com/lordrip) [@lhein](https://github.com/lhein) [@shivamG640](https://github.com/shivamG640) [@lburgazzoli](https://github.com/lburgazzoli) [@brunoNetId](https://github.com/brunoNetId) [@djelinek](https://github.com/djelinek) [@GuilhermeCamposo](https://github.com/GuilhermeCamposo) [@ibek](https://github.com/ibek) [@jcordes73](https://github.com/jcordes73) [@Mdenisco](https://github.com/Mdenisco) [@phantomjinx](https://github.com/phantomjinx) [@rstroop](https://github.com/rstroop) [@abkieling](https://github.com/abkieling) [@Shivam-Gu](https://github.com/Shivam-Gu) [@kumaradityaraj](https://github.com/kumaradityaraj) [@oscerd](https://github.com/oscerd) [@djelinek](https://github.com/djelinek) [@davsclaus](https://github.com/davsclaus)

Apologies in advance if we've missed anyone. 🙂
