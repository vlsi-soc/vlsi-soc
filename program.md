---
layout: default
title: "Program"
description: "Conference program, keynotes, and schedule for VLSI-SoC 2026"
---

{% include hero-carousel.html %}

<!-- QUICK LOGO -->
{% include logo-bar.html %}
<!-- END QUICK LOGO -->

<!-- MAIN CONTENT -->
<div class="container" id="key">
   <div class="justify-content-center txtcenter">
      {% include keynotes.html %}
   </div>

   <div class="justify-content-center" id="tec">
      <h2 class="ops-tt txtcenter mts-10">TECHNICAL PROGRAM</h2>
      <br />
      <p class="ops-t txtcenter same-line">Below is the detailed schedule for the VLSI-SoC 2026 Conference Program.</p>
      <br />

<style>
#tec-schedule { font-size: 13px; color: #111; }
#tec-schedule .tp-legend { display:flex; flex-wrap:wrap; gap:8px 20px; margin-bottom:22px; font-size:11.5px; color:#222; }
#tec-schedule .tp-leg { display:flex; align-items:center; gap:6px; }
#tec-schedule .tp-leg-bar { width:12px; height:12px; border-radius:2px; flex-shrink:0; }
#tec-schedule .tp-day {
  display:block; background:#1a2a4a; color:#fff; font-size:13px; font-weight:700;
  padding:6px 14px; border-radius:3px; margin:28px 0 8px; letter-spacing:.3px;
}
#tec-schedule table.tp-sched { width:100%; border-collapse:collapse; margin-bottom:8px; }
#tec-schedule table.tp-sched td { border:1px solid #bbb; padding:7px 10px; vertical-align:top; line-height:1.45; color:#111; }
#tec-schedule .tp-ca { width:5px; padding:0 !important; border-right:none !important; }
#tec-schedule .tp-ct { width:108px; white-space:nowrap; font-weight:700; font-size:12px;
  color:#111; background:#f0f2f5; text-align:center; vertical-align:middle; border-left:none !important; }
#tec-schedule .tp-ch { width:50%; }
#tec-schedule .ra  td{background:#f5f5f5;}           #tec-schedule .ra  .tp-ca{background:#888;}    #tec-schedule .ra  .tp-ct{background:#e8e8e8;}
#tec-schedule .rk  td{background:#deeeff;}           #tec-schedule .rk  .tp-ca{background:#1155cc;} #tec-schedule .rk  .tp-ct{background:#c5dcf7;}
#tec-schedule .rik td{background:#e8e0ff;}           #tec-schedule .rik .tp-ca{background:#5b21b6;} #tec-schedule .rik .tp-ct{background:#d4c9f7;}
#tec-schedule .rp  td{background:#d4f0e2;}           #tec-schedule .rp  .tp-ca{background:#166534;} #tec-schedule .rp  .tp-ct{background:#bbdfcc;}
#tec-schedule .rb  td{background:#f0f0f0;color:#444;}#tec-schedule .rb  .tp-ca{background:#aaa;}    #tec-schedule .rb  .tp-ct{background:#e4e4e4;color:#444;}
#tec-schedule .rpd td{background:#f3ecfd;}           #tec-schedule .rpd .tp-ca{background:#7c3aed;} #tec-schedule .rpd .tp-ct{background:#dccef7;}
#tec-schedule .rs  td{background:#fff3cd;}           #tec-schedule .rs  .tp-ca{background:#b45309;} #tec-schedule .rs  .tp-ct{background:#ffe9a0;}
#tec-schedule .rr  td{background:#ffe8e2;}           #tec-schedule .rr  .tp-ca{background:#b91c1c;} #tec-schedule .rr  .tp-ct{background:#fdd0c8;}
#tec-schedule .rc  td{background:#e8f0fb;}           #tec-schedule .rc  .tp-ca{background:#1a2a4a;} #tec-schedule .rc  .tp-ct{background:#d0dcee;}
#tec-schedule .rrec td{background:#d4f0e2;}          #tec-schedule .rrec .tp-ca{background:#166534;}#tec-schedule .rrec .tp-ct{background:#bbdfcc;}
#tec-schedule .rsoc td{background:#e8f7ef;}          #tec-schedule .rsoc .tp-ca{background:#0d6e3f;}#tec-schedule .rsoc .tp-ct{background:#b5ddc8;}
#tec-schedule .tp-t { font-weight:700; font-size:12.5px; color:#111; display:block; }
#tec-schedule .tp-s { font-size:11px; color:#333; margin-top:2px; display:block; }
#tec-schedule ul.tp-pp { margin-top:6px; padding-top:5px; border-top:1px solid rgba(0,0,0,.12); list-style:none; padding-left:0; }
#tec-schedule ul.tp-pp li { font-size:11px; color:#222; padding:2px 0 2px 18px; position:relative; }
#tec-schedule ul.tp-pp li::before { content:"#"; position:absolute; left:0; color:#777; font-size:10px; top:3px; }
#tec-schedule ul.tp-pp li b { color:#111; font-weight:700; }
#tec-schedule ul.tp-pp li.tp-po { color:#3b0764; font-style:italic; }
#tec-schedule ul.tp-pp li.tp-po::before { content:"⸎"; color:#7c3aed; top:2px; font-style:normal; }
#tec-schedule ul.tp-pp li.tp-inv { color:#7c2d12; font-style:italic; }
#tec-schedule ul.tp-pp li.tp-inv::before { content:"◆"; color:#b45309; top:2px; font-style:normal; }
#tec-schedule .tp-pdiv { border:none; border-top:1px dashed #c084fc; margin:5px 0 3px; }
#tec-schedule .tp-plbl { font-size:10px; color:#6b21a8; font-weight:700; display:block; margin-bottom:2px; }
#tec-schedule .tp-ttag { display:inline-block; font-size:9.5px; font-weight:700; background:#1a2a4a;
  color:#fff; border-radius:2px; padding:0 4px; margin-right:3px; vertical-align:middle; font-style:normal; }
