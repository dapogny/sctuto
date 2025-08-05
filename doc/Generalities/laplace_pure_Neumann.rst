.. _sec.lappureNeumann:

The Laplace equation with pure Neumann boundary conditions
======================================================================

.. ##################################################

This section deals with the pure Neumann problem for the Laplace operator. A comprehensive reference about this issue is the journal article :cite:`bochev2005finite`.

Let us consider the following boundary-value problem for the Laplace operator:

.. math::
  :label: eq.pureNeumann
  
  \text{Search for } u \text{ s.t. } \left\{
  \begin{array}{cl}
  -\Delta u = f & \text{in } \Omega, \\
  \frac{\partial u}{\partial n} = 0 & \text{on } \partial \Omega.
  \end{array}
  \right.

Here, the source $f$ belongs to the space $L^2(\Omega)$. The considered Neumann conditions are homogeneous, but inhomogeneous conditions could be analyzed by similar considerations. 

.. ##################################################
.. ##################################################

.. _sec.theoryPureNeumann:

A bit of theory
---------------

.. ##################################################
.. ##################################################

One subtle point about the pure Neumann problem :math:numref:`eq.pureNeumann` is that it is not necessarily well-posed. This is easily seen by multiplying both sides of the main equation by the constant function $1$ and using the :ref:`Green's formula <th.Green>`, which yields:

.. ##############

.. math:: 
  :label: eq.compatibility
  
  \int_\Omega f(\x) \:\text{d} \x = 0.

.. ##############

This equality is a \"compatibility condition\", bearing only on the data $f$ of the problem :math:numref:`eq.pureNeumann`. 
If it is not satisfied, :math:numref:`eq.pureNeumann` cannot possibly have a solution. 

On the other hand, when a solution $u$ to :math:numref:`eq.pureNeumann` exists, it cannot be unique since then any function of the form $u + c$, where $c$ is a real constant, is obviously also a solution.

These evidences of the ill-posedness of :math:numref:`eq.pureNeumann` are actually two sides of the same coin. They actually reflect a very general phenomenon called Fredholm alternative: loosely speaking, the more numerous the compatibility conditions to be satisfied by the data for existence of a solution, the higher the dimension of the kernel of the problem. 

Without entering any further into this deep mathematical topic, let us assume that the considered source $f$ satisfies :math:numref:`eq.compatibility`, and let us proceed formally to derive a variational formulation for :math:numref:`eq.pureNeumann`, along the lines of :numref:`sec.LM`. Because the solution $u$ to :math:numref:`eq.pureNeumann` will be defined up to a constant, we search for one such solution $u$ satisfying $\int_\Omega u(\x) \:\d \x = 0$. Formally multiplying the main equation in :math:numref:`eq.pureNeumann` by a smooth test function $v \in \calC^\infty(\overline\Omega)$, then applying the :ref:`Green's formula <th.Green>`, we obtain:

$$\int_\Omega \nabla u \cdot \nabla v \:\d \x = \int_\Omega fv \:\d \x.$$ 

Besides, it is enough to assume that this relation holds true only for test functions $v$ satisfying $\int_\Omega v \:\d\x=0$, since it is obviously satisfied for $v=1$, owing to :math:numref:`eq.compatibility`. Since the differential operator at the left-hand side involves first-order partial derivatives of $u$ and $v$, we are led to consider the functional space 

.. ##############

.. math:: 
  :label: eq.VPureNeumann
  
  V := \left\{ v \in H^1(\Omega) \text{ s.t. } \int_\Omega v \: \d \x = 0 \right\},
  
.. ##############

equipped with the norm $\lvert\lvert \cdot \lvert\lvert_{H^1(\Omega)}$.
These formal considerations lead us to introduce the following variational problem:

.. #############################

.. math:: 
  :label: eq.varfPureNeumann
  
  \text{Search for } u \in V \text{ s.t. } \forall v \in V, \quad \int_\Omega \nabla u \cdot \nabla v \:\d \x = \int_\Omega f v \:\d \x.

.. #############################

The well-posedness of :math:numref:`eq.varfPureNeumann` is the subject of the next proposition, whose proof is left as an exercise.

.. #############################

.. _prop.WPPureNeumann:

.. prf:proposition::

  Let $f \in L^2(\Omega)$ be a given source term. Then the variational problem :math:numref:`eq.varfPureNeumann` is well-posed.

.. #############################

.. ##########
.. admonition:: Exercise
   :class: admonition-exo

   Prove :numref:`prop.WPPureNeumann` thanks to the :ref:`Lax-Milgram theorem <th.LaxMilgram>`.

     *(Hint: The coercivity of the bilinear form at the right-hand side of* :math:numref:`eq.varfPureNeumann`, *rests on the* :ref:`Poincaré-Wirtinger inequality <prop.PoincareWirtinger>` *.)*
     
.. ##########


.. #############################

.. prf:remark:: 

  The compatibility condition :math:numref:`eq.compatibility` is not needed to guarantee the well-posedness of :math:numref:`eq.varfPureNeumann`. It however ensures that the variational solution $u$ is also solution to the original boundary-value problem :math:numref:`eq.pureNeumann` in a suitable sense. Indeed, arguing as in :numref:`rm.eqstrongweakneu` and without entering into details, one can show that $u$ is the unique $H^1(\Omega)$ function satisfying
  
  .. math::
  
    \left\{
    \begin{array}{cl}
    -\Delta u = f - \frac{1}{\lvert \Omega \lvert}\int_\Omega f(\x) \:\d \x & \text{in } \Omega, \\
    \frac{\partial u}{\partial n} = 0 & \text{on } \partial \Omega.
    \end{array}
    \right.
  
  where the main equation is understood in the sense of distributions. Note that its right-hand side satisfies the compatibility condition :math:numref:`eq.compatibility` and that it coincides with the original source term $f$ provided the latter satisfies :math:numref:`eq.compatibility`.

.. #############################


.. ##################################################
.. ##################################################

Two different numerical resolution methods
------------------------------------------

.. ##################################################
.. ##################################################

Although rigorous, the mathematical framework developed in the previous :numref:`sec.theoryPureNeumann` does not easily lend itself to numerical implementation. Indeed, the Finite Element discretization of the functional space :math:numref:`eq.VPureNeumann`, featuring functions with vanishing integral, is awkward. In the following, we describe two different mathematical and numerical approaches for the numerical resolution of :math:numref:`eq.pureNeumann`.

.. #############################

.. _sec.penNeu:

The penalization method
"""""""""""""""""""""""

.. #############################

Let $\e$ be a \"small\" parameter. We propose to approximate the solution $u$ to :math:numref:`eq.pureNeumann` by that $u_{\e}$ to the following problem:

  .. math::
    :label: eq.pureNeumannPen

    \text{Search for } u_{\e}\:\: \text{ s.t. }\:\: \left\{\begin{array}{cl}
    -\Delta u +\e u= f & \text{in } \Omega, \\
    \frac{\partial u_{\e}}{\partial n} = 0 & \text{on } \partial \Omega.
    \end{array}
    \right.

Intuitively, the above boundary-value problem is a slightly modified version of :math:numref:`eq.pureNeumann` where a small $0^{\text{th}}$ order term is added to the main equation. A variational formulation for this problem reads:

  .. math::
    :label: eq.varfpureNeumannPen
    
    \text{Search for } u_{\e} \in H^1(\Omega) \text{ s.t. } \forall v \in H^1(\Omega), \quad \int_\Omega \nabla u_{\e} \cdot \nabla v \:\d \x + \e \int_\Omega u_{\e} v \:\d \x = \int_\Omega f v \:\d \x.

A standard application of the :ref:`Lax-Milgram theory <sec.LM>` shows that this variational problem is well-posed: indeed, the added $0^{\text{th}}$ order term makes the bilinear form at the left-hand side coercive.

This penalization approach is made rigorous by the following proposition.

.. #####################

.. prf:proposition::

  Let $f \in L^2(\Omega)$ satisfy the compatibility condition :math:numref:`eq.compatibility`. The solution $u_{\e} \in H^1(\Omega)$ to the penalized Laplace equation :math:numref:`eq.pureNeumannPen` converges to the solution $u$ of the pure Neumann problem :math:numref:`eq.pureNeumann`:
  
  $$\lvert\lvert u_{\e} - u \lvert\lvert_{H^1(\Omega)} \xrightarrow{\e \to 0} 0.$$

.. #####################

.. ##########
.. admonition:: Proof
    :class: dropdown

    The proof uses results about :ref:`weak convergence <sec.weakcv>`.

    At first, taking $v=1$ in the variational formulation :math:numref:`eq.varfpureNeumannPen` for $u_\e$, we see immediately that $\int_\Omega u_{\e} \:\d\x =0$, because $f$ satisfies :math:numref:`eq.compatibility`.
    
    Now, taking $v=u_{\e}$, we obtain, in particular:
    
    $$\int_{\Omega} \lvert \nabla u_{\e} \lvert^2 \:\d \x \leq C \lvert\lvert f \lvert\lvert_{L^2(\Omega)} \lvert\lvert u _\e\lvert\lvert_{L^2(\Omega)}.$$
    
    The :ref:`Poincaré-Wirtinger inequality <prop.PoincareWirtinger>` then implies that $u_{\e}$ is bounded in $H^1(\Omega)$.
    Owing to :numref:`prop.seqcompactbounded`, we can thus extract a subsequence $\e_n$ of the $\e$ such that:
    
    $$u_{\e_n} \to u_* \text{ weakly in } H^1(\Omega), \text{ for a certain limit function }u_*.$$
    
    Passing to the weak limits in the variational problem :math:numref:`eq.varfpureNeumannPen` and in the relation $\int_\Omega u _{\e_n} \:\d x\ =0$, we see that:
    
    $$\forall v \in H^1(\Omega), \quad \int_\Omega \nabla u_{*} \cdot \nabla v \:\d\x  = \int_\Omega fv \:\d\x, \text{ and } \int_\Omega u_* \:\d\x=0, $$
    
    i.e. $u_*$ is the unique solution to the pure Neumann problem in the space $V$ defined by :math:numref:`eq.VPureNeumann`. 
    Invoking a :ref:`classical argument about the uniqueness of the limit <sec.uniquelim>`, we conclude that the whole sequence $u _\e$ converges to $u$ weakly in $H^1(\Omega)$.
    
    To conclude, we have to prove that this convergence is actually strong. To achieve this, we just expand the square:
    
    $$\begin{array}{ccl}
    \displaystyle\int_\Omega \lvert \nabla u_{\e} -\nabla u_* \lvert^2 \:\d\x &=&  \displaystyle\int_\Omega \lvert \nabla u _\e \lvert^2 \:\d\x +  \displaystyle\int_\Omega \lvert \nabla u \lvert^2 \:\d\x  - 2  \displaystyle\int_\Omega  \nabla u _\e \cdot \nabla u \:\d\x \\
    &=&  \displaystyle\int_\Omega f u _\e \:\d x +  \displaystyle\int_\Omega f u \:\d \x - 2  \displaystyle\int_\Omega f u _\e \:\d \x,
    \end{array}$$
    
    where we have used both variational problems :math:numref:`eq.varfpureNeumannPen` and :math:numref:`eq.varfPureNeumann` with $u$ and $u _\e$ as test functions, respectively. Eventually, the right-hand side of the above equality tends to $0$ as $\e \to 0$ because of the weak $H^1(\Omega)$ convergence of $u_\e$ to $u$, which ends the proof.
    
.. ##################################################
.. ##################################################

.. #############################

.. _sec.csNeu:

The constrained optimization method
"""""""""""""""""""""""""""""""""""

.. #############################

In this section, we develop an alternative viewpoint about the variational problem :math:numref:`eq.varfPureNeumann`, which is inspired by constrained optimization theory, a subject whose basic stakes are recalled in :numref:`app.recalloptim`.

Let us recall that $V$ stands for the space of functions in $H^1(\Omega)$ with vanishing average on $\Omega$, see :math:numref:`eq.VPureNeumann`. The energy version of the Lax-Milgram theorem in :numref:`lem.corLM` states that $u$ is the unique solution to the following energy minimization problem:

$$\min_{v \in V} E(v), \text{ where } E(v) := \frac12 \int_\Omega \lvert \nabla v\lvert^2 \:\d \x - \int_\Omega fv \:\d \x.$$

Let us reformulate this as a constrained optimization problem:

$$\min_{v \in H^1(\Omega)} E(v) \text{ s.t. } \int_\Omega v \:\d x =0. $$

The necessary and sufficient optimality condition for this problem states that a solution $u \in H^1(\Omega)$ to the latter should satisfy: 

$$\exists \lambda \in \R, \text{ s.t. } \forall v \in H^1(\Omega), \quad \int_\Omega \nabla u \cdot \nabla v \:\d \x - \int_\Omega fv \:\d\x + \lambda \int_\Omega v \:\d \x = 0.$$

In particular, this relation should hold true for $v=1$, which implies that the Lagrange multiplier $\lambda$ necessarily equals:

$$\lambda = \frac{1}{\lvert\Omega\lvert} \int_\Omega f(\x) \:\d\x. $$

It follows that $u$ is thus solution to the variational problem:

$$\text{Search for } u \in V, \text{ s.t. } \forall v \in V, \quad \int_\Omega \nabla u \cdot \nabla v \:\d \x = \int_\Omega \widetilde{f} v \:\d\x,  $$
 
where $\widetilde f := f - \frac{1}{\lvert\Omega\lvert}\int_\Omega f\:\d\x$ is the $0$ averaged version of $f$. In other words, $u$ is the unique solution in $V$ to the version of :math:numref:`eq.pureNeumann` featuring the $0$ averaged right-hand side $\widetilde{f}$.
In particular, if $f \in L^2(\Omega)$ satisfies the condition :math:numref:`eq.compatibility`, the solution $u$ to :math:numref:`eq.pureNeumann` can be calculated by searching for the unique pair $(u,\lambda) \in H^1(\Omega) \times \R$ satisfying the following variational problem:

.. math::
  
  \text{Search for } (u,\lambda) \in H^1(\Omega) \times \R \text{ s.t. } \forall (v,\mu) \in H^1(\Omega) \times \R, \quad \left\{
  \begin{array}{l}
  \displaystyle\int_\Omega \nabla u \cdot \nabla v \:\d \x + \lambda \displaystyle\int_\Omega v \:\d \x = \displaystyle\int_\Omega fv \:\d\x, \\
  \mu \displaystyle\int_\Omega u \:\d\x = 0,
  \end{array}
  \right.

or equivalently: 

.. math::
  :label: eq.varpbulambda
  
  \text{Search for } (u,\lambda) \in H^1(\Omega) \times \R \text{ s.t. } \forall (v,\mu) \in H^1(\Omega) \times \R, \quad \int_\Omega \nabla u \cdot \nabla v \:\d \x + \lambda \int_\Omega v \:\d \x  +  \mu \int_\Omega u \:\d\x = \int_\Omega fv \:\d\x.

.. ##################################################
.. ##################################################

Implementation of the pure Neumann problem
------------------------------------------

.. ##################################################
.. ##################################################

We exemplify the resolution of the pure Neumann problem :math:numref:`eq.pureNeumann` with an example. The implementation of the penalization strategy of :numref:`sec.penNeu` is simple enough, and it is left as an :ref:`exercise <exo.Neu>`. 

.. ##########

.. _exo.Neu:

.. admonition:: Exercise
   :class: admonition-exo

   Implement the penalization approach in :numref:`sec.penNeu` to solve the pure Neumann problem :math:numref:`eq.pureNeumann`.

.. ##########

The solution based on the constrained optimization viewpoint of :numref:`sec.csNeu` is slightly more involved. The assembly of the Finite Element problem :math:numref:`eq.varpbulambda`, posed over the product space $H^1(\Omega) \times \R$, requires handling the Finite Element matrices associated to the three components of its left-hand side. This can be realized by using the syntax elements of :numref:`sec.FEmats`, as described in the following listing.
The complete numerical implementation of both approaches is proposed :download:`here <./codes/laplace_pure_Neumann.edp>`, and the numerical results are presented on :numref:`fig.LapPureNeumann`.

.. ############
.. code-block::

  /* Resolution of the problem using Lagrange multipliers */
  int nv = Vh.ndof;

  /* Bilinear form for the Laplace equation */
  varf varlap(u,v) = int2d(Th)(dx(u)*dx(v)+dy(u)*dy(v));

  /* Bilinear form for the additional np*1 block */
  varf vb(u,v) = int2d(Th)(1.0*v);

  matrix A = varlap(Vh,Vh); // matrix with size nv*nv
  real[int] B = vb(0,Vh); // Column bloc with size nv*1

  /* Matrix of the augmented problem */
  matrix Aa = [[A,B],[B',0]]; // B' = transpose of B

  /* Construction of the right-hand side */
  varf vrhs(u,v) =  int1d(Th,1)(gin*v) + int1d(Th,2)(gout*v);
  real[int] b = vrhs(0,Vh);
  real[int] ba(nv+1);
  ba = [b,0.0];

  /* Inversion of the augmented system */
  set(Aa,solver=UMFPACK);
  real[int] ua = Aa^-1*ba;
  [u[],l] = ua;  // Comprehension of vector ua

.. ############

.. #################@

.. _fig.LapPureNeumann:

.. figure:: ../figures/LapPureNeumann.png
   :scale: 35 %

   Resolution of the pure Neumann problem :math:numref:`eq.pureNeumann`; (Left) Setting of the test-case: heat is entering $\Omega$ from the left boundary $\Gamma_{\text{in}}$ with a flux $g_{\text{in}}$ and is leaving $\Omega$ from the right boundary $\Gamma_{\text{out}}$ with a flux $g_{\text{out}}$; (right) Plot of the solution.

.. #################@
