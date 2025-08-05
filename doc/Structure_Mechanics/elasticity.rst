An introduction to linear elasticity
=====================================

.. ##################################################
.. ##################################################

This section deals with the physical model of linear elasticity describing the displacement of mechanical structures. 
Elasticity generally refers to the ability of an object to deform under the effect of loads, and to return to its exact initial configuration when they cease to be applied.

We consider particular instances of such situations, that hinge on two simplifying assumptions:

  - When the applied load is sufficiently small, so is the deformation, and the regime is linear. 
  
  - We restrict ourselves to considering time-independent situations. After a transient regime, the situations is assumed to have reached a state of equilibrim.  

The classical model of linear elasticity builds on three ingredients:

  - The first ingredient is kinematics, i.e. a description of the elastic body and its deformation, without making any reference to the efforts that have caused the latter. This is studied in :numref:`sec.kinematics`.
  
  - The second ingredient is a model for efforts. They key concept in this respect is that of Cauchy's stress tensor, which is discussed in :numref:`sec.stresses`.
  
  - The last ingredient is a connection between efforts and deformations: a constitutive law, depending on the mechanical characteristics of the elastic material, relates the applied stresses on a structure with the induced deformation. This is discussed in :numref:`sec.constitutivelaws`.

The reader primarily interested in the mathematical formulation of linear elasticity can directly jump to :numref:`sec.elasBVP`.
Eventually, much intuition about mechanical structures can be gleaned by adopting an energy viewpoint. This is dicussed in :numref:`sec.elasenergy`.

When it comes to the description of a medium $\Omega$, two paradigms are available:
  
  - The :ref:`Lagrangian <glos.Lagrangian>` point of view assumes a reference configuration :math:`\widehat{\Omega}` (for instance, the state of :math:`\Omega` at rest, or at the initial time of study).

  - The :ref:`Eulerian <glos.Eulerian>` point of view considers all quantities of interest at the time :math:`t` and point :math:`\x \in \Omega` of interest.

While the former point of view is generally adopted in the field of structural mechanics, it is customary to rely on the latter in fluid mechanics.


.. ##################################################
.. ##################################################

.. _sec.notelas:

Notations regarding vectors and tensors
---------------------------------------

.. ##################################################
.. ##################################################

Before getting into the core of the matter, let us set some notations.
Let $\sigma, \tau$ be two second-order tensors, i.e. mappings on $\Omega$ whose values $\sigma(\x)$, $\tau(\x)$ are square $d \times d$ matrices, $\x \in \Omega$. Their entries are denoted by $\sigma_{ij}$ and $\tau_{ij}$, $i,j=1,...,d$, respectively.

  - The :ref:`Frobenius inner product <glos.Frobenius>` $\sigma : \tau$ between $\sigma$ and $\tau$ is the real-valued quantity defined by:
    
    $$\sigma : \tau = \sum\limits_{i,j=1}^d {\sigma_{ij} \tau_{ij}} = \text{tr}(\sigma^T \tau).$$
  
  -  The :ref:`divergence of a tensor <glos.divtensor>` of :math:`\sigma` is the vector :math:`\text{div} \sigma` with size :math:`d` whose coordinates are the divergence of the rows of :math:`\sigma`, that is:
     
     .. math::
        (\text{div} \sigma)_i = \sum\limits_{j=1}^d{\frac{\partial \sigma_{ij}}{\partial x_j}}, \:\: i=1,...,d.
        
.. ##########

.. prf:proposition::

    Let :math:`\sigma: \Omega \to {\mathcal S}(\mathbb{R}^d)` be a smooth symmetric tensor field, and let :math:`\u : \Omega \to \mathbb{R}^d` be a smooth function. Then:
    
    .. math::
       \int_{\Omega}{\text{div} \sigma \cdot \u \:\d\x } = \int_{\partial \Omega}{( \sigma \n )\cdot \u \:\d s} - \int_\Omega{\sigma : e(\u) \:\d \x}.

.. ##########
.. ##########

.. admonition:: Proof
    :class: dropdown
  
    This is a simple adaptation of the basic Green's theorem.
    
.. ##########



