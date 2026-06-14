---
title: "From S to Staircase: The Infinite Iteration of a Sigmoid on Its Own Box"
type: paper
created: 2026-06-14T10:00:00+00:00
updated: 2026-06-14T10:00:00+00:00
---

# From S to Staircase: The Infinite Iteration of a Sigmoid on Its Own Box

*A small, complete study of one well-behaved map. Take an S-shaped curve that
sends a box $[a,b]$ to itself, pinned at the corners $f(a)=a$, $f(b)=b$ and at
the centre $f(c)=c$. Apply it to itself again and again. We track the slope, the
two "knees" where the curve runs parallel to the diagonal, and the displacement
$g(x)=f(x)-x$ that reads the whole dynamics off a single graph. The conclusion
is clean and provable: inside its box this map has no hysteresis, no escape to
infinity, and no endless cycles — and its infinite iteration is a **staircase**.
Pushed to the limit, the sigmoid becomes a step function.*

## Abstract

Let $f:[a,b]\to[a,b]$ be a smooth, strictly increasing **S-curve** (one
inflection) fixing the two ends and the centre,

$$
f(a)=a,\qquad f(c)=c,\qquad f(b)=b,
$$

with the S **steep in the middle**: $f'(c)>1$ and $f'(a),f'(b)<1$. We study the
infinite application $f^\infty=\lim_{N\to\infty}f^{N}$.

