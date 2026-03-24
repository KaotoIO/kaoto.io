---
title: "DataMapper"
description: "update here"
date: 2026-03-25
weight: 4
draft: true
---

Some instructions:

1. All the text and references should be written in this index file

2. You can add sub-folders (ex. in manual folder) and inside add index.md

3. The featured image for the main folder (ex.metadata) should be saved as featured.png

4. Example of useful shortcodes for image-code toggle, images and youtube videos:


{{< img-toggle src="./partial-route.webp" lang="yaml" >}}
- route:
    id: route-2573
    from:
      id: from-3280
      uri: file-watch
      parameters:
        path: /tmp/tutorial/
        recursive: false
      steps:
        - log:
            message: Detected ${header.CamelFileEventType} on file ${header.CamelFileName}
              at ${header.CamelFileLastModified}
{{< /img-toggle >}}

{{< figure src="dm-04-01-icon-opt.png" alt="Opt icon for optional field" caption="Opt icon for optional field" class="image" >}}

{{< youtube id="nuzl3p986Mc" class="video" title="DataMapper Expansion Panels Demo" >}}

5. Use markdown features as you want and have fun!

6. Once finished, update the description, date and delete draft: true