#tec-schedule .tp-bpc { display:inline-block; font-size:9px; font-weight:700; background:#b8860b;
  color:#fff; border-radius:2px; padding:0 5px; margin-left:5px; vertical-align:middle; letter-spacing:.3px; }
#tec-schedule .tp-auth { font-size:10px; color:#555; display:block; margin-top:1px; font-style:italic; }
</style>

<div id="tec-schedule">

<div class="tp-legend">
  <span class="tp-leg"><span class="tp-leg-bar" style="background:#1155cc"></span>Academic keynote</span>
  <span class="tp-leg"><span class="tp-leg-bar" style="background:#5b21b6"></span>Industrial keynote</span>
  <span class="tp-leg"><span class="tp-leg-bar" style="background:#166534"></span>Panel / reception</span>
  <span class="tp-leg"><span class="tp-leg-bar" style="background:#7c3aed"></span>Poster display</span>
  <span class="tp-leg"><span class="tp-leg-bar" style="background:#b45309"></span>Special session</span>
  <span class="tp-leg"><span class="tp-leg-bar" style="background:#b91c1c"></span>Regular session</span>
  <span class="tp-leg"><span class="tp-leg-bar" style="background:#0d6e3f"></span>Social event</span>
  <span class="tp-leg"><span class="tp-leg-bar" style="background:#aaa"></span>Break / admin</span>
  <span class="tp-leg"><span class="tp-bpc" style="font-size:10px;padding:1px 6px;">BPC</span>&nbsp;Best Paper Candidate</span>
</div>

