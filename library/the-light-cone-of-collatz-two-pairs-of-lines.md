---
title: "The Light Cone of Collatz: Two Pairs of Lines and the Geometry of the Bounce"
type: paper
created: 2026-06-13T15:00:00+00:00
updated: 2026-06-13T15:00:00+00:00
---

# The Light Cone of Collatz: Two Pairs of Lines and the Geometry of the Bounce

*Read the Collatz map one step at a time on the plane $(x, T(x))$ and the two
branches become two lines. They cross at a vertex and open into a wedge — a
light cone — and every orbit is trapped on its two edges, bouncing between
them like a ball settling into a funnel. This paper builds the cone exactly,
proves the bounce is confined and contracting, reads the collapse through the
theory of the infinite application of a function, and then compares it,
honestly, with the mirror cone of the $3x-1$ map.*

## Abstract

A single Collatz step is two lines. On the plane that plots the next value
$T(x)$ against the current value $x$, the odd branch is the line $y = 3x+1$
and the even branch is the line $y = x/2$. The two lines meet at the **cone
vertex** $V = \left(-\tfrac25, -\tfrac15\right)$ and open, toward $+\infty$,
into a wedge we call the **light cone** of the map. We prove three things
about it. First, the diagonal $y = x$ — the bisector, the line of fixed
points — runs strictly *inside* the cone, because the branch slopes $\tfrac12$
and $3$ straddle $1$. Second, every orbit point $(x_n, x_{n+1})$ lies exactly
on one of the two edges, so a trajectory is a sequence of bounces confined to
the boundary of the cone; the cone is invariant and the orbit never leaves it.
Third, the bounce **contracts**: one odd step multiplies by $3$, and the
trailing halvings divide, on average, by $4$, so the mean multiplier per
macrostep is exactly $\tfrac34 = e^{\log 3 - 2\log 2}$, a measured
$e^{-0.2877}$. A ball that cannot escape a downward-drifting funnel rolls to
the bottom: this is the geometric face of convergence, and it is the same
"asymptotic shadow that survives iteration" studied in *The Elementary Theory
of the Infinite Application of a Function*.

Then we mirror it. The $3x-1$ map has the **same cone up to a reflection
through the origin** — vertex $V' = \left(\tfrac25, \tfrac15\right)$, the same
diagonal inside, the same $\tfrac34$ drift (measured $e^{-0.2876}$) — and yet
it has *three* terminal cycles, $\{1,2\}$, $\{5,7,10,14,20\}$, and an
$18$-element cycle, instead of one. The cone confines and contracts
identically in both worlds, so it cannot, by itself, distinguish one drain
from three. This is the same wall met from a different side in *The
Indestructible Set*: the geometry is real, the proof it seems to offer is not.
The cone explains why every orbit is *trapped and shrinking*; it is silent on
*which* drain at the bottom of the funnel catches it.

All numerical claims are reproduced by
`library/scripts/collatz_light_cone.py`.

---

## 1. One step is two lines

Throughout, $T$ is the $3x+b$ map on the positive integers,

$$
T(x) =
\begin{cases}
x/2 & x \text{ even},\\[2pt]
3x + b & x \text{ odd},
\end{cases}
$$

with $b = +1$ the Collatz map and $b = -1$ its sign-flipped twin. Plot a step
as a point: put the current value on the horizontal axis and the next value
$T(x)$ on the vertical axis. Because $T$ has two branches, every point of every
orbit lands on one of two straight lines:

$$
\ell_{\text{odd}} : y = 3x + b,
\qquad
\ell_{\text{even}} : y = \tfrac{x}{2}.
$$

There is nothing approximate here. An even number is sent *exactly* to the
line of slope $\tfrac12$; an odd number is sent *exactly* to the line of slope
$3$. The dynamics of a famously irregular sequence is, locally, the cleanest
object in the plane: a choice between two lines.

These two lines are the edges of a wedge. The whole paper is the study of that
wedge.

---

## 2. The cone and its vertex

The two edges cross where $3x + b = \tfrac{x}{2}$, that is at
$\tfrac52 x = -b$, giving the **vertex**

