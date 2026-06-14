---
title: "From S to Staircase: The Infinite Iteration of a Sigmoid on Its Own Box"
type: paper
created: 2026-06-14T10:00:00+00:00
updated: 2026-06-14T13:00:00+00:00
---

# From S to Staircase: The Infinite Iteration of a Sigmoid on Its Own Box

*A small, complete study of one well-behaved family of maps. Take an S-shaped
curve that sends a box $[a,b]$ to itself, pinned at the corners $f(a)=a$,
$f(b)=b$ and at the centre $f(c)=c$, and apply it to itself again and again. We
track the slope, the "knees" where the curve runs parallel to the diagonal, and
the displacement $g(x)=f(x)-x$ that reads the whole dynamics off a single graph.
The conclusion is clean and provable: inside its box this map has no hysteresis,
no escape to infinity, and no endless cycles — its infinite iteration is always a
**staircase**, with treads at the attracting fixed points and risers at the
repelling ones. How many stairs depends on the shape: a simple steep-centre S
gives a single threshold at $c$; a double-bend S with a gentle, attracting centre
gives the two-step staircase $a\to c\to b$. The critical slope $f'=1$ decides
which.*

## Abstract

Let $f:[a,b]\to[a,b]$ be a smooth, strictly increasing **S-curve** fixing the
two ends and the centre,

$$
f(a)=a,\qquad f(c)=c,\qquad f(b)=b,
$$

and consider the infinite application $f^\infty=\lim_{N\to\infty}f^{N}$.