<!-- SUNDAY -->
<span class="tp-day">Sunday, 11 October 2026 – Tutorials Day</span>
<table class="tp-sched">
  <tr class="ra"><td class="tp-ca"></td><td class="tp-ct">08:00–09:00</td><td><span class="tp-t">Registration</span></td></tr>
  <tr class="rk"><td class="tp-ca"></td><td class="tp-ct">09:00–10:20</td>
    <td class="tp-ch"><span class="tp-t">Tutorial 1</span><span class="tp-s">80 min · TBA</span></td>
    <td class="tp-ch"><span class="tp-t">Tutorial 2</span><span class="tp-s">80 min · TBA</span></td>
  </tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">10:20–10:40</td><td><span class="tp-t">Coffee Break</span><span class="tp-s">20 min</span></td></tr>
  <tr class="rk"><td class="tp-ca"></td><td class="tp-ct">10:40–12:00</td>
    <td class="tp-ch"><span class="tp-t">Tutorial 1 (cont.)</span><span class="tp-s">80 min · TBA</span></td>
    <td class="tp-ch"><span class="tp-t">Tutorial 2 (cont.)</span><span class="tp-s">80 min · TBA</span></td>
  </tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">12:00–13:00</td><td><span class="tp-t">Lunch Break</span><span class="tp-s">60 min</span></td></tr>
  <tr class="rk"><td class="tp-ca"></td><td class="tp-ct">13:00–14:20</td>
    <td class="tp-ch"><span class="tp-t">Tutorial 3</span><span class="tp-s">80 min · TBA</span></td>
    <td class="tp-ch"><span class="tp-t">Tutorial 4</span><span class="tp-s">80 min · TBA</span></td>
  </tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">14:20–14:40</td><td><span class="tp-t">Coffee Break</span><span class="tp-s">20 min</span></td></tr>
  <tr class="rk"><td class="tp-ca"></td><td class="tp-ct">14:40–16:00</td>
    <td class="tp-ch"><span class="tp-t">Tutorial 3 (cont.)</span><span class="tp-s">80 min · TBA</span></td>
    <td class="tp-ch"><span class="tp-t">Tutorial 4 (cont.)</span><span class="tp-s">80 min · TBA</span></td>
  </tr>
  <tr class="rp"><td class="tp-ca"></td><td class="tp-ct">16:30–</td><td>
    <span class="tp-t">IFIP WG10.5 Working Group Meeting</span>
    <span class="tp-s">Closed session · Duration TBA</span>
  </td></tr>
</table>

