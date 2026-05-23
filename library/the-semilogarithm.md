---
title: The Semilogarithm
type: paper
created: 2026-05-23T13:00:00+00:00
updated: 2026-05-23T13:15:00+00:00
---

# The Semilogarithm

## Abstract

This paper studies a function $s$ satisfying the functional equation

$$
s(s(x))=\log x.
$$

Such a function may be called a semilogarithm, because it is a compositional
square root of the natural logarithm. The goal is not only to define the object
formally, but also to map its values in a way that reveals known constants and
structural constraints. In particular, the equation implies that two successive
applications of $s$ move a value exactly as one application of $\log$ does.

## Definition

Let $I$ be a set on which the natural logarithm and the compositions involved
are meaningful. A semilogarithm on $I$ is a function

$$
s:I \to I
$$

such that

$$
s(s(x))=\log x.
$$

Equivalently, if composition is denoted by $\circ$, then

$$
s \circ s = \log.
$$

Thus $s$ is a functional square root of the logarithm.

This is different from the numerical square root of $\log x$. In general,

$$
s(x) \neq \sqrt{\log x}.
$$

The square root here is taken with respect to composition, not multiplication.

## Immediate Consequences

The defining equation gives direct information at familiar points:

$$
s(s(e))=1,
$$

because $\log e=1$;

$$
s(s(1))=0,
$$

because $\log 1=0$;

and

$$
s(s(e^a))=a
$$

for every real number $a$ for which the expression belongs to the chosen domain.

In particular,

$$
s(s(e^e))=e,
$$

$$
s(s(e^{e^e}))=e^e,
$$

and, more generally, if

$$
E_0=1, \qquad E_{n+1}=e^{E_n},
$$

then

$$
\log E_{n+1}=E_n,
$$

so the semilogarithm must satisfy

$$
s(s(E_{n+1}))=E_n.
$$

This gives a natural discrete skeleton for the function.

## A Value Map

The previous relation suggests introducing intermediate values between known
logarithmic steps. Define formal half-step values $H_n$ by

$$
H_n=s(E_{n+1}).
$$

Then

$$
s(H_n)=E_n.
$$

Therefore the semilogarithm maps the chain

$$
E_{n+1} \longmapsto H_n \longmapsto E_n.
$$

For the first values this gives

$$
e \longmapsto H_0 \longmapsto 1,
$$

$$
e^e \longmapsto H_1 \longmapsto e,
$$

$$
e^{e^e} \longmapsto H_2 \longmapsto e^e.
$$

The values $H_n$ are not determined by the equation alone. They are the new
intermediate constants introduced by taking a compositional square root of the
logarithm. A specific theory of the semilogarithm must decide where these
half-step values lie.

## Non-Uniqueness

The equation

$$
s \circ s = \log
$$

does not determine a unique function without additional assumptions such as
monotonicity, analyticity, domain restrictions, or normalization conditions.

Indeed, knowing that

$$
s(s(e))=1
$$

does not by itself determine $s(e)$. If we set

$$
s(e)=a,
$$

then the equation only forces

$$
s(a)=1.
$$

The intermediate value $a$ is a choice. The same phenomenon occurs for every
point $x$: the equation fixes the result after two steps, but not necessarily
the result after one step.

Thus the semilogarithm should be understood as a family of possible functions,
not as a single elementary function.

## Abel Coordinates

A systematic way to describe a semilogarithm is to use an Abel coordinate. Suppose
there exists a function $\Phi$ such that

$$
\Phi(\log x)=\Phi(x)+1.
$$

Then one may define a half-iterate of the logarithm by

$$
s(x)=\Phi^{-1}\left(\Phi(x)+\frac{1}{2}\right).
$$

Applying $s$ twice gives

$$
s(s(x))
=\Phi^{-1}\left(\Phi(x)+1\right)
=\log x.
$$

In these coordinates, the logarithm is a unit translation, while the
semilogarithm is a half-unit translation.

This representation clarifies the value map. If

$$
\Phi(E_n)=c+n,
$$

then

$$
\Phi(H_n)=c+n+\frac{1}{2}.
$$

