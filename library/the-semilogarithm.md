---
title: The Semilogarithm
type: paper
created: 2026-05-23T13:00:00+00:00
updated: 2026-05-23T14:50:00+00:00
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

## Derivative Relations

Since the derivative of the logarithm is known, the defining equation of the
semilogarithm gives information about the derivative of $s$. Starting from

$$
s(s(x))=\log x,
$$

and differentiating both sides, we obtain

$$
s'(s(x))s'(x)=\frac{1}{x}.
$$

Thus the derivative of $s$ at $x$ is coupled with the derivative of $s$ at the
shifted point $s(x)$. Equivalently,

$$
s'(s(x))=\frac{1}{xs'(x)}.
$$

This is a functional equation for the derivative of the semilogarithm.

The commutation law gives a second relation. Since

$$
s(\log x)=\log(s(x)),
$$

we may differentiate both sides. The derivative of the left-hand side is

$$
\frac{s'(\log x)}{x},
$$

while the derivative of the right-hand side is

$$
\frac{s'(x)}{s(x)}.
$$

Therefore,

$$
\frac{s'(\log x)}{x}=\frac{s'(x)}{s(x)},
$$

or

$$
s'(\log x)=\frac{x s'(x)}{s(x)}.
$$

This is the special relation that emerges by equating the derivatives of
$s(\log x)$ and $\log(s(x))$. It says that the derivative at the logarithmic
point $\log x$ is determined by the derivative at $x$, scaled by the ratio
$x/s(x)$.

Combining the two derivative identities gives two equivalent ways to transport
local slope information:

$$
s'(s(x))s'(x)=\frac{1}{x},
$$

and

$$
s'(\log x)=\frac{x s'(x)}{s(x)}.
$$

The first relation moves from $x$ to the semilogarithmic point $s(x)$. The
second relation moves from $x$ to the logarithmic point $\log x$.

### Consequences at Normalized Values

Under the normalization

$$
s\left(\frac{1}{2}\right)=0,
$$

we also have

$$
s(1)=\frac{1}{2}, \qquad s(e)=\sqrt e, \qquad s(\sqrt e)=1.
$$

Let

$$
a=s'(1).
$$

The derivative equation at $x=1$ gives

$$
s'\left(s(1)\right)s'(1)=1,
$$

hence

$$
s'\left(\frac{1}{2}\right)=\frac{1}{a}.
$$

The derivative equation at $x=\frac{1}{2}$ gives

$$
s'(0)s'\left(\frac{1}{2}\right)=2,
$$

so

$$
s'(0)=2a.
$$

The commutation derivative at $x=e$ gives

$$
s'(1)=\frac{e s'(e)}{s(e)}.
$$

Since $s(e)=\sqrt e$, we obtain

$$
s'(e)=\frac{a}{\sqrt e}.
$$

Finally, using

$$
s'(s(e))s'(e)=\frac{1}{e},
$$

we get

$$
s'(\sqrt e)=\frac{1}{\sqrt e\,a}.
$$

Thus the local derivatives around the normalized chain are not arbitrary. They
are determined by a single parameter $a=s'(1)$:

| Point | Value of the derivative |
|---:|---:|
| $0$ | $2a$ |
| $1/2$ | $1/a$ |
| $1$ | $a$ |
| $\sqrt e$ | $1/(\sqrt e\,a)$ |
| $e$ | $a/\sqrt e$ |

The parameter $a$ remains free because the functional equation determines how
slopes are transported, but it does not by itself fix the initial slope. A full
analytic construction of the semilogarithm would need to determine or normalize
this value.

## A Normalization Through Zero

A natural way to reduce the freedom of the semilogarithm is to impose a
normalization. We now choose the condition

$$
s\left(\frac{1}{2}\right)=0.
$$

This means that the semilogarithm passes through zero at the value $1/2$. This
single choice has several consequences.

First, applying the defining equation at $x=1/2$ gives

$$
s\left(s\left(\frac{1}{2}\right)\right)=\log\left(\frac{1}{2}\right).
$$

Since $s(1/2)=0$, we obtain

$$
s(0)=-\log 2.
$$

Thus the value that follows zero under the semilogarithm is not $-\infty$, but
rather the finite negative number $-\log 2$.

Second, using the commutation law

$$
s(\log x)=\log(s(x)),
$$

with $x=1$, we get

$$
s(0)=\log(s(1)).
$$

Since $s(0)=-\log 2$, this gives

$$
\log(s(1))=-\log 2,
$$

and therefore

$$
s(1)=\frac{1}{2}.
$$

So the normalization produces the chain

$$
1 \longmapsto \frac{1}{2} \longmapsto 0 \longmapsto -\log 2.
$$

The next step is singular. Since

$$
s(s(0))=\log 0,
$$

and

$$
\log 0=-\infty
$$

as a limit from the positive side, we obtain

$$
s(-\log 2)=-\infty.
$$

Thus the finite negative value that is sent to $-\infty$ is

$$
-\log 2.
$$