.. ##################################################
.. ##################################################

.. _sec.kinematics:

Kinematics
-------------

.. ##################################################
.. ##################################################

As we have mentioned, elastic structures are usually described in a Lagrangian manner. Let us represent the configuration at rest of the structure by a domain $\Omega \subset \R^d$, and the displacement of the structure by a vector field $\u : \Omega \to \R^d$, which encodes the location $\x + \u(\x)$ of any point $\x \in \Omega$ after deformation: the deformed configuration of the structure is $(\text{Id} + \u)(\Omega)$, as depicted on :numref:`fig.sketchelas`.

.. #######

.. _fig.sketchelas:
.. figure:: ../figures/sketchelas.png
   :scale: 40 %

   The elastic structure :math:`\Omega` realizes the displacement $\u$ under the effect of body forces $\textbf{f} : \Omega \to \mathbb{R}^d$ and surface loads $\textbf{g} : \Gamma_N \to \mathbb{R}^d$.

.. #######


In this section, we are interested with linear elasticity, where the displacement :math:`u` and all its derivatives are assumed to be small, which allows for major simplifications in the mathematical equations.

The relative motion of the points of a structure :math:`\Omega` undergoing a displacement $\u$ is measured in terms of the linearized strain tensor $e(\u) : \Omega \to \mathbb{R}^{d \times d}_{\text{\rm sym}}$, defined by:

.. math::
  e(\u) = \frac12 (\nabla \u + \nabla \u ^T).
  
For a point $\x \in \Omega$, the physical interpretation of the matrix $e(\u)(\x)$ is as follows, see :numref:`fig.strain` for an illustration:

  - For :math:`i=1,\ldots,d`, the diagonal entry :math:`e(u)(x)_{ii}` encodes the stretching or the compression effect induced by :math:`u` in the direction :math:`e_i`; the length :math:`h \ll 1` of the small line segment with endpoints :math:`x` and :math:`x + he_i` becomes, after deformation:

    .. math::
       \lvert x + he_i + u(x+he_i) - (x+u(x)) \lvert \approx h + h e(u)(x)_{ii} .

  -  For :math:`i,j=1,\ldots,d`, :math:`i\neq j`, :math:`e(u)(x)_{ij}` measures the distortion of angles between the directions :math:`e_i` and :math:`e_j`; more precisely,

     .. math::
        e(u)(x)_{ij} = \frac{1}{2}(\kappa_1+ \kappa_2), \text{ where }  \kappa_1 \approx \tan \kappa_1 \approx \frac{\partial u_2}{\partial x_1}, \text{ and } \kappa_2 \approx \tan \kappa_2 \approx \frac{\partial u_1}{\partial x_2}.

.. #######

.. _fig.strain:
.. figure:: ../figures/diagoffdiagstrain.png
   :scale: 40 %

   Physical interpretation of the entries of the strain tensor :math:`e(u)(x)`; (a) The diagonal entry :math:`e(u)(x)_{ii}` appraises the variation of the segment :math:`[x,x+he_i]` after deformation; (b) The off-diagonal entry :math:`e(u)(x)_{12}` measures the variation of the angle between :math:`[x,x+he_1]` and :math:`[x,x+he_2]` after deformation.

.. #######

Another means to appraise how :math:`e(u)` accounts for the deformation of lengths and angles induced by :math:`u` is the following. Let :math:`[0,1] \ni t \mapsto \gamma(t)` be a curve drawn within :math:`\Omega`, with length:

.. math::
   \ell(\gamma) = \int_0^1 \lvert \gamma^\prime(t) \lvert \:\text{d} t.
   
The deformed version of :math:`\gamma` is the curve :math:`[0,1] \ni t \mapsto (\text{Id} + u)( \gamma(t))`, whose length equals:

.. math::
  \begin{array}{>{\text{d}isplaystyle}cc>{\text{d}isplaystyle}l}
  \ell((\text{Id} + u)\circ \gamma) &=& \displaystyle\int_0^1 \sqrt{C(u)(\gamma(t)) \gamma^\prime(t) \cdot \gamma^\prime(t)} \:\text{d} t, \\
  &\approx& \ell(\gamma) + \displaystyle\int_0^1 e(u)(\gamma(t)) \frac{\gamma^\prime(t)}{|\gamma^\prime(t)|} \cdot \frac{\gamma^\prime(t)}{|\gamma^\prime(t)|}  |\gamma^\prime(t)| \:\text{d} t,
  \end{array}