$$
V_b = \left(-\tfrac{2b}{5},\; -\tfrac{b}{5}\right),
\qquad
V_{+1} = \left(-\tfrac25, -\tfrac15\right),
\quad
V_{-1} = \left(\tfrac25, \tfrac15\right).
$$

To the right of the vertex the line of slope $3$ runs above the line of slope
$\tfrac12$, and the region between them,

$$
\mathcal C_b = \left\{ (x,y) : \tfrac{x}{2} \le y \le 3x + b,\ x \ge -\tfrac{2b}{5} \right\},
$$

is the **light cone** of the map — the open mouth of the funnel, opening toward
$+\infty$.

**Theorem 1 (the bisector lives inside the cone).** *The diagonal $y = x$, the
line on which output equals input, passes through the interior of
$\mathcal C_b$ for every $x > -\tfrac{2b}{5}$.*

*Proof.* A line of slope $m$ through the region lies between the edges exactly
when $\tfrac12 < m < 3$. The diagonal has slope $1$, and $\tfrac12 < 1 < 3$.
At any $x>0$ the wedge spans the vertical interval $[\tfrac{x}{2},\,3x+b]$,
which contains $x$ since $\tfrac{x}{2} \le x \le 3x + b$ for $x \ge 0$ (the
second inequality needs $x \ge -b/2$, true for $x>0$ when $b=\pm1$). $\square$

The diagonal matters because its intersections with the edges are the **fixed
points of the branches**: $y = x$ meets $\ell_{\text{odd}}$ at
$x = -\tfrac{b}{2}$ and $\ell_{\text{even}}$ at $x = 0$. The cone is built
around the line of no change, and the orbit, as we will see, drifts *down that
line* toward the vertex.

---

## 3. The bounce: orbits live on the edges

The figure shows the two cones with a sample orbit threaded through each.

![The Collatz light cone (left, $3x+1$) and its mirror, the $3x-1$ cone (right). The odd edge $y=3x+1$ (slope 3) and the even edge $y=x/2$ (slope 1/2) meet at the vertex $V$; the dashed diagonal $y=x$ runs inside the shaded wedge. The orbit from 7 bounces off the edges, drifting down the bisector toward the vertex.](library/images/collatz-light-cone.png)

The black path is not a cobweb in the usual sense. Each point $(x_n, x_{n+1})$
sits on an edge; the segment to the next point $(x_{n+1}, x_{n+2})$ carries the
output of one step to the input of the next. The orbit therefore *bounces*
between the high edge (after an odd step it is thrown up to slope $3$) and the
low edge (each even step slides it down slope $\tfrac12$), zig-zagging across
the mouth of the cone and working its way toward the narrow end.

**Proposition 2 (confinement).** *Every orbit point of $T$ lies on an edge of
$\mathcal C_b$, and hence in $\mathcal C_b$. The cone is invariant: the orbit
never leaves it.*

*Proof.* Immediate from the definition of $T$: an even input lands on
$\ell_{\text{even}}$, an odd input on $\ell_{\text{odd}}$, and both edges are
contained in $\mathcal C_b$ for inputs $x \ge 1 > -\tfrac{2b}{5}$. Verified for
all starting values $n < 5000$ and $200$ steps each in
`collatz_light_cone.py`. $\square$

The confinement is the whole point of the "light cone" name borrowed from
physics: it is the region the dynamics is *allowed* to be in. A relativistic
particle cannot leave its light cone; a Collatz orbit cannot leave its bounce
cone. Where the analogy improves on the original is that here the cone is not
just a boundary on motion — it is a **funnel with a downhill drift**, and that
is the next section.

---

## 4. The drift: the funnel rolls downhill

Confinement alone does not force collapse; a ball can rattle inside a level
funnel forever. What pulls the Collatz orbit to the vertex is that the bounce,
on average, loses height.

Group the steps into **macrosteps**: one odd step $x \mapsto 3x+b$ followed by
the run of halvings it triggers, $3x+b \mapsto (3x+b)/2 \mapsto \cdots$ until
an odd number reappears. The multiplier of one macrostep is

$$
\mu = \frac{3}{2^{k}},
$$

