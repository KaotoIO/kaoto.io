---
title: 'Home'
date: 2024-06-07
type: landing

design:
  # Default section spacing
  spacing: "1rem"

sections:
  # the big teaser block
  - block: hero2
    content:
      title: The Integration Designer for<br/>[Apache Camel](https://camel.apache.org)
      text: Lower the barrier of getting started with Apache Camel and empower your team to integrate systems with ease by leveraging the Kaoto Open Source Designer. Build your integrations and test them locally for a fast feedback loop.
      primary_action:
        icon: computer-desktop-solid
        text: Installation
        url: docs/installation
      secondary_action:
        text: Try Online
        url: "https://red.ht/kaoto"
      announcement:
        text: "Kaoto 2.6 is available!"
        link:
          text: "Check it out!"
          url: "blog/kaoto-2.6-release/"
    design:
      css_class: "dark"
      background:
        color: '#293133'
  
  - block: markdown
    id: lowcode
    content:
      title: 
      text: |-
        !["Show Kaoto with source and design view side by side"](kaoto-lowcode.png)

  # features
  - block: features
    id: features
    content:
      title: Features
      text: Kaoto has been designed with a focus on enabling users to quickly prototype Apache Camel integrations without deep Camel knowledge or having to write complex Java code.
      items:
        - name: Based on Apache Camel
          icon: camel-logo
          description: Kaoto utilizes the Apache Camel models and schemas to always offer you all available upstream Camel features. 
        - name: VS Code Extension
          icon: vscode
          description: Kaoto comes as an extension you can easily install from the Microsoft Marketplace. You can install it directly from inside your VS Code instance.
        - name: Care about developers
          icon: code-bracket
          description: Kaoto is a low code / no code visual editor for Apache Camel integrations. Using Kaoto will lower the barrier for integration developers to get started with Apache Camel.
        - name: Free Libre and Open Source
          icon: open-source
          description: Truly open with no vendor lock-in. Use, reuse, share, modify, and resell to your needs. Own Kaoto and make it yours, making sure your use cases are covered.
        - name: Built-In Catalog
          icon: book-open
          description: Kaoto provides you access to a catalog of 300+ Camel Components, 200+ Kamelets and a variety of Enterprise Integration Patterns to choose from. Each of them comes with a documentation to help you get started.
        - name: Rapid Prototyping
          icon: rocket-launch
          description: Building your integration while running it in parallel in Dev Mode gives you a quick turnaround on your changes and enables you to quickly prototype your Camel routes. 
  
  - block: cta-image-paragraph
    id: details
    content:
      items:
        - title: Visual Integration Editor
          text: Design your Camel routes, Kamelets and Pipes in a visual low-code / no-code way.
          image: canvas.png
        - title: Built-in Catalog
          text: Browse the comprehensive built-in catalog containing a vast number of available Camel Components (Connectors), Enterprise Integration Patterns as well as Kamelets provided by Apache Camel.
          image: catalog.png
        - title: Easy Configuration
          text: Selecting a figure on the graphical canvas will open up a configuration form to the right side which allows you to easily do your customizations.
          image: configform.png
        - title: Built-in Data Mapping & Transformation UI
          text: Use the Kaoto DataMapper to map data between input and output structures and to transform it to your needs.
          image: datamapper.png
        
  - block: markdown
    id: youtube
    content:
      title: Kaoto Introduction
      text: Watch this introduction video showing how to get started with Kaoto<br/><br/>{{< youtube ADU0j7VFCxs >}}<br/>
    design:
      css_class: "light"

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
      css_class: "dark"
      background:
        color: "#293133"
      spacing:
        # Reduce bottom spacing so the testimonial appears vertically centered between sections
        padding: ["1rem", 0, 0, 0]

  # displays all picture inside the <logo_folder>
#  - block: logos
#    id: customers
#    content:
#      title: Integrating with Kaoto
#      text: 
#      logo_folder: companies/
#    design:
#      background:        
---
