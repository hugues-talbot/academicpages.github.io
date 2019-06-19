---
title: "Research"
permalink: /research/
author_profile: true
---


I'm a researcher in [computer vision](https://en.wikipedia.org/wiki/Computer_vision), which is a very wide field. My interests include:

 * AI - Machine learning 
 * Medical imaging 
 * Image segmentation
 * Optimisation
 * Mathematical morphology

I'll try and give a bit of context around these items

### AI - Machine learning
Artificial Intelligence (AI) is a very popular and hot research topic at present. In the context of
computer vision, AI is useful for detecting and classifying regions of interests in images (objects).
This is important in many contexts, for example in medicine; but also in bio-medicine (cellular imaging)
and many other contexts.

### Medical imaging
[Medical imaging](https://en.wikipedia.org/wiki/Medical_imaging) is closely linked with the medical specialties of [radiology](https://en.wikipedia.org/wiki/Radiology) and [nuclear imaging](https://en.wikipedia.org/wiki/Nuclear_medicine). The
context is to help medical doctors discover and diagnose diseases, as well as treat and follow up patients with these diseases.
Some diseases do not have an immediate imaging aspect but many do. In the last few years, I've been involved in
projects around:

 * The vascular system of the brain via the [Vivabrain](https://anr.fr/Projet-ANR-12-MONU-0010) project. See also [here](http://icube-vivabrain.unistra.fr/index.php/Presentation).
  * The vascular system of the heart
  * Skin lesions classification, in particular for diagnosing melanoma.

More recently, I've been working in Oncology (cancer therapy) in collaboration with physicians from [Institut Gustave Roussy](https://www.gustaveroussy.fr/en) (IGR).

### Image segmentation
Image segmentation is the process of discovering and identifying objects in images. It is a fundamental problem
in computer vision and equivalent in difficulty with AI.


### Optimisation
Mathematical optimisation is an area of applied mathematics. This is a very powerful modeling tool.
Most processes in physics and in biology are the result of an optimisation process. For example, the
way light travels in a medium can be interpreted in terms of a shortest path between two points.

Many problems in imaging are the results of imperfect observations, resulting in fuzzy and noisy
images. Recovering clean data from noisy observation can be formulated as an _inverse problem_, for
which optimisation is a natural framework.

Image segmentation, computer-aided tomography, MRI imaging, are all instances of inverse problems
for which optimisation can be useful.

There are many sub-areas of optimisation. Beyond inverse problems I'm also interested in efficient
discrete optimisation algorithms. Computer scientists like to use these extensively, particularly
in relation with graph theory.

### Mathematical morphology
Mathematical morphology is a well-developed, non-linear theory of imaging. I've been working in
this area since my PhD days, and I still contribute regularly.

{% comment %}
{% include base_path %}


{% for post in site.research %}
  {% include archive-single.html %}
{% endfor %}

{% endcomment %}