where :math:`C(u)` is the right Cauchy-Green strain tensor defined by

.. math::
  C(u) = (\text{I} + \nabla u)^T (\text{I} + \nabla u).
  
The latter depends in a nonlinear way on :math:`u`, and it measures exactly the deformation of lengths incurred by the displacement :math:`u`. The linearized strain tensor :math:`e(u)` is the linear part of the tensor :math:`\frac12(C(u)-\text{I})`. Considering :math:`e(u)` in place of :math:`C(u)` is the first source of linearity in the classical linear elasticity model; this simplification is called the geometric linearity assumption.

.. ##################################################
.. ##################################################

.. _sec.stresses:

Stresses
-------------

.. ##################################################
.. ##################################################


The second ingredient in the description of an elastic structure :math:`\Omega` is the representation of internal and external efforts, also called stresses.

Cauchy's stress tensor
^^^^^^^^^^^^^^^^^^^^^^

This task involves Cauchy's stress tensor :math:`\sigma : \Omega \to \mathbb{R}^{d \times d}`: for any point :math:`x \in \Omega` and any unit vector :math:`n \in \mathbb{S}^{d-1}`, :math:`\sigma(x) n` is the force applied by the outer medium on the face of an infinitesimally small cube of material around :math:`x`, see :numref:`fig.3stress`.
The entries of the tensor :math:`\sigma(x)` can be separated between traction-compression entries and shear components, as depicted on :numref:`fig.3stress` (b), (c):

  - For :math:`i=1,\ldots,d`, :math:`\sigma(x)_{ii}` represents the :math:`i^{\text{th}}` component of the force applied on the face oriented by :math:`e_i`; it thus accounts for a compression effect when :math:`\sigma(x)_{ii} < 0`, and a stretching (or dilation) effect if :math:`\sigma(x)_{ii} >0`.
  
  - For :math:`i,j=1,\ldots,d`, :math:`i\neq j`, the off-diagonal entry :math:`\sigma(x)_{ij}` is the :math:`i^{\text{th}}` component of the force applied on the face oriented by :math:`e_j`; it accounts for a shearing effect, whereby this face undergoes a tangential deformation.

.. #######

.. _fig.3stress:
.. figure:: ../figures/stress3.png
   :scale: 40 %
   
   The stress tensor: (a) For :math:`x\in \Omega` and :math:`n \in \mathbb{S}^{d-1}`, the vector :math:`\sigma(x) n` is the force imposed by the outer medium onto the face oriented by :math:`n` of a small cube around :math:`x`; (b) The diagonal entries of :math:`\sigma(x)` account for the compression efforts felt by this cube; (c) The off-diagonal entries encode the shear effects imposed on this cube.

.. #######

.. ##########

.. prf:theorem::

    The stress is linear.

.. ##########
.. ##########

.. admonition:: Proof
    :class: dropdown
  
    Cauchy's tetrahedron 
    
.. ##########


The laws of equilibrium
^^^^^^^^^^^^^^^^^^^^^^^^

