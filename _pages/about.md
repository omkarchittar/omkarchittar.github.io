---
layout: about
title: Home
seo_title: Omkar Chittar | Software Engineer / AI Engineer
permalink: /
description: Software Engineer / AI Engineer building production AI systems. RAG, agents, evaluation, MLOps, and software that connects AI to real workflows.
---

<section class="home-hero" aria-labelledby="hero-title">
  <p class="eyebrow">Omkar Chittar <span aria-hidden="true">/</span> Orlando, FL</p>
  <h1 id="hero-title"><span class="hero-role">Software Engineer / AI Engineer</span>Building production AI systems<span class="accent">.</span></h1>
  <p class="hero-intro">I build RAG applications, agent workflows, and evaluation systems that turn AI capabilities into reliable software.</p>
  <p class="hero-context">From knowledge discovery to workflow automation, my focus is on getting AI into production and keeping it useful.</p>
  <div class="portfolio-actions">
    <a class="portfolio-button primary" href="#selected-work">Explore selected work <span aria-hidden="true">↗</span></a>
    <a class="portfolio-button" href="{{ '/assets/pdf/resume.pdf' | relative_url }}" download>Download resume (PDF)</a>
  </div>
  <ul class="hero-topics" aria-label="Engineering focus">
    <li>RAG</li><li>Agents</li><li>Evaluation</li><li>MLOps</li><li>Full-stack software</li>
  </ul>
</section>

<section class="home-section" id="selected-work" aria-labelledby="selected-work-title">
  <div class="section-heading">
    <div><p class="eyebrow">01 / Applied AI</p><h2 id="selected-work-title">Selected Work</h2></div>
    <a class="text-link" href="{{ '/projects/' | relative_url }}">All work <span aria-hidden="true">↗</span></a>
  </div>
  <p class="section-intro">Full-stack applications and AI systems for estimating, knowledge discovery, and operational support.</p>
  {% include selected_work.liquid %}
</section>

<section class="home-section" id="capabilities" aria-labelledby="capabilities-title">
  <p class="eyebrow">02 / How I build</p>
  <h2 id="capabilities-title">Engineering Capabilities</h2>
  <div class="capability-grid">
    <article><span class="capability-index" aria-hidden="true">01</span><h3>RAG &amp; agents</h3><p>Ingestion, embeddings, vector retrieval, grounded generation, tool calling, and guardrails.</p><p class="capability-tools">LangChain · LangGraph · FAISS · Bedrock</p></article>
    <article><span class="capability-index" aria-hidden="true">02</span><h3>Evaluation &amp; reliability</h3><p>Golden sets, retrieval checks, regression harnesses, and prompt and embedding experiments.</p><p class="capability-tools">Ragas · Retrieval evaluation · Quality regression</p></article>
    <article><span class="capability-index" aria-hidden="true">03</span><h3>MLOps &amp; production</h3><p>Deployment workflows, access controls, logging, monitoring, and serving cost optimization.</p><p class="capability-tools">MLflow · Docker · CI/CD · AWS · GCP</p></article>
    <article><span class="capability-index" aria-hidden="true">04</span><h3>Full-stack software</h3><p>Python backends and React/TypeScript frontends, document-ingestion pipelines, computation engines, and automated testing.</p><p class="capability-tools">Python · React · TypeScript · Flask · REST APIs</p></article>
  </div>
</section>

<section class="home-section" id="experience" aria-labelledby="experience-title">
  <p class="eyebrow">03 / Delivery</p>
  <h2 id="experience-title">Experience &amp; Impact</h2>
  <div class="experience-list">
    <article class="experience-item">
      <p class="experience-date">Nov 2025 — Present</p>
      <div><h3>Lead Software Engineer</h3><p class="experience-company">NBCUniversal · Universal Creative and UDX</p><p>Led delivery of 10 products from concept into production across 6 business functions. Work spans a full-stack estimating platform, contract lifecycle software, retrieval and evaluation infrastructure, and cost intelligence.</p><p class="experience-impact">Estimating and takeoff time reduced from 6 hours to 30 minutes · Approximately 900 automated tests backing the platform.</p></div>
    </article>
    <article class="experience-item">
      <p class="experience-date">Aug 2024 — Nov 2025</p>
      <div><h3>AI Engineer</h3><p class="experience-company">FOX Sports</p><p>Built AI solutions for media post-production: a Slack agent for ML pipeline monitoring, a natural-language-to-SQL assistant, evaluation tooling, and automated metadata extraction.</p><p class="experience-impact">35% less issue-resolution time with the Slack agent · 40% less ad-hoc reporting effort with the conversational assistant.</p></div>
    </article>
  </div>
  <a class="text-link" href="{{ '/cv/' | relative_url }}">View full experience <span aria-hidden="true">↗</span></a>
</section>

<section class="home-section about-section" id="about" aria-labelledby="about-title">
  <div>
    <p class="eyebrow">04 / Background</p>
    <h2 id="about-title">About</h2>
    <p>I'm Omkar, a software engineer focused on making AI useful in real systems. I care about the work around the model: connecting it to the right data, evaluating its behavior, and supporting it in production.</p>
    <p>My earlier work at Sakar Robotics and my Master's in Robotics at the University of Maryland built my foundation in machine learning, perception, and software engineering. Today, I bring that background to production AI applications.</p>
    <p>I also founded Sai Classes and mentor students through FIRST LEGO League.</p>
    <div class="about-links"><a class="text-link" href="{{ '/projects/' | relative_url }}#earlier-work">Earlier work</a><a class="text-link" href="{{ '/teaching/' | relative_url }}">Teaching &amp; mentoring</a></div>
  </div>
  <img class="about-portrait" src="{{ '/assets/img/omkar-chittar.jpg' | relative_url }}" alt="Omkar Chittar" loading="lazy" decoding="async" width="600" height="670">
</section>

<section class="home-section contact-section" id="contact" aria-labelledby="contact-title">
  <p class="eyebrow">05 / Get in touch</p>
  <h2 id="contact-title">Contact</h2>
  <p>Let's talk about useful AI systems and the software that makes them work.</p>
  <a class="contact-email" href="mailto:{{ site.email }}">{{ site.email }}</a>
  <div class="contact-links">
    <a href="https://www.linkedin.com/in/{{ site.linkedin_username }}">LinkedIn <span aria-hidden="true">↗</span></a>
    <a href="https://github.com/{{ site.github_username }}">GitHub <span aria-hidden="true">↗</span></a>
    <a href="{{ '/cv/' | relative_url }}">Resume <span aria-hidden="true">↗</span></a>
  </div>
</section>
