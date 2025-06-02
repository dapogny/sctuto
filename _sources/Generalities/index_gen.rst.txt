.. _chap.start:

Getting started
================

This chapter introduces the fundamental mathematical background for the Finite Element method.
The first :numref:`sec.anafunc`, :numref:`sec.LM` and :numref:`sec.FE` are mainly of mathematical nature, and contain rudiments about functional analysis, variational problems, and the theory behind the Finite Element Method.
The next :numref:`sec.lap` and :numref:`sec.visu` are oriented towards practice: convenient numerical softwares are presented, notably the $\texttt{FreeFem}$ environment and $\texttt{medit}$. 
Eventually, :numref:`sec.eigen`, :numref:`sec.dirtgv` and :numref:`sec.lappureNeumann` are application examples that are interesting per se, and are carefully detailed, offering opportunities to showcase some of the building blocks of the methods developed in the subsequent chapters.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Functional analysis <anafunc.rst>
   Lax-Milgram framework <varpbs.rst>
   The Finite Element method <FEtheory.rst>
   Laplace equation <laplace.rst>
   Visualization <visualization.rst>
   Meshes <mesh.rst>
   Eigenvalues <eigen.rst>
   Penalization for Dirichlet conditions <dirpen.rst>
   Pure Neumann <laplace_pure_Neumann.rst>

