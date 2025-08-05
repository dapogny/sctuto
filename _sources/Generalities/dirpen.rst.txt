.. _sec.dirtgv:

Imposing Dirichlet boundary conditions by exact penalization
============================================================

.. ##########

In this section, we present a simple and efficient numerical method to enforce the Dirichlet boundary conditions of a boundary-value problem. 
This method is actually the one used in most Finite Element libraries; in particular, it is the numerical recipe underlying the keyword :code:`on` in $\texttt{FreeFem}$.

To set ideas, let us consider the Laplace equation with homogeneous Dirichlet boundary conditions of :numref:`sec.lap`. Reusing the notations of the latter, its variational formulation reads:

.. ##########

.. math::
  :label: eq.dirpen
  
  \text{Search for } u \in H^1_0(\Omega) \text{ s.t. } \forall v \in H^1_0(\Omega), \:\: \int_{\Omega}{\nabla u \cdot \nabla v \:\d \x} = \int_{\Omega}{fv\:\d\x}.

.. ##########

The direct implementation of the Finite Element Method for the discretization and solution of this problem is somewhat tedious, even in the case of the relatively simple $\P_1$ Lagrange Finite Element method described in :numref:`sec.FE`. This task indeed requires to assemble the stiffness matrix $K_h$ by retaining only those degrees of freedom lying in the interior of $\Omega$, which raises cumbersome renumbering issues of the vertices of the mesh $\calT_h$.
    
A much simpler approach consists in approximating $u$ by the solution $u_\e \in H^1(\Omega)$ to the following problem:

.. ##########

.. math::
  :label: eq.dirpen2
  
  \text{Search for } u _\e \in H^1(\Omega) \text{ s.t. } \forall v \in H^1(\Omega), \:\: \int_{\Omega}{\nabla u_\e \cdot \nabla v \:\d\x} + \frac{1}{\varepsilon}\int_{\partial \Omega}{u _\e v \:\d s} = \int_{\Omega}{fv\:\d\x},

.. ##########

where $\varepsilon$ is a \"very small\" parameter (typically of the order of $10^{-20}$).
Intuitively, $u_\e$ does not exactly equal $0$ on $\partial \Omega$, but the second integral in the left-hand side of :math:numref:`eq.dirpen2` is a large penalization of its values on $\partial \Omega$.

The validity of this approach is assessed by the following theoretical exercise. 

.. ##########
.. admonition:: Exercise
   :class: admonition-exo

   This exercise uses the notions of compactness and weak convergence in Hilbert spaces, recalled in :numref:`sec.compact`. 
   
     (1) Prove the following version of the :ref:`Poincaré's inequality <prop.Poincare>`: there exists a constant $C >0$ such that:
     
         $$\forall u \in H^1(\Omega), \quad \int_\Omega u^2 \:\d \x \leq C \left( \int_\Omega \lvert \nabla u \lvert^2 \:\d\x + \int_{\partial \Omega} u^2 \:\d s \right). $$

     (2) Prove that the solution $u_\e$ to :math:numref:`eq.dirpen2` is bounded in $H^1(\Omega)$, independently of the value of $\e$, i.e. that there exists a constant $C >0$ such that, for $\e >0$ small enough, 
     
         $$\lvert\lvert u _\e \lvert\lvert_{H^1(\Omega)} \leq C \lvert\lvert f \lvert\lvert_{L^2(\Omega)}. $$
         
         Deduce that there exists a function $u_* \in H^1(\Omega)$ such that:
    
         $$u_\e \xrightarrow{\e \to 0} u_* \text{ weakly in } H^1(\Omega).$$
    
     (3) Prove that $u_*$ is the unique solution $u \in H^1_0(\Omega)$ to the exact variational problem :math:numref:`eq.dirpen`.

     (4) Prove that $u_\e$ actually converges to $u$ strongly in $H^1(\Omega)$ when the penalization parameter $\e$ vanishes, i.e. 
    
         $$\lvert\lvert u _\e - u \lvert\lvert_{H^1(\Omega)} \xrightarrow{\e \to 0} 0.$$
      
