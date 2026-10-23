---
layout: about
title: Home
seo_title: Omkar Chittar | Software Engineer
permalink: /
description: Software engineer building full-stack applications, reliable services, developer tools, and production data pipelines.
point_cloud: true
---

{% assign estimating = site.data.selected_work | where: 'id', 'estimating-platform' | first %}
{% assign debugging = site.data.selected_work | where: 'id', 'ci-debugging' | first %}
{% assign media = site.data.selected_work | where: 'id', 'media-pipelines' | first %}
{% assign legal = site.data.selected_work | where: 'id', 'knowledge-discovery' | first %}
{% assign monitoring = site.data.selected_work | where: 'id', 'operational-agents' | first %}

<section class="ed-hero">
  <div class="hero-meta"><span>SOFTWARE ENGINEER</span><span>SUNNYVALE, CALIFORNIA</span></div>
  <h1>
    I make ideas<br>
    <span class="second-line">work in the <em>real world.</em></span>
  </h1>
  <div class="ed-hero-bottom">
    <div class="ed-hero-intro">
      <p>
        I turn complex problems into useful software. From the first sketch to the production system,
        I build for the people on the other side.
      </p>
      <a class="hero-work-link" href="#selected-work">Explore my work <span aria-hidden="true">↓</span></a>
    </div>
    <div class="ed-cloud">
      <div class="ed-cloud-meta"><span>ALWAYS CONNECTING DOTS</span><button id="cloud-pause" type="button">Pause motion</button></div>
      <div class="ed-cloud-stage">
        <canvas
          id="point-cloud"
          width="700"
          height="480"
          role="img"
          aria-label="Terracotta point cloud forming an intricate three-dimensional mathematical knot. Use the reconstruction slider below to move between scattered points and a clear shape."
        ></canvas>
        <div class="ed-static-orbit" aria-hidden="true">◎</div>
        <span class="ed-cloud-axis" aria-hidden="true"
          >Y ↑<br>
          └── X</span
        >
      </div>
      <div class="ed-cloud-controls">
        <div><label for="reconstruction">A little order from the noise.</label><output id="cloud-value" for="reconstruction">100%</output></div>
        <input type="range" id="reconstruction" min="0" max="100" value="100">
        <p>Drag to explore · A study in creative coding</p>
      </div>
    </div>
  </div>
  <div class="ed-proof">
    <span>RECENTLY BUILDING AT</span><strong>NBCUniversal</strong><span class="proof-divider">/</span><strong>FOX Sports</strong
    ><span class="proof-end">Thoughtful systems. Useful software.</span>
  </div>
</section>
<section class="ed-work" id="selected-work">
  <div class="section-top">
    <p class="eyebrow">01 / SELECTED WORK</p>
    <p>A few things I've helped bring into the world.</p>
  </div>
  <article class="ed-feature">
    <div class="ed-project-copy">
      <span class="project-number">01—</span>
      <p class="eyebrow">{{ estimating.context }} / FULL-STACK ENGINEERING</p>
      <h2>
        Six hours.<br>
        Thirty minutes.<br>
        <em>Time back.</em>
      </h2>
      <p>{{ estimating.summary }}</p>
      <div class="ed-project-stat"><strong>6h → 30m</strong><span>Estimating & takeoff time</span></div>
      <a class="text-link" href="{{ '/projects/' | relative_url }}#estimating-platform">Explore the project <span aria-hidden="true">↗</span></a>
    </div>
    {% include project_art.liquid project=estimating.id %}
  </article>
  <div class="ed-secondary">
    <article>
      {% include project_art.liquid project=debugging.id %}
      <p class="eyebrow">{{ debugging.context }} / DEVELOPER TOOLS</p>
      <h3>From a failed build to a next step.</h3>
      <p>{{ debugging.summary }}</p>
      <a class="text-link" href="{{ '/projects/' | relative_url }}#ci-debugging">Explore the CI debugging agent ↗</a>
    </article>
    <article>
      {% include project_art.liquid project=media.id %}
      <p class="eyebrow">{{ media.context }} / DATA PIPELINES</p>
      <h3>Media, made searchable.</h3>
      <p>{{ media.summary }}</p>
      <a class="text-link" href="{{ '/projects/' | relative_url }}#media-pipelines">Explore the media pipelines ↗</a>
    </article>
    <article>
      {% include project_art.liquid project=legal.id %}
      <p class="eyebrow">{{ legal.context }} / SEARCH & DATA INFRASTRUCTURE</p>
      <h3>Answers with a paper trail.</h3>
      <p>{{ legal.summary }}</p>
      <a class="text-link" href="{{ '/projects/' | relative_url }}#knowledge-discovery">Explore legal retrieval ↗</a>
    </article>
    <article>
      {% include project_art.liquid project=monitoring.id %}
      <p class="eyebrow">{{ monitoring.context }} / EVENT-DRIVEN SYSTEMS</p>
      <h3>Less noise. Faster resolution.</h3>
      <p>{{ monitoring.summary }} {{ monitoring.details | last }}</p>
      <a class="text-link" href="{{ '/projects/' | relative_url }}#operational-agents">Explore operational monitoring ↗</a>
    </article>
  </div>
  <a class="all-work" href="{{ '/projects/' | relative_url }}">Browse all projects <span aria-hidden="true">↗</span></a>
</section>
<section class="ed-about" id="about">
  <div class="ed-person">
    <p class="eyebrow">02 / THE PERSON BEHIND THE SYSTEMS</p>
    <figure class="ed-portrait">
      <img
        src="{{ '/assets/img/omkar-chittar.jpg' | relative_url }}"
        width="600"
        height="670"
        alt="Portrait of Omkar Chittar"
        loading="lazy"
        decoding="async"
      >
      <figcaption>
        OMKAR CHITTAR<br>
        <span>Software engineer</span>
      </figcaption>
    </figure>
  </div>
  <div>
    <h2>
      Curiosity is the<br>
      <em>through line.</em>
    </h2>
    <p>
      I build full-stack software: the interfaces people use, the services behind them, and the data flows that connect everything. My work at
      NBCUniversal and FOX Sports spans estimating platforms, search infrastructure, and operational tools.
    </p>
    <p>
      I care about how the pieces fit together: clear interfaces, automated testing, thoughtful architecture, and software that holds up beyond the
      demo.
    </p>
    <a class="text-link" href="{{ '/teaching/' | relative_url }}">Teaching & mentoring ↗</a>
  </div>
  <aside>
    <span>MY TOOLBOX</span>
    <p>
      Python & TypeScript<br>
      APIs & integrations<br>
      Testing & deployment<br>
      Search & data pipelines
    </p>
    <a href="{{ '/publications/' | relative_url }}">Research & publications ↗</a>
  </aside>
</section>
<section class="ed-contact" id="contact">
  <p class="eyebrow">03 / WHAT COULD WE BUILD?</p>
  <h2>
    Good things start<br>
    with <em>a conversation.</em>
  </h2>
  <a href="mailto:{{ site.email }}">Say hello <span aria-hidden="true">↗</span></a>
</section>
