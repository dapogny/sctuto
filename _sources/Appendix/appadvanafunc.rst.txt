.. _sec.appadvanafunc:

More advanced functional analysis
==================================

.. ##################################################
.. ##################################################

.. _app.nemitski: 

Nemitski operators
---------------------

.. ##################################################
.. ##################################################

This section deals with a class of operations that is frequently encountered in non linear problems. 
We refer to :cite:`ambrosetti1995primer` for more details.

Throughout this section, $\Omega$ is a bounded set in $\R^d$. 

.. ################
.. prf:definition::

    A function $f : \Omega \times \R \to \R$ is called a Caratheodory function if it satisfies the following two properties: 
    
    - For almost every $\x \in \Omega$, the mapping $s \mapsto f(\x,s)$ is continuous. 
      
    - For all $s \in \R$, the mapping $\x \mapsto f(x,s)$ is measurable.
   
.. ################

Now, to each Caractheodory function, we associate formally a (non linear) operator $T_f$ acting on functions $u : \Omega \to \R$ via the following formula:

$$T_f u (\x) = f(\x, u(\x)). $$

Under suitable conditions on the function $f$, this defines a mapping between certain Lebesgue spaces, as made more specific by the following statement. 

.. ################
.. prf:theorem::

   Let $p,q \geq 1$, and let $f : \Omega \times \R \to \R$ be a Caratheodory function, satisfying the following growth condition:
   
   $$\text{For a.e. } \x \in \Omega \text{ and all } s \in \R, \quad \lvert f(x,s) \lvert \leq a + b \lvert s \lvert^{\frac{p}{q}}.$$
   
   Then the mapping $T_f$ maps $L^p(\Omega)$ into $L^q(\Omega)$, and it defines a continuous operator between these spaces.
   
.. ################

The following statement now gives sufficient conditions for this mapping to be differentiable. 

.. ################
.. prf:theorem:: Differentiability of Nemitski operators, case $p>2$

   Let $p > 2$ be given, and let $f : \Omega \times \R \to \R$ be a Caratheodory function such that: 
   
     - The function $\Omega \ni \x \mapsto f(\x,0)$ is bounded on $\Omega$; 
     
     - It holds, for a.e. $\x \in \Omega$ and all $s \in \R$, $\left\lvert \frac{\partial f}{\partial s} (\x,s) \right\lvert \leq a + b \lvert s \lvert^{p-2}$. 
     
   Then the mapping $T_f$ defines a continuous operator from $L^p(\Omega)$ into $L^{p^\prime}(\Omega)$, where $p^\prime$ is the conjugate exponent of $p$. Moreover, this mapping is Fréchet differentiable, with derivative: 
   
   $$f(\x,u(\x)+v(\x))  = f(\x,u(\x)) + \frac{\partial f}{\partial s} (\x,u(\x)) v(\x) + \o(\lvert\lvert v \lvert\lvert_{L^p(\Omega)}).  $$ 
   
.. ################

Note that the operator $T_f$ is well defined as an operator from $L^p(\Omega)$ into $L^{p^\prime}(\Omega)$, since the above condition in particular implies, upon integration, that:

$$\lvert f(\x,s) \lvert \leq a + b \lvert s \lvert^{p-1}, \text{ for different constants } a,b >0.$$


The above theorem does not cover the case where $p=2$. A similar -- albeit a little weaker -- statement holds in this case, under slightly stronger assumptions. 

.. ################
.. prf:theorem:: Differentiability of Nemitski operators, case $p=2$

   Let $f : \Omega \times \R \to \R$ be a Caratheodory function such that $\frac{\partial f}{\partial s}$ is also a Caratheodory function. Assume in addition that:
   
   $$\text{There exists a constant } C >0 \text{ s.t. } \lvert f(\x,s) \lvert \leq C \text{ for a.e. } \x \in \Omega \text{ and all } s \in \R. $$
     
   Then $T_f$ is a continuous operator from $L^2(\Omega)$ into itself. Moreover, this mapping is Gâteaux differentiable at every $u \in L^2(\Omega)$, i.e.
   
   $$\forall v \in L^2(\Omega), \quad \left\lvert\left\lvert \frac{f(\x,u(\x)+t(v(\x))) - f(\x,u(\x))}{t}  - \frac{\partial f}{\partial s}(\x,u(\x)) v(\x)\right\lvert\right\lvert \xrightarrow{t\to 0} 0.$$ 
   
.. ################

.. ##########
.. admonition:: Exercise
   :class: admonition-exo

   Show that the mapping $T:H^1(\Omega) \to L^2(\Omega)$, defined by:
   
   $$\forall u \in H^1(\Omega), \quad T(u) = \max(0,u)$$
   
   is Fréchet differentiable at any $u \in H^1(\Omega)$, with derivative:
   
   $$T^\prime(u)(h) = \chi_{\left\{ u \geq 0\right\}} h.$$
 
.. ##########

.. ##########
.. admonition:: Correction
    :class: dropdown
    
    Bla bla bla
    
.. ##########

