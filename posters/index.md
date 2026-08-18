---
layout: default
title: Posters
permalink: /posters/
---

# Posters

<div class="poster-list">

{% assign posters = site.posters | sort: "name" %}

{% for poster in posters %}
  <article class="poster-list-item">
    <h3>
      <a href="{{ poster.url | relative_url }}">
        {{ poster.name }}
      </a>
    </h3>

    {% if poster.authors %}
      <div class="poster-list-authors">
        {{ poster.authors | join: ", " }}
      </div>
    {% endif %}
  </article>
{% endfor %}

</div>
