---
layout: default
title: Posters
permalink: /posters/
---

# Posters

<div class="poster-group">
  <div class="poster-group-title">Posters</div>

  {% assign posters = site.posters | sort: "number" %}

  {% for poster in posters %}
    <article class="poster-item">
      <div class="poster-number">
        {{ poster.number }}
      </div>

      <div class="poster-list-content">
          <a class="poster-title" href="{{ poster.url | relative_url }}">
            {{ poster.name }}
          </a>
    
          {% if poster.authors %}
            <div class="poster-authors">
              {{ poster.authors | join: ", " }}
            </div>
          {% endif %}
      </div>

    </article>
  {% endfor %}
</div>
