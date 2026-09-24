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
#tec-schedule .tp-spk { font-size:10px; color:#1a2a4a; display:block; margin-top:1px; font-weight:700; }
#tec-schedule .tp-room { display:inline-block; font-size:9.5px; font-weight:700; background:#fff; color:#1a2a4a; border:1px solid #1a2a4a; border-radius:2px; padding:0 5px; margin-right:4px; letter-spacing:.3px; }
#tec-schedule .tp-fmt { display:block; font-size:9.5px; color:#555; margin-top:1px; }
#tec-schedule .tp-mode { font-size:10.5px; color:#1a2a4a; display:block; margin-top:2px; }
#tec-schedule .tp-chair { font-size:10.5px; color:#7c2d12; display:block; margin-top:1px; font-weight:700; }
#tec-schedule .tp-chair em { font-weight:400; }
#tec-schedule li.tp-hit { outline:2px solid #f59e0b; background:#fff7d6; border-radius:2px; }
#tp-finder { border:1px solid #1a2a4a; border-radius:6px; padding:14px 16px; margin:0 0 24px; background:#f4f7fb; }
#tp-finder label { font-weight:700; color:#1a2a4a; display:block; margin-bottom:6px; font-size:14px; }
#tp-finder input { width:100%; box-sizing:border-box; font-size:15px; padding:9px 11px; border:1px solid #9aa7bd; border-radius:4px; }
#tp-finder .tp-hint { font-size:11.5px; color:#555; margin-top:5px; }
#tp-results .tp-card { background:#fff; border:1px solid #cfd8e6; border-left:4px solid #b91c1c; border-radius:4px; padding:9px 12px; margin-top:8px; font-size:13px; line-height:1.5; }
#tp-results .tp-card.po { border-left-color:#7c3aed; }
#tp-results .tp-card.ch { border-left-color:#b45309; }
#tp-results .tp-card .k { color:#555; }
#tp-results .tp-card a { color:#1155cc; font-size:12px; }
#tp-results .tp-none { font-size:13px; color:#555; margin-top:8px; }
#tec-schedule .tp-auth { font-size:10px; color:#555; display:block; margin-top:1px; font-style:italic; }
</style>

<div id="tp-finder">
  <label for="tp-q">Find your paper, presentation or session</label>
  <input id="tp-q" type="search" placeholder="Type your name, paper ID (e.g. 94) or part of the title" autocomplete="off">
  <div class="tp-hint">Search covers paper IDs, titles, authors, speakers and session chairs.</div>
  <div id="tp-results" aria-live="polite"></div>
</div>

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
    <td class="tp-ch"><span class="tp-t">Tutorial 1</span><span class="tp-s"><span class="tp-room">Atrium A</span>80 min · Christos Sotiriou</span></td>
    <td class="tp-ch"><span class="tp-t">Tutorial 2</span><span class="tp-s"><span class="tp-room">Atrium B</span>80 min · Cédric Marchand</span></td>
  </tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">10:20–10:40</td><td><span class="tp-t">Coffee Break</span><span class="tp-s">20 min</span></td></tr>
  <tr class="rk"><td class="tp-ca"></td><td class="tp-ct">10:40–12:00</td>
    <td class="tp-ch"><span class="tp-t">Tutorial 1 (cont.)</span><span class="tp-s"><span class="tp-room">Atrium A</span>80 min · Christos Sotiriou</span></td>
    <td class="tp-ch"><span class="tp-t">Tutorial 2 (cont.)</span><span class="tp-s"><span class="tp-room">Atrium B</span>80 min · Cédric Marchand</span></td>
  </tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">12:00–13:00</td><td><span class="tp-t">Lunch Break</span><span class="tp-s">60 min</span></td></tr>
  <tr class="rk"><td class="tp-ca"></td><td class="tp-ct">13:00–14:20</td>
    <td class="tp-ch"><span class="tp-t">Tutorial 3</span><span class="tp-s"><span class="tp-room">Atrium A</span>80 min · Ricardo Reis</span></td>
    <td class="tp-ch"><span class="tp-t">Tutorial 4</span><span class="tp-s"><span class="tp-room">Atrium B</span>80 min · Maksim Jenihhin</span></td>
  </tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">14:20–14:40</td><td><span class="tp-t">Coffee Break</span><span class="tp-s">20 min</span></td></tr>
  <tr class="rk"><td class="tp-ca"></td><td class="tp-ct">14:40–16:00</td>
    <td class="tp-ch"><span class="tp-t">Tutorial 3 (cont.)</span><span class="tp-s"><span class="tp-room">Atrium A</span>80 min · Ricardo Reis</span></td>
    <td class="tp-ch"><span class="tp-t">Tutorial 4 (cont.)</span><span class="tp-s"><span class="tp-room">Atrium B</span>80 min · Maksim Jenihhin</span></td>
  </tr>
  <tr class="rp"><td class="tp-ca"></td><td class="tp-ct">16:30–</td><td>
    <span class="tp-t">IFIP WG10.5 Working Group Meeting</span>
    <span class="tp-s"><span class="tp-room">Atrium A</span>Closed session · Duration TBA</span>
  </td></tr>
</table>

