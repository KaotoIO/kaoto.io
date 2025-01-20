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

.roadmap-card.completed::before {
    background: #4CAF50;
    border: 5px solid #4CAF50;
    left: -40px; /* Adjusted to center the circle */
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
        <div class="icon" style="background-image: url('./bug.png');"></div>
        <div class="content">
            <h3>Visual Debugger</h3>
            <p>Enable users to visually debug their integrations and inspect the contents of the messages</p>
            <div class="delivery-time">2025</div>
        </div>
    </div>
    <div class="roadmap-card">
        <div class="icon" style="background-image: url('./datamapper.png');"></div>
        <div class="content">
            <h3>DataMapper JSON Support</h3>
            <p>Add support for JSON mappings</p>
            <div class="delivery-time">2025</div>
        </div>
    </div>
    <div class="roadmap-card">
        <div class="icon" style="background-image: url('./puzzle.png');"></div>
        <div class="content">
            <h3>Connections Wizard</h3>
            <p>Provide an easy way to configure connections (for instance to databases or brokers) via a wizard like functionality</p>
            <div class="delivery-time">2025</div>
        </div>
    </div>
    <div class="roadmap-card">
        <div class="icon" style="background-image: url('./build.png');"></div>
        <div class="content">
            <h3>Maven support</h3>
            <p>Provide better support for working with Maven based integration projects like CSB or CEQ</p>
            <div class="delivery-time">2025</div>
        </div>
    </div>
    <div class="roadmap-card">
        <div class="icon" style="background-image: url('./openapi.svg');"></div>
        <div class="content">
            <h3>OpenAPI support</h3>
            <p>Provide better support for working with OpenAPI in your integrations</p>
            <div class="delivery-time">2025</div>
        </div>
    </div>
    <div class="roadmap-card">
        <div class="icon" style="background-image: url('./vscode.svg');"></div>
        <div class="content">
            <h3>Enhanced Kaoto Extension</h3>
            <p>Create a dedicated Kaoto view which provides a better overview and easier access to needed functionality</p>
            <div class="delivery-time">Q1 / 2025</div>
        </div>
    </div>
    <div class="roadmap-card">
        <div class="icon" style="background-image: url('./xmlsupport.png');"></div>
        <div class="content">
            <h3>XML IO DSL Support</h3>
            <p>Additionally to YAML DSL we would like to offer users to use the XML IO DSL</p>
            <div class="delivery-time">Q1 / 2025</div>
        </div>
    </div>
    <div class="roadmap-card">
        <div class="icon" style="background-image: url('./stop.png');"></div>
        <div class="content">
            <h3>Drag & Drop Support</h3>
            <p>Enable users to quickly move steps on the canvas with Drag & Drop</p>
            <div class="delivery-time">Q1 / 2025</div>
        </div>
    </div>
    <div class="roadmap-card completed">
        <div class="icon" style="background-image: url('./datamapper.png');"></div>
        <div class="content">
            <h3>DataMapper (Tech Preview)</h3>
            <p>Initial release of a visual datamapper supporting XML mappings</p>
            <div class="delivery-time">Q4 / 2024</div>
        </div>
    </div>
    <div class="roadmap-card completed">
        <div class="icon" style="background-image: url('./camel-logo.svg');"></div>
        <div class="content">
            <h3>Multi Version Support</h3>
            <p>Provide support for multiple Apache Camel versions, both upstream and downstream</p>
            <div class="delivery-time">Q3 / 2024</div>
        </div>
    </div>
    <div class="roadmap-card completed">
        <div class="icon" style="background-image: url('./logo-kaoto.png');"></div>
        <div class="content">
            <h3>Kaoto 2.0 Release</h3>
            <p>Release version 2.0 of Kaoto which marks the first big release after switching the focus fully to providing a visual designer for Apache Camel and moving to a new tech stack</p>
            <div class="delivery-time">Q2 / 2024</div>
        </div>
    </div>
</div>