This answers the boundary question: under this normalization, the point before
$-\infty$ in the semilogarithmic chain is $-\log 2$.

The same normalization also determines the first positive half-step above $1$.
From the earlier relation

$$
s(1)=\log(s(e)),
$$

we get

$$
\frac{1}{2}=\log(s(e)).
$$

Therefore,

$$
s(e)=e^{1/2}=\sqrt e.
$$

Consequently,

$$
s(\sqrt e)=1.
$$

The normalized semilogarithmic chain around the elementary constants is then

$$
e \longmapsto \sqrt e \longmapsto 1 \longmapsto \frac{1}{2}
\longmapsto 0 \longmapsto -\log 2 \longmapsto -\infty.
$$

More generally, the half-step constants become fixed. Since

$$
H_0=s(e)=\sqrt e,
$$

and

$$
H_n=e^{H_{n-1}},
$$

we obtain

$$
H_1=e^{\sqrt e}, \qquad H_2=e^{e^{\sqrt e}}, \qquad
H_3=e^{e^{e^{\sqrt e}}}, \ldots
$$

Thus the normalization $s(1/2)=0$ selects a concrete value map from the family
of possible semilogarithms.

## Alternative Normalization: $s(1/\sqrt e)=0$

The previous normalization was

$$
s\left(\frac{1}{2}\right)=0.
$$

We now compare it with the alternative condition

$$
s\left(\frac{1}{\sqrt e}\right)=0.
$$

This choice is especially natural because

$$
\log\left(\frac{1}{\sqrt e}\right)=-\frac{1}{2}.
$$

Applying the defining equation at $x=1/\sqrt e$ gives

$$
s\left(s\left(\frac{1}{\sqrt e}\right)\right)
=\log\left(\frac{1}{\sqrt e}\right).
$$

Since $s(1/\sqrt e)=0$, we obtain

$$
s(0)=-\frac{1}{2}.
$$

Thus, under this alternative normalization, the value following zero is exactly
$-1/2$ rather than $-\log 2$.

Using the commutation law

$$
s(\log x)=\log(s(x)),
$$

with $x=1$, we get

$$
s(0)=\log(s(1)).
$$

Since $s(0)=-1/2$, this gives

$$
\log(s(1))=-\frac{1}{2},
$$

and therefore

$$
s(1)=e^{-1/2}=\frac{1}{\sqrt e}.
$$

So this normalization produces the chain

$$
1 \longmapsto \frac{1}{\sqrt e} \longmapsto 0 \longmapsto -\frac{1}{2}.
$$

The next step is singular. Since

$$
s(s(0))=\log 0,
$$

we obtain

$$
s\left(-\frac{1}{2}\right)=-\infty.
$$

Therefore the negative finite point sent to $-\infty$ is exactly

$$
-\frac{1}{2}.
$$

This explains why the value $-1/2$ is structurally important: it appears if the
zero of the semilogarithm is placed at $1/\sqrt e$ instead of at $1/2$.

The positive side also changes. From

$$
s(1)=\log(s(e)),
$$

we get

$$
\frac{1}{\sqrt e}=\log(s(e)),
$$

so

$$
s(e)=e^{1/\sqrt e}.
$$

Consequently,

$$
s(e^{1/\sqrt e})=1.
$$

The normalized chain becomes

$$
e \longmapsto e^{1/\sqrt e} \longmapsto 1
\longmapsto \frac{1}{\sqrt e} \longmapsto 0
\longmapsto -\frac{1}{2} \longmapsto -\infty.
$$

### Comparison of the Two Normalizations

The two choices can be compared directly:

| Normalization | $s(0)$ | Point sent to $-\infty$ | $s(1)$ | $s(e)$ |
|---|---:|---:|---:|---:|
| $s(1/2)=0$ | $-\log 2$ | $-\log 2$ | $1/2$ | $\sqrt e$ |
| $s(1/\sqrt e)=0$ | $-1/2$ | $-1/2$ | $1/\sqrt e$ | $e^{1/\sqrt e}$ |

The first normalization is arithmetically simple at the zero point because it
uses $1/2$. The second normalization is logarithmically simple because
$\log(1/\sqrt e)=-1/2$, making the negative singular point exactly $-1/2$.

More generally, if one imposes

$$
s(c)=0,
$$

then the defining equation gives

$$
s(0)=\log c.
$$

The commutation law gives

$$
s(1)=c,
$$

and the singular point is

$$
s(\log c)=-\infty.
$$

Thus the choice of the zero $c$ determines the chain

$$
1 \longmapsto c \longmapsto 0 \longmapsto \log c \longmapsto -\infty.
$$

For $c=1/2$, this gives $\log c=-\log 2$. For $c=1/\sqrt e$, it gives
$\log c=-1/2$.

## Comparing $\log x$, $\log(s(x))$, and $\log(\log x)$

The commutation law

$$
s(\log x)=\log(s(x))
$$

suggests comparing three quantities:

$$
\log x, \qquad \log(s(x)), \qquad \log(\log x).
$$