<!-- MONDAY -->
<span class="tp-day">Monday, 12 October 2026 – Conference Day 1</span>
<table class="tp-sched">
  <tr class="ra"><td class="tp-ca"></td><td class="tp-ct">08:00–08:30</td><td><span class="tp-t">Registration</span></td></tr>
  <tr class="ra"><td class="tp-ca"></td><td class="tp-ct">08:30–09:00</td><td><span class="tp-t">Welcome Ceremony</span></td></tr>
  <tr class="rk"><td class="tp-ca"></td><td class="tp-ct">09:00–10:00</td><td>
    <span class="tp-t">Academic Keynote 1 – Sustainable and Secure Computing: the Last Frontier</span>
    <span class="tp-s">Prof. Giovanni De Micheli · EPFL, Switzerland · Plenary · 60 min</span>
  </td></tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">10:00–10:20</td><td><span class="tp-t">Coffee Break + PhD &amp; Student Forum</span><span class="tp-s">20 min</span></td></tr>
  <tr class="rr"><td class="tp-ca"></td><td class="tp-ct">10:20–11:50</td>
    <td class="tp-ch">
      <span class="tp-t">RS1 – AI/ML Hardware Architectures I</span>
      <span class="tp-s">Track 1 · 4 papers + 2 poster presentations · 90 min</span>
      <ul class="tp-pp">
        <li><b>141</b> CIM-Blocks: A Synthesizable Multi-Precision Compute-in-Memory CGRA with Bit-Serial Data Reuse</li>
        <li><b>18</b> At-the-Roofline Sparse Tensor Contractions on Vector Processors for Transformer Inference</li>
        <li><b>24</b> Optimizing ML Workload Partitioning between CPUs and CIM Accelerators for Heterogeneous Computing</li>
        <li><b>71</b> Hardware-Aware Vision Transformer Deployment on a Convolution-Centric AI SoC</li>
        <hr class="tp-pdiv"><span class="tp-plbl">Poster presentations</span>
        <li class="tp-po"><span class="tp-ttag">T1</span><b>53</b> S4oP: Operator-level Pruning of Structured State Space Models for Resource-Constrained Devices</li>
        <li class="tp-po"><span class="tp-ttag">T2</span><b>34</b> Physically-Aware Preemptive Virtual Channels for Deadlock-Free AXI Networks-on-Chip</li>
      </ul>
    </td>
    <td class="tp-ch">
      <span class="tp-t">RS6 – System Verification, Test &amp; Dependability</span>
      <span class="tp-s">Tracks 11+12 · 4 papers + 1 poster presentation · 85 min</span>
      <ul class="tp-pp">
        <li><b>86</b> Hardware Support for Statistical Methods Applied to Hardware-Software Verification and Debugging</li>
        <li><b>94</b> Counterfactual Exploit Validation on CHERI-enabled RISC-V Using Virtual Prototypes <span class="tp-bpc">BPC</span></li>
        <li><b>65</b> RISCar: RISC-V In a Simulated Car for DNN Training and Deployment in AD Systems</li>
        <li><b>76</b> Energy-Aware Fast and Accurate Design Space Exploration of Near-Memory Computing</li>
        <hr class="tp-pdiv"><span class="tp-plbl">Poster presentation</span>
        <li class="tp-po"><span class="tp-ttag">T11</span><b>31</b> AI-based Automated HDL Validation Using Abstract Syntax Tree and Signal Trace Analysis</li>
      </ul>
    </td>
  </tr>
  <tr class="rik"><td class="tp-ca"></td><td class="tp-ct">11:50–12:30</td><td>
    <span class="tp-t">Industrial Keynote 1 – What is the IP Reuse Trap for Digital Hardware, and How Can It Be Escaped?</span>
    <span class="tp-s">Prof. Wolfgang Ecker · Infineon / TU Munich, Germany · Plenary · 40 min</span>
  </td></tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">12:30–13:30</td><td><span class="tp-t">Lunch Break</span><span class="tp-s">60 min</span></td></tr>
  <tr class="rr"><td class="tp-ca"></td><td class="tp-ct">13:30–15:00</td>
    <td class="tp-ch">
      <span class="tp-t">RS3 – Digital Design &amp; EDA I</span>
      <span class="tp-s">Track 4 · Synthesis &amp; Optimization · 4 papers + 2 poster presentations · 90 min</span>
      <ul class="tp-pp">
        <li><b>149</b> Automated RTL Complexity Estimation with Synthesis-Validated Optimization and Programmatic Code Transformation <span class="tp-bpc">BPC</span></li>
        <li><b>90</b> SPFD-Based Resynthesis for Dual-Output LUT Networks <span class="tp-bpc">BPC</span></li>
        <li><b>110</b> No Tree Required: Predicting Post-CTS Clock Timing from Placement Features Alone</li>
        <li><b>133</b> Allocating a Unified Domain Platform Following Market Analysis Using ProdDSE</li>
        <hr class="tp-pdiv"><span class="tp-plbl">Poster presentations</span>
        <li class="tp-po"><span class="tp-ttag">T4</span><b>116</b> A Self-Recoverable Nonvolatile Magnetic Latch with High-Speed SEU-Tolerant Backup Module</li>
        <li class="tp-po"><span class="tp-ttag">T4</span><b>72</b> A Scalable End-to-End Framework for Multi-Objective Design Space Exploration: Application to AI Accelerators</li>
      </ul>
    </td>
    <td class="tp-ch">
      <span class="tp-t">RS7 – Embedded Systems &amp; Low-Power Design</span>
      <span class="tp-s">Tracks 5+7 · 4 papers + 2 poster presentations · 90 min</span>
      <ul class="tp-pp">
        <li><b>1</b> A Silicon-Validated High-Frequency RISC-V SoC for Extreme-Temperature Applications</li>
        <li><b>147</b> Interpretable Fuzzy Control for Lightweight Cache Replacement and Prefetch Throttling in RISC-V SoCs</li>
        <li><b>21</b> An event-Driven ASK Demodulator Based on Slope Measurements for low-Power Applications</li>
        <li><b>146</b> Separate Read-Write Differential 11T SRAM-based In-Memory Computing Architecture</li>
        <hr class="tp-pdiv"><span class="tp-plbl">Poster presentations</span>
        <li class="tp-po"><span class="tp-ttag">T5</span><b>38</b> R5-Link: Enhancing RISC-V Multi-Core Efficiency with Hardware Message Passing Channels in a 2D Mesh Network</li>
        <li class="tp-po"><span class="tp-ttag">T6</span><b>118</b> Surrogate-assisted DTCO for 1T1C FeMFET Bitcells: A Comparative Study on Model Choice and Data Sampling</li>
      </ul>
    </td>
  </tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">15:00–15:20</td><td><span class="tp-t">Coffee Break + PhD &amp; Student Forum</span><span class="tp-s">20 min</span></td></tr>
  <tr class="rs"><td class="tp-ca"></td><td class="tp-ct">15:20–16:50</td>
    <td class="tp-ch">
      <span class="tp-t">SS 154 – Edge AI for Smart Agriculture</span>
      <span class="tp-s">Organizer: Theocharis Theocharides · 4 papers · 90 min</span>
      <ul class="tp-pp">
        <li><b>161</b> Embedded Systems for Precision Agriculture Monitoring: An Electronics Designer's Perspective
          <span class="tp-auth">Peppi · Torrisi · Gullino · Manfrini · Petti · De Marchi</span></li>
        <li><b>172</b> Neuromorphic Vision Technologies in Smart Agriculture: Challenges and Opportunities
          <span class="tp-auth">Peres · Bertozzi</span></li>
        <li><b>173</b> Edge AI for Smart and Precision Agriculture: An Overview of Robotic Vision for Field Perception and Decision Support
          <span class="tp-auth">Theocharides · Savva · Phakoukaki</span></li>
        <li><b>174</b> Pollin8: Species-Level Pollinator and Pest Counting on a Milliwatt System-on-Chip
          <span class="tp-auth">Constantinescu · Wiese · Consani · Kartsch · Benini · Atienza</span></li>
      </ul>
    </td>
    <td class="tp-ch">
      <span class="tp-t">SS 85 – Emerging &amp; Reliable Computing for Scalable Intelligence</span>
      <span class="tp-s">Organizer: Juergen Becker · 2 invited talks + 2 papers · 90 min</span>
      <ul class="tp-pp">
        <li class="tp-inv"><b>–</b> Emerging Technologies &amp; The Chiplet Revolution <em>(invited)</em>
          <span class="tp-auth">Guohao Dai</span></li>
        <li><b>177</b> Evaluating Block Arithmetic Formats for Efficient AI Inference Hardware
          <span class="tp-auth">Christopoulos · Genssler · Amrouch · Sauer</span></li>
        <li><b>178</b> Efficient Neural Network Inference on CPU-Centered Edge Device
          <span class="tp-auth">Grace Li Zhang</span></li>
        <li class="tp-inv"><b>–</b> SoC – Service on a Chip <em>(invited talk)</em>
          <span class="tp-auth">Markus Abel</span></li>
      </ul>
    </td>
  </tr>
  <tr class="rrec"><td class="tp-ca"></td><td class="tp-ct">17:30–19:00</td>
    <td>
      <span class="tp-t">Welcome Reception</span>
      <span class="tp-s">Welcome Cocktail is the first social gathering between all conference delegates and it will take place at the St. Raphael Resort. It will be a relaxing evening during which delegates will have the opportunity to talk to colleagues and peers, while enjoying local drinks and ample canapés, with a view of the calming waters of the Mediterranean Sea.</span>
    </td>
  </tr>
