<h1 align="center">
  <a href="https://kaoto.io"><img src="./assets/media/logo-kaoto.png" alt="Kaoto"></a>
</h1>

<p align=center>
  <a href="https://github.com/KaotoIO/kaoto.io/blob/main/LICENSE"><img src="https://img.shields.io/github/license/KaotoIO/kaoto.io?color=blue&style=for-the-badge" alt="License"/></a>
  <a href="https://www.youtube.com/@KaotoIO"><img src="https://img.shields.io/badge/Youtube-Follow-brightgreen?color=red&style=for-the-badge" alt="Youtube"" alt="Follow on Youtube"></a>
  <a href="https://camel.zulipchat.com/#narrow/stream/441302-kaoto"><img src="https://img.shields.io/badge/zulip-join_chat-brightgreen?color=yellow&style=for-the-badge" alt="Zulip"/></a>
  <a href="https://kaoto.io"><img src="https://img.shields.io/badge/Kaoto.io-Visit-white?color=indigo&style=for-the-badge" alt="Zulip"/></a>
</p><br/>

<h2 align="center">Kaoto - The Integration Designer for <a href="https://camel.apache.org">Apache Camel</a></h2>

<p align="center">
  <a href="https://kaoto.io/docs/installation">Documentation</a> |
  <a href="https://kaoto.io/workshop/">Workshops</a> |
  <a href="https://kaoto.io/contribute/">Contribute</a> |
  <a href="https://camel.zulipchat.com/#narrow/stream/441302-kaoto">Chat</a>
</p>

# Kaoto

Kaoto is a visual editor for Apache Camel integrations. It offers support in creating and editing Camel Routes, Kamelets and Pipes. Kaoto also has a built-in catalog with available Camel components, Enterprise Integration Patterns and Kamelets provided by the Apache Camel community.

Have a quick look at our online demo instance:
[https://kaotoio.github.io/kaoto/](https://kaotoio.github.io/kaoto/)

This repository holds the website for [https://kaoto.io/](https://kaoto.io/). Built with [Hugo Blox](https://hugoblox.com/).

## Installing Prerequisites

You will need to install some tools to be able to build and run this project locally.

### GO

You will need Go installed to build the project. Check your package manager of choice or visit the GO Installation page below.

[GO Installation](https://go.dev/doc/install)

### Hugo

You will need Hugo installed to run this project locally. You can do this via your package manager or visit the Hugo Installation page below.

[Hugo Installation](https://gohugo.io/installation/)

## Build

```bash
pnpm install
```

## Development

```bash
hugo server
```

**Once Hugo started successfully, you will find the page at [http://localhost:1313](http://localhost:1313).**

> [!NOTE]
> The **port 1313** is **default**.
>
> However this port can be different for you if it is already in use. Please check the console output for the right URL.