This comparison must be made carefully, because each expression has its own
domain restrictions. The expression $\log x$ is real for $x>0$. The expression
$\log(\log x)$ is real only for

$$
x>1,
$$

and it is positive only for $x>e$. The expression $\log(s(x))$ is real only
where

$$
s(x)>0.
$$

Under the normalization $s(1/2)=0$, the forced values give

$$
s(1)=\frac{1}{2}, \qquad s(\sqrt e)=1, \qquad s(e)=\sqrt e.
$$

Therefore $\log(s(x))$ becomes real along the forced positive chain once
$s(x)>0$.

### The Containment Region

For $x>e$, the two logarithmic curves satisfy

$$
\log(\log x)<\log x.
$$

Thus the natural bounded region is the vertical band

$$
\mathcal{R}=\left\{(x,y):x>e,\ \log(\log x)<y<\log x\right\}.
$$

The question is whether the semilogarithmic curve

$$
y=\log(s(x))
$$

lies inside this region, namely whether

$$
\log(\log x)<\log(s(x))<\log x.
$$

The opposite ordering

$$
\log x<\log(s(x))<\log(\log x)
$$

cannot hold for $x>e$, because the endpoints are already ordered as
$\log(\log x)<\log x$.

At the forced value $x=e$, we obtain

$$
\log(\log e)=\log 1=0,
$$

$$
\log(s(e))=\log(\sqrt e)=\frac{1}{2},
$$

and

$$
\log e=1.
$$

Thus

$$
0<\frac{1}{2}<1.
$$

At the next forced value, $x=e^{\sqrt e}$, we have

$$
s(e^{\sqrt e})=e,
$$

so

$$
\log(s(e^{\sqrt e}))=1.
$$

Also,

$$
\log(e^{\sqrt e})=\sqrt e,
$$

and

$$
\log(\log(e^{\sqrt e}))=\log(\sqrt e)=\frac{1}{2}.
$$

Hence

$$
\frac{1}{2}<1<\sqrt e.
$$

These anchor values support the containment

$$
\log(\log x)<\log(s(x))<\log x
$$

on the positive region where all three quantities are defined, provided the
chosen semilogarithm is monotone and behaves as a genuine half-step between the
identity and the logarithm in Abel coordinates.

### What the Graph Shows

The generated graph is included below.

![Normalized semilogarithm plot](library/images/semilogarithm-normalized.png)

The curve labelled $s(x)$ in the graph is not an analytic construction of the
semilogarithm. It is an interpolated model through the forced values

$$
0\mapsto -\log 2,
\quad
\frac{1}{2}\mapsto 0,
\quad
1\mapsto \frac{1}{2},
\quad
\sqrt e\mapsto 1,
\quad
e\mapsto \sqrt e.
$$

The script uses monotone linear interpolation between these anchors. Therefore
the plotted green curve is not the true analytic object

$$
\log(s(x)),
$$

but rather

$$
\log(s_{\mathrm{interp}}(x)).
$$

This explains why it appears continuous and regular in the graph: the continuity
comes from interpolation, not from an analytic solution of the semilogarithm
problem.

### Two Different Descents to $-\infty$

There are two different descents in the picture, and they must not be confused.

First, the normalization gives

$$
s(0)=-\log 2
$$

and

$$
s(-\log 2)=-\infty.
$$

So the semilogarithm itself has a singular descent at

$$
x=-\log 2\approx -0.6931.
$$

This is a statement about $s(x)$.

Second, because

$$
s\left(\frac{1}{2}\right)=0,
$$

the expression $\log(s(x))$ has its own logarithmic descent at

$$
x=\frac{1}{2}.
$$

Indeed, if $s(x)\to 0^+$, then

$$
\log(s(x))\to -\infty.
$$

This is a statement about $\log(s(x))$, not about $s(x)$ itself.

Therefore the apparent descent near $x=1/2$ belongs to the plotted curve
$\log(s_{\mathrm{interp}}(x))$. The negative singular value of the
semilogarithm is instead

$$
-\log 2,
$$

not $-1/2$. If the picture visually suggests $-1/2$, that is because the
vertical line $x=1/2$ is the positive zero of $s(x)$, where the logarithm of
$s(x)$ becomes singular. It is not the negative point where $s(x)$ itself is
sent to $-\infty$.

The updated plot therefore shows both features: a dashed heuristic branch for
$s(x)\to-\infty$ as $x\to-\log 2^+$, and a separate vertical marker at
$x=1/2$ for $\log(s(x))\to-\infty$.

Nevertheless, the graph is useful as a geometric map. It shows the expected
position of the semilogarithmic half-step curve between the two bounding curves
$\log(\log x)$ and $\log x$ at the forced values. A proof for a genuine analytic
semilogarithm would require constructing an Abel coordinate $\Phi$ satisfying

$$
\Phi(\log x)=\Phi(x)+1
$$

and then defining

$$
s(x)=\Phi^{-1}\left(\Phi(x)+\frac{1}{2}\right).
$$

Only after that construction could the containment inequality be studied as an
analytic theorem rather than as an interpolation-supported observation.

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