.. ##########

.. ##########
.. admonition:: Correction
    :class: dropdown

    (1) The proof of this inequality relies on a contradiction argument very similar to that of the proof of  :ref:`Poincaré's inequality <prop.Poincare>`, and we omit the proof for brevity.
        
        
    (2) Taking $u_\e$ as test function in the variational problem :math:numref:`eq.dirpen2`, we obtain:
        $$\int_\Omega \lvert \nabla u _\e \lvert^2 \:\d x + \frac{1}{\e} \int_{\partial \Omega} u _\e^2 \:\d s = \int_\Omega f u _\e \:\d \x. $$
        Now combining the Cauchy-Schwarz inequality with the Poincaré's inequality proved in the former question, we obtain:
        $$\begin{array}{ccl}
        \displaystyle\int_\Omega \lvert \nabla u _\e \lvert^2 \:\d x + \frac{1}{\e} \displaystyle\int_{\partial \Omega} u _\e^2 \:\d s &\leq& \lvert\lvert f \lvert\lvert_{L^2(\Omega)} \lvert\lvert u _\e \lvert\lvert_{L^2(\Omega)} \\ 
        &\leq& C \lvert\lvert f \lvert\lvert_{L^2(\Omega)} \left( \displaystyle\int_\Omega \lvert \nabla u _\e \lvert^2 \:\d\x + \displaystyle\int_{\partial \Omega} u _\e^2 \:\d s\right)^{\frac{1}{2}} \\
        &\leq& C \lvert\lvert f \lvert\lvert_{L^2(\Omega)} \left( \displaystyle\int_\Omega \lvert \nabla u _\e \lvert^2 \:\d\x + \frac{1}{\e}\displaystyle\int_{\partial \Omega} u _\e^2 \:\d s\right)^{\frac{1}{2}}.
        \end{array}
        $$
        This proves that:
        $$\displaystyle\int_\Omega \lvert \nabla u _\e \lvert^2 \:\d x + \frac{1}{\e} \displaystyle\int_{\partial \Omega} u _\e^2 \:\d s \leq C \lvert\lvert f \lvert\lvert_{L^2(\Omega)}^2,$$
        and in particular, $u_\e$ is a bounded sequence in $H^1(\Omega)$. 
        
        Now invoking :numref:`prop.seqcompactbounded`, there exists a subsequence $u_{\e_k}$ of $u_\e$ and a function $u_* \in H^1(\Omega)$ such that:
        $$u_{\e_k} \xrightarrow{k \to \infty} u_* \text{ weakly in } H^1(\Omega). $$
                
    (3) For a fixed test function $v \in H^1(\Omega)$, the variational equation :math:numref:`eq.dirpen2` rewrites: 
        $$\int_{\partial\Omega} u _{\e_k} v \:\d s = - \e_k \int_\Omega \nabla u _{\e_k} \cdot \nabla v \:\d \x + \e_k \int_\Omega f v \:\d \x. $$
        Since the sequence $u_{\e_k}$ is bounded in $H^1(\Omega)$ and the trace operator is continuous from $H^1(\Omega)$ into $H^{1/2}(\partial \Omega)$, we may take limits in the previous expression, which yields: 
        $$\int_{\partial \Omega} u_* v \:\d s = 0.$$
        Since this holds for an arbitrary function $v \in H^1(\Omega)$, it follows that $u_* = 0$ on $\partial \Omega$.
        Now, for a given test function $v \in H^1_0(\Omega)$, the variational problem :math:numref:`eq.dirpen2` reads: 
        $$\int_{\Omega}{\nabla u _{\e_k} \cdot \nabla v \:\d\x}  = \int_{\Omega}{fv\:\d\x}.$$
        Passing to the limit in this expression thanks to the weak $H^1(\Omega)$ convergence of $u_{\e_k}$ to $u_*$, we see that $u_*$ satisfies :math:numref:`eq.dirpen`. The solution to this variational problem being unique, we obtain that $u_* = u$. 
        
        At this point, we have proved that the particular subsequence $u_{\e_k}$ of $u_\e$ that we have considered converges weakly in $H^1(\Omega)$ to the unique solution $u$ to :math:numref:`eq.dirpen`. Since this holds true for any weakly convergent subsequence of $u_\e$, we deduce from :ref:`a classical argument based on the uniqueness of the weak limit <sec.uniquelim>` that the whole sequence $u_\e$ weakly converges to $u$ in $H^1(\Omega)$.
        
    (4) By expanding the squares, we see that:
        $$\displaystyle\int_\Omega \lvert \nabla u _\e  - \nabla u \lvert^2 \:\d \x + \frac{1}{\e} \displaystyle\int_{\partial \Omega}\lvert  u _\e - u \lvert ^2 \:\d s =  \displaystyle\int_\Omega \lvert \nabla u _\e \lvert^2 \:\d \x +  \displaystyle\int_\Omega \lvert \nabla u \lvert^2 \:\d \x - 2  \displaystyle\int_\Omega  \nabla u _\e \cdot \nabla u \:\d \x + \frac{1}{\e}\int_{\partial \Omega} u _\e^2 \:\d s.$$
        Now invoking the variational problems :math:numref:`eq.dirpen` and :math:numref:`eq.dirpen2` respectively satisfied by $u _\e$ and $u$, we obtain:
        $$\displaystyle\int_\Omega \lvert \nabla u _\e  - \nabla u \lvert^2 \:\d \x + \frac{1}{\e} \displaystyle\int_{\partial \Omega}\lvert  u _\e - u \lvert ^2 \:\d s = -\frac{1}{\e} \int_{\partial \Omega} u _\e^2 \:\d s + \int_\Omega f u _\e \:\d \x + \int_\Omega f u \:\d \x - 2 \int_{\Omega} f u \:\d \x + \frac{1}{\e} \int_{\partial \Omega} u _\e^2 \:\d s. $$
        Rearranging the foregoing expression, we obtain:
        $$\displaystyle\int_\Omega \lvert \nabla u _\e  - \nabla u \lvert^2 \:\d \x + \frac{1}{\e} \displaystyle\int_{\partial \Omega}\lvert  u _\e - u \lvert ^2 \:\d s = \int_\Omega f (u _\e - u) \:\d \x. $$
        Since $u _\e \to u$ weakly in $H^1(\Omega)$, the right-hand side in the above equality tends to $0$ as $\e \to 0$, which is the expected conclusion.
   
.. ##########

The practical implementation of the penalization method for Dirichlet boundary conditions is relatively straightforward, and it is left as an exercise; the solution can be downloaded :download:`here <./codes/laplace_pen_Dirichlet.edp>`. 

.. ##########
.. admonition:: Exercise
   :class: admonition-exo
   
    Let $\Omega \subset \R^2$ be the L-shaped domain represented in :numref:`fig.LShapeLap` (left), and let $f = 1$. Let $u \in H^1_0(\Omega)$ and $u_\e \in H^1(\Omega)$ be the unique solutions to :math:numref:`eq.dirpen` and :math:numref:`eq.dirpen`, respectively. 

    (1) Solve the penalized problem for $u_\e$ with $\texttt{FreeFem}$; you may try out different values for the parameter $\e$.

    (2) Adapt the above penalization trick to the numerical resolution of the following version of the Laplace equation:
  
        $$\left\{\begin{array}{cl} - \Delta u = 0 & \text{in } \Omega, \\ u = 1 & \text{on }\partial \Omega, \end{array} \right.$$
      
.. ##########

