---
layout: page
title: Projects
permalink: /projects/
description: Software, computer vision, and algorithm projects, alongside selected professional work.
nav: true
nav_order: 2
---

<nav class="project-jump-links" aria-label="Browse projects">
  <a href="#earlier-work">Project galleries</a>
  <a href="#project-index">All projects</a>
  <a href="#professional-work">Professional work</a>
</nav>

<section class="portfolio-projects" id="earlier-work" aria-labelledby="earlier-work-title">
  <h2 id="earlier-work-title">Project galleries</h2>
  <p class="section-intro">Explore the original collections, with project images, animations, and implementation details.</p>
  <div class="earlier-work-grid">
    {% assign gallery_projects = site.projects | sort: 'importance' %}
    {% for project in gallery_projects %}
      <article class="earlier-work-card">
        <a href="{{ project.url | relative_url }}">
          {% include gallery_art.liquid project=project %}
          <h3>{{ project.title }}</h3>
        </a>
        <p>{{ project.description }}</p>
      </article>
    {% endfor %}
  </div>
</section>

<section class="home-section portfolio-projects" id="project-index" aria-labelledby="project-index-title">
  <h2 id="project-index-title">All projects</h2>
  <p class="section-intro">The complete repository collection, including the individual projects in the galleries above.</p>
  <ul class="project-index">
    {% assign repositories = site.data.repositories.github_repos | sort %}
    {% for repository in repositories %}
      {% assign name = repository | split: '/' | last | replace: '_', ' ' | replace: '-', ' ' %}
      <li>
        <a href="https://github.com/{{ repository }}">
          {% include repository_thumbnail.liquid repository=repository %}
          <span class="project-index-name">{{ name }}</span>
          <span aria-hidden="true">↗</span>
        </a>
      </li>
    {% endfor %}
  </ul>
</section>

<section class="home-section portfolio-projects" id="professional-work" aria-labelledby="production-work-title">
  <h2 id="production-work-title">Professional work</h2>
  <p class="section-intro">Selected applications, developer tools, and data infrastructure from NBCUniversal and FOX Sports.</p>
  {% include selected_work.liquid detailed=true %}
</section>
