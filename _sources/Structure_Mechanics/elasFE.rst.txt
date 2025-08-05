.. _sec.FEelas:

Resolution of the linear elasticity system with the Finite Element Method
==========================================================================

.. ##########
.. ##########

This section deals with the use of the Finite Element Method for the solution of the linear elasticity system.
Much of the treatment of this system is very similar to that of the Laplace equation and its avatars, discussed in :numref:`sec.lap`.


.. ##########
.. ##########

The variational setting for linear elasticity
----------------------------------------------

.. ##########
.. ##########

The variational formulation for this problem reads: 
$$\text{Search for } \u \in H^1_{\Gamma_D}(\Omega)^d \text{ s.t. } \forall \v \in H^1_{\Gamma_D}(\Omega)^d, \quad \int_\Omega Ae(\u) : e(\v) \:\d \x = \int_\Omega \f \cdot \v \:\d \x + \int_{\Gamma_N} \g \cdot \v \:\d s $$

The well-posedness of this problem follows from the classical Lax-Milgram theory, described in :numref:`sec.LM`. The only missing ingredient is the following result. 

.. ##########

.. prf:proposition:: Korn's inequality

   Assume that $\Gamma_D$ has non empty surface measure. Then there exists a constant $C >0$ such that: 
   
   $$\forall \u \in H^1_{\Gamma_D}(\Omega)^d, \quad \lvert\lvert \u \lvert\lvert_{H^1(\Omega)^d} ^2 \leq C \int_\Omega \lvert\lvert e(\u) \lvert\lvert^2 \:\d \x.$$    

.. ##########

The intuition about this result is the following: the displacement functions such that $e(\u)=0$ are the rigid-body motions, i.e. the compositions with translations and rotations. The rigid-body motions that vanish on a region of $\Gamma_D$ with positive surface measure must be zero.

Making this idea mathematically rigorous is quite difficult, and it goes beyond the scope of this book; we refer to Th. 6.3.4 in :cite:`ciarlet2021mathematical`.

.. ##########
.. admonition:: Exercise
  :class: admonition-exo

  Prove the well-posedness of the variational problem by admitting Korn's inequality. 

.. ##########

.. ##########
.. admonition:: Exercise (A study of rigid-body motions)
  :class: admonition-exo

  Bla bla 
  
.. ##########


.. ##########
.. ##########

Resolution of a basic problem in linear elasticity
---------------------------------------------------

.. ##########
.. ##########

.. ##########

.. _sec.FEElasBasic:

A basic resolution example
"""""""""""""""""""""""""""

.. ##########

Use of variational formulations over tensor product spaces.

Situation; connecting rod in internal combustion engines?
The small end of the rod is connected to the piston, and it undergoes linear motion (i.e inhomogeneous Neumann). 
The big end is connected to the cranckpin (homogeneous Dirichlet B.C.), and the goal of the device is to convert the input linear motion into rotational motion. 

Calculation of stress

.. ##########

.. _sec.visuElas:

A complement about vizualization of vector fields
""""""""""""""""""""""""""""""""""""""""""""""""""

.. ##########

Vizualization: 
- Vector fields with medit 
- How to toggle a displacement with medit. 


.. ##########
.. ##########

A bimaterial situation
-----------------------

.. ##########
.. ##########

Or multi-material, like in ferrite. 
Observe the deformations of the different materials, depending on the Young's modulus.

.. ##########
.. ##########

Vibrations in an elastic structure 
----------------------------------

.. ##########
.. ##########

This section deals with the calculation of eigenvalues of the linear elasticity system. It is the counterpart in this physical context of :numref:`sec.eigen`.


.. ##########

A few words about resonance of mechanical structures
"""""""""""""""""""""""""""""""""""""""""""""""""""""

.. ##########

Such modal analysis is very important in structural engineering, where for instance, a structure may continue to vibrate and take the form of the corresponding mode, when submitted to motion at this particular frequency (earthquake, pedestrians on a bridge).

Resonance frequencies are particularly harmful, especially when damping is low. Then, even a very small amount of input energy can result in large deformations.

Let us consider a volumic load $\f(t,\x)$ depending on time and space. One can prove that the elastic displacement is the solution $\u(t,\x)$ to the time-dependent version of the linear elasticity system:

$$\frac{\partial^2 \u}{\partial t^2}(t,\x) - \dv(\sigma)(t,\x) = \f(t,\x). $$

.. ##########

Numerical computation of structural resonances
"""""""""""""""""""""""""""""""""""""""""""""""

.. ##########

Shear wall example (crane? Mast?)


.. ##########
.. ##########

The ersatz material method
--------------------------

.. ##########
.. ##########


.. ##########
.. ##########

A 3d example
-------------

.. ##########
.. ##########

A beam with an I shaped cross-section.