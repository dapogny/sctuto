Complements of functional analysis
====================================

This appendix is a pot-pourri of results in functional analysis that underlie some of the theoretical developments of this book.

.. ##################################################
.. ##################################################

.. _sec.Banachcontraction:

The Banach contraction mapping theorem
----------------------------------------

.. ##################################################
.. ##################################################

.. ########

.. _th.BanachFP:

.. prf:theorem:: Banach contraction mapping
   
   Let $E$ be a Banach space, and let $A : E \to E$ be a (possibly non linear) mapping. Assume that $A$ is a contraction, i.e. there exists $k<1$ such that:
   
   $$\forall u,v \in E, \quad \lvert\lvert Au - Av \lvert\lvert < k \lvert\lvert u - v \lvert\lvert. $$
   
   Then $A$ has a unique fixed point $u^* \in V$, i.e. there is a unique $u^* \in V$ such that $Au^* = u^*$.  
   

.. ########

.. ##################################################
.. ##################################################

.. _sec.uniquelim:

The uniqueness of the limit argument
-------------------------------------

.. ##################################################
.. ##################################################

Let $V$ be a topological vector space. This argument is generic, but the reader which does not want to bother with the language of topological vector spaces can think of $V$ as a Hilbert space, equipped with notion of strong or weak convergence. 

.. ########

.. prf:lemma::
   
   Let $\left\{u_n\right\}_{n\in \N}$ be a sequence of elements in $V$ such that there exists $u^* \in V$ with the following property:
   $$\text{From any subsequence }\left\{u_{n_k}\right\}_{k \in \N} \text{ of }u_n, \text{ one can extract a sub-subsequence }\left\{u_{n_{k_l}}\right\}_{l \in \N} \text{ converging to }u^*.$$ 
   Then, the whole sequence $\left\{u_n\right\}_{n\in \N}$ converges to $u^*$.

.. ########

.. ########

.. prf:proof::
   
   We argue by contradiction, assuming that $\left\{u_n\right\}_{n\in \N}$ does not converge to $u^*$. 
   
   On the one hand, by negating the definition of convergence of a sequence, there exists an open subset $U$ of $V$ containing $u^*$ and a subsequence $\left\{u_{n_k}\right\}_{k\in \N}$ of $\left\{u_n\right\}_{n\in \N}$ such that $u_{n_k} \in V \setminus U$ for all $k \in \N$.
   
   On the other hand, the assumption implies that there exists a sub-subsequence $\left\{u_{n_{k_l}}\right\}_{l \in \N}$ of $\left\{u_{n_k}\right\}_{k\in \N}$ which converges to $u^*$. In particular, for $l$ large enough, $u_{n_{k_l}}$ belongs to $U$. 
   
   We have come to the desired contradiction: such an element $u_{n_{k_l}}$ cannot belong to $U$ and $V \setminus U$ at the same time.
   
.. ########


.. ##################################################
.. ##################################################

.. _sec.weakcv:

Weak convergence in a Hilbert space
------------------------------------

.. ##################################################
.. ##################################################

This section recalls a few facts about the important notion of weak convergence. Note that many of these hold true in a larger context, that of reflexive Banach spaces, although we shall not need such generality. See again :cite:`brezis2010functional` for more details.

.. ########

.. prf:definition::
  
   A sequence $u_n \in H$ converges weakly to an element $u \in H$ if:
   
   $$\forall v \in H, \quad ( u_n, v )_H \xrightarrow{n \to \infty} 0.$$
   
.. ########

A few useful properties of weakly convergent sequences are listed below.

.. ########

.. prf:proposition::
  
   Let $u_n$ be a sequence in $H$, which converges weakly to an element $u \in H$. Then,
   
     - $u$ is the unique weak limit of the sequence $u_n$.
     
     - $u_n$ is bounded.
   
.. ########

The following very important fact states the weak sequential compactness of bounded subsets of a Hilbert space.

.. ########

.. _prop.seqcompactbounded:

.. prf:proposition::
  
   Let $u_n$ be a bounded sequence in $H$. Then there exists a subsequence $n_k$ and $u \in H$ such that $u_{n_k}$ converges weakly to $u$.
   
.. ########

.. ##################################################
.. ##################################################

.. _sec.compact:

Compactness
------------

.. ##################################################
.. ##################################################

.. ########

.. _def.compact: 

.. prf:definition::
  
   Let $H_1$, $H_2$ be two Hilbert spaces. A linear operator $T : H_1 \to H_2$ is called compact if for any sequence $u_n$ of elements in $H_1$ converging weakly to some $u^* \in H_1$, the sequence $T u_n \in H_2$ converges strongly in $H_2$.
   
.. ########

An example of a compact operator which is crucial in applications arises in the context of Sobolev spaces, broached in :numref:`sec.Sobolev`. 

.. ########

.. _th.Rellich: 

.. prf:theorem:: Rellich theorem
  
   Let $\Omega$ be a bounded Lipschitz domain in $\R^d$. Then the injection $H^1(\Omega) \to L^2(\Omega)$ is compact.
   
.. ########


