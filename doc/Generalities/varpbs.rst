.. _sec.LM:

The Lax-Milgram variational theory
==================================

This section deals with the Lax-Milgram theory, which offers an elegant and efficient viewpoint on boundary value problems. 
It is in particular the conceptual basis of the Finite Element method for their numerical solution, which is the focus of the next :numref:`sec.FE`.

To set ideas, the guiding model of this presentation is the Laplace equation, equipped with homogeneous Dirichlet boundary conditions:

.. math::
  :label: eq:lap
  
  \left\{
  \begin{array}{cl}
  -\Delta u = f & \text{in } \Omega, \\
  u=0 & \text{on } \partial \Omega.
  \end{array}
  \right.

Here, $\Omega$ is a bounded and Lipschitz domain in $\R^d$ ($d=2$ or $3$) and the source term $f$ belongs to $L^2(\Omega)$. 
The variational point of view consists in looking at a boundary value problem such as :math:numref:`eq:lap` as a variational problem, of the form:

.. math::
  :label: eq:lapvarfLM

  \text{Search for } u \in V \text{ s.t. } \forall v \in V, \:\: a(u,v) = \ell(v),
  
where
 - $V$ is a suitable functional space,
 - $a(\cdot,\cdot)$ is a bilinear form on $V$, which encodes the differential operator at play ($-\Delta$ in the present case),
 - $\ell : V \to \R$ is a linear form, depending on the data of the problem (here, the source $f$).
 
From the theoretical perspective, this variational framework makes it possible to derive simple and powerful conditions guaranteeing the well-posedness of a boundary value problem of the form :math:numref:`eq:lap`. In numerical practice, it is the basic ingredient of the Finite Element Method, as we shall see in the next :numref:`sec.FE`.

.. ##################################################
.. ##################################################

.. _sec.bvptovarf: 

From classical boundary-value problems to their variational formulations
-------------------------------------------------------------------------

.. ##################################################
.. ##################################################

The variational point of view over boundary value problems originates from the idea of duality, underlying the :ref:`theory of distributions <app.distrib>`, that we have broached (and actually, carefully avoided) in :numref:`sec.Sobolev`. A function $u$ is seen through via its effect by integration against a collection of test functions. Pushing this idea a little further, the fulfillment of a boundary value problem is evaluated against suitable test functions. 

For concreteness, let us illustrate this idea with our model problem :math:numref:`eq:lap`. Assuming for the moment that the latter has a smooth solution, multiplication of the main equation by a smooth test function $v$ yields:

$$- \int_\Omega \Delta u v \:\d \x = \int_\Omega fv \:\d \x. $$

Now using the :ref:`Green's formula <sec.Green>`, we obtain:

.. math:: 
  :label: eq:avtvar

  - \int_{\partial \Omega} \frac{\partial u}{\partial n} v \:\d s + \int_\Omega \nabla u \cdot \nabla v \:\d \x = \int_\Omega f v \:\d \x,

an equation that involves only the first-order derivatives of $u$. Since $u$ satisfies the boundary condition $u=0$ on $\partial \Omega$, it is tempting to require the same behavior from $v$, which yields:

.. math::
  :label: eq:var
  
  \int_{\Omega}{\nabla u \cdot \nabla v \:\d\x} = \int_\Omega{fv\:\d\x}.


Let us now wonder under which conditions on the sought function $u$ and the test function $v$ the above identity :math:numref:`eq:var` actually makes sense.
 - The integral in the left-hand side of :math:numref:`eq:var` is well-defined as soon as the derivatives of $u$ and $v$ belong to $L^2(\Omega)$, which is the case if $u,v \in H^1(\Omega)$.
 - The integral in the right-hand side of :math:numref:`eq:var` makes sense, in particular, if $f \in L^2(\Omega)$ and $v \in H^1(\Omega)$.
 - The boundary condition $u=0$ on $\partial \Omega$ can be understood in the :ref:`sense of traces <sec.traces>` if $u$ is assumed to lie in $H^1(\Omega)$. Moreover, we managed to get rid of the boundary integral in :math:numref:`eq:avtvar` by assuming the same behavior for the test function $v$.  

All in all, the expression :math:numref:`eq:var` entices us to search for a weak solution of :math:numref:`eq:lap` as the solution to the following variational problem, that is called the \"weak formulation\" of :math:numref:`eq:lap`:


.. math::
  :label: eq:vardefinitive
  
  \text{Search for } u \in H^1_0(\Omega) \text{ s.t. } \forall v \in H^1_0(\Omega), \:\: \int_\Omega{\nabla u \cdot \nabla v \:\d\x} = \int_\Omega{fv\:\d\x}.

In spite of its a priori unintuitive character, the above variational problem is much easier to analyze than the original version :math:numref:`eq:lap`. The main motivation of the above derivation is that there is a wonderful mathematical theory devoted to the well-posedness of such problems, as we are going to see in the sequel. 

Before we do so, let us insist that the above conversion of the original \"strong\" form of the problem :math:numref:`eq:lap` into its weak form :math:numref:`eq:vardefinitive` is merely formal: for instance, we have never claimed that a function $u$ is solution to the former if and only if it is solution to the latter. Actually, we have not even specified what we mean for a function $u$ to be a solution to :math:numref:`eq:lap` (whereas this notion is clear for the variational problem :math:numref:`eq:vardefinitive`)! The next proposition somehow elucidates this connection between both formulations with the help of the theory of distributions; it can be omitted on first reading. 

.. ################
.. prf:proposition::

   Let $u$ be a function in $H^1_0(\Omega)$; then $u$ is one solution to the variational problem :math:numref:`eq:vardefinitive` if and only if it holds:
  
   $$-\Delta u = f \text{ in the sense of distributions on }\Omega.$$

.. ################

.. ##########
.. admonition:: Proof
    :class: dropdown

    Let $u$ be a function in $H^1_0(\Omega)$. 
    
    If $u$ satisfies $-\Delta u = f$ in the sense of distributions in $\Omega$, then by definition of the Laplace operator in the sense of distributions, it holds:
    
    .. math:: 
      :label: eq:varfproofeqvar
      
      \text{For all test function } \varphi \in \calC^\infty_c(\Omega), \quad \int_\Omega \nabla u \cdot \nabla \varphi \:\d \x = \int_\Omega f \varphi \:\d\x. 
     
    Now since by definition $\calC^\infty(\Omega)$ is dense in $H^1_0(\Omega)$, for all function $v \in H^1_0(\Omega)$, there exists a sequence $\varphi_n \in \calC^\infty(\Omega)$ such that:
     
    $$\lvert\lvert v -\varphi_n \lvert\lvert_{H^1_0(\Omega)} \xrightarrow{n \to \infty} 0.$$
     
    Hence, using the relation :math:numref:`eq:varfproofeqvar` for each $n$ and letting $n$ tend to infinity, we obtain that:
     
    $$\forall \varphi \in H^1_0(\Omega), \quad \int_\Omega \nabla u \cdot \nabla v \:\d \x = \int_\Omega f \varphi \:\d\x,$$
     
    i.e. $u$ is one solution to the variational problem :math:numref:`eq:vardefinitive`. 
    
    Conversely, if $u \in H^1_0(\Omega)$ is one solution to :math:numref:`eq:vardefinitive`, then, in particular, it satisfies this problem for functions $\varphi \in \calC^\infty_c(\Omega)$, and so it satisfies $-\Delta u = f$ in the sense of distributions in $\Omega$.
     
.. ##########

In this course, we shall not dwell on the equivalence between the \"classical\" strong form of a boundary-value problem and its variational counterpart, and we shall actually define a \"solution\" to a boundary-value problem as a solution to its variational form. 

.. ##################################################
.. ##################################################

.. _sec.LaxMilgram:

The abstract Lax-Milgram theory
--------------------------------

.. ##################################################
.. ##################################################

This subsection deals with abstract variational problems. The setting is the following:
let :math:`V` be a (real) Hilbert space, :math:`a(\cdot, \cdot) : V \times V \to \mathbb{R}` be a bilinear form, and :math:`\ell : V \to \mathbb{R}` be a linear form. We consider a variational problem of the form:

.. math::
  :label: eq.varpb

  \text{Search for } u \in V \text{ such that: } \forall v \in V, \:\: a(u,v) = \ell(v).

In particular, this setting applies directly to the variational formulation :math:numref:`eq:var` for :math:numref:`eq:lap` by taking:

.. math::
  V = H^1_0(\Omega), \:\: a(u,v) = \int_\Omega \nabla u \cdot \nabla v \:\d \x, \text{ and } \ell(v) = \int_\Omega fv\:\d\x.

The well-known Lax-Milgram theorem gives sufficient conditions, which are often satisfied in practice, for this problem to be well-posed:

.. _th.LaxMilgram:

.. prf:theorem:: Lax Milgram
  
  Let $V$ be a real Hilbert space, $a: V \times V \to \mathbb{R}$ be a bilinear form, and $\ell: V \to \mathbb{R}$ be a linear form. Assume that:
  
    -  The bilinear form $a$ is continuous: there exists $M \geq 0$ such that
    
         .. math::
            \forall u,v \in V, \:\: | a(u,v) | \leq M || u || || v ||.
            
    -  The form $a$ is coercive: there exists $\alpha >0$ such that:
    
          .. math::
             \forall u \in V, \:\: \alpha || u ||^2 \leq a(u,u).
             
    -  The linear form $\ell$ is continuous.

  Then, there exists a unique function $u$ satisfying :math:numref:`eq.varpb`. The latter additionally fulfills the following a priori estimate:
  
  .. math::
    :label: eq.stabLM
     
       \lvert\lvert u \lvert\lvert \leq \frac{1}{\alpha} \lvert\lvert \ell \lvert\lvert_{V^*}.

Let us check that the variational problem :math:numref:`eq.varpb` associated to the Laplace equation :math:numref:`eq:lap` satisfies the assumptions of the Lax-Milgram theorem:

  - As we have seen in :numref:`sec.Sobolev`, the space $V = H^1_0(\Omega)$ is a Hilbert space.
  
  - The form $a(\cdot, \cdot)$ defined in :math:numref:`eq:lapvarfLM` is coercive, since, for any $u \in V$,
    
    $$a(u,u) = \int_\Omega \lvert \nabla u \lvert^2\:\d\x \geq \alpha \lvert\lvert u \lvert\lvert^2_{H^1(\Omega)} \text{ for some constant } \alpha >0, $$
  
    as follows from the :ref:`Poincaré inequality <prop.Poincare>`.
  
  - The linear form $\ell$ is continuous, since by the Cauchy-Schwarz inequality, it holds:
  
    $$\lvert \ell(u)\lvert = \left\lvert \int_\Omega f u \:\d\x \right\lvert \leq \lvert\lvert f \lvert\lvert_{L^2(\Omega)}\lvert\lvert u \lvert\lvert_{L^2(\Omega)} \leq  \lvert\lvert f \lvert\lvert_{L^2(\Omega)}\lvert\lvert u \lvert\lvert_{H^1(\Omega)}.$$

.. prf:remark::

  - The inequality :math:numref:`eq.stabLM` is an important conclusion of the :ref:`Lax-Milgram theorem <th.LaxMilgram>`. It indeed guarantees that the solution $u$ to :math:numref:`eq.varpb` depends continuously on the \"data\" $\ell$, i.e. that the following linear mapping is continuous:
  
  $$V^* \ni \ell \mapsto \text{ the solution } u \text{ with right-hand side } \ell.$$
  
    In particular, a small perturbation of the right-hand side $\ell$ does not degrade \"too much\" the solution $u$.
  
  - The conditions of the Lax-Milgram theorem are only sufficient, and not necessary: it may very well happen that the problem :math:numref:`eq:lapvarfLM` be well-posed while $a$ is not coercive. We shall return in a next chapter to other types of conditions ensuring this well-posedness.
  
The :ref:`Lax-Milgram theorem <th.LaxMilgram>` has the following useful \"energetic version\", which expresses the solution $u$ to the variational problem :math:numref:`eq.varpb` as the unique minimizer of an energy functional.

.. ##########

.. _lem.corlM:

.. prf:lemma::
  
  Let $V$ be a Hilbert space, and let $a(\cdot,\cdot): V \times V \to \R$ and $\ell : V \to \R$ be bilinear and linear forms on $V$, respectively. We assume that the hypotheses of the :ref:`Lax-Milgram theorem <th.LaxMilgram>` are satisfied, and that, in addition, the bilinear form $a(\cdot,\cdot)$ is symmetric, i.e.
  
  $$\forall u, v \in V, \quad a(u,v) = a(v,u).$$
  
  Then, the energy functional $J:V \to \R$ defined by
  
  $$J(u) = \frac{1}{2} a(u,u) - \ell(u)$$
  
  has a unique minimizer over $V$, which is the unique solution to the variational problem :math:numref:`eq.varpb`.

.. ##########

.. ##########
.. admonition:: Proof
    :class: dropdown

    Let $u^* \in V$ be the unique solution to :math:numref:`eq.varpb`, and let $u$ be any minimizer of $J$ over $V$, if any. We aim to show that  $u=u^*$. 
    
    The minimality of $J$ at $u$ implies that, for any $v \in V$ and $t >0$, it holds:
    
    $$J(u+tv) \geq J(u),$$
    
    By expanding the definition of $J$, using the symmetry of $a(\cdot,\cdot)$ and rearranging, we obtain:
    
    $$t a(u,v) + \frac{t^2}{2} a(v,v) - t \ell(v) \geq 0.$$
    
    Now dividing both sides by $t>0$ and letting $t$ tend to $0$, it follows:
    
    $$a(u,v) - \ell(v) \geq 0.$$
    
    Since the above reasoning is valid for arbitrary $v\in V$, repeating the argument with $-v$ in place of $v$, we actually obtain:
    
    $$\forall v \in V, \quad a(u,v) = \ell(v).$$
    
    Thus, we have proved that if $u$ is a minimizer of $J$ over $V$, it is necessarily one solution to the variational problem :math:numref:`eq.varpb`, which is unique by :numref:`th.LaxMilgram`. Hence, $u=u^*$.
    
    Conversely, let us prove that $u^*$ is one minimizer of $J$. Repetition of the above calculation yields:
    
    $$\begin{array}{ccl}
    \forall v \in V, \quad J(u^* + v) - J(v) &=& \underbrace{a(u^*,v)-\ell(v)}_{=0} + \frac{1}{2} a(v,v)\\
    &\geq& 0.\\
    \end{array}$$
      
    Hence, $u^*$ is one minimizer of $J$, which ends the proof.
.. ##########


.. ##################################################
.. ##################################################

.. _sec.varpbNeu:

A worked example: homogeneous Neumann boundary conditions
---------------------------------------------------------

.. ##################################################
.. ##################################################

Let us now consider the following Laplace-like problem, featuring homogeneous Neumann boundary conditions:

.. math::
  :label: eq:lapNeumann
  
  \left\{
  \begin{array}{cl}
  -\Delta u + u = f & \text{in } \Omega, \\
  \frac{\partial u}{\partial n}=0 & \text{on } \partial \Omega,
  \end{array}
  \right.

where the source term $f$ belongs to $L^2(\Omega)$. Note the presence of a $0^{\text{th}}$-order term in the main equation of :math:numref:`eq:lapNeumann`, whose relevance will show up a little later. 
  
To construct a variational formulation for this problem, we multiply the main equation with a smooth test function $v \in \calC^\infty(\overline \Omega)$, and we integrate. This yields:

$$-\int_\Omega \Delta u v \:\d \x + \int_\Omega uv \:\d \x = \int_\Omega fv \:\d \x.$$

An application of :ref:`Green's formula <th.Green>` now yields: 

.. math::
  :label: eq:lapNeumannvarf
  
  \int_\Omega \nabla u \cdot \nabla v \:\d \x + \int_\Omega uv \:\d \x = \int_\Omega fv \:\d \x,

where the boundary integral vanishes because of the boundary condition $\frac{\partial u}{\partial n} = 0$ on $\partial \Omega$. 

Let us now look at closer at the above variational problem, and wonder under which conditions it fits into the framework of the Lax-Milgram theory. At first, so that all the terms in there make sense, $u$ and the test function $v$ should be chosen in the space $H^1(\Omega)$ of functions having derivatives in $L^2(\Omega)$. Let us now verify that this formulation fulfills the assumptions of the :ref:`Lax-Milgram theorem <th.LaxMilgram>`: 

  - The bilinear form $a(u,v)$ is continuous on $H^1(\Omega)$.
  
  - It is coercive, indeed: 
  
    $$\forall u \in H^1(\Omega), \quad a(u,u) = \int_\Omega u^2 \:\d\x + \int_\Omega \lvert \nabla u \lvert^2 \:\d \x = \lvert\lvert u \lvert\lvert^2_{H^1(\Omega)}. $$
    
    This feature is due to the addition of a $0^{\text{th}}$-order term in the main equation of :math:numref:`eq:lapNeumann`.
    
  - The linear form $\ell$ is continuous on $L^2(\Omega)$, as in the previous section. 
  
Hence, the problem :math:numref:`eq:lapNeumannvarf` is well-posed.

.. ##########

.. _rm.eqstrongweakneu:
  
.. prf:remark::

  Let us briefly comment about the equivalence between the strong form :math:numref:`eq:lapNeumann` of the Neumann problem and its weak form :math:numref:`eq:lapNeumannvarf`:
  
  - If $u$ is a function in $H^1(\Omega)$ satisfying the problem :math:numref:`eq:lapNeumann`, then the main equation shows that $\nabla u \in \Hdiv(\Omega)$. Therefore, the normal trace $\frac{\partial u}{\partial n} = \nabla u \cdot \n$ is well-defined as an element in $H^{-1/2}(\partial \Omega)$, and the boundary condition in :math:numref:`eq:lapNeumann` makes sense in this space.
  
  - On the contrary, if $u$ is a function in $H^1(\Omega)$ satisfying the variational problem :math:numref:`eq:lapNeumannvarf`, then it follows immediately that $\nabla u$ belongs to $\Hdiv(\Omega)$. The first line of :math:numref:`eq:lapNeumann` holds true in the sense of distributions by restricting test functions to elements in $\calC^\infty_c(\Omega)$, and the boundary conditions holds true in $H^{-1/2}(\partial \Omega)$ on account of the trace theorem for functions in $\Hdiv(\Omega)$, see :numref:`prop.traceHdiv`.
  
.. ##########

.. ##########

.. admonition:: Exercise
  :class: admonition-exo

   In this exercise, the boundary $\partial\Omega$ of the domain $\Omega$ is made of two complementary open regions $\Gamma_D$, $\Gamma_N$: 
   
   $$\partial \Omega = \overline{\Gamma_D} \cup \overline{\Gamma_N}, \text{ where } \Gamma_D \cap \Gamma_N = \emptyset. $$
   
   We consider the following mixed Dirichlet-Neumann problem: 
   
   .. math::
     :label: eq:mixedLaplace 
  
     \left\{
     \begin{array}{cl}
     -\Delta u = f & \text{in } \Omega, \\
     u=0 & \text{on } \Gamma_D,\\
     \frac{\partial u}{\partial n}=0 & \text{on } \Gamma_N.
     \end{array}
     \right.
     
  1 - Prove that the function space $H^1_{\Gamma_D}(\Omega)$, defined by:
   
  $$H^1_{\Gamma_D}(\Omega)  = \left\{u \in H^1(\Omega) \text{ s.t. } u =0 \text{ on } \Gamma_D \right\}$$
  
  is a Hilbert space when equipped with the classical inner product of $H^1(\Omega)$.
    
  2 - Propose a variational formulation for the above mixed problem. 
    
  3 - Use the Lax-Milgram theorem to prove the well-posedness of this variational problem.
    
.. ##########

.. ##########
.. admonition:: Correction
    :class: dropdown

    1 - This follows from the fact that $H^1_{\Gamma_D}(\Omega)$ is a closed subspace of $H^1(\Omega)$, since we already know from :numref:`sec.Sobolev` that the latter is a Hilbert space. To see thus, let $u_n \in H^1_{\Gamma_D}(\Omega)$ be a sequence of functions converging in $H^1(\Omega)$ to some element $u\in H^1(\Omega)$. By the continuity of the trace operator, since all the traces $u_n \lvert_{\partial \Omega}$ vanish on $\Gamma_D$, then so does $u\lvert_{\partial \Omega}$, and so $u \in H^1_{\Gamma_D}(\Omega)$.
    
    2 - Like in the previous sections, we proceed in a formal manner. Let $\varphi \in \calC^\infty(\overline\Omega)$ be a smooth function up to the boundary $\partial \Omega$. Multiplying the main equation of :math:numref:`eq:mixedLaplace` by $\varphi$ and integrating, we obtain:
    
    $$-\int_\Omega \Delta u \:\varphi \:\d \x = \int_\Omega f\varphi \:\d \x; $$
    
    now using :ref:`Green's formula <sec.Green>`, if follows:
    
    $$- \int_{\partial \Omega} \frac{\partial u}{\partial n} \varphi \:\d s + \int_\Omega \nabla u \cdot \nabla \varphi \:\d \x = \int_\Omega f \varphi \:\d \x, $$
    
    and invoking the homogeneous Neumann boundary condition on $\Gamma_N$, this reduces to: 
    
    $$- \int_{\Gamma_N} \frac{\partial u}{\partial n} \varphi \:\d s + \int_\Omega \nabla u \cdot \nabla \varphi \:\d \x = \int_\Omega f \varphi \:\d \x. $$
    
    At this point, we note that, in light of the assumption of the :ref:`Lax-Milgram theorem <th.LaxMilgram>`, we would like that the first boundary integral in this formulation vanish, and that the test function $\varphi$ somehow \"resemble\" the sought function $u$. Both aims can be fulfilled by imposing $\varphi$ to vanish on $\Gamma_D$, i.e. taking $\varphi \in H^1_{\Gamma_D}(\Omega)$. 
    
    All things considered, we propose the following variational formulation for the problem :math:numref:`eq:mixedLaplace`:
    
    $$\text{Search for } u \in H^1_{\Gamma_D}(\Omega) \text{ s.t. for all } v \in H^1_{\Gamma_D}(\Omega),\quad  \int_\Omega \nabla u \cdot \nabla \varphi \:\d \x = \int_\Omega f \varphi \:\d \x. $$
    
    3 - We have already proved that $H^1_{\Gamma_D}(\Omega)$ is a Hilbert space. The continuity of the bilinear and linear forms involved in the formulation are proved exactly as in the model setting of :numref:`sec.LaxMilgram`. When it comes to the coercivity of the bilinear form, we have, for al $u \in H^1_{\Gamma_D}(\Omega)$, 
    
    $$\begin{array}{ccl}
    \displaystyle\int_\Omega \lvert\nabla u \lvert^2 \:\d \x &=& \displaystyle\frac12 \displaystyle\int_\Omega \lvert\nabla u \lvert^2 \:\d \x + \displaystyle\frac12 \int_\Omega \lvert\nabla u \lvert^2 \:\d \x \\
    &\geq& \displaystyle\frac12 \displaystyle\int_\Omega \lvert\nabla u \lvert^2 \:\d \x + c\displaystyle \int_\Omega u^2 \:\d \x \\
    &\geq& \min(\frac12,c) \lvert\lvert u \lvert\lvert^2_{H^1_{\Gamma_D}(\Omega)},
    \end{array}$$
   
    where we have used the adapted version of Poincaré's inequality from :numref:`prop.PoincareGammaD` to pass from the first line to the second one. 
    
    
    
.. ##########