<!-- MONDAY -->
<span class="tp-day">Monday, 12 October 2026 – Conference Day 1</span>
<table class="tp-sched">
  <tr class="ra"><td class="tp-ca"></td><td class="tp-ct">08:00–08:30</td><td><span class="tp-t">Registration</span></td></tr>
  <tr class="ra"><td class="tp-ca"></td><td class="tp-ct">08:30–09:00</td><td><span class="tp-t">Welcome Ceremony</span><span class="tp-s">Plenary · Megaron AB</span></td></tr>
  <tr class="rk"><td class="tp-ca"></td><td class="tp-ct">09:00–10:00</td><td>
    <span class="tp-t">Academic Keynote 1 – Sustainable and Secure Computing: the Last Frontier</span>
    <span class="tp-s">Prof. Giovanni De Micheli · EPFL, Switzerland · Plenary · Megaron AB · 60 min</span>
  </td></tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">10:00–10:20</td><td><span class="tp-t">Coffee Break + PhD &amp; Student Forum</span><span class="tp-s">20 min</span></td></tr>
  <tr class="rr"><td class="tp-ca"></td><td class="tp-ct">10:20–11:50</td>
    <td class="tp-ch">
      <span class="tp-t">RS1 – AI/ML Hardware Architectures I</span>
      <span class="tp-s"><span class="tp-room">Megaron AB</span>
      <span class="tp-mode">Papers: 16 min talk + 4 min Q&amp;A · Posters: 5 min presentation</span>
      <span class="tp-chair" data-chair="Fernanda Kastensmidt">Session Chair: Fernanda Kastensmidt · UFRGS, Brazil <em>(to be confirmed)</em></span>Track 1 · 4 papers + 2 poster presentations · 90 min</span>
      <ul class="tp-pp">
        <li data-id="141" data-poster="0"><b>141</b> CIM-Blocks: A Synthesizable Multi-Precision Compute-in-Memory CGRA with Bit-Serial Data Reuse
          <span class="tp-auth">Manil Dev Gomony, Tobias Hommelen and Henk Corporaal</span><span class="tp-spk">Speaker: Henk Corporaal · Eindhoven University of Technology</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="18" data-poster="0"><b>18</b> At-the-Roofline Sparse Tensor Contractions on Vector Processors for Transformer Inference
          <span class="tp-auth">Bowen Wang, Chi Zhang, Diyou Shen, Renzo Andri, Navaneeth Kunhi Purayil and Luca Benini</span><span class="tp-spk">Speaker: Bowen Wang · ETH Zurich</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="24" data-poster="0"><b>24</b> Optimizing ML Workload Partitioning between CPUs and CIM Accelerators for Heterogeneous Computing
          <span class="tp-auth">Joel Klein, Rebecca Pelke, Roberto Laudani, Jan Moritz Joseph and Rainer Leupers</span><span class="tp-spk">Speaker: Joel Klein · RWTH Aachen University</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="71" data-poster="0"><b>71</b> Hardware-Aware Vision Transformer Deployment on a Convolution-Centric AI SoC
          <span class="tp-auth">Shaown Mojumder, Calvin-Leon Bauer, Simon Friedrich, Martin Friedrich, Emil Matúš and Gerhard Fettweis</span><span class="tp-spk">Speaker: Shaown Mojumder · TU Dresden</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <hr class="tp-pdiv"><span class="tp-plbl">Poster presentations</span>
        <li class="tp-po" data-id="53" data-poster="1"><span class="tp-ttag">T1</span><b>53</b> S4oP: Operator-level Pruning of Structured State Space Models for Resource-Constrained Devices
          <span class="tp-auth">Marco Deano, Filippo Ziche and Nicola Bombieri</span><span class="tp-spk">Speaker: Marco Deano · University of Verona</span><span class="tp-fmt">5 min presentation</span></li>
        <li class="tp-po" data-id="34" data-poster="1"><span class="tp-ttag">T2</span><b>34</b> Physically-Aware Preemptive Virtual Channels for Deadlock-Free AXI Networks-on-Chip
          <span class="tp-auth">Lorenzo Leone, Luca Colagrande and Luca Benini</span><span class="tp-spk">Speaker: Lorenzo Leone · ETH Zurich</span><span class="tp-fmt">5 min presentation</span></li>
      </ul>
    </td>
    <td class="tp-ch">
      <span class="tp-t">RS6 – System Verification, Test &amp; Dependability</span>
      <span class="tp-s"><span class="tp-room">Megaron C</span>
      <span class="tp-mode">Papers: 16 min talk + 4 min Q&amp;A · Posters: 5 min presentation</span>
      <span class="tp-chair" data-chair="Gunar Schirner">Session Chair: Gunar Schirner · Northeastern University, USA <em>(to be confirmed)</em></span>Tracks 11+12 · 4 papers + 1 poster presentation · 85 min</span>
      <ul class="tp-pp">
        <li data-id="86" data-poster="0"><b>86</b> Hardware Support for Statistical Methods Applied to Hardware-Software Verification and Debugging
          <span class="tp-auth">Debanjan Das, Ryan Robucci and Dhananjay Phatak</span><span class="tp-spk">Speaker: Debanjan Das · University of Maryland Baltimore County</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="94" data-poster="0"><b>94</b> Counterfactual Exploit Validation on CHERI-enabled RISC-V Using Virtual Prototypes <span class="tp-bpc">BPC</span>
          <span class="tp-auth">Andreas Hinterdorfer, Manfred Schlägl and Daniel Große</span><span class="tp-spk">Speaker: Andreas Hinterdorfer · Johannes Kepler University Linz</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="65" data-poster="0"><b>65</b> RISCar: RISC-V In a Simulated Car for DNN Training and Deployment in AD Systems
          <span class="tp-auth">Ahmed Mahmoudi, Hassan Shayea, Mladen Berekovic and Rolf Meyer</span><span class="tp-spk">Speaker: Ahmed Mahmoudi · University of Lübeck</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="76" data-poster="0"><b>76</b> Energy-Aware Fast and Accurate Design Space Exploration of Near-Memory Computing
          <span class="tp-auth">Hichem Benamara, Maha Kooli, Lorenzo Ciampolini, Thaddée Bricout, Pascal Vivet and Ian O'Connor</span><span class="tp-spk">Speaker: Hichem Benamara · CEA</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <hr class="tp-pdiv"><span class="tp-plbl">Poster presentation</span>
        <li class="tp-po" data-id="31" data-poster="1"><span class="tp-ttag">T11</span><b>31</b> AI-based Automated HDL Validation Using Abstract Syntax Tree and Signal Trace Analysis
          <span class="tp-auth">Shubrojyoti Karmakar, Shayon Mitra, Rijoy Mukherjee and Rajat Subhra Chakraborty</span><span class="tp-spk">Speaker: Shubrojyoti Karmakar · IIT Kharagpur</span><span class="tp-fmt">5 min presentation</span></li>
      </ul>
    </td>
  </tr>
  <tr class="rik"><td class="tp-ca"></td><td class="tp-ct">11:50–12:30</td><td>
    <span class="tp-t">Industrial Keynote 1 – What is the IP Reuse Trap for Digital Hardware, and How Can It Be Escaped?</span>
    <span class="tp-s">Prof. Wolfgang Ecker · Infineon / TU Munich, Germany · Plenary · Megaron AB · 40 min</span>
  </td></tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">12:30–13:30</td><td><span class="tp-t">Lunch Break</span><span class="tp-s">60 min</span></td></tr>
  <tr class="rr"><td class="tp-ca"></td><td class="tp-ct">13:30–15:00</td>
    <td class="tp-ch">
      <span class="tp-t">RS3 – Digital Design &amp; EDA I</span>
      <span class="tp-s"><span class="tp-room">Megaron AB</span>
      <span class="tp-mode">Papers: 16 min talk + 4 min Q&amp;A · Posters: 5 min presentation</span>
      <span class="tp-chair" data-chair="Henk Corporaal">Session Chair: Henk Corporaal · Eindhoven University of Technology, Netherlands <em>(to be confirmed)</em></span>Track 4 · Synthesis &amp; Optimization · 4 papers + 2 poster presentations · 90 min</span>
      <ul class="tp-pp">
        <li data-id="149" data-poster="0"><b>149</b> Automated RTL Complexity Estimation with Synthesis-Validated Optimization and Programmatic Code Transformation <span class="tp-bpc">BPC</span>
          <span class="tp-auth">Sanika Malve, Yogita Kapse, Prathibha Shringare and Neelima Kolhare</span><span class="tp-spk">Speaker: TBC</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="90" data-poster="0"><b>90</b> SPFD-Based Resynthesis for Dual-Output LUT Networks <span class="tp-bpc">BPC</span>
          <span class="tp-auth">Andrea Costamagna, Chang Meng and Giovanni De Micheli</span><span class="tp-spk">Speaker: Andrea Costamagna · Synopsys</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="110" data-poster="0"><b>110</b> No Tree Required: Predicting Post-CTS Clock Timing from Placement Features Alone
          <span class="tp-auth">Yiyu Wang, Wei Xing and Yuanqing Cheng</span><span class="tp-spk">Speaker: Yuanqing Cheng · Beihang University</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="133" data-poster="0"><b>133</b> Allocating a Unified Domain Platform Following Market Analysis Using ProdDSE
          <span class="tp-auth">Bruno Morais and Gunar Schirner</span><span class="tp-spk">Speaker: Gunar Schirner · Northeastern University</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <hr class="tp-pdiv"><span class="tp-plbl">Poster presentations</span>
        <li class="tp-po" data-id="116" data-poster="1"><span class="tp-ttag">T4</span><b>116</b> A Self-Recoverable Nonvolatile Magnetic Latch with High-Speed SEU-Tolerant Backup Module
          <span class="tp-auth">Shengyuan Yan, Kaili Zhang, Wentao Huang, Lang Zeng, Bi Wang, Yue Zhang, Yuanqi Hu, Weisheng Zhao and Deming Zhang</span><span class="tp-spk">Speaker: Shengyuan Yan · Beihang University</span><span class="tp-fmt">5 min presentation</span></li>
        <li class="tp-po" data-id="72" data-poster="1"><span class="tp-ttag">T4</span><b>72</b> A Scalable End-to-End Framework for Multi-Objective Design Space Exploration: Application to AI Accelerators
          <span class="tp-auth">Lilia Zaourar, Benoit Tain, Dahibou Fall Sow, Raphael Millet and Mohamed Benazouz</span><span class="tp-spk">Speaker: Benoit Tain · CEA</span><span class="tp-fmt">5 min presentation</span></li>
      </ul>
    </td>
    <td class="tp-ch">
      <span class="tp-t">RS7 – Embedded Systems &amp; Low-Power Design</span>
      <span class="tp-s"><span class="tp-room">Megaron C</span>
      <span class="tp-mode">Papers: 16 min talk + 4 min Q&amp;A · Posters: 5 min presentation</span>
      <span class="tp-chair" data-chair="Denisa-Andreea Constantinescu">Session Chair: Denisa-Andreea Constantinescu · EPFL / University of Basel, Switzerland <em>(to be confirmed)</em></span>Tracks 5+7 · 3 papers + 2 poster presentations · 90 min</span>
      <ul class="tp-pp">
        <li data-id="1" data-poster="0"><b>1</b> A Silicon-Validated High-Frequency RISC-V SoC for Extreme-Temperature Applications
          <span class="tp-auth">Malte Hawich, Tobias Stuckenberg, Jan Szücs, Malte Rücker, Rochus Nowosielski and Holger Blume</span><span class="tp-spk">Speaker: Malte Hawich · Leibniz University Hannover</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="147" data-poster="0"><b>147</b> Interpretable Fuzzy Control for Lightweight Cache Replacement and Prefetch Throttling in RISC-V SoCs
          <span class="tp-auth">Om Maheshwari and Dr. Bikram Paul</span><span class="tp-spk">Speaker: TBC</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="21" data-poster="0"><b>21</b> An event-Driven ASK Demodulator Based on Slope Measurements for low-Power Applications
          <span class="tp-auth">Gaël Ousset, Sylvain Engels, Estelle Lauga-Laroze, Xavier Lesage and Laurent Fesquet</span><span class="tp-spk">Speaker: Gaël Ousset · STMicroelectronics / TIMA</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <hr class="tp-pdiv"><span class="tp-plbl">Poster presentations</span>
        <li class="tp-po" data-id="38" data-poster="1"><span class="tp-ttag">T5</span><b>38</b> R5-Link: Enhancing RISC-V Multi-Core Efficiency with Hardware Message Passing Channels in a 2D Mesh Network
          <span class="tp-auth">Yosef Ida, Nachman Abargil, Alex Grinshpun, Sarit Shvimer and Freddy Gabbay</span><span class="tp-spk">Speaker: TBC</span><span class="tp-fmt">5 min presentation</span></li>
        <li class="tp-po" data-id="118" data-poster="1"><span class="tp-ttag">T6</span><b>118</b> Surrogate-assisted DTCO for 1T1C FeMFET Bitcells: A Comparative Study on Model Choice and Data Sampling
          <span class="tp-auth">Rosario Pronsato, Antoine Cauquil, Miqueas Filsinger, Damien Deleruyelle and Ian O'Connor</span><span class="tp-spk">Speaker: Rosario Pronsato · INL – École Centrale de Lyon</span><span class="tp-fmt">5 min presentation</span></li>
      </ul>
    </td>
  </tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">15:00–15:20</td><td><span class="tp-t">Coffee Break + PhD &amp; Student Forum</span><span class="tp-s">20 min</span></td></tr>
  <tr class="rs"><td class="tp-ca"></td><td class="tp-ct">15:20–16:50</td>
    <td class="tp-ch">
      <span class="tp-t">SS 154 – Edge AI for Smart Agriculture</span>
      <span class="tp-s"><span class="tp-room">Megaron AB</span>
      <span class="tp-mode">Papers: 16 min talk + 4 min Q&amp;A</span>
      <span class="tp-chair" data-chair="Theocharis Theocharides">Session Chair(s): Theocharis Theocharides (organizers)</span>Organizer: Theocharis Theocharides · 4 papers · 90 min</span>
      <ul class="tp-pp">
        <li data-id="161" data-poster="0"><b>161</b> Embedded Systems for Precision Agriculture Monitoring: An Electronics Designer's Perspective
          <span class="tp-auth">Lorenzo Peppi, Alessandro Torrisi, Michele Gullino, Luigi Manfrini, Luisa Petti and Luca De Marchi</span><span class="tp-spk">Speaker: Lorenzo Peppi  · University of Bologna</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="172" data-poster="0"><b>172</b> Neuromorphic Vision Technologies in Smart Agriculture: Challenges and Opportunities
          <span class="tp-auth">Luca Peres and Davide Bertozzi</span><span class="tp-spk">Speaker: Luca Peres · The University of Manchester</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="173" data-poster="0"><b>173</b> Edge AI for Smart and Precision Agriculture: An Overview of Robotic Vision for Field Perception and Decision Support
          <span class="tp-auth">Theocharis Theocharides, Antonis Savva and Yiota Victoria Phakoukaki</span><span class="tp-spk">Speaker: Antonis Savva · KIOS CoE, University of Cyprus</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="174" data-poster="0"><b>174</b> Pollin8: Species-Level Pollinator and Pest Counting on a Milliwatt System-on-Chip
          <span class="tp-auth">Denisa-Andreea Constantinescu, Philip Wiese, Mattia Consani, Victor Kartsch, Luca Benini and David Atienza</span><span class="tp-spk">Speaker: Denisa-Andreea Constantinescu · EPFL / University of Basel</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
      </ul>
    </td>
    <td class="tp-ch">
      <span class="tp-t">SS 85 – Emerging &amp; Reliable Computing for Scalable Intelligence</span>
      <span class="tp-s"><span class="tp-room">Megaron C</span>
      <span class="tp-mode">Papers: 16 min talk + 4 min Q&amp;A</span>
      <span class="tp-chair" data-chair="Juergen Becker">Session Chair(s): Juergen Becker (organizers)</span>Organizer: Juergen Becker · 2 invited talks + 2 papers · 90 min</span>
      <ul class="tp-pp">
        <li class="tp-inv"><b>–</b> Emerging Technologies &amp; The Chiplet Revolution <em>(invited)</em>
          <span class="tp-auth">Guohao Dai</span></li>
        <li data-id="177" data-poster="0"><b>177</b> Evaluating Block Arithmetic Formats for Efficient AI Inference Hardware
          <span class="tp-auth">Stefanos Christopoulos, Paul Genssler, Hussam Amrouch and Christian Sauer</span><span class="tp-spk">Speaker: Stefanos Christopoulos · Synopsys</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="178" data-poster="0"><b>178</b> Efficient Neural Network Inference on CPU-Centered Edge Device
          <span class="tp-auth">Grace-Li Zhang</span><span class="tp-spk">Speaker: Grace Li Zhang · TU Darmstadt</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
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
    <span class="tp-s">Prof. Valeria Bertacco · University of Michigan, USA · Plenary · Megaron AB · 60 min</span>
  </td></tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">10:00–10:20</td><td>
    <span class="tp-t">Coffee Break + Poster Display</span>
    <span class="tp-s">20 min · All 10 posters displayed simultaneously</span></td></tr>
  <tr class="rr"><td class="tp-ca"></td><td class="tp-ct">10:20–11:50</td>
    <td class="tp-ch">
      <span class="tp-t">RS2 – AI/ML Architectures &amp; Computing Paradigms</span>
      <span class="tp-s"><span class="tp-room">Megaron AB</span>
      <span class="tp-mode">Papers: 16 min talk + 4 min Q&amp;A · Posters: 5 min presentation</span>
      <span class="tp-chair" data-chair="Yuanqing Cheng">Session Chair: Yuanqing Cheng · Beihang University, China <em>(to be confirmed)</em></span>Tracks 1+3 · 4 papers + 2 poster presentations · 90 min</span>
      <ul class="tp-pp">
        <li data-id="30" data-poster="0"><b>30</b> Chip-Agnostic Hardware-Aware Training for ADC-Efficient BNNs in SOT-MRAM Crossbars
          <span class="tp-auth">Bruno Lovison Franco, Aymen Romdhane, Jonathan Miquel, David Novo and Pascal Benoit</span><span class="tp-spk">Speaker: Bruno Lovison Franco · LIRMM, University of Montpellier</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="104" data-poster="0"><b>104</b> PreDSE: Predictive Design Space Exploration for FPGA CNN Dataflow Accelerators
          <span class="tp-auth">Arthur Ely, Ian Kersz Amaral, Michael Jordan, José Rodrigo Azambuja, Antonio Carlos Schneider Beck and Fernanda Kastensmidt</span><span class="tp-spk">Speaker: Fernanda Kastensmidt · UFRGS</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="37" data-poster="0"><b>37</b> A Noise-based Obfuscation Technique for Safe and Secure In-Memory AI inference
          <span class="tp-auth">Luca Parrini, Reetwik Das, Benjamin Hettwer, Taha Soliman, Chester Rebeiro and Norbert Wehn</span><span class="tp-spk">Speaker: Luca Parrini · RPTU Kaiserslautern</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="23" data-poster="0"><b>23</b> New Obfuscation Strategies for Approximate Adders
          <span class="tp-auth">Rostislav Husa, Vojtech Mrazek and Lukas Sekanina</span><span class="tp-spk">Speaker: Rostislav Husa · Brno University of Technology</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <hr class="tp-pdiv"><span class="tp-plbl">Poster presentations</span>
        <li class="tp-po" data-id="66" data-poster="1"><span class="tp-ttag">T3</span><b>66</b> Reducing the Footprint of Approximate Ternary Neural Networks via Per-Neuron Input Permutations
          <span class="tp-auth">Zdenek Vasicek, Vojtech Mrazek and Georgios Zervakis</span><span class="tp-spk">Speaker: Zdenek Vasicek · Brno University of Technology</span><span class="tp-fmt">5 min presentation</span></li>
        <li class="tp-po" data-id="131" data-poster="1"><span class="tp-ttag">T5</span><b>131</b> Deployment of a Safety-Critical, Distilled YOLOV8m Vision System on a Dual-Core, 1MB, BLE-Connected Programmable Logic Controller
          <span class="tp-auth">Rayan Malik, Mohammed Alnaqbi, Mohamed Zakkaria, Nasser Alhemeiri, Esrat Khan and Ibrahim Elfadel</span><span class="tp-spk">Speaker: Rayan Malik · Khalifa University</span><span class="tp-fmt">5 min presentation</span></li>
      </ul>
    </td>
    <td class="tp-ch">
      <span class="tp-t">RS5 – Hardware Security &amp; Testing</span>
      <span class="tp-s"><span class="tp-room">Megaron C</span>
      <span class="tp-mode">Papers: 16 min talk + 4 min Q&amp;A · Posters: 5 min presentation</span>
      <span class="tp-chair" data-chair="Malte Hawich">Session Chair: Malte Hawich · Leibniz University Hannover, Germany <em>(to be confirmed)</em></span>Tracks 8+12 · 4 papers + 1 poster presentation · 85 min</span>
      <ul class="tp-pp">
        <li data-id="56" data-poster="0"><b>56</b> A Differential Power Analysis Attack Exploiting Early Propagation Effect in Dual-Rail Pre-Charge Logic Circuits
          <span class="tp-auth">Aniruddh Holemadlu, Rupa Yashaswi Panduga, Nima Kavand, Shubham Rai and Akash Kumar</span><span class="tp-spk">Speaker: Aniruddh Holemadlu · Ruhr University Bochum</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="98" data-poster="0"><b>98</b> Self-Interpretable Hardware Trojan Detection on Gate-Level Netlists with Sufficient and Necessary GNN Explanations
          <span class="tp-auth">Marwa Dhiaf</span><span class="tp-spk">Speaker: Marwa Dhiaf · Queen's University Belfast</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="109" data-poster="0"><b>109</b> SW-PUF: An ML-Resistant Strong PUF Architecture Using Weak-PUF Entropy and Ascon-Hash Obfuscation
          <span class="tp-auth">Jiaxin Li, Bi Wang, Hanbin Wang, Jingyu Gou, Yuan Ma and Zhaohao Wang</span><span class="tp-spk">Speaker: Jiaxin Li · Beihang University</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="105" data-poster="0"><b>105</b> JTAG You’re It: A Scalable JTAG Network in Chiplet Arrays via Fabric-Reuse
          <span class="tp-auth">Kristoffer Westring, William Marnfeldt, Alex Allfjord, Per Andersson, Joachim Rodrigues and Victor Åberg</span><span class="tp-spk">Speaker: Kristoffer Westring · Lund University</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <hr class="tp-pdiv"><span class="tp-plbl">Poster presentation</span>
        <li class="tp-po" data-id="111" data-poster="1"><span class="tp-ttag">T8</span><b>111</b> Side-channel aware design of FeFET based memory for cryptographic SBox implementation
          <span class="tp-auth">Cédric Marchand, Miqueas Filsinger, Ian O'Connor, Stefan Slesazeck and Thomas Mikolajick</span><span class="tp-spk">Speaker: Cédric Marchand · École Centrale de Lyon</span><span class="tp-fmt">5 min presentation</span></li>
      </ul>
    </td>
  </tr>
  <tr class="rik"><td class="tp-ca"></td><td class="tp-ct">11:50–12:30</td><td>
    <span class="tp-t">Industrial Keynote 2 – Low Power IC Design for a Sustainable World</span>
    <span class="tp-s">Victor Grimblatt · Synopsys, Chile · Plenary · Megaron AB · 40 min</span>
  </td></tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">12:30–13:30</td><td><span class="tp-t">Lunch Break</span><span class="tp-s">60 min</span></td></tr>
  <tr class="rp"><td class="tp-ca"></td><td class="tp-ct">13:30–14:15</td><td>
    <span class="tp-t">Panel – AI as the Chip Designer: Evolution or Illusion?</span>
    <span class="tp-s">Plenary · Megaron AB · 45 min · Frank K. Gurkaynak (ETH Zürich) · Sandro Belfanti (Chipmind)</span>
  </td></tr>
  <tr class="rs"><td class="tp-ca"></td><td class="tp-ct">14:15–15:45</td>
    <td class="tp-ch">
      <span class="tp-t">SS 150a – Sustainable Intelligence at the Edge (Part 1)</span>
      <span class="tp-s"><span class="tp-room">Megaron AB</span>
      <span class="tp-mode">Papers: 16 min talk + 4 min Q&amp;A</span>
      <span class="tp-chair" data-chair="Cathal Hoare · Tiziana Margaria">Session Chair(s): Cathal Hoare · Tiziana Margaria (organizers)</span>Organizers: Cathal Hoare · Tiziana Margaria · 3 papers · 90 min</span>
      <ul class="tp-pp">
        <li data-id="158" data-poster="0"><b>158</b> TinySimpleNet: A SimpleNet for Unsupervised Industrial Anomaly Detection on Edge Devices
          <span class="tp-auth">Luigi Capogrosso, Enrico Fraccaroli, Michele Magno and Franco Fummi</span><span class="tp-spk">Speaker: Luigi Capogrosso · IT:U Austria</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="159" data-poster="0"><b>159</b> On the deployment of Egocentric Pose Estimation Algorithms at the Edge
          <span class="tp-auth">Ferdinando Pompanin, Enrico Martini, Franco Fummi and Nicola Bombieri</span><span class="tp-spk">Speaker: Ferdinando Pompanin · University of Verona</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="160" data-poster="0"><b>160</b> Sustainable SoftPLCs at the Edge: An Open-Source Path to Right-Sizing and Retrofitting Industrial Automation
          <span class="tp-auth">Gioacchino Ivan Noto and Nicola Dall'Ora</span><span class="tp-spk">Speaker: Nicola Dall'Ora · Guglielmo Marconi University</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
      </ul>
    </td>
    <td class="tp-ch">
      <span class="tp-t">SS 155 – DfT, Reliability &amp; Functional Safety for Edge AI SoCs</span>
      <span class="tp-s"><span class="tp-room">Megaron C</span>
      <span class="tp-mode">Papers: 16 min talk + 4 min Q&amp;A</span>
      <span class="tp-chair" data-chair="Maksim Jenihhin · Matteo Sonza Reorda">Session Chair(s): Maksim Jenihhin · Matteo Sonza Reorda (organizers)</span>Organizers: Maksim Jenihhin · Matteo Sonza Reorda · 1 invited talk + 3 papers · 90 min</span>
      <ul class="tp-pp">
        <li class="tp-inv"><b>–</b> Towards Dependable Edge AI: Reliability Assessment and Hardening Across the Compute Stack <em>(invited)</em>
          <span class="tp-auth">Matteo Sonza Reorda</span></li>
        <li data-id="162" data-poster="0"><b>162</b> DfT-Assisted Testing of Resistive Short Defects in SRAM-Based In-Memory Computing Architectures
          <span class="tp-auth">Dimitrios Stylianos Lampridis, Yiorgos Tsiatouhas, Maria K. Michael and Theocharis Theocharides</span><span class="tp-spk">Speaker: Dimitrios Stylianos Lampridis · University of Cyprus</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="166" data-poster="0"><b>166</b> NURSE: Syndrome-Guided Runtime Correction of Pipeline Interconnect Faults in RISC-V Processors
          <span class="tp-auth">Ashwin Santhosh, Artur Jutman, Endri Kaja, Wolfgang Ecker and Maksim Jenihhin</span><span class="tp-spk">Speaker: Ashwin Santhosh · Tallinn University of Technology</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="168" data-poster="0"><b>168</b> Towards ISO 26262-compliant Vector Processors: Combining STLs and LBIST
          <span class="tp-auth">Gustavo Vilar de Farias, Dwijesh Kurada, Sergiu-Mohamed Abed, Juan-David Guerrero-Balaguera, Josie Esteban Rodriguez Condia, Ahmet Cagri Bagbaba, Felipe Augusto da Silva and Matteo Sonza Reorda</span><span class="tp-spk">Speaker: Dwijesh Kurada · Cadence Design Systems</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
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
    <span class="tp-s">Prof. Freddy Gabbay · Hebrew University of Jerusalem, Israel · Plenary · Megaron AB · 60 min</span>
  </td></tr>
  <tr class="rpd"><td class="tp-ca"></td><td class="tp-ct">10:00–10:20</td><td>
    <span class="tp-t">Coffee Break + Poster Display</span>
    <span class="tp-s">20 min · All 10 posters displayed simultaneously</span>
  </td></tr>
  <tr class="rr"><td class="tp-ca"></td><td class="tp-ct">10:20–11:40</td>
    <td class="tp-ch">
      <span class="tp-t">RS4 – Digital Design &amp; EDA II</span>
      <span class="tp-s"><span class="tp-room">Megaron AB</span>
      <span class="tp-mode">Papers: 16 min talk + 4 min Q&amp;A</span>
      <span class="tp-chair" data-chair="Cédric Marchand">Session Chair: Cédric Marchand · École Centrale de Lyon, France <em>(to be confirmed)</em></span>Tracks 3+4 · Timing, Async &amp; FPGA · 3 papers · 80 min</span>
      <ul class="tp-pp">
        <li data-id="79" data-poster="0"><b>79</b> Efficient Scalable Approximate Multipliers via Significance-Driven Partial Product Removal <span class="tp-bpc">BPC</span>
          <span class="tp-auth">Sergio Castillo Mohedano, Victor Åberg, Joachim Rodrigues and Masoud Nouripayam</span><span class="tp-spk">Speaker: Victor Åberg · Lund University</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="44" data-poster="0"><b>44</b> AutoSDC: Correct-by-Construction Timing Constraint Generation via Hybrid Neuro-Structural Training, Multivariate Quality Prediction, and Recursive Signoff-Driven Refinement
          <span class="tp-auth">Abhishek Nigam, Anubhav Sharma, Vinod Singh and Vanshika Garg</span><span class="tp-spk">Speaker: Anubhav Sharma · Quest Global</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="81" data-poster="0"><b>81</b> A Robust Asymmetric Delay Cell for High-Performance 4-Phase Bundled-Data Circuits
          <span class="tp-auth">Jessica Gonsalves Santos, Cristiano Merio, Adrien Godard, Ali Naimi, Sylvain Engels, Robin Wilson and Laurent Fesquet</span><span class="tp-spk">Speaker: Jéssica Gonsalves Santos · Univ. Grenoble Alpes, TIMA</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
      </ul>
    </td>
    <td class="tp-ch">
      <span class="tp-t">RS8 – Communications, Sensing &amp; Emerging Technologies</span>
      <span class="tp-s"><span class="tp-room">Megaron C</span>
      <span class="tp-mode">Papers: 16 min talk + 4 min Q&amp;A</span>
      <span class="tp-chair" data-chair="Luigi Capogrosso">Session Chair: Luigi Capogrosso · IT:U, Austria <em>(to be confirmed)</em></span>Tracks 2+6+9 · 4 papers · 80 min</span>
      <ul class="tp-pp">
        <li data-id="40" data-poster="0"><b>40</b> Community-Based ILP for Application Mapping and Deadlock-Free Routing on Large NoCs
          <span class="tp-auth">Shuang Liu, Anisha Acharya and Martin Radetzki</span><span class="tp-spk">Speaker: Shuang Liu · University of Stuttgart</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="15" data-poster="0"><b>15</b> White Rabbit–Enabled Deterministic Triggering for Bi-Static ISAC in 6G
          <span class="tp-auth">Arthur Finkelmann, Christian Karle, Ulrich Langenbach, Vladimir Sidorenko, Benjamin Nuß, Jürgen Becker and Henrik Scheidt</span><span class="tp-spk">Speaker: Arthur Finkelmann · Karlsruhe Institute of Technology</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="91" data-poster="0"><b>91</b> Selective frame processing for accelerating visual SLAM
          <span class="tp-auth">Yihan Wang, Mehuli Ghosh, Jimil Irick, Kamil Amanowicz, Varun Darshana Parekh, Kevin Irick, Laurent Itti and Vijaykrishnan Narayanan</span><span class="tp-spk">Speaker: Antonis Savva · University of Cyprus</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="54" data-poster="0"><b>54</b> Impact of Programming Pattern Strategy on ReRAM Relaxation and Retention Stability <span class="tp-bpc">BPC</span>
          <span class="tp-auth">Marcelo Correa Cueto, Bastien Giraud, Marc Drouard, Gabriel Molas and Gaël Pillonnet</span><span class="tp-spk">Speaker: Marcelo Correa Cueto · Université Grenoble Alpes</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
      </ul>
    </td>
  </tr>
  <tr class="rik"><td class="tp-ca"></td><td class="tp-ct">11:40–12:20</td><td>
    <span class="tp-t">Industrial Keynote 3 – Bridging the Gap Between Research and Industry Through Embedded Systems</span>
    <span class="tp-s">Odysseas Economides · HardwareX Engineering, Cyprus · Plenary · Megaron AB · 40 min</span>
  </td></tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">12:20–13:20</td><td><span class="tp-t">Lunch Break</span><span class="tp-s">60 min</span></td></tr>
  <tr class="rs"><td class="tp-ca"></td><td class="tp-ct">13:20–14:50</td>
    <td class="tp-ch">
      <span class="tp-t">SS 150b – Sustainable Intelligence at the Edge (Part 2)</span>
      <span class="tp-s"><span class="tp-room">Megaron AB</span>
      <span class="tp-mode">Papers: 16 min talk + 4 min Q&amp;A</span>
      <span class="tp-chair" data-chair="Cathal Hoare · Tiziana Margaria">Session Chair(s): Cathal Hoare · Tiziana Margaria (organizers)</span>Organizers: Cathal Hoare · Tiziana Margaria · 4 papers · 90 min</span>
      <ul class="tp-pp">
        <li data-id="163" data-poster="0"><b>163</b> LLM-Driven Optimization of Large Language Model Inference
          <span class="tp-auth">Amir Aminifar</span><span class="tp-spk">Speaker: Amir Aminifar · Lund University</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="164" data-poster="0"><b>164</b> A Federated Cyber-Physical Edge Architecture for Smart Hospital Room Automation
          <span class="tp-auth">Matteo Iervasi, Tawite Noe Marthe, Mascuud Mohamed Ali, Abdulaziz Abdulkadir Hassan and Florenc Demrozi</span><span class="tp-spk">Speaker: Florenc Demrozi · University of Stavanger</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="170" data-poster="0"><b>170</b> Toward a Unified Memristive Edge Platform for Sensing, Security, and Neuromorphic Computing
          <span class="tp-auth">Heba Abunahla</span><span class="tp-spk">Speaker: Heba Abunahla · TU Delft</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="171" data-poster="0"><b>171</b> Embedded Intelligence at the Edge: Recommender Systems, Efficient Simulation, and Operator-Centred Decision Support
          <span class="tp-auth">Cathal Hoare and Tiziana Margaria</span><span class="tp-spk">Speaker: Cathal Hoare · University College Dublin</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
      </ul>
    </td>
    <td class="tp-ch">
      <span class="tp-t">SS 16 – Design, Testing &amp; Reliability of Memristive-based Compute-in-Memory Architectures</span>
      <span class="tp-s"><span class="tp-room">Megaron C</span>
      <span class="tp-mode">Papers: 16 min talk + 4 min Q&amp;A</span>
      <span class="tp-chair" data-chair="Surendra Hemaram · Anteneh Gebregiorgis">Session Chair(s): Surendra Hemaram · Anteneh Gebregiorgis (organizers)</span>Organizers: Surendra Hemaram · Anteneh Gebregiorgis · 1 invited talk + 3 papers · 90 min</span>
      <ul class="tp-pp">
        <li class="tp-inv"><b>–</b> Emerging Compute Paradigms – Opportunities and Challenges <em>(invited)</em>
          <span class="tp-auth">Norbert Wehn</span></li>
        <li data-id="167" data-poster="0"><b>167</b> ECC-Assisted Fault Tolerance in Memristive Crossbar-based CIM Architectures: An Overview
          <span class="tp-auth">Surendra Hemaram, Said Hamdioui and Anteneh Gebregiorgis</span><span class="tp-spk">Speaker: Surendra Hemaram · TU Delft</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="169" data-poster="0"><b>169</b> Variability Aware Neuro-Memristive Networks: Hardware Software Co-design Approaches
          <span class="tp-auth">Aleena Kabeer, Darshitha Dinesh and Alex James</span><span class="tp-spk">Speaker: TBC</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
        <li data-id="175" data-poster="0"><b>175</b> Testing RRAM-Based Brain-Inspired Architectures after Manufacturing: Challenges and Solutions
          <span class="tp-auth">Leticia Maria Bolzani Poehls and Andre Lucas Chinazzo</span><span class="tp-spk">Speaker: Leticia Maria Bolzani Poehls · IHP GmbH</span><span class="tp-fmt">16 min talk + 4 min Q&amp;A</span></li>
      </ul>
    </td>
  </tr>
  <tr class="rb"><td class="tp-ca"></td><td class="tp-ct">14:50–15:10</td><td><span class="tp-t">Coffee Break</span><span class="tp-s">20 min</span></td></tr>
  <tr class="rc"><td class="tp-ca"></td><td class="tp-ct">15:10–16:10</td><td>
    <span class="tp-t">Closing Ceremony &amp; Awards</span>
    <span class="tp-s">Plenary · Megaron AB · Conference ends 16:10</span>
  </td></tr>
