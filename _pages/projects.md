---
layout: page
title: Projects
permalink: /projects/
description: Selected production AI work, with earlier projects in robotics and computer vision.
nav: true
nav_order: 2
---

<section class="portfolio-projects" aria-labelledby="production-work-title">
  <h2 id="production-work-title">Selected Work</h2>
  <p class="section-intro">Highlights from my work at NBCUniversal and FOX Sports.</p>
  {% include selected_work.liquid detailed=true %}
</section>

<section class="home-section portfolio-projects" id="earlier-work" aria-labelledby="earlier-work-title">
  <p class="eyebrow">Foundations in perception &amp; autonomy</p>
  <h2 id="earlier-work-title">Earlier Work</h2>
  <p class="section-intro">Robotics and computer vision projects that shaped my approach to machine learning and engineering.</p>
  <div class="earlier-work-grid">
    {% assign earlier_projects = site.projects | where: 'category', 'earlier-work' | sort: 'importance' %}
    {% for project in earlier_projects %}
      <article class="earlier-work-card">
        <a href="{{ project.url | relative_url }}">
          <img src="{{ project.img | relative_url }}" alt="" loading="lazy" width="480" height="270">
          <h3>{{ project.title }}</h3>
        </a>
        <p>{{ project.description }}</p>
      </article>
    {% endfor %}
  </div>
  <a class="text-link" href="{{ '/repositories/' | relative_url }}">Browse earlier repositories <span aria-hidden="true">↗</span></a>
</section>