</table>

<!-- TUESDAY -->
<span class="tp-day">Tuesday, 13 October 2026 – Conference Day 2</span>
<table class="tp-sched">
  <tr class="rk"><td class="tp-ca"></td><td class="tp-ct">09:00–10:00</td><td>
    <span class="tp-t">Academic Keynote 2 – Envisioning SoC Design with an Army of Agentic Minions</span>
    <span class="tp-s">Prof. Valeria Bertacco · University of Michigan, USA · Plenary · 60 min</span>
  </td></tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">10:00–10:20</td><td><span class="tp-t">Coffee Break</span><span class="tp-s">20 min</span></td></tr>
  <tr class="rr"><td class="tp-ca"></td><td class="tp-ct">10:20–11:50</td>
    <td class="tp-ch">
      <span class="tp-t">RS2 – AI/ML Architectures &amp; Computing Paradigms</span>
      <span class="tp-s">Tracks 1+3 · 4 papers + 2 poster presentations · 90 min</span>
      <ul class="tp-pp">
        <li><b>30</b> Chip-Agnostic Hardware-Aware Training for ADC-Efficient BNNs in SOT-MRAM Crossbars</li>
        <li><b>104</b> PreDSE: Predictive Design Space Exploration for FPGA CNN Dataflow Accelerators</li>
        <li><b>37</b> A Noise-based Obfuscation Technique for Safe and Secure In-Memory AI inference</li>
        <li><b>23</b> New Obfuscation Strategies for Approximate Adders</li>
        <hr class="tp-pdiv"><span class="tp-plbl">Poster presentations</span>
        <li class="tp-po"><span class="tp-ttag">T3</span><b>66</b> Reducing the Footprint of Approximate Ternary Neural Networks via Per-Neuron Input Permutations</li>
        <li class="tp-po"><span class="tp-ttag">T5</span><b>131</b> Deployment of a Safety-Critical, Distilled YOLOV8m Vision System on a Dual-Core, 1MB, BLE-Connected Programmable Logic Controller</li>
      </ul>
    </td>
    <td class="tp-ch">
      <span class="tp-t">RS5 – Hardware Security &amp; Testing</span>
      <span class="tp-s">Tracks 8+12 · 4 papers + 1 poster presentation · 85 min</span>
      <ul class="tp-pp">
        <li><b>56</b> A Differential Power Analysis Attack Exploiting Early Propagation Effect in Dual-Rail Pre-Charge Logic Circuits</li>
        <li><b>98</b> Self-Interpretable Hardware Trojan Detection on Gate-Level Netlists with Sufficient and Necessary GNN Explanations</li>
        <li><b>109</b> SW-PUF: An ML-Resistant Strong PUF Architecture Using Weak-PUF Entropy and Ascon-Hash Obfuscation</li>
        <li><b>105</b> JTAG You're It: A Scalable JTAG Network in Chiplet Arrays via Fabric-Reuse</li>
        <hr class="tp-pdiv"><span class="tp-plbl">Poster presentation</span>
        <li class="tp-po"><span class="tp-ttag">T8</span><b>111</b> Side-channel aware design of FeFET based memory for cryptographic SBox implementation</li>
      </ul>
    </td>
  </tr>
  <tr class="rik"><td class="tp-ca"></td><td class="tp-ct">11:50–12:30</td><td>
    <span class="tp-t">Industrial Keynote 2 – Low Power IC Design for a Sustainable World</span>
    <span class="tp-s">Victor Grimblatt · Synopsys, Chile · Plenary · 40 min</span>
  </td></tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">12:30–13:30</td><td><span class="tp-t">Lunch Break</span><span class="tp-s">60 min</span></td></tr>
  <tr class="rp"><td class="tp-ca"></td><td class="tp-ct">13:30–14:15</td><td>
    <span class="tp-t">Panel – AI as the Chip Designer: Evolution or Illusion?</span>
    <span class="tp-s">Plenary · 45 min · Frank K. Gurkaynak (ETH Zürich) · Sandro Belfanti (Chipmind)</span>
  </td></tr>
  <tr class="rs"><td class="tp-ca"></td><td class="tp-ct">14:15–15:45</td>
    <td class="tp-ch">
      <span class="tp-t">SS 150a – Sustainable Intelligence at the Edge (Part 1)</span>
      <span class="tp-s">Organizers: Cathal Hoare · Tiziana Margaria · 3 papers · 90 min</span>
      <ul class="tp-pp">
        <li><b>158</b> TinySimpleNet: A SimpleNet for Unsupervised Industrial Anomaly Detection on Edge Devices
          <span class="tp-auth">Capogrosso · Fraccaroli · Magno · Fummi</span></li>
        <li><b>159</b> On the Deployment of Egocentric Pose Estimation Algorithms at the Edge
          <span class="tp-auth">Pompanin · Martini · Fummi · Bombieri</span></li>
        <li><b>160</b> Sustainable SoftPLCs at the Edge: An Open-Source Path to Right-Sizing and Retrofitting Industrial Automation
          <span class="tp-auth">Noto · Dall'Ora</span></li>
      </ul>
    </td>
    <td class="tp-ch">
      <span class="tp-t">SS 155 – DfT, Reliability &amp; Functional Safety for Edge AI SoCs</span>
      <span class="tp-s">Organizers: Maksim Jenihhin · Matteo Sonza Reorda · 1 invited talk + 3 papers · 90 min</span>
      <ul class="tp-pp">
        <li class="tp-inv"><b>–</b> Towards Dependable Edge AI: Reliability Assessment and Hardening Across the Compute Stack <em>(invited)</em>
          <span class="tp-auth">Matteo Sonza Reorda</span></li>
        <li><b>162</b> DfT-Assisted Testing of Resistive Short Defects in SRAM-Based In-Memory Computing Architectures
          <span class="tp-auth">Lampridis · Tsiatouhas · Michael · Theocharides</span></li>
        <li><b>166</b> NURSE: Syndrome-Guided Runtime Correction of Pipeline Interconnect Faults in RISC-V Processors
          <span class="tp-auth">Santhosh · Jutman · Kaja · Ecker · Jenihhin</span></li>
        <li><b>168</b> Towards ISO 26262-compliant Vector Processors: Combining STLs and LBIST
          <span class="tp-auth">Vilar de Farias · Kurada · Abed · Guerrero-Balaguera · Rodriguez Condia · Bagbaba · da Silva · Sonza Reorda</span></li>
      </ul>
    </td>
  </tr>
  <tr class="rpd"><td class="tp-ca"></td><td class="tp-ct">15:45–16:05</td><td>
    <span class="tp-t">Coffee Break + Poster Display</span>
    <span class="tp-s">20 min · All 10 posters displayed simultaneously</span>
  </td></tr>
  <tr class="rsoc"><td class="tp-ca"></td><td class="tp-ct">17:00–19:00</td><td>
    <span class="tp-t">Conference Tour – Historical Limassol</span>
    <span class="tp-s">Departure from St. Raphael Resort by air-conditioned buses with licensed tour guides · Walking tour (weather permitting) of the historical sites and landmarks in the centre of Limassol</span>
  </td></tr>
  <tr class="rsoc"><td class="tp-ca"></td><td class="tp-ct">19:30–23:00</td><td>
    <span class="tp-t">Conference Dinner – Traditional Cypriot Evening</span>
    <span class="tp-s">Local tavern · Authentic Cypriot dishes complemented with local drinks, desserts, and traditional entertainment</span>
  </td></tr>