</table>

<div class="justify-content-center txtcenter" id="soc">
      <h2 class="ops-tt txtcenter mts-10">SOCIAL PROGRAM</h2>
      <br />
      <p class="ops-t txtcenter same-line">Join us for two social gatherings during the conference — a great opportunity to connect with colleagues and peers outside of the technical sessions.</p>
      <br />

      <div class="row col-md-12" style="margin-bottom:40px; text-align:left">
         <div class="col-md-12">
            <h3 style="color:#1a2a4a; margin-bottom:20px"><b>Welcome Reception</b></h3>
            <p class="ops-t" style="margin-bottom:10px"><b>Date:</b> Monday, 12 October &nbsp;·&nbsp; <b>Time:</b> 17:30–19:00 &nbsp;·&nbsp; <b>Location:</b> Venue hotel grounds <span style="font-size:0.9em; color:#666">(exact location may vary depending on weather)</span></p>
            <div style="text-align:justify; margin-bottom:20px">
               <p class="ops-t">The Welcome Reception is the first social gathering between all conference delegates and it will take place at the St. Raphael Resort. It will be a relaxing evening during which delegates will have the opportunity to talk to colleagues and peers, while enjoying local drinks and ample canapés, with a view of the calming waters of the Mediterranean Sea.</p>
               <br />
               <div style="display:grid; grid-template-columns:1fr 1fr; gap:15px; margin:25px 0">
                  <img src="{{ '/img/event/cocktail-1.jpg' | relative_url }}" alt="Welcome Reception canapés" style="width:100%; height:300px; object-fit:cover; border-radius:5px;">
                  <img src="{{ '/img/event/cocktail-2.jpeg' | relative_url }}" alt="Welcome Reception spread" style="width:100%; height:300px; object-fit:cover; border-radius:5px;">
               </div>
            </div>
         </div>
      </div>

      <div class="row col-md-12" style="margin-bottom:40px; text-align:left">
         <div class="col-md-12">
            <h3 style="color:#1a2a4a; margin-bottom:20px"><b>Tour and Conference Dinner</b></h3>
            <p class="ops-t" style="margin-bottom:10px"><b>Date:</b> Tuesday, 13 October &nbsp;·&nbsp; <b>Departure:</b> 17:15 from the Hotel Lobby <span style="font-size:0.9em; color:#666">(please meet at the Lobby at 17:00)</span></p>
            <div style="text-align:justify; margin-bottom:20px">
               <p class="ops-t">We will depart from St. Raphael Resort by air-conditioned buses with licensed tour guides for a walking tour (weather permitting) of the historical sites and landmarks in the centre of Limassol. We will then head to a local tavern for an authentic Cypriot meze dinner accompanied by local drinks and desserts and live traditional entertainment. Upon return, the buses will be stopping at all conference hotels.</p>
               <br />
               <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:15px; margin:25px 0">
                  <img src="{{ '/img/event/cyprus-meze.jpg' | relative_url }}" alt="Cypriot meze dinner" style="width:100%; height:300px; object-fit:cover; border-radius:5px;">
                  <img src="{{ '/img/event/cyprus-entertainment.jpg' | relative_url }}" alt="Traditional Cypriot entertainment" style="width:100%; height:300px; object-fit:cover; border-radius:5px;">
                  <img src="{{ '/img/event/cyprus-night.jpeg' | relative_url }}" alt="Conference dinner evening" style="width:100%; height:300px; object-fit:cover; border-radius:5px;">
               </div>
            </div>
         </div>
      </div>

      <br />
   </div>
