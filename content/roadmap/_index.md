---
title: Roadmap
---

<style>
h1 {
    text-align: center;
}

.roadmap-container {
    display: flex;
    flex-direction: column;
    gap: 20px;
    position: relative;
    padding-left: 60px;
}

.roadmap-timeline {
    position: absolute;
    left: 30px; /* Adjusted to center the circle */
    top: 0;
    width: 5px;
    background: lightgray;
    height: 100%; /* Adjusted to cover the height of the container */
}

.roadmap-card {
    display: flex;
    align-items: center;
    border: 3px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    width: 100%;
    box-shadow: 0 8px 10px rgba(0, 0, 0, 0.2);
    position: relative;
}

.roadmap-card.wip {
    border-color:rgb(255, 166, 0);
    border-width: 3px; /* Increased border width */
}

.roadmap-card.completed {
    border-color: #4CAF50;
    border-width: 3px; /* Increased border width */
}

.roadmap-card .icon {
    font-size: 40px;
    background-size: cover; 
    background-repeat: no-repeat; 
    width: 60px; 
    height: 60px; 
    flex: 0 0 80px 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 40px;
}

.roadmap-card .content {
    flex: 1;
}

.roadmap-card .content h3 {
    margin: 0;
    font-size: 1.2em;
    font-weight: bold;
}

.roadmap-card .content p {
    margin: 10px 0;
    font-size: 0.8em;
}

.roadmap-card .content .delivery-time {
    font-style: italic;
    color: #555;
    font-weight: bold;
    font-size: 0.8em;
    text-align: right;
    padding-right: 10px
}

.roadmap-card::before {
    content: '';
    position: absolute;
    left: -40px; /* Adjusted to center the circle */
    top: 50%;
    transform: translateY(-50%);
    width: 20px;
    height: 20px;
    border-radius: 50%;
    border: 5px solid lightgray;
    background: lightgray;
}

.roadmap-card::after {
    content: '';
    position: absolute;
    left: -20px; /* Adjusted to align with the circle */
    top: 50%;
    transform: translateY(-50%);
    width: 19px;
    height: 2px;
    background: lightgray;
    border: 3px solid lightgray;
}

.roadmap-card.wip::before {
    background:rgb(255, 166, 0);
    border: 5px solid rgb(255, 166, 0);
    left: -40px; /* Adjusted to center the circle */
}

.roadmap-card.wip::after {
    background: rgb(255, 166, 0);
    border: 3px solid rgb(255, 166, 0);
}

.roadmap-card.completed::before {
    background: #4CAF50;
    border: 5px solid #4CAF50;
    left: -40px; /* Adjusted to center the circle */
}

.roadmap-card.completed::after {
    background: #4CAF50;
    border: 3px solid #4CAF50;
}

.roadmap-description {
    text-align: center;
    font-style: italic;
    color: #555;
    font-weight: bold;
    font-size: 1em;
    padding-bottom: 20px
}
</style>

<p class="roadmap-description">
This roadmap is subject to change.
</p>