</table>

<!-- WEDNESDAY -->
<span class="tp-day">Wednesday, 14 October 2026 – Conference Day 3</span>
<table class="tp-sched">
  <tr class="rk"><td class="tp-ca"></td><td class="tp-ct">09:00–10:00</td><td>
    <span class="tp-t">Academic Keynote 3 – Do We Really Need All the Bits? Value-Driven Approximate Computing for AI Accelerators</span>
    <span class="tp-s">Prof. Freddy Gabbay · Hebrew University of Jerusalem, Israel · Plenary · 60 min</span>
  </td></tr>
  <tr class="rpd"><td class="tp-ca"></td><td class="tp-ct">10:00–10:20</td><td>
    <span class="tp-t">Coffee Break + Poster Display</span>
    <span class="tp-s">20 min · All 10 posters displayed simultaneously</span>
  </td></tr>
  <tr class="rr"><td class="tp-ca"></td><td class="tp-ct">10:20–11:40</td>
    <td class="tp-ch">
      <span class="tp-t">RS4 – Digital Design &amp; EDA II</span>
      <span class="tp-s">Tracks 3+4 · Timing, Async &amp; FPGA · 4 papers · 80 min</span>
      <ul class="tp-pp">
        <li><b>79</b> Efficient Scalable Approximate Multipliers via Significance-Driven Partial Product Removal <span class="tp-bpc">BPC</span></li>
        <li><b>44</b> AutoSDC: Correct-by-Construction Timing Constraint Generation via Hybrid Neuro-Structural Training, Multivariate Quality Prediction, and Recursive Signoff-Driven Refinement</li>
        <li><b>129</b> Exploring the Impact of 2D Convolutional Layer Hyperparameters in FPGA Implementation</li>
        <li><b>81</b> A Robust Asymmetric Delay Cell for High-Performance 4-Phase Bundled-Data Circuits</li>
      </ul>
    </td>
    <td class="tp-ch">
      <span class="tp-t">RS8 – Communications, Sensing &amp; Emerging Technologies</span>
      <span class="tp-s">Tracks 2+6+9 · 4 papers · 80 min</span>
      <ul class="tp-pp">
        <li><b>40</b> Community-Based ILP for Application Mapping and Deadlock-Free Routing on Large NoCs</li>
        <li><b>15</b> White Rabbit–Enabled Deterministic Triggering for Bi-Static ISAC in 6G</li>
        <li><b>91</b> Selective frame processing for accelerating visual SLAM</li>
        <li><b>54</b> Impact of Programming Pattern Strategy on ReRAM Relaxation and Retention Stability <span class="tp-bpc">BPC</span></li>
      </ul>
    </td>
  </tr>
  <tr class="rik"><td class="tp-ca"></td><td class="tp-ct">11:40–12:20</td><td>
    <span class="tp-t">Industrial Keynote 3 – Bridging the Gap Between Research and Industry Through Embedded Systems</span>
    <span class="tp-s">Odysseas Economides · HardwareX Engineering, Cyprus · Plenary · 40 min</span>
  </td></tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">12:20–13:20</td><td><span class="tp-t">Lunch Break</span><span class="tp-s">60 min</span></td></tr>
  <tr class="rs"><td class="tp-ca"></td><td class="tp-ct">13:20–14:50</td>
    <td class="tp-ch">
      <span class="tp-t">SS 150b – Sustainable Intelligence at the Edge (Part 2)</span>
      <span class="tp-s">Organizers: Cathal Hoare · Tiziana Margaria · 4 papers · 90 min</span>
      <ul class="tp-pp">
        <li><b>163</b> LLM-Driven Optimization of Large Language Model Inference
          <span class="tp-auth">Amir Aminifar</span></li>
        <li><b>164</b> A Federated Cyber-Physical Edge Architecture for Smart Hospital Room Automation
          <span class="tp-auth">Iervasi · Noe Marthe · Mohamed Ali · Abdulkadir Hassan · Demrozi</span></li>
        <li><b>170</b> Toward a Unified Memristive Edge Platform for Sensing, Security, and Neuromorphic Computing
          <span class="tp-auth">Heba Abunahla</span></li>
        <li><b>171</b> Embedded Intelligence at the Edge: Recommender Systems, Efficient Simulation, and Operator-Centred Decision Support
          <span class="tp-auth">Cathal Hoare · Tiziana Margaria</span></li>
      </ul>
    </td>
    <td class="tp-ch">
      <span class="tp-t">SS 16 – Design, Testing &amp; Reliability of Memristive-based Compute-in-Memory Architectures</span>
      <span class="tp-s">Organizers: Surendra Hemaram · Anteneh Gebregiorgis · 1 invited talk + 3 papers · 90 min</span>
      <ul class="tp-pp">
        <li class="tp-inv"><b>–</b> Emerging Compute Paradigms – Opportunities and Challenges <em>(invited)</em>
          <span class="tp-auth">Norbert Wehn</span></li>
        <li><b>167</b> ECC-Assisted Fault Tolerance in Memristive Crossbar-based CIM Architectures: An Overview
          <span class="tp-auth">Hemaram · Hamdioui · Gebregiorgis</span></li>
        <li><b>169</b> Variability Aware Neuro-Memristive Networks: Hardware Software Co-design Approaches
          <span class="tp-auth">Kabeer · Dinesh · James</span></li>
        <li><b>175</b> Testing RRAM-Based Brain-Inspired Architectures after Manufacturing: Challenges and Solutions
          <span class="tp-auth">Bolzani Poehls · Chinazzo</span></li>
      </ul>
    </td>
  </tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">14:50–15:10</td><td><span class="tp-t">Coffee Break</span><span class="tp-s">20 min</span></td></tr>
  <tr class="rc"><td class="tp-ca"></td><td class="tp-ct">15:10–16:10</td><td>
    <span class="tp-t">Closing Ceremony &amp; Awards</span>
    <span class="tp-s">Conference ends 16:10</span>
  </td></tr>
</table>

<div class="justify-content-center txtcenter" id="soc">
      <h2 class="ops-tt txtcenter mts-10">SOCIAL PROGRAM</h2>
      <br />
      <p class="ops-t txtcenter same-line"> Info will be posted. (TBA)</p>
      <br /><br />
   </div>
</div>
