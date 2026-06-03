---
title: A Survey of Informal Proof Strategies for the Collatz Conjecture
type: paper
created: 2026-06-03T09:30:00+00:00
updated: 2026-06-03T09:30:00+00:00
---

# A Survey of Informal Proof Strategies for the Collatz Conjecture

*Exploratory notes toward a spectral interpretation of the Collatz dynamics.*

## Abstract

The Collatz conjecture states that the sequence defined by

$$
T(n) =
\begin{cases}
n/2 & n \text{ even},\\[2pt]
3n+1 & n \text{ odd}
\end{cases}
$$

always reaches the cycle

$$
1 \to 4 \to 2 \to 1
$$

for every positive integer $n$.

This document collects a series of ideas, intuitions, analogies, and possible
strategies that emerged during an informal exploration of the problem. Many of
the ideas recorded here are speculative, incomplete, or probably wrong, but they
are preserved as potential sources of insight. None of the strategies described
currently constitutes a proof of the conjecture; together they form a *map* of
the directions explored.

## 1. Proof by Contradiction

Initial idea: suppose there exists a number that never reaches $1$, and analyse
the structural consequences of this hypothesis. The possible cases are:

- divergence to infinity;
- an alternative cycle;
- a bounded, non-periodic trajectory.

The goal would be to show that each possibility leads to a contradiction.

## 2. Inductive Strategy

Attempt: if Collatz holds for all numbers less than $n$, then it holds for $n$.

Problem: trajectories can rise far above $n$ before descending. For example,

$$
27
$$

reaches values far larger than $27$, which blocks the direct application of
classical induction.

## 3. The Inverse Collatz Tree

Build the tree of predecessors. For a number $n$:

- the even predecessor is

$$
2n,
$$

- the odd predecessor is

$$
\frac{n-1}{3}
$$

when admissible.

Question: does the inverse tree cover all the naturals? A possible approach is
to show that every number belongs to the tree rooted at $1$.

## 4. Analysis of the Tree's Leaves

Observation: there is a threshold beyond which many nodes have a single
predecessor. One could study the statistical distribution of nodes with:

- one child;
- two children.

## 5. Removing the `if`

Continuous rewriting of the map:

$$
f(x) = \frac{7x+2}{4} - \frac{5x+2}{4}\cos(\pi x).
$$

On the integers,

$$
\cos(\pi n) = (-1)^{n},
$$

and one recovers Collatz exactly. The advantage is the transformation of an
arithmetic problem into an analytic one.

## 6. Harmonic Expansion

Interpretation: parity is replaced by a phase,

$$
(-1)^{n} = e^{i\pi n},
$$

and Collatz becomes a harmonic system.

## 7. Taylor Series Expansion

Substituting

$$
\cos(\pi x) = \sum_{k=0}^{\infty} (-1)^{k}\frac{(\pi x)^{2k}}{(2k)!},
$$

Collatz is represented as an infinite series. A possible approach is to study
the asymptotic behaviour of the series.

## 8. Spectral Interpretation

Hypothesis: the integers represent resonance points. On the integers,

$$
e^{i\pi n} = \pm 1,
$$

so the integers sample exclusively the extremes of the phase.

## 9. The Fundamental Oscillator

Interpret the terminal cycle

$$
1 \to 4 \to 2
$$

as a fundamental wave. Collatz does not collapse toward a *number*; it collapses
toward a *rhythm*.

## 10. Phase Classes

Definition:

$$
\phi(n) = s(n) \bmod 3,
$$

where $s(n)$ is the stopping time. Numbers are then classified into three
phases.

## 11. The Continuous Wave Associated with the Cycle

Construct a periodic function

$$
w(t+3) = w(t)
$$

that interpolates

$$
1, 4, 2.
$$

A possible approach is to study the residue.

## 12. Residue Relative to the Fundamental Wave

Definition:

$$
r(t) = x(t) - w(t + \phi).
$$

Hypothesis:

$$
r(t) \to 0
$$

for every trajectory.

## 13. A Hidden Lyapunov Function

Search for a quantity

$$
E(n)
$$

such that

$$
E(T(n)) < E(n)
$$

always. The central idea: there exists an *energy* that decreases even when

$$
3n+1 > n.
$$

## 14. Analysis of the Zeros

Definition:

$$
g(x) = f(x) - x.
$$

Study the zeros as equilibrium points, by analogy with:

- the logarithm;
- the exponential;
- polynomials.

## 15. Study of the Iterates

Generalisation:

$$
f^{k}(x) - x.
$$

Its zeros represent:

- fixed points;
- cycles;
- periodic attractors.

## 16. Analysis over the Reals

Continuous extension of the map. Observation: non-integer values may

- diverge;
- oscillate;
- behave entirely differently from the integers.

Question: why are the integers stable?

## 17. The Resonance Hypothesis

Interpretation: the integers constitute synchronised states of the continuous
dynamics. Reals out of phase are expelled.

## 18. Geometric Interpretation

The attractors are interpreted as perspective vanishing points. Trajectories
converge toward a stable geometric object.

## 19. Compression of Information

The dynamics

$$
f \to f^{\infty}
$$

loses information: many different dynamics can produce the same attractor.

## 20. Analogy with Feedback

In control theory,

$$
\frac{G}{1 + GH}
$$

represents an infinite loop written in closed form. Question: is there a closed
form for

$$
\mathrm{Collatz}^{\infty}?
$$

## 21. The Theory of Infinite Applications

General idea: build a theory of

$$
f^{\infty}
$$

as a primary mathematical object, of which Collatz would be a particular case.

## 22. Inverse Analysis

The inverse problem: given an attractor, which dynamics generates it? In the
Collatz case, given

$$
\{1, 4, 2\},
$$

which functions produce that cycle?

## 23. Philosophical Interpretation

A possible principle: the observed mathematical structures may be the stable
residue of infinite iterative processes. Collatz would then be one of the
simplest cases in which such a mechanism becomes observable.

## Conclusion

The ideas collected here can be grouped into four broad families.

1. **Combinatorial approaches** — inverse tree, induction, covering of the
   naturals.
2. **Dynamical approaches** — attractors, cycles, Lyapunov functions.
3. **Harmonic approaches** — phase, fundamental oscillator, spectral
   decomposition.
4. **Philosophical approaches** — the theory of infinite applications, emergent
   objects, compression of information.

None of the strategies described currently constitutes a proof of the Collatz
conjecture. They do, however, provide a map of the directions explored and of
the possible connections between number theory, dynamical systems, and harmonic
analysis.

The curious point is that, looking over the list, the most original thread is
not the inverse tree or induction (which are classical), but the idea that the
cycle $1 \to 4 \to 2$ can be interpreted as a **fundamental mode**, and that
Collatz can be studied as a problem of **synchronisation toward an oscillator**.
This is the line furthest from the standard literature, and the one that
generated the most ideas during the discussion.