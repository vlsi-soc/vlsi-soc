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
    <h5 class="ops-t txtcenter wow fadeIn"><br /><br /><b>Conference Theme: "<i>To Be Announced</i>"</b></h5>

    <div class="col-md-12 mt-5">
      <div class="row mt-5">
        <div class="divider-dashed"></div>
        <div class="col-md-6 mt-5" style="text-align:justify">
          <p class="ops-tt"><b>VLSI-SOC 2026 is the 34<sup>th</sup></b> in a series of international conferences sponsored by the International Federation for Information Processing Technical Committee 10 Working Group 5, IEEE CEDA, and IEEE CASS. The conference serves as a global platform for academic and industrial experts to exchange ideas and present groundbreaking research in <b>Very Large Scale Integration</b> (VLSI) and <b>System-on-Chip</b> (SoC) design. Topics span architectures, circuits, devices, design automation, verification, test, and security for digital, analog, and mixed-signal systems.
          <br /><b>Under the theme "To Be Announced,"</b> VLSI-SOC 2026 will explore advanced research areas including heterogeneous, neuromorphic, brain-inspired, biologically-inspired, and approximate computing systems. The conference will foster collaboration and innovation to address the rapidly evolving challenges in the field.</p>
        </div>

        <div class="col-md-6 mt-5" style="text-align:justify">
          <p class="ops-t"><b>VLSI-SOC 2026 will be held in Limassol, Cyprus,</b> a vibrant city known for its rich history, cultural heritage, and picturesque coastal landscapes. Situated along the Mediterranean coast, Limassol seamlessly blends ancient traditions with modern attractions. The city boasts UNESCO World Heritage Sites, including the Kourion archaeological site and Amathus ruins, offering a glimpse into its storied past. Visitors will also enjoy its renowned culinary scene, lively festivals, and pristine beaches.</p>
          <p class="ops-t">Limassol's dynamic urban setting, combined with its status as a leading Mediterranean destination, provides an ideal backdrop for fostering intellectual exchange and professional networking during VLSI-SOC 2026. We look forward to welcoming you to this unforgettable event.</p>
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