Three tools do all the work, and they are the tools of the infinite-application
program. The **displacement** $g(x)=f(x)-x$ turns the dynamics into a single
graph: its zeros are the fixed points, and its sign is the direction of flow.
The **first derivative** sets the **critical threshold** $f'=1$: a fixed point
*attracts* where $f'<1$ and *repels* where $f'>1$ — so the slope crossing $1$ is
exactly where a point's role flips from tread to threshold. And the **knees**,
defined by $g'(x)=f'(x)-1=0$ (equivalently $f'(x)=1$), are the local extrema of
$g$ and the places where the slope crosses that critical threshold.

The central result is a single law:

> **The infinite application of a monotone S-self-map is a staircase. Its treads
> are the attracting fixed points ($f'<1$); its risers stand at the repelling
> fixed points ($f'>1$), which are the basin thresholds. The number of treads is
> the number of attracting fixed points, and that number is set by how many times
> the S crosses the diagonal.**

This is forced by one structural fact (Section 5): a continuous increasing
self-map has **no orbit of period $>1$** — every orbit is monotone and bounded,
hence converges to a fixed point. So there is no hysteresis, no escape, no
endless cycling; only treads and risers.

The deepest organizing idea (Section 8) is that the right classifier is not the
*shape* of the S but the **rotation of its central tangent** — the multiplier
$s=f'(c)$. As $s$ turns down from vertical through $45°$ ($s=1$, a saddle-node
that births the middle tread) past horizontal into negative slope ($s=-1$, a
period-doubling that births a $2$-cycle), the curve is *forced* through one-step
staircase $\to$ two-step staircase $\to$ N-shape with cycles and chaos. The
double-bend is not a different object; it is the same S with its centre tangent
rotated below $45°$.

How many treads depends, in this first pass, on the *shape* of the S — the point
on which a first, too-hasty reading of this study was wrong.
A **simple** S (a single inflection) crosses the diagonal at most three times,
so it yields at most a *one*-step staircase: with a **steep centre**
($f'(c)>1$) the centre repels and $f^\infty(x)=a$ on $[a,c)$, $\,b$ on $(c,b]$
(threshold at $c$); with a **gentle centre** ($f'(c)<1$) the centre attracts and
the whole open box drains to it (one central tread). But a **double-bend** S
(two inflections, five diagonal crossings) makes $a,c,b$ *all* attracting with
two repellers $r_1,r_2$ between them, and then

$$
f^\infty(x)=\begin{cases}a,& a\le x<r_1,\\[2pt] c,& r_1<x<r_2,\\[2pt] b,& r_2<x\le b,\end{cases}
$$

the genuine **two-step staircase $a\to c\to b$**, with the thresholds at the
repellers, not at the knees. The knees do not decide *where* a point goes; they
mark the critical slope $f'=1$ and, as the S deepens, they are the **birthplaces**
of new treads (a saddle-node tangency where $g$ touches the diagonal). On the
canonical simple S $f(x)=3x^2-2x^3$ everything is exact (one step, threshold
$c=\tfrac12$, knees $(3\mp\sqrt3)/6$); on the double-bend
$f(x)=x-6\,x(x-\tfrac14)(x-\tfrac12)(x-\tfrac34)(x-1)$ the basins are
$[0,\tfrac14)\to0$, $(\tfrac14,\tfrac34)\to\tfrac12$, $(\tfrac34,1]\to1$ — the
two-step $a\to c\to b$, verified.

All numerical claims are reproduced by `library/scripts/s_map_staircase.py`.

---

## 1. The S-map and its three anchors

We study a map that does the simplest interesting thing a curve can do on a box:
it is an **S**. Formally, $f:[a,b]\to[a,b]$ is continuous, strictly increasing,
and S-shaped — convex on one half of the box and concave on the other, with a
single inflection between them. We pin it at three points,

$$
f(a)=a,\qquad f(c)=c,\qquad f(b)=b,
$$

the two corners of the box and its centre $c=\tfrac{a+b}{2}$. These are the three
**anchors**: the places where the curve meets the diagonal $y=x$, hence the three
fixed points of the dynamics.

The canonical example, which we carry throughout because every quantity in it is
exact, is the **smoothstep** on $[0,1]$,

$$
f(x)=3x^2-2x^3,
$$

with $f(0)=0$, $f(\tfrac12)=\tfrac12$, $f(1)=1$. It is the gentlest honest S: a
cubic, increasing on $[0,1]$, steep in the middle and flat at the ends. Picture
a switch that, nudged, snaps toward whichever end you are closer to — that is the
behaviour we are about to make precise.

![The S-map study. Top-left: the curve $f(x)=3x^2-2x^3$, the diagonal, the three fixed points $a,c,b$, the two knees $g_1,g_2$, and two cobweb orbits — one falling to $a$, one climbing to $b$. Top-right: the displacement $g(x)=f(x)-x$ (zeros at the fixed points, extrema at the knees) with its derivative $g'=f'-1$. Bottom-left: $f^N$ for $N=1,2,3,5,10,30$ steepening into a step function at $c=1/2$. Bottom-right: $f'$, which exceeds $1$ only between the knees, so the centre is the one expanding region.](library/images/s-map-staircase.png)

---

## 2. The displacement $g(x)=f(x)-x$: the whole dynamics on one graph

Iteration is hard to see in the curve $f$ itself; it is easy to see in the
**displacement**

$$
g(x)\;=\;f(x)-x,
$$

the quantity the infinite-application program calls the fundamental difference,
because its sign says, at each point, whether one step pushes right or left:

$$
g(x)>0 \Rightarrow f(x)>x\ (\text{move right}),\qquad
g(x)<0 \Rightarrow f(x)<x\ (\text{move left}).
$$

Reading $g$ for our S (top-right panel): it vanishes at the three anchors
$a,c,b$ — those are the fixed points, where a step does nothing. Between them it
keeps a definite sign. For the steep-middle S,

$$
g<0 \text{ on } (a,c),\qquad g>0 \text{ on } (c,b).
$$

For the smoothstep, $g(x)=3x^2-2x^3-x$, and one checks $g(0)=g(\tfrac12)=g(1)=0$
directly. So the flow is unambiguous: everything in $(a,c)$ is pushed **left,
toward $a$**; everything in $(c,b)$ is pushed **right, toward $b$**; and $c$ sits
on the watershed, pushed nowhere but unstable to either side. The single graph of
$g$ already contains the verdict — two basins divided at $c$ — before we iterate
anything.

---

## 3. The knees: where the curve runs parallel to the diagonal

Now the feature the close-up reveals. As $x$ runs from $a$ to $b$, the slope
$f'$ starts below $1$ (flat near $a$), rises above $1$ through the steep middle,
and falls back below $1$ near $b$. By continuity it equals $1$ at exactly two
points. These are the **knees**:

$$
g'(x)=f'(x)-1=0 \quad\Longleftrightarrow\quad f'(x)=1,
\qquad\text{call the solutions } g_1\in(a,c),\ g_2\in(c,b).
$$

They are precisely the **local extrema of the displacement** $g$ (since $g'=0$
there), the points where the curve is locally parallel to the diagonal — the
"knees" of the S, where it bends from flat to steep and back. For the smoothstep,
$f'(x)=6x-6x^2$, so $f'(x)=1$ gives $6x^2-6x+1=0$ and

$$
g_{1}=\frac{3-\sqrt3}{6}\approx0.2113,\qquad
g_{2}=\frac{3+\sqrt3}{6}\approx0.7887,
$$

with $g(g_1)=-0.0962$ (the minimum of $g$) and $g(g_2)=+0.0962$ (the maximum).
The second derivative confirms and dates them: $g''=f''=6-12x$ vanishes at
$x=\tfrac12=c$, so the **inflection of the S is the centre fixed point itself**,
and $g''$ has opposite signs at $g_1$ and $g_2$, marking one as a minimum and one
as a maximum.

The knees mark a **critical threshold**, and this is the right place to credit
the intuition that drove this study. The slope $f'=1$ is the dividing line of all
the dynamics: where $f'<1$ the map *contracts* (pulls toward), where $f'>1$ it
*expands* (pushes away). A fixed point is therefore an **attractor exactly when
its slope is below the threshold** and a **repeller when above it** — and a
fixed point's role can be made to flip simply by changing the slope through $1$.
That is precisely the correct mechanism: *if the slope at the centre drops below
the critical threshold, $c$ becomes an attractor* (a gentle-centre S); if it
stays above, $c$ repels (the steep-centre S of the smoothstep, where
$f'(c)=\tfrac32>1$).

But one must separate two roles the slope plays, because conflating them is the
easy mistake. The threshold $f'=1$ governs **stability at the fixed points**;
it does *not*, on its own, place the **basin boundaries**. For the simple
steep-centre S the knees $g_1,g_2$ are *not* fixed points — $g(g_1)=-0.096\neq0$
— so they are not thresholds between basins; they are the points of **maximal
displacement**, the steepest part of the slide, the steepest *riser*. A point
started between $g_1$ and $c$ does not stop at the knee and does not go to $c$:
$g<0$ there, so it slides past $g_1$, fastest at the knee, all the way down to
$a$. (Run it: from $x_0=0.4$, between $g_1\approx0.21$ and $c=0.5$, the orbit
goes $0.4\to0.352\to0.284\to\cdots\to0$.) The destiny is the *fixed point*; the
knee only shapes the descent. The basin boundary is the repelling fixed point —
here $c$ — not the knee.

This distinction is exactly what opens the door to the richer behaviour. To make
$c$ a genuine **tread** (an attractor over an interval, the middle step of an
$a\to c\to b$ staircase) we must drop its slope below the threshold *and* supply
two new repelling fixed points to bound its basin. That is the double-bend S of
Section 6 — and there the intuition "attraction changes near the bends" becomes
literally true, at the two repellers $r_1,r_2$.

---

## 4. Stability from the first derivative

The first derivative at each anchor classifies it, by the textbook criterion
$|f'|<1\Rightarrow$ attracting, $|f'|>1\Rightarrow$ repelling. For the
**steep-centre** simple S studied so far:

| anchor | $f'$ (steep-centre S) | $f'$ (smoothstep) | verdict |
|---|---|---|---|
| $a$ | $<1$ | $0$ | attracting |
| $c$ | $>1$ | $3/2$ | repelling |
| $b$ | $<1$ | $0$ | attracting |

The ends are sinks, the centre is a source. (For the smoothstep the ends are
*super-attracting*, $f'=0$, so convergence there is quadratic — the staircase
treads are not merely reached but reached very fast.) This is the bottom-right
panel: $f'$ pokes above the dashed line $f'=1$ only on the interval $(g_1,g_2)$
straddling $c$ — the lone expanding zone, bracketed by the knees — and lies below
it on the two flanks that drain into $a$ and $b$.

---

## 5. No hysteresis, no infinities, no endless cycles

The intuition's final hypothesis — that locally, inside its box, this map has
neither hysteresis nor blow-up nor unending cycles — is not a hope but a theorem,
and it rests on one property we have used implicitly throughout: $f$ is
**increasing**.

**No hysteresis.** $f$ is a single-valued function: the next state is a
deterministic function of the current one, with no dependence on history. There
is nothing for a hysteresis loop to be made of. (This is exactly the contrast
with the quantized renderings elsewhere in this notebook, where the *machine*
injected a history-dependence the map itself does not have.)

**No escape to infinity.** $f$ maps $[a,b]$ into $[a,b]$. Every iterate stays in
the compact box by construction; there is no "infinity" to run to.

**No endless cycles.** Here is the load-bearing fact:

**Proposition (monotone self-maps do not cycle).** *Let $f:[a,b]\to[a,b]$ be
continuous and strictly increasing. Then every orbit is monotone and converges
to a fixed point; in particular $f$ has no periodic orbit of period $>1$.*

*Proof.* Take any $x_0$ and compare it with $x_1=f(x_0)$. If $x_0\le x_1$, apply
the increasing map $f$ to both sides: $x_1=f(x_0)\le f(x_1)=x_2$, and inductively
$x_n\le x_{n+1}$ for all $n$ — the orbit is nondecreasing. If instead $x_0\ge
x_1$, the same step gives a nonincreasing orbit. Either way the orbit is monotone
and bounded (it lives in $[a,b]$), so it converges to some $L\in[a,b]$; by
continuity $f(L)=L$, a fixed point. A period-$2$ point would need $x_0$ and
$x_1\neq x_0$ swapped by $f$, i.e. $x_0<x_1$ and $x_1<x_0$ — impossible for a
monotone orbit. $\square$

The smoothstep run confirms it numerically: orbits from $0.05,0.2,0.49$ descend
monotonically to $0$; orbits from $0.51,0.8,0.95$ climb monotonically to $1$;
none oscillates. Monotonicity is the whole reason an S-curve cannot do anything
exotic — cycles, chaos, strange attractors all require the map to *fold*, and an
increasing map never folds.

---

## 6. The staircase law, and the one-step case

Assemble the pieces. Section 5 guarantees every orbit converges monotonically to
a fixed point; Section 4 sorts the fixed points into attractors and repellers by
the threshold $f'=1$; Section 2 reads the basins off the sign of $g$. Together
they give the general law, valid for *any* monotone S-self-map:

> **Staircase law.** $f^\infty$ is constant on the open basin of each attracting
> fixed point, equal to that fixed point. So $f^\infty$ is a **staircase**: its
> **treads** are the attracting fixed points, its **risers** stand at the
> repelling fixed points (the basin boundaries). The number of treads equals the
> number of attractors, and is bounded by the number of times the S crosses the
> diagonal.

For the simple steep-centre S this gives a **one-step** staircase. Sections 2
and 4 made $a,b$ attracting and $c$ repelling, so

$$
\boxed{\,f^\infty(x)=
\begin{cases}
a, & a\le x<c,\\[2pt]
c, & x=c,\\[2pt]
b, & c<x\le b
\end{cases}\,}
\qquad(\text{steep-centre simple S}).
$$

Two treads at $a$ and $b$, one riser at the threshold $c$ (the lone unstable
point, which only $x=c$ ever lands on). The bottom-left panel of the first figure
watches it form: $f^1$ is the gentle S, $f^2$ steeper, and by $f^{30}$ the curve
is a vertical jump at $c=\tfrac12$. The sigmoid does not *approximate* a step —
iterated to the limit, it *becomes* one. Here the knees are not destinations:
each iteration amplifies the slope in the expanding zone $(g_1,g_2)$ and flattens
it outside, so the steep middle steepens into the riser while the flanks flatten
into the treads.

---

## 7. The two-step staircase $a\to c\to b$: a double-bend S

The one-step picture is *not* the whole story, and the way it is exceeded is the
genuinely interesting case — the one the staircase law was stated generally to
capture. To get a true **two-step** staircase $a\to c\to b$, with $c$ an
attracting tread over a whole interval, the law tells us exactly what is needed:
three attractors $a,c,b$ and, between them, two repellers $r_1,r_2$ as basin
walls — **five** fixed points, i.e. an S that crosses the diagonal five times.

A simple sigmoid cannot do this. With a single inflection, $f'$ is unimodal, so
$g'=f'-1$ vanishes at most twice and $g=f-x$ has at most three zeros: a
single-inflection S crosses the diagonal at most three times, and so yields at
most one step. The two-step staircase requires a **double-bend** S — two
inflections, a gentle attracting centre flanked by two steep repelling shoulders.
A clean exact example on $[0,1]$:

$$
f(x)=x-6\,x\!\left(x-\tfrac14\right)\!\left(x-\tfrac12\right)\!\left(x-\tfrac34\right)\!(x-1),
$$

increasing on $[0,1]$, with five fixed points and slopes

$$
f'(0)=0.44,\quad f'(\tfrac14)=1.14,\quad f'(\tfrac12)=0.91,\quad f'(\tfrac34)=1.14,\quad f'(1)=0.44.
$$

Now the centre $c=\tfrac12$ is **below** the critical threshold ($f'=0.91<1$): it
has become an attractor, exactly as the slope argument predicts. The two
shoulders $r_1=\tfrac14,\,r_2=\tfrac34$ are **above** it ($f'=1.14>1$): repellers,
the basin walls. The staircase law then gives the two-step:

$$
\boxed{\,f^\infty(x)=
\begin{cases}
a=0, & 0\le x<\tfrac14,\\[2pt]
c=\tfrac12, & \tfrac14<x<\tfrac34,\\[2pt]
b=1, & \tfrac34<x\le 1
\end{cases}\,}
\qquad(\text{double-bend S}).
$$

Verified directly: orbits from $0.1,0.24$ fall to $0$; from $0.26,0.5,0.74$
settle on $\tfrac12$; from $0.76,0.9$ climb to $1$. The thresholds are the
repellers $r_1,r_2$ — *near the bends of the S*, which is exactly the
"attraction changes at the bends" the geometry suggests, made precise: the
change of attraction happens at the repelling fixed points, the steep shoulders,
not at the gentle centre and not at the literal knees $f'=1$ (which sit slightly
inside them). The middle tread $c$ is real, occupies the whole interval
$(r_1,r_2)$, and survives to the limit.

![The double-bend S and its two-step staircase. Left: the curve crosses the diagonal five times — three attracting treads $a,c,b$ (filled dots) and two repelling thresholds $r_1,r_2$ (open dots); three cobwebs settle on $0$, $\tfrac12$, $1$. Right: $f^N$ for $N=1,2,4,8,20,60$ sharpening into the two-step staircase $a\to c\to b$, with the risers forming at the repellers $r_1=\tfrac14,\,r_2=\tfrac34$.](library/images/s-map-two-step.png)

This already corrects the motivating question: whether the limit is a one-step or
a two-step staircase is not a property of "the S" in the abstract but of how many
times the curve crosses the diagonal and the slope at each crossing. But there is
a still better way to see *why* the second crossing-pair appears at all — not as a
shape one chooses, but as a consequence forced by rotating a single tangent. That
is the next section, and it is the right axis for the whole classification.

---

## 8. The right axis: rotate the central tangent, don't change the shape

Sections 6–7 sorted the behaviour by *shape* — simple S versus double-bend. That
is the wrong axis. The right one is sharper and canonical: classify by the **slope
of the tangent at the centre**, $s=f'(c)$ — the central multiplier, which is the
one conjugacy-invariant of the fixed point. The "change of shape" is not an
independent choice; it is *forced* by rotating that tangent. Picture the tangent
at $c$ pinned and turning, while the ends $a,b$ stay fixed and attracting, and
follow $s=f'(c)=\tan\theta$.

**The two-step is forced, not drawn.** When $s>1$ (tangent steeper than the
diagonal, toward vertical) the centre repels: with $a,b$ attracting we have
attract–repel–attract, the one-step staircase. Now rotate the tangent down through
$45°$. The instant $s<1$ the centre *attracts*, so $a,c,b$ are three consecutive
attractors — which a continuous map cannot have without a repeller between each
pair. Two fixed points are therefore **compelled into existence**, and one sees
exactly where: with $g'(a),g'(c),g'(b)<0$, the displacement $g=f-x$ goes negative
just right of $a$ yet must return to $0$ at $c$, so by the intermediate value
theorem it has a zero $r_1\in(a,c)$ crossing *upward* — $f'(r_1)>1$, a repeller —
and symmetrically $r_2\in(c,b)$. The double-bend is not a shape you elect to draw;
it is the shape the curve is forced into the moment its central tangent tilts below
$45°$. (Verified by blending the one-step map into the two-step map: the
fixed-point count jumps $3\to5$ exactly as $s$ crosses $1$, and the basin of $c$
opens from a single point to the whole interval $(r_1,r_2)$.)

**Past horizontal: the N and the wild.** Keep turning. At $s=0$ the tangent is
horizontal and $c$ is super-attracting. Past it, $s<0$: the tangent tilts
*downward*, $f$ stops being increasing at $c$, and the curve folds into an **N**.
The monotonicity that guaranteed "no cycles" (Section 5) is now gone, and the tame
staircase theorem lapses. At $s=-1$ (tangent at $-45°$) the centre **period-
doubles**: it loses stability and a **$2$-cycle** is born around it (verified: the
cubic with $f'(c)=-1$ shows a $2$-cycle of vanishing amplitude, widening to
$\{\tfrac13,\tfrac23\}$ by $f'(c)=-\tfrac54$). Beyond, $s<-1$, the N deepens, its
humps push across the diagonal, and the cascade to longer cycles and chaos begins
— the regime of the wild maps (the logistic map, the Collatz crests, the
Mandelbrot boundary). The knees, here, are the humps that "peek across the
diagonal," each crossing a newly forced fixed point: the geometry the motivating
intuition described.

So one number — the central multiplier — organizes the entire catalogue:

| $f'(c)$ | central tangent | centre | infinite application |
|---|---|---|---|
| $>1$ | steep up (→ vertical) | repeller | one-step staircase (treads $a,b$) |
| $=1$ | $45°$ | neutral | **saddle-node**: middle tread is born |
| $0<\cdot<1$ | shallow up | attractor | two-step $a\to c\to b$ |
| $=0$ | horizontal | super-attractor | two-step, fastest approach |
| $-1<\cdot<0$ | shallow down (N) | attractor | two-step, alternating approach |
| $=-1$ | $-45°$ | neutral | **period-doubling**: $2$-cycle is born |
| $<-1$ | steep down (N) | repeller | cycles $\to$ chaos (the wild) |

![Classifying by the rotation of the central tangent. Left: holding $a,b$ fixed and attracting, the central tangent rotates from slope $1.5$ (one-step, three fixed points) down through $1$ to $0.91$ — the curve is forced to bulge across the diagonal, creating the two repellers $r_1,r_2$ (open dots) of the two-step staircase. Middle: destiny versus central slope; for $f'(c)>1$ only the two outer treads $0,1$ are reached, and at the saddle-node $f'(c)=1$ a third tread at $\tfrac12$ appears. Right: rotated past horizontal to slope $-1.3$, the map is an N — non-monotone — and a cobweb spirals onto a $2$-cycle: the gateway out of the tame staircase into cycles and chaos.](library/images/s-map-tangent-rotation.png)

This is the corrected classification, and it settles the motivating point. The
double-S was never a composite object; it is the simple S with its central tangent
rotated past $45°$, which *forces* the extra crossings. The very same rotation,
continued past horizontal, is the bridge out of the tame staircase world into the
wild one: the moment the tangent tilts below horizontal, monotonicity breaks and
cycles appear. The classification is not by what the curve *looks like*, but by
**how its central tangent is turned** — and the two critical angles, $f'(c)=+1$
(saddle-node) and $f'(c)=-1$ (period-doubling), are where the destiny changes
kind.

---

## 9. How many steps? The count, and the place in the program

The pattern generalizes cleanly. The number of treads of $f^\infty$ is the number
of attracting fixed points of $f$, and attractors and repellers must alternate
along $[a,b]$ (between two attractors sits a repelling wall). So the staircase has
$k$ treads exactly when $f$ has $2k-1$ fixed points (counting the bounding
behaviour), and that count is limited by the shape: an S with $m$ inflections can
cross the diagonal at most $m+2$ times. One inflection $\Rightarrow$ at most one
step; two inflections $\Rightarrow$ up to the two-step $a\to c\to b$; more bends,
more steps. **Iterating an S to infinity always yields a staircase; how many
stairs is set by how many times the S meets the diagonal.**

The whole dichotomy is carried by one quantity, the slope of the displacement at
a fixed point, $g'(\,\cdot\,)=f'(\,\cdot\,)-1$ — the same vertex-displacement that
decided one drain from three in *The Light Cone of Collatz*, here deciding tread
from threshold and so the very number of stairs. And the result needs only
**monotonicity**: an increasing self-map cannot fold, hence cannot cycle, escape,
or carry hysteresis (Section 5), so its infinite application is always this tame
object.

This places the study inside the larger program. In the language of *The
Elementary Theory of the Infinite Application of a Function*, $f^\infty$ is a new
object built from $f$, and its destiny here is the gentlest of the catalogue: a
**finite array** of point-attractors assembled into a staircase. The displacement
$g=f-x$ is the reading instrument; the critical slope $f'=1$ is where it changes
the local verdict; and the monotone self-map is the one setting where the infinite
application can be written in closed form. It is the clean baseline against which
the wild cases — the non-hyperbolic, the average-but-not-uniform, the
quantization-sensitive — are precisely the departures from one of these
hypotheses.

---

## 10. Conclusion

An S-curve on its own box is a switch with a memoryless rule. Its displacement
$g=f-x$ shows the basins; the critical slope $f'=1$ sorts each diagonal crossing
into an attracting tread or a repelling threshold; and because the map is
increasing it cannot fold, so it cannot cycle, escape, or carry hysteresis —
every orbit slides monotonically to a fixed point. The infinite application is
therefore always a **staircase**: treads at the attractors, risers at the
repellers. How many stairs is decided by the shape — by how many times the S
meets the diagonal. A simple steep-centre S gives one step, a hard threshold at
the unstable centre $c$; a double-bend S with a gentle attracting centre gives
the **two-step $a\to c\to b$**, with the thresholds at the two repelling
shoulders. The knees $f'=1$ are not destinations but the critical slope that
decides each crossing — and, as the centre is lowered through that threshold, the
birthplace of a new middle tread. The corrected headline: iterating an S to
infinity yields a staircase, and the centre is a step of it precisely when its
slope has dropped below one.

---

## Reproducing the Results

All numerical claims are reproduced by:

```
python3 library/scripts/s_map_staircase.py
```

The script works two maps on $[0,1]$. For the simple steep-centre S
$f(x)=3x^2-2x^3$: it locates the fixed points $0,\tfrac12,1$ and classifies them
by $f'$ ($0,\tfrac32,0$); solves $f'(x)=1$ for the knees $g_{1,2}=(3\mp\sqrt3)/6$
and reports the displacement extrema $g(g_{1,2})=\mp0.0962$; checks $f''=0$ at the
centre; verifies that orbits between $g_1$ and $c$ go to $a$ (not to $c$), and that
all orbits are monotone with no cycles, giving the one-step staircase; and renders
the four-panel figure `library/images/s-map-staircase.png`. For the double-bend S
$f(x)=x-6\,x(x-\tfrac14)(x-\tfrac12)(x-\tfrac34)(x-1)$: it confirms the five fixed
points with $a,c,b$ attracting and $r_1,r_2$ repelling, checks the basins
$[0,\tfrac14)\to0$, $(\tfrac14,\tfrac34)\to\tfrac12$, $(\tfrac34,1]\to1$, and
renders `library/images/s-map-two-step.png` (the double-bend S with cobwebs and
$f^N$ forming the two-step staircase $a\to c\to b$). Finally it produces
`library/images/s-map-tangent-rotation.png`: blending the one-step map into the
two-step map to rotate the central tangent, it shows the fixed-point count jump
$3\to5$ as $f'(c)$ crosses $1$ (the saddle-node birthing the middle tread), the
destiny-versus-central-slope diagram, and an N-shaped map ($f'(c)=-1.3$) whose
cobweb spirals onto a $2$-cycle — the period-doubling gateway to the wild
regime.