The stress tensor allows to express the conditions of equilibrium of a structure $\Omega$.
Let $f: \Omega \to \R^d$ be the density of body forces (e.g. gravity) at play in $\Omega$,
and let $g: \Gamma_N \to \R^d$ be the density of surface loads, applied on a fixed subset $\Gamma_N$ of $\partial \Omega$. Then:

  - The law of balance of linear momentum states that, for each subdomain $\omega \Subset \Omega$, the sum of the body forces inside $\omega$ and the forces applied by the rest of the structure on $\partial \omega$ must vanish, i.e.
    
    .. math::
       \int_\omega f \:\text{d} x + \int_{\partial \omega} \sigma n \:\text{d} s = 0.
       
    After application of the Green's formula of \cref{prop.Green}, this rewrites:
    
    .. math::
      \int_\omega (\text{div}(\sigma) + f ) \:\text{d} x= 0,
      
    and since this relation should hold for any subdomain $\omega \Subset \Omega$, it follows:
    
    .. math::
       -\text{div}(\sigma) = f \text{ in } \Omega.
       
  - Applying the same principle inside a small enough subdomain $\omega \subset \Omega$ whose boundary contains a portion of $\Gamma_N$, we obtain:
    
    .. math::
      \int_\omega f \:\text{d} x + \int_{\partial \omega \cap \Gamma_N} g \:\text{d} s + \int_{\partial \omega \setminus \overline{\Gamma_N}} \sigma n \:\text{d} s = 0,

    that is:
    
    .. math::
       \int_\omega f \:\text{d} x +  \int_{\partial \omega} \sigma \cdot n \:\text{d} s +  \int_{\partial \omega \cap \Gamma_N} g \:\text{d} s -\int_{\partial \omega \cap \Gamma_N} \sigma n \:\text{d} s = 0.

    Using Green's formula on the second term in the above left-hand side together with the fact that :math:`-\text{div}(\sigma) = f` inside :math:`\omega`, we obtain that the first two terms of the above equation vanish; since $\omega$ is arbitrary, this entails:

    .. math::
       \sigma n = g \text{ on } \Gamma_N.
       
    Note that this fact can also be understood as an application of the law of reciprocal actions.
    
One last consequence of equilibrium is that :math:`\Omega` should be in rotational equilibrium. This implies the symmetry of the stress tensor, as expressed by the next result.

.. ##########

.. prf:theorem:: Cauchy's theorem

    For any point :math:`x \in \Omega`, the tensor :math:`\sigma(x)` is symmetric:
    
    .. math::
       \forall x \in \Omega, \quad \sigma(x) = \sigma(x)^T.

.. ##########
.. ##########

.. admonition:: Proof
    :class: dropdown
  
    This is a non trivial consequence of the law of balance of momentum: no subdomain :math:`\omega \Subset \Omega` should undergo rotational efforts induced by the outer medium.
    
.. ##########
   
.. ##################################################
.. ##################################################

.. _sec.constitutivelaws:

Constitutive laws
-----------------

.. ##################################################
.. ##################################################


The above description of an elastic structure is completed by a constitutive
relation between the stress :math:`\sigma` inside :math:`\Omega` and the induced strain $e(\u)$.
In multiple applications, it is supposed to be linear, of the form:

.. math::
  \sigma = A e(\u) , \text{ or equivalently } e(\u) = S \sigma.
  
Here, the a priori inhomogeneous (i.e. space dependent) tensor :math:`A` and its inverse :math:`S` are the Hooke's tensor and the compliance tensor of the material, respectively.
For $\x \in \Omega$, $A(\x)$ and $S(\x)$ are linear mappings from :math:`\Rsym` into itself, encoding the local properties of the constituent material of :math:`\Omega` around :math:`x`, in a way which we now discuss more precisely. To this end, we focus on the three-dimensional context;
the 2d case is evoked in :numref:`rem.elas2d`. Also, to simplify the discussion, we assume the considered material to be homogeneous.

In general, :math:`A` is a fourth-order tensor :math:`A = \left\{A_{ijkl} \right\}_{i,j,k,l=1,\ldots,3}` with the following symmetries:

.. math::
  \forall i,j,k,l=1,\ldots,3, \quad A_{ijkl} = A_{klij}, \text{ and } A_{ijkl} = A_{jikl} = A_{ijlk}.
  
Hence, :math:`A` has :math:`21` independent entries.
Fortunately, most materials present symmetries, which allows to reduce the number of these independent entries:

