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



Lectures
--------

| Entry                                                  | Description                                                 |
| --------                                               |------------------------------------------------------------ |
| [Introduction](/files/01_intro_optim_en.pdf)           | Introduction to optimisation                                |
| [The Simplex algorithm](/files/02_simplexe_en.pdf)     | An algorithm for solving linear programs                    |
| [Limit cases of the Simplex](/files/03_limites_en.pdf) | The limiting cases for the simplex, like how to start it    |
| [Duality](/files/04_duality_en.pdf)                    | LP and duality. Interpretation and algorithms               |
| [Integer Programming](/files/05_ip_formulation_en.pdf) | Formulation and examples                                    |
| [IP resolution](/files/06_resolution_en.pdf)           | Resolution of Integer Programs: Cuts and Branch & Bound     |
| [Transport Problems](/files/07_transport_formulation_en.pdf) | Transport problems are a simpler case of LP/IP        |
| [Resolution of transport problems](/files/08_transport_solution_en.pdf) | Resolution of transport problems           |
| [Network problems](/files/09_network_problems_en.pdf)  | Network problems, including maxflow and the network simplex |


Tutorials
---------

| Entry                                                  | Description                                                 |
| --------                                               |------------------------------------------------------------ |
| [Tutorial 1 text](/files/TD1-algo_en.pdf)              | Simplex algorithm, examples, formulations                   |
| [Tutorial 2 text](/files/TD2_optim_en.pdf)             | Solving LP problems with spreadsheets. Duality              |
| [Tutorial 3 text](/files/TD3-algo_en.pdf)              | This tutorial is on integer programming                     |
| [Tutorial 4 text](/files/TD4_cs_en.pdf)                | This tutorial is *assignment 1*                             |
| [solving the TSP](/files/TD5-tsp.pdf)                  | Solving the TSP. This is *assignment 2*                     |


Solutions
---------

| Entry                                                  | Description                                                 |
| --------                                               |------------------------------------------------------------ |
| [Tutorial 1 solution](/files/TD1-solution.pdf)         | Solution to the first tutorial |
| [a Python Simplex solver](/files/simplexe.py)          | Basic, commented Simplex solver |
| [Sudoku solver](/files/Sudoku_ilp.ipynb)               | It requires [cvxopt](http://cvxopt.org/install/index.html). |


Code 1
------

Here you will find verbose, straightforward, numpy-based code for the
simplex.

Here is the basic code, [a Python Simplex solver](/files/simplexe.py),
with no claim with respect to efficiency. Here is a 
[Python Notebook](/files/Simplexe.ipynb), with worked out examples.

I recommend you try the Python Notebook version. Here is the
[online rendering](https://nbviewer.jupyter.org/urls/hugues-talbot.github.io/files/Simplexe.ipynb)
of this notebook. 



Thanks
------

Special thank to Dr. Maria Vakalopoulou and Pr. Fragkiskos Maillaros.



Sudoku solver
-----------

Here is a nice [Sudoku solver](/files/Sudoku_ilp.ipynb) written in Python. It requires
[cvxopt](http://cvxopt.org/install/index.html).


Challenges 
---------

Students can elect to participate to a relevant Kaggle challenge. I recommend this new
[particle tracking](https://www.kaggle.com/c/trackml-particle-identification)
challenge. The top prize is 12,000\$ !

Other relevant challenges will be posted here.

Alternative project
-------------------

The Kaggle challenge is obviously very challenging. An alternative project is to implement
a peg-solitaire solver.

Here are a couple of articles on how this might be done [Article 1](/files/Peg_Solitaire_1.pdf) ; [Article 2](/files/Peg_Solitaire_2.pdf).