where $k$ is the number of trailing halvings. The exponent $k$ is governed by
the $2$-adic valuation of $3x+b$; across odd inputs it follows the geometric
law $\Pr[k = j] = 2^{-j}$, with mean $\mathbb E[k] = 2$. Therefore the mean
log-multiplier per macrostep is

$$
\mathbb E[\log \mu] = \log 3 - \mathbb E[k]\,\log 2 = \log 3 - 2\log 2 = \log\tfrac34 \approx -0.2877.
$$

**Theorem 3 (the average contraction is $\tfrac34$).** *Modelling the trailing
valuation as geometric, the typical macrostep multiplies the value by
$\tfrac34$. The orbit is, on average, a geometric contraction toward the
vertex of the cone.*

The script measures this directly over the odd inputs below $10^5$ and returns
$-0.2877$ for $b=+1$ and $-0.2876$ for $b=-1$ — the predicted $\log\tfrac34$ to
four places, and, tellingly, **the same value for both maps**. A funnel that
both confines (Proposition 2) and contracts (Theorem 3) is a funnel whose ball
rolls to the bottom: this is the geometric statement of convergence. It is a
statement about the *typical* orbit, in the sense of an average over residues —
which is exactly where its strength ends, and §7 makes that explicit.

---

## 5. The collapse as an infinite application

The theory developed in *The Elementary Theory of the Infinite Application of a
Function* studies what survives when a map is applied not a few times but an
infinite number of times — "the collapse, the stable residue, of iterative
processes." Read through that lens, the cone is a picture of the residue.

The fundamental object there is the diagonal and its crossings with the graph:
the fixed points are the zeros of $g(x) = f(x) - x$, the intersections of the
graph with $y = x$, and they separate the dynamical basins. Our cone carries
exactly this structure, doubled: two edges, two crossings with the bisector,
at $x = 0$ and $x = -b/2$. The infinite application of $T$ is the limit of the
bounce, and the bounce — confined to the cone, contracting toward the vertex —
has for its asymptotic shadow the **bottom of the funnel**. The named map
$T$ is, in that book's phrase, "the visible outer layer"; underneath lies the
single attractor the infinite application exposes.

For $b = +1$ that attractor is, on the integers, the terminal oscillation
$1 \to 4 \to 2 \to 1$ — the orbit cannot reach the literal vertex
$\left(-\tfrac25,-\tfrac15\right)$, which is negative and irrational, so it
parks at the smallest cycle the lattice allows near the narrow end of the cone.
The infinite application does not converge to a point in the strict sense; as
that book insists for the bell, it becomes *an oscillation upon the limit*
rather than the limit itself. The cone says the same: the funnel narrows to a
vertex the integers cannot occupy, so the orbit settles into the tightest
bounce available — the $3$-cycle at the throat.

---

## 6. Why $1$? The throat of the cone

The point $(1,1)$ sits on the bisector, inside the cone (at $x=1$ the wedge
spans $y \in [\tfrac12, 4]$, and $1$ is between). The terminal cycle is the set
of edge points $(1,4), (4,2), (2,1)$ — three corners of the bounce at the
narrowest place the integer lattice reaches before the vertex. In the funnel
picture, $1$ is *where the ball comes to rest* because it is the lowest lattice
point on the bisector that the contracting bounce can hold: below it the cone
has already pinched past the smallest positive integer.

This is the honest content of the slogan "$1$ is inside the cone." It is true,
and it is suggestive, but — as the next section shows — it is not
discriminating, because $1$ is inside the $3x-1$ cone too.

---

## 7. The mirror cone: the honest obstruction

Set $b = -1$. The vertex flips to $V' = \left(\tfrac25, \tfrac15\right)$, the
exact reflection of $V$ through the origin. The even edge is unchanged; the odd
edge $y = 3x - 1$ is the slope-$3$ line through the new vertex. The diagonal
still runs inside the wedge (Theorem 1 holds for both signs). The drift is
still $\log\tfrac34$ (Theorem 3 returned $-0.2876$). **The two cones are mirror
images, and every structural property we have proved holds identically for
both.**

And yet the destinies differ completely. The $3x+1$ map has the single
positive cycle $\{1,2,4\}$. The $3x-1$ map has **three**:

$$
\{1,2\}, \qquad \{5,7,10,14,20\}, \qquad \{17,25,34,37,41,50,55,61,68,74,82,91,110,122,136,164,182,272\}.
$$

