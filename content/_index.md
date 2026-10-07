---
title: 'Home'
date: 2023-10-24
type: landing

# SEO Meta Tags
description: 'Open source Apache Camel integration designer with a visual editor, 300+ components, Kamelets, EIPs, and a visual Data Mapper for VS Code.'
keywords:
  - Apache Camel Designer
  - Visual Integration Editor
  - Low Code Integration
  - Camel Route Designer
  - VS Code Camel Extension
  - Kamelets Editor
  - Enterprise Integration Patterns
  - Open Source Integration Tool

# Open Graph / Social Media
images:
  - 'kaoto-lowcode.png'  # Or create kaoto-og.png (1200x630px)

# Structured Data (JSON-LD)
seo:
  title: 'Kaoto - Visual Designer for Apache Camel Integrations'
  description: 'Open source Apache Camel integration designer with a visual editor, 300+ components, Kamelets, EIPs, and a visual Data Mapper for VS Code.'
  canonical: 'https://kaoto.io/'
  noindex: false
  nofollow: false

sections:
  - block: hero2
    content:
      title: <span class="text-2xl sm:text-3xl lg:text-4xl font-semibold text-gray-700 dark:text-gray-300">Visual Integration Designer<br/>for [Apache Camel](https://camel.apache.org)</span>
      text: Lower the barrier of getting started with Apache Camel and empower your team to integrate systems with ease by leveraging the Kaoto Open Source Designer. Build your integrations and test them locally for a fast feedback loop.
      image: "kaoto-lowcode2.gif"
      primary_action:
        icon: computer-desktop-solid
        text: Installation
        url: docs/installation
      secondary_action:
        text: Quickstart
        url: docs/quickstart/
      tertiary_action:
        text: Try Online
        url: "https://red.ht/kaoto"
      announcement:
        text: "Kaoto 2.13 has been released!"
    design:
      spacing:
        padding: ["1rem", 0, "1rem", 0]
      css_class: "dark"
      background:
        color: "#0d1117"
  # latest updates (blog & workshops)
  - block: latest
    id: latest
    content:
      title: Latest Updates
      text: Recent news, releases, and workshops from the Kaoto community
      count: 3
    design:
      spacing:
        padding: [0, 0, 0, 0]
  # features
  - block: kaoto-features
    id: features
    content:
      title: Features
      text: Everything you need to design, configure, and prototype Apache Camel integrations with zero boilerplate.
      items:
        - name: Based on Apache Camel
          icon: hero/camel-logo
          description: Kaoto utilizes the Apache Camel models and schemas to always offer you all available upstream Camel features, components, and EIPs.
        - name: VS Code Extension
          icon: hero/vscode
          description: Kaoto comes as an extension you can easily install from the Microsoft Marketplace or Open VSX directly inside your IDE.
          link:
            text: "Install from Marketplace"
            url: "https://marketplace.visualstudio.com/items?itemName=redhat.vscode-kaoto"
        - name: Visual DataMapper
          icon: code-bracket
          description: Visually map data between complex input and output schemas (JSON, XML, CSV) with full XPath 3.1 & XSLT 3.0 support and variables.
          link:
            text: "Read DataMapper Guide"
            url: "docs/datamapper/"
        - name: 300+ Component Catalog
          icon: book-open
          description: Instant access to a rich catalog of 300+ Camel Components, 200+ Kamelets, and Enterprise Integration Patterns with integrated docs.
        - name: Rapid Prototyping & Dev Mode
          icon: rocket-launch
          description: Build and run your integrations locally in Dev Mode for instant turnaround and a fast feedback loop on your changes.
        - name: Free Libre & Open Source
          icon: hero/open-source
          description: Truly open with Apache 2.0 license and zero vendor lock-in. Developed transparently by the community on GitHub.
          link:
            text: "View on GitHub"
            url: "https://github.com/KaotoIO/kaoto"
    design:
      spacing:
        padding: [0, 0, 0, 0]
  - block: slideshow
    id: slideshow-section
    content:
      title: Integration Developers Feedback
      text: See what our users have to say
      items:
        - name: "Richard Stroop"
          role: "High Wizard of Integration at Red Hat"
          image: "media/people/richard_s.png"
          text: "It's come so far and it's so good now!"
    design:
      spacing:
        # Reduce bottom spacing so the testimonial appears vertically centered between sections
        padding: [0, 0, 0, 0]
---
