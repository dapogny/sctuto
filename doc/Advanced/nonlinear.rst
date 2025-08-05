.. _sec.nonlinear:

A first encounter with nonlinear problems
==========================================

.. ##########
.. ##########

This section deals with nonlinear variational problems, essentially exemplifying the use of Newton's method in this context. 
We shall retrieve similar techniques later on, in our study of :ref:`non linear elasticity problems <sec.hyperelasticity>` or the :ref:`Navier-Stokes equations <sec.hyperelasticity>`.

A good reference about the use of Newton's method in multiple contexts is :cite:`deuflhard2011newton`.

.. #######

.. figure:: ../figures/under_work.png
   :scale: 40 %

.. #######

.. ##########
.. ##########

.. _sec.Newton:

The Newton-Raphson method
--------------------------

.. ##########
.. ##########

Let $X, Y$ be two Banach spaces and let $F : X \to Y$ be a differentiable mapping; we search for a solution $x \in X$ to the (a priori nonlinear) equation:

.. math:: 
  :label: eq.Newtonsearch
  
  \text{Search for } x \in X, \:\:\text{ s.t. }\:\: F(x) = 0.

To achieve this goal, the Newton-Raphson method starts from an initial guess $x_0$, and then produces a series of points $x^n$, $n = 0,...,$ where each successive term $x^{n+1}$ is obtained from $x^n$ via application of a \"small\" correction $h^n$:

$$x^{n+1} = x^n + h^n.$$ 

The correction $h^n$ is calculated from a linearization of the original equation :math:numref:`eq.Newtonsearch` about the current iterate $x^n$:

$$F(x^n + h^n) = 0 \text{ is replaced by } F(x^n) + F^\prime(x^n)(h^n) = 0;$$

in other terms, we solve the following equation:

.. math:: 
  :label: eq.Newtonlin

  F^\prime(x^n)(h^n) =−F(x^n).

The Newton-Raphson method reads as follows.

  - Initialization: Select an initial guess $x^0 \in X$.
  
  - For $n=0,\ldots,$ until convergence: 
  
    - Calculate the solution $h^n$ to the linearized equation :math:numref:`eq.Newtonlin`. 
       
    - Set $x^{n+1} = x^n + h^n$.


This procedure converges quite fast—in principle—to one solution to the equation (3.2.3). Let us em-
phasize on one major drawback of the Newton-Raphson procedure. Depending on the particular function
A(x) and the initial guess x0, this procedure may experience diﬃculties in convergence.


Talk about continuation -- sometimes called \"homotopy\" in the literature. 

.. ##########
.. ##########

An application example: a non linear Laplace equation
-----------------------------------------------------

.. ##########
.. ##########

This problem originates from magnetostatics. 