- Isotropic materials exhibit the same behavior in all directions of space; their Hooke's tensor :math:`A` is completely characterized by two scalar parameters :math:`\lambda` and :math:`\mu`, called the Lamé parameters of the material:

  .. math::
    :label: eq.isoA
    
    \forall \xi \in \mathbb{R}_{\text{sym}}^{3\times 3} , \quad A\xi = 2\mu \xi + \lambda \tr(\xi) \I.

  The parameter :math:`\mu` is called the shear modulus; it corresponds to the angular deviation caused by a unit shear stress, see :numref:`fig.muEnu` (a); the physical interpretation of :math:`\lambda` is unfortunately not as clear. Usually, two more physical quantities :math:`E` and :math:`\nu` are used, from which :math:`\lambda` and :math:`\mu` can be retrieved as:
  
  .. math::
   \mu = \frac{E}{2(1+\nu)}, \text{ and } \lambda = \frac{E\nu}{(1+\nu)(1-2\nu)}.
   
  The Young's modulus :math:`E` measures the resistance of the material to traction and compression, and the Poisson's ratio :math:`\nu` measures its resistance to transverse deformations, see :numref:`fig.muEnu` (b).
  
- A more general class of materials is that of orthotropic materials. These possess three orthogonal planes of symmetry, and as a result, they enjoy different properties along the corresponding axes. They are characterized by one Young's modulus :math:`E_i` in each direction :math:`i=1,2,3`, one Poisson's ratio :math:`\nu_{ij}` and one shear modulus :math:`G_{ij}` for each pair :math:`i\neq j`. One example of an orthotropic material is depicted on :numref:`fig.woodConcrete` (a).

- Transversely isotropic materials have a particular form of orthotropy. They have one plane of symmetry, and show an isotropic behavior within any plane parallel to the latter. The physical properties of a material with transverse isotropy, say in direction :math:`e_3`, are characterized by five independent parameters: two Young's moduli :math:`E_3` and :math:`E_1 = E_2` encoding the resistance to stretching in the transverse and longitudinal directions, respectively, two Poisson's ratios :math:`\nu_{13} = \nu_{23}` and :math:`\nu_{12}` and the shear modulus :math:`G_{13} = G_{23}` between the transverse and longitudinal directions. One example of a transversely isotropic material is depicted on :numref:`fig.woodConcrete` (b).

.. #######

.. _fig.muEnu:
.. figure:: ../figures/muEnu.png
   :scale: 60 %
   
   Elastic parameters: (a) The shear modulus :math:`\mu` accounts for the force :math:`\sigma_{23} = \mu \alpha` that should be applied on the face oriented by :math:`e_3` of a piece of material in the transverse direction :math:`e_2` to create an angle :math:`\alpha` with the :math:`e_3` direction; (b) The Young's modulus :math:`E = \sigma/L` accounts for the amplitude of the force :math:`\sigma` needed to stretch a piece of material by a length :math:`L`; the Poisson's ratio :math:`\nu = -\ell / L` measures the relative transverse displacement in this process.

.. #######

.. #######

.. _fig.woodConcrete:
.. figure:: ../figures/woodConcrete.png
   :scale: 60 %
   
   Two different elastic materials: (a) Wood is an orthotropic material with large stiffness in the direction of the grain, low stiffness in the radial direction, and intermediate stiffness in the azimuthal direction; (b) Fiber-reinforced concrete is a transversely isotropic material: it is much stiffer in the direction of the metallic fibers than in the orthogonal directions.
   
.. #######

.. #######
.. _rem.elas2d:
.. prf:remark::

  The above considerations related to the elastic properties of structures take place in the physically prevalent setting of three space dimensions. The definition of the Hooke's tensor :math:`A` of a 2d structure depends on how the latter accounts for a 3d one which is invariant in the :math:`e_3` direction. In plane stress, where the components :math:`\sigma_{i3} = \sigma_{3i}` of the stress tensor vanish (:math:`i=1,2,3`), the Lamé parameters :math:`\lambda` and :math:`\mu` characterizing the 2d tensor :math:`A` in :math:numref:`eq.isoA` are obtained from the Young's modulus :math:`E` and the Poisson's ratio :math:`\nu` of the 3d material via the relations:
  
    .. math::
      \mu = \frac{E}{2(1+\nu)}, \text{ and } \lambda = \frac{E\nu}{1-\nu^2}.
      
  In plane strain, where the components :math:`e(u)_{i3} = e(u)_{3i}` of the strain tensor vanish, one has instead:
  
  .. math::
    \mu = \frac{E}{2(1+\nu)}, \text{ and } \lambda = \frac{E\nu}{(1+\nu)(1-2\nu)}.