Three tools do all the work, and they are the tools of the infinite-application
program. The **displacement** $g(x)=f(x)-x$ turns the dynamics into a single
graph: its zeros are the fixed points $a,c,b$, and its sign is the direction of
flow. The **first derivative** $f'$ gives stability — $a,b$ attract ($f'<1$),
$c$ repels ($f'>1$). And the **knees** $g_1,g_2$, defined by $g'(x)=f'(x)-1=0$
(equivalently $f'(x)=1$), are the local extrema of $g$: the steepest risers of
the eventual staircase and the exact thresholds between local contraction and
expansion. The inflection of the S is the zero of $f''$, and for a symmetric S
it coincides with the centre $c$.

The destiny is then forced by a single structural fact: a continuous increasing
self-map of an interval has **no periodic orbit of period $>1$** — every orbit
is monotone and bounded, hence convergent to a fixed point. So there is no
hysteresis (the map is single-valued and deterministic), no escape (it is a
self-map of a compact box), and no endless cycling. The infinite application is
therefore the **step function**

$$
f^\infty(x)=\begin{cases}a,& a\le x<c,\\[2pt] c,& x=c,\\[2pt] b,& c<x\le b,\end{cases}
$$

a staircase whose treads are the attracting fixed points and whose single riser
sits at the repelling centre $c$. The knees do not change *where* a point goes;
they shape *how steeply* it gets there. On the canonical example $f(x)=3x^2-2x^3$
on $[0,1]$ everything is exact: fixed points $0,\tfrac12,1$; knees
$g_{1,2}=(3\mp\sqrt3)/6\approx0.211,\,0.789$ with $g(g_{1,2})=\mp0.096$;
inflection at $c=\tfrac12$. Iterating the sigmoid to infinity sharpens it into a
hard threshold at $c$.

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

What the knees *mean* dynamically is the answer to the intuition that motivates
this study. Move a little away from $a$: there $f'<1$, the map is a contraction,
and the orbit eases back to $a$. Push on toward $c$: there $f'>1$, the map
expands, and the orbit is flung away from $c$. The knee $g_1$ is the exact
boundary between these two regimes — the place of **maximal displacement** on
$(a,c)$, the steepest part of the descent, the steepest **riser** of the
staircase we are about to meet. So the knee is not a destination; it is the
inflection of the journey. A point does not stop at $g_1$ — it moves *fastest*
there and continues to $a$. The reading "if I move a little from $a$ the orbit
heads toward the knee" is right about the *shape* of the descent (it sweeps down
through $g_1$) and is corrected only in its destination: the destiny is the fixed
point $a$, and $g_1$ is the knee of the slide into it.

---

## 4. Stability from the first derivative

The first derivative at each anchor classifies it, by the textbook criterion
$|f'|<1\Rightarrow$ attracting, $|f'|>1\Rightarrow$ repelling:

| anchor | $f'$ (general S) | $f'$ (smoothstep) | verdict |
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

## 6. The infinite application is a staircase

Assemble the pieces. Section 2 split the box into two basins at $c$; Section 4
made $a,b$ attracting and $c$ repelling; Section 5 guaranteed every orbit
converges monotonically to a fixed point. There is only one possibility for the
limit, and it depends only on which basin the start lies in:

$$
\boxed{\,f^\infty(x)=\lim_{N\to\infty}f^{N}(x)=
\begin{cases}
a, & a\le x<c,\\[2pt]
c, & x=c,\\[2pt]
b, & c<x\le b.
\end{cases}\,}
$$

This is a **step function** — a staircase with two treads, at heights $a$ and
$b$, joined by a single riser at the threshold $c$ (the lone unstable point,
which only $x=c$ itself ever lands on). The bottom-left panel watches it form:
$f^1$ is the gentle S; $f^2$ is steeper; by $f^{30}$ the curve is
indistinguishable from a vertical jump at $c=\tfrac12$. The sigmoid does not
*approximate* a step — iterated to the limit, it *becomes* one.

The knees now take their proper place. They never were destinations; they are the
hinges on which the riser steepens. Each application of $f$ amplifies the slope
in the expanding zone $(g_1,g_2)$ and flattens it outside, so the steep middle
gets steeper and the flat flanks get flatter — the S tightening, iteration after
iteration, into the threshold. The whole story is the single sentence: **between
the knees the curve climbs away from the centre; outside them it settles onto an
end; the limit of doing this forever is a step.**

---

## 7. The dual S, and the place of this in the program

If the S is **flat in the middle** instead of steep — $f'(c)<1$ and
$f'(a),f'(b)>1$ — every sign flips: the centre $c$ becomes the lone attractor,
the ends become repelling, and the staircase has a single central tread (the
whole open box drains to $c$) with risers at $a$ and $b$. Nothing else changes,
because the only ingredient the result truly needs is **monotonicity**
(Section 5). The dichotomy is entirely carried by the sign of the displacement's
slope at the centre, $g'(c)=f'(c)-1$ — the same vertex-displacement quantity that
decided one drain from three in *The Light Cone of Collatz*, here deciding two
treads from one.

This places the little study inside the larger program. In the language of *The
Elementary Theory of the Infinite Application of a Function*, the infinite
application $f^\infty$ is a new object built from $f$, and its destiny here is the
tamest of the catalogue: a **finite array** of point-attractors, assembled into a
staircase. The displacement $g=f-x$ is the reading instrument; the knees
$f'=1$ are where its derivative changes the local verdict; and the monotone
self-map is the one setting where the infinite application can be written down in
closed form — no hysteresis, no infinities, no cycles. It is the clean baseline
against which the wild cases (the non-hyperbolic, the average-but-not-uniform,
the quantization-sensitive) are precisely the departures from one or another of
these three hypotheses.

---

## 8. Conclusion

An S-curve on its own box is a switch with a memoryless rule. Its displacement
$g=f-x$ shows two basins meeting at the centre; its slope marks the centre as a
source and the ends as sinks; its knees, where $f'=1$, are the steepest risers,
not resting places. Because the map is increasing it cannot fold, so it cannot
cycle, and being a self-map of a box it cannot escape; every orbit slides
monotonically to an end. The infinite application is therefore a staircase, and
the sigmoid, applied without end, is revealed as a step function — a hard
threshold sitting exactly on the unstable centre, with the knees recording how
steeply the world on either side was swept toward its destiny.

---

## Reproducing the Results

All numerical claims are reproduced by:

```
python3 library/scripts/s_map_staircase.py
```

The script works the canonical S-map $f(x)=3x^2-2x^3$ on $[0,1]$: it locates the
fixed points $0,\tfrac12,1$ and classifies them by $f'$ ($0,\tfrac32,0$); solves
$f'(x)=1$ for the knees $g_{1,2}=(3\mp\sqrt3)/6$ and reports the displacement
extrema $g(g_{1,2})=\mp0.0962$; checks $f''=0$ at the centre $c=\tfrac12$;
verifies that orbits from a spread of seeds are monotone and land on $0$ or $1$
(no cycles); and renders the four-panel figure
`library/images/s-map-staircase.png` (the S-map with cobwebs, the displacement
$g$ and its derivative, the staircase-forming $f^N$, and $f'$ crossing $1$ at the
knees).
