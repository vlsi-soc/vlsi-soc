---
layout: default
title: "VLSI-SoC 2026"
description: "IFIP/IEEE International Conference on Very Large Scale Integration SoC (VLSI-SoC)"
---

{% include hero-carousel.html %}

<!-- QUICK LOGO -->
{% include logo-bar.html %}
<!-- END QUICK LOGO -->

<!-- CONFERENCE THEME & DESCRIPTION -->
<div class="container">
  <div class="justify-content-center">
  {% assign home_intro = site.data.home_intro %}
  <h5 class="ops-t txtcenter wow fadeIn"><br /><br /><b>{{ home_intro.theme.label }}: "<i>{{ home_intro.theme.title }}</i>"</b></h5>

    <div class="row">
      <embed src="{{ '/docs/VLSI-SoC-2026-Presentation.pdf' | relative_url }}" type="application/pdf" width="100%" height="800px">
    </div>
    <div class="col-md-12 mt-5">
      <div class="row mt-5">
        <div class="divider-dashed"></div>
        <div class="col-md-6 mt-5" style="text-align:justify">
          {% for paragraph in home_intro.intro_columns.left.paragraphs %}
            <p class="{{ paragraph.class }}">
              {{ paragraph.content 
                | replace: '__EDITION__', site.data.conference.edition 
                | replace: '__YEAR__', site.data.conference.year }}
            </p>
          {% endfor %}
        </div>

        <div class="col-md-6 mt-5" style="text-align:justify">
          {% for paragraph in home_intro.intro_columns.right.paragraphs %}
          <p class="{{ paragraph.class }}">{{ paragraph.content }}</p>
          {% endfor %}
        </div>
      </div>
    </div>
  </div>
</div>

{% include topics.html %}

<!-- MAIN CONTENT - Organizing Committee Section -->
<div class="bxshadow-top" style="background-color:#292C33">
  <div class="container" style="padding-top:80px" id="orgcomit">
    {% include organizing_committee.html dark_bg=true title="ORGANIZATION COMMITTEE" %}
  </div>
</div>

<!-- Steering Committee Section -->
<div class="bxshadow-top" style="background-color:#292C33">
  <div class="container" style="padding-top:80px" id="stcomit">
    <div class="justify-content-center txtcenter">
      <h3 class="ops-tt txtcenter" style="color:#F8CF5F;">STEERING COMMITTEE</h3>
      <br />
      <div class="row col-md-12">
        <div class="col-md-6 align-left-mobile wow fadeIn" style="text-align:right;">
          <i class="fa fa-user inline-mobile" aria-hidden="true" style="display:none;color:white"></i>
          <p class="ops-t c-white inline-mobile">STEERING COMMITTEE</p>
        </div>
        <div class="col-md-6 wow fadeIn" style="text-align:left;border-left: solid 1px white">
          <p class="ops-2t c-gray">
            {% for member in site.data.steering_committee.members %}
              {{ member.name }}{% if member.role %} ({{ member.role }}){% endif %}, {{ member.affiliation }}
              {% unless forloop.last %}<br />{% endunless %}
            {% endfor %}
          </p>
        </div>
      </div>
      <br /><br />
    </div>
  </div>
</div>

{% include deadlines.html %}

{% include news.html %}

<!-- About Conference Section -->
<div class="bxshadow-top" style="background-color:#292C33">
  <div class="container" style="padding-top:80px">
    <div class="justify-content-center txtcenter">
      <h3 id="about" class="ops-tt txtcenter" style="color:#F8CF5F;">ABOUT THE CONFERENCE</h3>
      <br />
      <div class="row col-md-12">
        <div class="col-md-12 wow fadeIn">
          <p class="ops-2t c-gray" style="text-align:justify;">
            The IFIP/IEEE International Conference on Very Large Scale Integration (VLSI-SoC) is a well-established 
            international forum to present and discuss the latest research and developments in all aspects of VLSI 
            and SoC design. The conference provides a platform for researchers and practitioners from academia and 
            industry to exchange ideas and share their experiences in all aspects of VLSI and SoC design.
          </p>
        </div>
      </div>
      <br /><br />
    </div>
    <br />
  </div>
</div>