.. #######

.. #######
.. prf:remark::

  The strain tensor :math:`e(u)` is by essence a Lagrangian quantity, as it is defined on the reference configuration :math:`\Omega` of the structure. On the contrary, stresses are naturally expressed in the Eulerian variable, i.e. on the deformed configuration :math:`(\text{Id} + u)(\Omega)`. Hence, the constitutive law should relate :math:`e(u)` with a transported version of the stress tensor :math:`\sigma` onto the reference configuration, called the Piola-Kirchoff stress tensor. In the present setting, this difficulty is ignored since both notions of stress tensors coincide at leading order, as the displacement of the structure is small, see the discussion in Chap. 13 of :cite:`temam2005mathematical` about this point.

.. #######

.. ##################################################
.. ##################################################

.. _sec.elasBC:

Boundary conditions
--------------------

.. ##################################################
.. ##################################################

Clamping, traction, two-phase

.. ##################################################
.. ##################################################

.. _sec.elasBVP:

Towards mathematical modeling: a typical boundary value problem
---------------------------------------------------------------

.. ##################################################
.. ##################################################

Gathering the concepts of the previous sections, we are in position to write down a prototype for boundary-value problems in the physical context of linearly elastic structures.

Let $\Omega \subset \R^d$ be a structure which is attached on a region $\Gamma_D$ of its boundary;
it is submitted to body forces $\textbf{f} : \Omega \to \R^d$ and surface loads $\textbf{g} : \Gamma_N \to \R^d,$ applied on a region $\Gamma_N$ of $\partial \Omega$ disjoint from $\Gamma_D$. The displacement $\u$ of $\Omega$ is the solution to the following system:

