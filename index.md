---
layout: default
title: "VLSI-SoC 2026"
description: "IFIP/IEEE International Conference on Very Large Scale Integration SoC (VLSI-SoC)"
---

{% include hero-carousel.html %}

<!-- QUICK LOGO -->
{% include logo-bar.html %}
<!-- END QUICK LOGO -->

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

<!-- Deadlines Section -->
<div class="bxshadow-top" style="background-color:#F0641B">
  <div class="container" style="padding-top:80px">
    <div class="justify-content-center txtcenter">
      <h3 id="deadlines" class="ops-tt txtcenter" style="color:white;"><b>DEADLINES</b></h3>
      <br />
      <div class="row col-md-12 txt-center">
        <div class="row col-md-12">
          <div class="col-md-6 align-left-mobile wow fadeIn" style="text-align:right;">
            <i class="fa fa-clock inline-mobile" aria-hidden="true" style="display:none;color:white"></i>
            <p class="ops-t c-white inline-mobile"><b>Regular papers & Special sessions</b></p>
          </div>
          <div class="col-md-6" style="text-align:left;border-left: solid 1px white">
            <p class="ops-2t c-gray"><b> Abstract registration: April 28, 2026<br />
                Full paper submission: May 05, 2026
                <br /> Special session proposal: April 27, 2026
                <br /> Notification of acceptance: June 16, 2026
                <br /> Camera ready: July 07, 2026</b></p>
          </div>
        </div>
      </div>
      <br /><br />
      <div class="row col-md-12 txt-center">
        <div class="row col-md-12">
          <div class="col-md-6 align-left-mobile wow fadeIn" style="text-align:right;">
            <i class="fa fa-clock inline-mobile" aria-hidden="true" style="display:none;color:white"></i>
            <p class="ops-t c-white inline-mobile">PhD Contributions</p>
          </div>
          <div class="col-md-6" style="text-align:left;border-left: solid 1px white">
            <p class="ops-2t c-gray"><b> PhD &amp; Student Forum submission:: July 02, 2026
                <br /> Notification of acceptance: July 23, 2026
                <br /> Camera ready: July 23, 2026</b></p>
          </div>
        </div>
        <br /><br />
      </div>
    </div>
    <br />
    <br />
  </div>
</div>

<!-- News Section -->
<div class="bxshadow-top">
  <div class="container" style="padding-top:80px">
    <div class="justify-content-center txtcenter">
      <h3 id="news" class="ops-tt txtcenter c-azure">NEWS</h3>
      <br />
      <div class="row col-md-12 txt-center">
        <div class="row col-md-12">
          <div class="col-md-6 align-left-mobile wow fadeIn" style="text-align:right;">
            <i class="fa fa-newspaper inline-mobile" aria-hidden="true" style="display:none;color:#5A8FDC"></i>
            <p class="ops-t c-azure inline-mobile">Latest Updates</p>
          </div>
          <div class="col-md-6" style="text-align:left;border-left: solid 1px #5A8FDC">
            <p class="ops-2t">
              <b>Website is live!</b><br />
              Stay tuned for more updates.
            </p>
          </div>
        </div>
      </div>
      <br /><br />
    </div>
    <br />
  </div>
</div>

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