The first two are short; the third has eighteen members. Three drains at the
bottom of a funnel that is geometrically indistinguishable, edge for edge,
drift for drift, from the funnel with one drain.

**This is the wall.** A confinement-plus-contraction argument concludes "the
ball reaches *a* bottom" — and that is *true* for $3x-1$ as well; every $3x-1$
orbit does reach one of its three cycles. What the cone cannot deliver is
*uniqueness of the bottom*. The geometry that traps and shrinks the orbit is
symmetric under the reflection $b \mapsto -b$, while the cycle count is not, so
no property invariant under that reflection — and every property in §§2–5 is —
can separate one cycle from three. The same obstruction appears in *The
Indestructible Set* from the set-theoretic side: the $3n-1$ map "satisfies
identical set-level laws while having three cycles instead of one." Here it is
the identical *cone-level* laws. Two routes, one wall.

---

## 8. What the cone sees, and what it does not

The cone is an honest instrument. It sees, exactly:

- **Confinement** (Prop. 2): the orbit is a sequence of bounces on two lines,
  trapped in the wedge, never escaping to a third regime.
- **The bisector at the core** (Thm. 1): the line of fixed points runs through
  the cone, and the orbit drifts along it.
- **Contraction** (Thm. 3): the typical macrostep is a $\tfrac34$ shrink, so
  the funnel runs downhill and the bounce loses height on average.
- **A single attractor for the infinite application** in the sense of §5: a
  narrowing throat that the integers can only fill with a small terminal cycle.

It does not see:

- **Which** terminal cycle a given orbit reaches — the discrimination that
  separates $3x+1$ from $3x-1$ is invisible to every cone property, because
  the cones are mirror images.
- **Whether the contraction is universal** rather than merely average. Theorem
  3 is an expectation over residues; a single orbit can climb for a long time
  (the upper edge has slope $3$), and "on average downhill" is not "always
  arrives." Turning the average drift into a guarantee for *every* starting
  value is precisely the conjecture, and the cone leaves it open.

The path forward is the one named at the close of *The Indestructible Set*: not
a stronger confinement, however tight, but bounce-to-bounce composition that
the symmetric geometry cannot capture — an argument sensitive to the sign of
$b$, because the answer is.

---

## 9. Conclusion: a true funnel, an incomplete proof

Two lines, one vertex, one wedge. The Collatz map, read one step at a time,
is a ball bouncing in a funnel that confines it (it never leaves the cone) and
drains it (every macrostep is, on average, a $\tfrac34$ contraction toward the
throat). That funnel is real, and it is the geometric body of the same
"asymptotic shadow" the infinite-application theory studies abstractly: the
collapse of an iterated map onto the residue it cannot shed.

But the $3x-1$ map bounces in the mirror of that funnel — same confinement,
same drift, same bisector — and drains into three pools, not one. So the cone,
for all its honesty, stops exactly where every honest picture of Collatz stops:
it proves the ball goes *down*, and is silent on *which* drain it finds. The
funnel is genuine; the proof it gestures at is not; and between the two the
conjecture sits, intact, waiting for an argument that knows the sign of $b$.

---

## Reproducing the Results

All numerical claims are reproduced by:

```
python3 library/scripts/collatz_light_cone.py
```

The script verifies, for both $b = +1$ and $b = -1$: the cone vertex
$V_b = (-2b/5, -b/5)$ and the containment of the diagonal in the wedge
(Theorem 1); that every orbit point $(x_n, x_{n+1})$ lies on an edge of the
cone, exhaustively for all starting values $n < 5000$ over $200$ steps each
(Proposition 2); the mean log-multiplier per macrostep, measured at $-0.2877$
($b=+1$) and $-0.2876$ ($b=-1$) against the predicted $\log\tfrac34 = -0.2877$
(Theorem 3); and the positive cycle structure — the single cycle $\{1,2,4\}$
for $b=+1$ versus the three cycles $\{1,2\}$, $\{5,7,10,14,20\}$, and the
$18$-element cycle for $b=-1$ (Section 7). It also renders the two-panel figure
`library/images/collatz-light-cone.png`.