.. math::
  \left\{
  \begin{array}{cl}
  -\text{div}(Ae(\u)) = \textbf{f} & \text{in } \Omega, \\
  \u = 0 & \text{on } \Gamma_D, \\
  Ae(\u) \n= \textbf{g} &\text{on } \Gamma_N, \\
  Ae(\u)\n = 0 & \text{on } \Gamma.
  \end{array}
  \right.

The mathematical framework associated to this system is similar to that presented in \cref{sec.1phaseconduc}.
The Hooke's tensor $A : \Omega \to \calL(\Rsym,\Rsym)$ is a smooth enough mapping satisfying the following ellipticity property:

.. math::
  \text{There exist constants } 0 < \alpha \leq \beta  < \infty \text{ s.t. } \forall x \in \Omega, \: \: \forall \xi \in \Rsym, \quad \alpha || \xi ||^2 \leq A(x) \xi : \xi \leq \beta ||\xi ||^2.
  
The body forces and surface loads $f$ and $g$ belong to the respective spaces $L^2(\Omega)^d$ and $L^2(\Gamma_N)^d$ and
the displacement $u$ is sought as the solution to the variational problem:

.. math::
  \text{Search for } u \in H^1_{\Gamma_D}(\Omega)^d \text{ s.t. } \forall v \in  H^1_{\Gamma_D}(\Omega)^d , \quad \int_\Omega Ae(u) : e(v) \:\text{d} x = \int_\Omega f \cdot v \:\text{d} x + \int_{\Gamma_N} g \cdot v \:\text{d} s,

whose well-posedness follows from the :ref:`Lax-Milgram theory <sec.LaxMilgram>` -- the coercivity of the involved bilinear form being a consequence of \cref{eq.ellelas} and the Korn's inequality, see for instance \cite{ciarlet2021mathematical}.


.. #######
.. prf:remark::

  The elliptic regularity theory, which loosely speaking ensures that, under suitable assumptions on :math:`\Omega`, :math:`f` and :math:`g`, the solution :math:`u` to \cref{eq.elas} is smooth, can be deployed pretty much as in the scalar case of the conductivity equation evoked in \cref{rem.ellregconduc}. As is exemplified in the sketch provided in \cref{sec.appellreg}, the pivotal ingredient of this theory is the ellipticity assumption \cref{eq.ellelas}, ensuring a control of the norm of $u$ in terms of the operator $\u \mapsto -\text{div}(Ae(\u))$.

.. #######

.. ##################################################
.. ##################################################

.. _sec.elasenergy:

Energy
------

.. ##################################################
.. ##################################################

Much intuition about the behavior of an elastic structure can be gleaned from energetic considerations. The fundamental result in this study is the following.

.. ##########

.. prf:theorem::
  
   Let the structure :math:`\Omega` under scrutiny be in a deformed state characterized by the displacement :math:`u`. The work done by internal forces when this structure is further displaced  by a small increment :math:`v` equals:

   .. math::
     :label: eq.workinternalelas
     
     -\int_{\Omega} \sigma(u) : e(v) \:\text{d} x.

   Equivalently, in order to bring the structure from the configuration defined by :math:`u` to that defined by :math:`u+v`, one has to supply an amount of energy equal to :math:`\int_\Omega \sigma(u) : e(v) \:\text{d} x`.

.. ##########
.. ##########

.. admonition:: Proof
    :class: dropdown
  
    Bla bla
    
.. ##########

Note that, when :math:`v` is of the form :math:`v = \text{d} h u` with :math:`\text{d} h \ll 1`, the work :math:numref:`eq.workinternalelas` is negative,
indicating that internal forces always work against the actual motion.

The total strain energy needed to bring :math:`\Omega` from rest to :math:`(\text{Id} + u)(\Omega)` is
obtained by integrating the above increment between both configurations, which reads:

.. math::
  \int_0^1  \int_\Omega \sigma(hu) : e(u) \:\text{d} x\:\text{d} h = \frac{1}{2} \int_\Omega \sigma(u): e(u) \:\text{d} x.
  
Physically, the elastic energy of a system is the potential energy stored in the latter as the deformation occurs under the effect of work performed on it.
This energy can then be converted and released under various forms, such as kinetic or thermal energy.

Likewise, when the structure is further deformed according to a small increment $v$ from the deformed configuration characterized by $u$, the work of external loads is

.. math::
  \int_\Omega f \cdot v \:\text{d} x + \int_{\Gamma_N} g \cdot v \:\text{d} s.
  
This quantity is positive when $v$ is oriented in the direction of the forces $f$ and $g$: intuitively, these then work in favor of the motion by handing energy to the system. The total work of $f$ and $g$ when $\Omega$ passes from rest to the deformed configuration $(\text{Id} + u)(\Omega)$ is obtained by a similar integration as above:

.. math::
  \int_\Omega f \cdot u \:\text{d} x + \int_{\Gamma_N} g \cdot u \:\text{d} s.

Finally, the total energy $E(u)$ stored by $\Omega$ in the displacement from rest to $(\text{Id} + u)(\Omega)$ equals:

.. math::
  E(u) :=  \frac{1}{2} \int_\Omega \sigma(u) : e(u) \:\text{d} x - \int_\Omega f \cdot u \:\text{d} x - \int_{\Gamma_N} g \cdot u \:\text{d} s.
  
The actual displacement $u_\Omega$ of $\Omega$, which we have characterized as the solution to \cref{eq.elas} in the previous section, is obtained by minimizing $E(u)$ among all the possible displacements of the structure, that is:

.. math::
  u_\Omega = \underset{u \in H^1_{\Gamma_D}(\Omega)^d}{\text{arg min}} \:E(u).

The mathematical equivalence between \cref{eq.elas} and \cref{eq.minpot} follows from a classical application of the Lax-Milgram theory.
Note that, using the variational problem \cref{eq.varfelas} satisfied by $u_\Omega$, the minimum value of the energy $E(u)$ reads:

.. math::
  E(u_\Omega) = \min\limits_{u \in H^1_{\Gamma_D}(\Omega)^d } E(u) = -\frac{1}{2} \int_\Omega Ae(u_\Omega) : e(u_\Omega) \:\text{d} x.
  
This quantity is always nonpositive, reflecting that the application of external forces $f$ and $g$ to the structure $\Omega$ always triggers a motion of the latter by conveying energy (which is thus subtracted from its potential energy).
