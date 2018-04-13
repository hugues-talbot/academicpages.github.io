---
title: "Discrete Optimisation"
collection: teaching
type: "Full course"
permalink: /teaching/2018_Discrete_Optimisation_CS
venue: "Centrale Supelec"
date: 2018-04-01
location: "Saclay, France"
---

Discrete Optimisation
===============

Discrete optimisation is a very large topic, that includes in particular
ways to formulate and solve combinatorial search and enumeration problem, which
are ubiquitous in Computer Science, Applied Mathematics, Operational
Research, Machine Learning, and more.

If you've ever wondered how to program a Sudoku solver for instance,
and how complex it would be, this course will tell you exactly how to
do it.

In this course, we begin with linear programming, which is a starting
point for many discrete-based algorithms. We consider the contraints
of adding integer and binary constraints, which allows us to formulate
decision problems, in particular NP-complete problems.

We next consider specialized algorithms for which enumeration is fast
and efficient, such as transport and flow problems.

All along the course we provide numerous examples and tutorial sessions.


Lecture 1
--------


[Introduction](/files/01_intro_optim_en.pdf)

Lecture 2
--------

[The Simplex algorithm](/files/02_simplexe_en.pdf)

Tutorial 1
--------

Simplex algorithm, examples, formulations: [Tutorial 1 text](/files/TD1-algo_en.pdf)

Solution: [Tutorial 1 solution](/files/TD1-solution.pdf)

Lecture 3
--------

[Limit cases of the Simplex](/files/03_limites_en.pdf)

Lecture 4
--------

[Duality](/files/04_duality_en.pdf)

Tutorial 2
--------

Solving LP problems with spreadsheets, duality:
[Tutorial 2 text](/files/TD2_optim_en.pdf)

Code 1
--------
Here you will find verbose, straightforward, numpy-based code for the
simplex.

Here is the basic code, [a Python Simplex solver](/files/simplexe.py),
with no claim with respect to efficiency. Here is a 
[Python Notebook](/files/Simplexe.ipynb), with worked out examples.

I recommend you try the Python Notebook version. Here is the
[online rendering](https://nbviewer.jupyter.org/urls/hugues-talbot.github.io/files/Simplexe.ipynb)
of this notebook. 

Lecture 5
-------

[Formulation of Integer Programming problems](/files/05_ip_formulation_en.pdf)

Lecture 6
-------

[Solution of Integer Programming problems](/files/06_resolution_en.pdf)