The unknown values $H_n$ are therefore the points with half-integer Abel
coordinates between $E_{n+1}$ and $E_n$.

## Commutation With the Logarithm

The equation

$$
s(s(x))=\log x
$$

implies an important exchange law. Since

$$
\log=s\circ s,
$$

we have

$$
s(\log x)=s(s(s(x)))
$$

and also

$$
\log(s(x))=s(s(s(x))).
$$

Therefore,

$$
s(\log x)=\log(s(x)).
$$

This identity does not add a new axiom; it follows from the definition of the
semilogarithm. It says that applying one logarithmic step and then a half-step
is equivalent to applying a half-step and then one logarithmic step.

This gives useful value relations. For example, if

$$
s(e)=H_0,
$$

then

$$
s(1)=s(\log e)=\log(s(e))=\log H_0.
$$

But the defining equation also gives

$$
s(s(1))=0.
$$

So the unknown value $H_0$ determines a chain

$$
e \longmapsto H_0 \longmapsto 1 \longmapsto \log H_0 \longmapsto 0.
$$

Similarly, if

$$
s(e^e)=H_1,
$$

then

$$
s(e)=s(\log(e^e))=\log(s(e^e))=\log H_1.
$$

Since $s(e)=H_0$, we get

$$
H_0=\log H_1,
$$

or equivalently

$$
H_1=e^{H_0}.
$$

In general, for the tower values

$$
E_0=1, \qquad E_{n+1}=e^{E_n},
$$

and the half-step values

$$
H_n=s(E_{n+1}),
$$

commutation gives

$$
H_{n-1}=\log H_n,
$$

or

$$
H_n=e^{H_{n-1}}.
$$

Thus the half-step constants form their own exponential tower:

$$
H_1=e^{H_0}, \qquad H_2=e^{H_1}, \qquad H_3=e^{H_2}, \ldots
$$

This is a meaningful value map. The equation alone still does not determine the
initial half-step $H_0=s(e)$, but once $H_0$ is chosen, the higher half-step
values are forced by the commutation relation.

## Mapping Around Known Values

The semilogarithm can be organized by the following table:

| $x$ | $\log x$ | Required semilogarithmic relation |
|---|---:|---|
| $1$ | $0$ | $s(s(1))=0$ |
| $e$ | $1$ | $s(s(e))=1$ |
| $e^e$ | $e$ | $s(s(e^e))=e$ |
| $e^{e^e}$ | $e^e$ | $s(s(e^{e^e}))=e^e$ |
| $e^a$ | $a$ | $s(s(e^a))=a$ |

The table shows that the known values are not usually values of $s$ itself, but
values of $s \circ s$. The task of constructing a semilogarithm is precisely the
task of inserting one coherent intermediate layer between each logarithmic step.

## Relation With Iteration

The logarithm can be iterated:

$$
\log^{\circ 0}(x)=x,
$$

$$
\log^{\circ 1}(x)=\log x,
$$

$$
\log^{\circ 2}(x)=\log(\log x),
$$

and so on. The semilogarithm is a fractional iterate:

$$
s(x)=\log^{\circ 1/2}(x).
$$

Thus

$$
s^{\circ 2}(x)=\log^{\circ 1}(x).
$$

More generally, if fractional iterates are available, one expects

$$
\log^{\circ a}(\log^{\circ b}(x))=\log^{\circ(a+b)}(x),
$$

and the semilogarithm corresponds to the case $a=1/2$.

## Conclusion

The semilogarithm is a compositional square root of the logarithm:

$$
s(s(x))=\log x.
$$

Its most important structural feature is that it inserts a half-step into the
usual logarithmic descent. Known values of the logarithm create the constraints

$$
e^a \longmapsto s(e^a) \longmapsto a,
$$

but the intermediate point $s(e^a)$ is not determined without further analytic
or geometric assumptions.

The central problem is therefore one of coherent interpolation: to construct a
function that maps known logarithmic chains into half-steps while preserving the
composition law. In Abel coordinates, this becomes the problem of turning the
logarithm into a translation and then taking half of that translation.
