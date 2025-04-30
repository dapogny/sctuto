Numerical tours in scientific computing
=======================================

This online book is a series of tutorials, intended as a comprehensive introduction to various aspects of scientific computing. 
It is mainly aimed to graduate students, although the most basic contents should already be available to undergraduates.
It might also be useful to researchers that have little prior knowledge about this field and wish to get more familiar with some of its aspects.
It is eventually for... me, a selfish excuse to learn many things!

These tours are intended to be pedagogic; the presentation is not minimal, and repetitions occur between different sections.
They are oriented towards practical and numerical applications. (Sketches of) Proofs are given when they help intuition; further details for the curious reader are provided in appendices, or in hidden boxes.

These tours are nowhere set in stone; quite the contrary, they are meant to evolve continuously. Please do not hesitate to contact me for any mistake or inappropriate content... and also to suggest your own application that I will happily upload!

Before getting started, let us highlight a few useful references.

  - The online `$\texttt{FreeFem}$ documentation <https://doc.freefem.org/introduction/index.html>`_  is a very rich source of various physical problems addressed with $\texttt{FreeFem}$.
  
  - The recent book :cite:`hecht2024pde` is focused on PDE-constrained optimization problems, solved with $\texttt{FreeFem}$. It can be freely downloaded `here <https://hal.science/hal-04724788/>`_.

Additionally, other online tutorials are available about (more or less closely) related topics: 
  
  - The amazing `Numerical Tours <http://www.numerical-tours.com/>`_ by G. Peyré offer an exhaustive overview of multiple issues in imaging and learning.
  
  - The `Numerical Tours in continuum mechanics <https://comet-fenics.readthedocs.io/en/latest/index.html>`_ by J. Bleyer revolve around various models in continuum mechanics. 
  
  - The `NGSolve tutorials <https://docu.ngsolve.org/ngs24/intro.html>`_ contain presentations of a full series of physical models, and their solution with the software $\texttt{NGSolve}$.


.. toctree::
   :numbered:
   :maxdepth: 2
   :caption: Contents:

   Generalities <Generalities/index_gen.rst>
   Advanced features <Advanced/index_adv.rst>
   Structure mechanics <Structure_Mechanics/index_structmech.rst>
   Fluid mechanics <Fluid_Mechanics/index_fl.rst>
   Optimal design <Optimal_design/index_od.rst>
   Appendix <Appendix/index_app.rst>
   Bibliography <Generalities/bibliography.rst>
   Glossary <Generalities/glossary.rst>