</div>

<script>
(function () {
  var norm = function (t) { return (t || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/\s+/g, ' ').trim(); };
  var root = document.getElementById('tec-schedule'), idx = [];
  function ctx(el) {
    var td = el.closest('td'), tr = el.closest('tr'), tbl = el.closest('table');
    var day = tbl.previousElementSibling;
    while (day && !day.classList.contains('tp-day')) day = day.previousElementSibling;
    var room = td.querySelector('.tp-room');
    return { session: td.querySelector('.tp-t').textContent, time: tr.querySelector('.tp-ct').textContent,
             day: day ? day.textContent : '', room: room ? room.textContent : '' };
  }
  root.querySelectorAll('li[data-id]').forEach(function (li) {
    li.id = 'paper-' + li.dataset.id;
    var o = ctx(li);
    o.type = 'paper'; o.el = li; o.id = li.dataset.id; o.poster = li.dataset.poster === '1';
    o.title = li.querySelector('b').nextSibling.textContent.trim();
    o.authors = li.querySelector('.tp-auth').textContent;
    o.speaker = li.querySelector('.tp-spk').textContent.replace(/^Speaker: /, '');
    o.fmt = li.querySelector('.tp-fmt').textContent;
    o.key = norm(o.id + ' ' + o.title + ' ' + o.authors + ' ' + o.speaker);
    idx.push(o);
  });
  root.querySelectorAll('.tp-chair').forEach(function (c, i) {
    var o = ctx(c), td = c.closest('td');
    td.id = td.id || ('session-' + i);
    o.type = 'chair'; o.anchor = td.id; o.name = c.dataset.chair; o.key = norm(o.name);
    idx.push(o);
  });
  var q = document.getElementById('tp-q'), out = document.getElementById('tp-results');
  function esc(t) { var d = document.createElement('div'); d.textContent = t; return d.innerHTML; }
  function where(o) {
    return '<span class="k">When/where:</span> ' + esc(o.day) + ' · ' + esc(o.time) + (o.room ? ' · Room ' + esc(o.room) : '') +
      '<br><span class="k">Session:</span> ' + esc(o.session);
  }
  function run() {
    root.querySelectorAll('.tp-hit').forEach(function (e) { e.classList.remove('tp-hit'); });
    var v = norm(q.value); out.innerHTML = '';
    var isId = /^\d+$/.test(v);
    if (!isId && v.length < 2) return;
    var terms = v.split(' ');
    var hits = idx.filter(function (o) {
      if (isId) return o.type === 'paper' && o.id === v;
      return terms.every(function (t) { return o.key.indexOf(t) > -1; });
    }).slice(0, 25);
    if (!hits.length) {
      out.innerHTML = '<div class="tp-none">No matching paper or session found. Try a paper ID, a surname or a word from the title.</div>';
      return;
    }
    out.innerHTML = hits.map(function (o) {
      if (o.type === 'chair') {
        return '<div class="tp-card ch"><b>Session chair: ' + esc(o.name) + '</b><br>' + where(o) +
          '<br><a href="#' + o.anchor + '">Show in program ↓</a></div>';
      }
      return '<div class="tp-card' + (o.poster ? ' po' : '') + '"><b>#' + esc(o.id) + ' – ' + esc(o.title) + '</b><br>' +
        '<span class="k">Authors:</span> ' + esc(o.authors) + '<br><span class="k">Speaker:</span> ' + esc(o.speaker) + '<br>' + where(o) + '<br>' +
        '<span class="k">Presentation:</span> ' + esc(o.fmt) +
        (o.poster ? ' in the session; the poster is also displayed during the coffee breaks on Tue 15:45–16:05 and Wed 10:00–10:20' : '') +
        '<br><a href="#paper-' + esc(o.id) + '">Show in program ↓</a></div>';
    }).join('');
    hits.forEach(function (o) { if (o.type === 'paper') o.el.classList.add('tp-hit'); });
  }
  q.addEventListener('input', run);
})();
</script>