<div class="roadmap-container">
    <div class="roadmap-timeline"></div>
    <div class="roadmap-card">
        <div class="icon" style="background-image: url('./images/bug.png');"></div>
        <div class="content">
            <h3>Visual Debugger</h3>
            <p>Enable users to visually debug their integrations and inspect the contents of the messages</p>
            <div class="delivery-time">2026</div>
        </div>
    </div>
    <div class="roadmap-card">
        <div class="icon" style="background-image: url('./images/citrus.png');"></div>
        <div class="content">
            <h3>Citrus Testing Support</h3>
            <p>Enable users to create and run tests for their integrations.</p>
            <div class="delivery-time">2026</div>
        </div>
    </div>
    <div class="roadmap-card">
        <div class="icon" style="background-image: url('./images/datamapper.png');"></div>
        <div class="content">
            <h3>DataMapper Data Preview</h3>
            <p>Test the results of your mapping configuration easily withing the UI</p>
            <div class="delivery-time">2026</div>
        </div>
    </div>
    <div class="roadmap-card">
        <div class="icon" style="background-image: url('./images/camel-logo.svg');"></div>
        <div class="content">
            <h3>Camel Infra Support</h3>
            <p>Enable users to leverage the Camel Infra features to test their integrations.</p>
            <div class="delivery-time">2026</div>
        </div>
    </div>
    <div class="roadmap-card">
        <div class="icon" style="background-image: url('./images/tracing.svg');"></div>
        <div class="content">
            <h3>Visual Tracing</h3>
            <p>Enable users to trace messages.</p>
            <div class="delivery-time">2026</div>
        </div>
    </div>
    <div class="roadmap-card">
        <div class="icon" style="background-image: url('./images/openapi.svg');"></div>
        <div class="content">
            <h3>OpenAPI support</h3>
            <p>Provide better support for working with OpenAPI in your integrations</p>
            <div class="delivery-time">2025</div>
        </div>
    </div>
    <div class="roadmap-card">
        <div class="icon" style="background-image: url('./images/puzzle.png');"></div>
        <div class="content">
            <h3>Connections</h3>
            <p>Provide an easy way to configure connections (for instance to databases or brokers) via a wizard like functionality</p>
            <div class="delivery-time">2025</div>
        </div>
    </div>
    <div class="roadmap-card wip">
        <div class="icon" style="background-image: url('./images/camel-logo.svg');"></div>
        <div class="content">
            <h3>Custom Kamelet Support</h3>
            <p>Allow users to define their own custom Kamelet catalog.</p>
            <div class="delivery-time">2025</div>
        </div>
    </div>
    <div class="roadmap-card completed">
        <div class="icon" style="background-image: url('./images/datamapper.png');"></div>
        <div class="content">
            <h3>DataMapper JSON Support</h3>
            <p>Add support for JSON mappings</p>
            <div class="delivery-time">Q3 / 2025</div>
        </div>
    </div>
    <div class="roadmap-card completed">
        <div class="icon" style="background-image: url('./images/build.png');"></div>
        <div class="content">
            <h3>Maven support</h3>
            <p>Provide better support for working with Maven based integration projects like CSB or CEQ</p>
            <div class="delivery-time">Q3 / 2025</div>
        </div>
    </div>
    <div class="roadmap-card completed">
        <div class="icon" style="background-image: url('./images/stop.png');"></div>
        <div class="content">
            <h3>Drag & Drop (Final)</h3>
            <p>Enable users to quickly move steps on the canvas with Drag & Drop</p>
            <div class="delivery-time">Q3 / 2025</div>
        </div>
    </div>
    <div class="roadmap-card completed">
        <div class="icon" style="background-image: url('./images/darklightmode.png');"></div>
        <div class="content">
            <h3>Dark & Light Mode Support</h3>
            <p>Enable users to switch between dark and light theme</p>
            <div class="delivery-time">Q2 / 2025</div>
        </div>
    </div>
    <div class="roadmap-card completed">
        <div class="icon" style="background-image: url('./images/vscode.svg');"></div>
        <div class="content">
            <h3>Enhanced Kaoto Extension</h3>
            <p>Create a dedicated Kaoto view which provides a better overview and easier access to needed functionality</p>
            <div class="delivery-time">Q2 / 2025</div>
        </div>
    </div>
    <div class="roadmap-card completed">
        <div class="icon" style="background-image: url('./images/xmlsupport.png');"></div>
        <div class="content">
            <h3>XML IO DSL Support</h3>
            <p>Additionally to YAML DSL we would like to offer users to use the XML IO DSL</p>
            <div class="delivery-time">Q2 / 2025</div>
        </div>
    </div>
    <div class="roadmap-card completed">
        <div class="icon" style="background-image: url('./images/stop.png');"></div>
        <div class="content">
            <h3>Drag & Drop (Tech Preview)</h3>
            <p>Initial support of Drag & Drop in the editor</p>
            <div class="delivery-time">Q1 / 2025</div>
        </div>
    </div>
    <div class="roadmap-card completed">
        <div class="icon" style="background-image: url('./images/datamapper.png');"></div>
        <div class="content">
            <h3>DataMapper (Tech Preview)</h3>
            <p>Initial release of a visual datamapper supporting XML mappings</p>
            <div class="delivery-time">Q4 / 2024</div>
        </div>
    </div>
    <div class="roadmap-card completed">
        <div class="icon" style="background-image: url('./images/camel-logo.svg');"></div>
        <div class="content">
            <h3>Multi Version Support</h3>
            <p>Provide support for multiple Apache Camel versions, both upstream and downstream</p>
            <div class="delivery-time">Q3 / 2024</div>
        </div>
    </div>
    <div class="roadmap-card completed">
        <div class="icon" style="background-image: url('./images/logo-kaoto.png');"></div>
        <div class="content">
            <h3>Kaoto 2.0 Release</h3>
            <p>Release version 2.0 of Kaoto which marks the first big release after switching the focus fully to providing a visual designer for Apache Camel and moving to a new tech stack</p>
            <div class="delivery-time">Q2 / 2024</div>
        </div>
    </div>
</div>
