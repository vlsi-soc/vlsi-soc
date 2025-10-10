---
layout: default
title: "Committee"
description: "Organizing, Program, and Steering Committees for VLSI-SoC 2026"
---

{% include hero-carousel.html %}

<!-- QUICK LOGO -->
{% include logo-bar.html %}
<!-- END QUICK LOGO -->

<!-- ORGANIZING COMMITTEE SECTION -->
<div class="container" id="orgcomit">
  <div class="bxshadow-top">
    <div class="container" style="padding-top:80px">
      {% include organizing_committee.html dark_bg=false %}
    </div>
  </div>

  <!-- PROGRAM COMMITTEE SECTION -->
  <div class="bxshadow-top" style="background-color:#292C33" id="progcomit">
    <div class="container" style="padding-top:80px">
      <div class="justify-content-center txtcenter">
        <h3 id="committee" class="ops-tt" style="color:#F8CF5F;">PROGRAM COMMITTEE</h3>
        <br />
      </div>
      <div>
        {% for track in site.data.program_committee.tracks %}
        {% assign topic = site.data.topics.tracks | where: "number", track.number | first %}
        {% assign track_title = topic.title | default: track.name %}
        <br />
        <div class="offset-md-3">
          <p class="ops-t c-white inline-mobile"><b>Track {{ track.number }}: {{ track_title }}</b></p>
        </div>
        <ul style="color:white;text-align:left;margin-left:30%">
          {% for chair in track.chairs %}
          <li>
            <p class="ops-t c-white"><u>{{ chair.name }}</u>, {{ chair.affiliation }} <i>(Track Chair)</i></p>
          </li>
          {% endfor %}
          {% for member in track.members %}
          <li>
            <p class="ops-t c-white">{{ member.name }}, {{ member.affiliation }}</p>
          </li>
          {% endfor %}
        </ul>
        <br />
        {% endfor %}
      </div>
    </div>
  </div>

  <!-- STEERING COMMITTEE SECTION -->
  <div class="bxshadow-top">
    <div class="container" style="padding-top:80px">
      <div class="justify-content-center txtcenter" id="stcomit">
        <h3 id="committee" class="ops-tt txtcenter c-azure">STEERING COMMITTEE</h3>
        <br />
        <div class="row col-md-12">
          <div class="col-md-6 align-left-mobile wow fadeIn" style="text-align:right;">
            <i class="fa fa-user inline-mobile" aria-hidden="true" style="display:none;color: #5A8FDC"></i>
            <p class="ops-t c-azure inline-mobile">STEERING COMMITTEE</p>
          </div>
          <div class="col-md-6 wow fadeIn" style="text-align:left;border-left: solid 1px  #5A8FDC">
            <p class="ops-2t">
              {% for member in site.data.steering_committee.members %}
                {{ member.name }}{% if member.role %} ({{ member.role }}){% endif %}, {{ member.affiliation }}
                {% unless forloop.last %}<br />{% endunless %}
              {% endfor %}
            </p>
            <br />
          </div>
          <br />
          <br /><br />
        </div>
        <br />
        <br />
      </div>
    </div>
  </div>
</div>
