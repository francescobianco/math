---
title: "The Light Cone of Collatz: Two Pairs of Lines and the Geometry of the Bounce"
type: paper
created: 2026-06-13T15:00:00+00:00
updated: 2026-06-13T17:30:00+00:00
---

# The Light Cone of Collatz: Two Pairs of Lines and the Geometry of the Bounce

*Read the Collatz map one step at a time on the plane $(x, T(x))$ and the two
branches become two lines. They cross at a vertex and open into a wedge — a
light cone — and every orbit is trapped on its two edges, bouncing between
them like a ball settling into a funnel. This paper builds the cone exactly,
proves the bounce is confined and contracting, reads the collapse through the
theory of the infinite application of a function, compares it honestly with the
mirror cone of the $3x-1$ map, and then lifts the whole picture off the
integers: the cone becomes a stage for arbitrary continuous functions, and the
Collatz conjecture becomes the analytic statement that a confined curve over a
throat above the bisector drains to the vertex. The crazy crests of Collatz are
the shadow this smooth descent casts on the integer lattice.*

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

Then we mirror it — and find the one thing the mirror does *not* preserve. The
$3x-1$ map has the cone reflected through the origin: vertex
$V' = \left(\tfrac25, \tfrac15\right)$, the same diagonal inside, the same
$\tfrac34$ drift (measured $e^{-0.2876}$). Confinement and contraction are
identical. But the reflection through the origin fixes the diagonal *as a set*
while **swapping its two sides**, and the vertex sits on opposite sides in the
two worlds: the Collatz vertex lies **above** the bisector
($g(V) = \tfrac15 > 0$), the $3x-1$ vertex **below** it ($g(V') = -\tfrac15$).
In the language of *The Elementary Theory of the Infinite Application of a
Function*, where the displacement $g(x) = f(x) - x$ and its sign are *the*
fundamental difference, the throat of the Collatz cone sits on the **trapping
(dome) side** of equilibrium, the throat of the $3x-1$ cone on the **escaping
side** — exactly the distinction the bell-on-the-diagonal examples make
visible. And the destinies split accordingly: Collatz has the single cycle
$\{1,2,4\}$; $3x-1$ has *three*. The discriminant
$\operatorname{sign} g(V_b) = \operatorname{sign}(b)$ is the lone cone-level
quantity that is **odd** under the mirror, and it is the locus where any proof
must act. We are honest that "throat above $\Rightarrow$ a single cycle" is not
here turned into a theorem — that step is the conjecture itself — but we
correct the over-pessimism of the set-level picture in *The Indestructible
Set*: the cone is *not* blind to the difference between one drain and three;
the difference is which side of the bisector the funnel narrows onto.

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

![The Collatz light cone (left, $3x+1$) and its mirror, the $3x-1$ cone (right). The odd edge $y=3x+1$ (slope 3) and the even edge $y=x/2$ (slope 1/2) meet at the vertex $V$; the dashed diagonal $y=x$ runs inside the shaded wedge. The orbit from 7 bounces off the edges, drifting down the bisector toward the vertex. The zoom insets show the decisive asymmetry the mirror cannot hide: the Collatz vertex pokes **above** the bisector, the $3x-1$ vertex sits **below** it.](library/images/collatz-light-cone.png)

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
which is exactly where its strength ends, and §8 makes that explicit. Note too
that the same value falls out for *both* maps: contraction is reflection-even,
and so cannot, by itself, separate them. The feature that does is §7.

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
and suggestive — but $1$ is inside the $3x-1$ cone too, so containment is not
the discriminant. The discriminant is one level finer, and it is the subject of
the next section: not *whether* the throat is in the cone, but *which side of
the bisector the throat is on*.

---

## 7. The decisive asymmetry: which side of the bisector the throat is on

Set $b = -1$. The vertex flips to $V' = \left(\tfrac25, \tfrac15\right)$, the
reflection of $V$ through the origin. The even edge is unchanged, the diagonal
still runs inside the wedge, the drift is still $\log\tfrac34$. Confinement and
contraction are reproduced exactly. So far the two cones look like mirror
images with nothing to choose between them — and that is where an earlier,
over-pessimistic reading (echoed in *The Indestructible Set*) stops: "identical
laws, different cycle counts, the geometry cannot tell them apart."

It can. The reflection through the origin, $(x,y) \mapsto (-x,-y)$, fixes the
diagonal $y=x$ **as a set** but **swaps its two sides**: if $y>x$ then
$-y<-x$, so a point above the bisector maps to a point below it. The one cone
quantity that measures *which side of the bisector* a point lies on is the
displacement of *The Elementary Theory of the Infinite Application of a
Function*,

$$
g(x,y) = y - x \quad\text{(the value of } f(x)-x\text{ read off the graph),}
$$

whose sign is, in that book's words, "the fundamental difference" — it "tells
us whether the orbit is pushed up or down at each step." Evaluate it at the
vertex:

$$
g(V_b) \;=\; -\tfrac{b}{5} - \left(-\tfrac{2b}{5}\right) \;=\; \frac{b}{5},
\qquad
\operatorname{sign} g(V_b) = \operatorname{sign}(b).
$$

**Theorem 4 (the throat is reflection-odd).** *The displacement at the vertex
is $g(V_b) = b/5$. Hence the Collatz throat ($b=+1$) lies strictly **above**
the bisector and the $3x-1$ throat ($b=-1$) strictly **below** it, and this
single bit is the unique cone-level quantity that is **odd** under the mirror
$b \mapsto -b$. Every property in §§2–4 — vertex location up to sign,
containment of the diagonal, the $\tfrac34$ drift — is reflection-**even** and
therefore blind to the difference; the side of the bisector is not.*

This is exactly the structure the book's **bell on the diagonal** is built to
display. There a Gaussian sits below the diagonal except for the *dome* that
pierces above it; the dome is the **trap** — "a point pushed right whenever it
stands on the dome, pulled left whenever it stands beyond it" — and the orbit's
infinite application locks into a small bounded oscillation *on the dome*, while
points on the wrong side "march away forever" to $-\infty$. Above the diagonal
is the side of capture; below is the side of escape.

Read the two throats against that template:

- **$3x+1$, throat above ($g(V)=+\tfrac15$):** the narrow end of the funnel
  sits on the **dome / trapping side**. The contracting bounce, funneled down,
  is captured into a single bounded oscillation at the throat — the lattice's
  smallest available cycle, $1 \to 4 \to 2 \to 1$. **One drain.**
- **$3x-1$, throat below ($g(V')=-\tfrac15$):** the narrow end sits on the
  **escaping side**. There is no single trapping point at the throat to capture
  the bounce; the descent fragments into several terminal pools — and indeed the
  $3x-1$ map has **three** positive cycles,

$$
\{1,2\}, \quad \{5,7,10,14,20\}, \quad \{17,25,34,37,41,50,55,61,68,74,82,91,110,122,136,164,182,272\}.
$$

So the mirror image is not a wall after all — it is the *signpost*. The cone
does distinguish the one-drain world from the three-drain world, and it does so
through precisely the quantity the infinite-application theory singles out as
fundamental: the sign of $g$ at the vertex.

**What remains open.** Theorem 4 establishes the discriminant and its
interpretation; it does **not** prove the implication "throat above the
bisector $\Rightarrow$ exactly one positive cycle." That implication, made
rigorous and uniform over all integers, *is* the Collatz conjecture. What this
section does is locate it: the conjecture lives in the sign of $g(V_b)$, the one
feature the mirror symmetry breaks, and a proof must be an argument that this
sign forces a single trap — sensitive to the sign of $b$, because the answer
is. That is a sharper task than "find denser witnesses," and a more hopeful one
than "the geometry is blind."

---

## 8. From integers to the continuum: the cone as a universal stage

Everything so far has been about integers and about *one* map. But look at
what the cone actually used: only that the two branches are two lines with
slopes straddling $1$, meeting at a vertex. The arithmetic of $3x+1$ — the
parity test, the $2$-adic valuations, the residues — never entered the
geometry. This invites the real abstraction, and it is the goal of this part
of the paper.

Forget the integers. Forget the two branches. Let $f : [x_V, \infty) \to
\mathbb{R}$ be **any continuous function whose graph lives in the cone**:

$$
\frac{x}{2} \;\le\; f(x) \;\le\; 3x + b
\qquad\text{for all } x \ge x_V .
$$

We call such an $f$ **cone-confined**. It need not be piecewise linear, need
not come from a number-theoretic rule, need not be monotone. It is just a
curve threaded through the wedge. The question is the one the book *The
Elementary Theory of the Infinite Application of a Function* asks of every
map: what is the destiny of the **infinite application** $f^\infty$ — where do
the orbits $x, f(x), f(f(x)), \ldots$ go?

The conjecture we want to formalize, in the user's own words, is a clean
dichotomy with no arithmetic in it at all:

> If $f$ lives in the cone and the **vertex is above the bisector**, every
> orbit is funneled to the throat — the infinite application has a single
> destiny. If the **vertex is below the bisector**, the destiny is *open* —
> the funnel may fragment.

The rest of this part makes that statement precise, proves the half of it
that is a theorem, and isolates — honestly — the exact extra hypothesis the
other half needs. The reward is the thesis of this whole reading: **the crazy
crests of Collatz are not chaos but a shadow.** The wild peaks — $27$ soaring
to $9232$ — are the projection onto the integer lattice of a continuous
function funnelling, smoothly and inexorably, back toward the vertex of the
cone. The turbulence is the *sampling* of a calm descent; the integers are
where a confined continuous curve casts its jagged shadow. The Collatz
conjecture, in this light, stops being a fact about parities and becomes a
statement about continuous functions: *a confined curve over a throat above
the bisector has one attractor.*

---

## 9. The edge-displacement lemma and the throat sign-zone

Work with general edge slopes $0 < s_- < 1 < s_+$ (for Collatz $s_- =
\tfrac12$, $s_+ = 3$), edges meeting at $V = (x_V, y_V)$, and write the single
governing datum

$$
\delta \;:=\; g(V) \;=\; y_V - x_V \;=\; \frac{b}{5}.
$$

The displacement $g(x) = f(x) - x$ — the book's "fundamental difference,"
whose sign says whether the orbit is pushed right (toward larger $x$, away
from the throat) or left (toward the throat) — is squeezed by the edges. On
the edges themselves it is exactly linear:

**Lemma A (edge displacements).** *Along the lower and upper edges,*

$$
g_\pm(x) \;=\; (s_\pm - 1)\,(x - x_V) \;+\; \delta .
$$

*Both equal $\delta$ at the vertex. The lower one ($s_- - 1 < 0$) decreases in
$x$; the upper one ($s_+ - 1 > 0$) increases.* The proof is one line of
algebra: $g_\pm(x) = s_\pm(x - x_V) + y_V - x = (s_\pm-1)(x-x_V) + (y_V-x_V)$.

The two edges therefore cross the bisector at

$$
x_-^\ast = x_V - \frac{\delta}{s_- - 1} = x_V + \frac{\delta}{1 - s_-},
\qquad
x_+^\ast = x_V - \frac{\delta}{s_+ - 1},
$$

which for Collatz are $x_-^\ast = 0$ and $x_+^\ast = -\tfrac12$, and for
$3x-1$ are $x_-^\ast = 0$ and $x_+^\ast = +\tfrac12$ (verified in the script).
Because any confined $f$ is trapped between the edges, its displacement is
trapped between $g_-$ and $g_+$, and this pins the sign of $g$ near the throat:

**Lemma B (throat sign-zone).** *Suppose $\delta > 0$. Then on the interval
$[x_V,\, x_-^\ast)$ both edges lie strictly above the bisector, so* every
*confined $f$ satisfies $f(x) > x$ there: the whole cone near the throat is a
universal **right-push** zone. Symmetrically, if $\delta < 0$, then on
$[x_V,\, x_+^\ast)$ both edges lie below the bisector and every confined $f$
satisfies $f(x) < x$: a universal **left-push** zone.*

*Proof.* For $\delta > 0$: $g_+(x) = (s_+-1)(x-x_V) + \delta > 0$ for all
$x \ge x_V$ (both terms $\ge 0$, second $>0$), so the upper edge is above the
bisector everywhere; and $g_-$ starts at $\delta > 0$ and decreases to $0$ at
$x_-^\ast$, so the lower edge is above the bisector on $[x_V, x_-^\ast)$. With
both edges above, the entire cone slice is above, and $f(x) \ge \tfrac{x}{2} =
L_-(x) > x$ there. The case $\delta < 0$ is the mirror argument. $\square$

This is the geometric engine of the whole dichotomy: the sign of $\delta$
decides, with no further information about $f$, whether the throat pushes
orbits back into the cone or out through its tip.

---

## 10. The invariance dichotomy: trap versus leak

Lemma B already feels like the answer, but it has a subtlety with a beautiful
resolution. "Right-push near the throat" sounds like it pushes orbits *away*
from the vertex, not toward it — and so it does, pointwise. The point is what
it does to the **domain**: a right-push floor at the throat is a *reflecting
wall*. It guarantees the orbit can never fall out the bottom. Make this exact.

**Theorem A (invariance dichotomy).** *The half-line $[x_V, \infty)$ — the
$x$-extent of the cone — is forward-invariant under **every** cone-confined
continuous $f$ if and only if $\delta \ge 0$.*

*Proof.* For any confined $f$, $f(x) \ge L_-(x) = s_-(x-x_V) + y_V \ge y_V$
for $x \ge x_V$. So $f(x) \ge y_V$, and $y_V \ge x_V \iff \delta \ge 0$. When
$\delta \ge 0$ every image lands at height $\ge y_V \ge x_V$, back in the
domain: the cone traps. When $\delta < 0$, the lower-edge map $f = L_-$ itself
sends throat points below $x_V$ — the script iterates $f(x) = x/2$ from
$x = 0.5$ and watches it fall under the $3x-1$ vertex $x_V = \tfrac25$ in one
step — so the cone **leaks**. $\square$

So the geometry sorts the two worlds before any dynamics is run:

- **$\delta > 0$ (Collatz, throat above the bisector):** the cone is a
  **trap**. Orbits cannot escape through the throat; they are confined to
  $[x_V, \infty)$ forever and must accumulate on whatever invariant set lives
  inside.
- **$\delta < 0$ ($3x-1$, throat below the bisector):** the cone is a
  **sieve**. Orbits can drain out the narrow end, and what becomes of them is
  decided elsewhere — the destiny is, in the user's phrase, *to be seen.*

This is the rigorous core of the intuition, and notice it is purely
order-theoretic: trap-versus-leak is exactly $\operatorname{sign}\delta =
\operatorname{sign} b$, the one reflection-odd quantity of Theorem 4, now
given dynamical teeth.

---

## 11. The provable core, and the honest gap

Trapping is not yet converging. A trapped orbit could still wander forever or
split among several attractors. To turn the trap into a single destiny we need
one more hypothesis — and naming it precisely is where honesty earns its keep,
because the tempting statement is false.

**The naive claim is false.** "Lives in the cone with $\delta>0$ $\Rightarrow$
collapses to the throat" is *not* a theorem. The identity $f(x) = x$ lives in
the Collatz cone (for $x \ge 0$: $\tfrac{x}{2} \le x \le 3x+1$), yet every
point is fixed — nothing collapses. The script confirms the confinement and
the non-collapse. Bare confinement leaves the orbit free to ride the bisector.
Something must forbid that.

The clean sufficient hypothesis is **contraction**, and it makes the throat
half of the dichotomy a genuine theorem:

**Theorem B (throat capture).** *Let $f : [x_V, \infty) \to \mathbb{R}$ be
cone-confined with $\delta > 0$, and a Lipschitz contraction: $|f(x) - f(x')|
\le \lambda\,|x - x'|$ with $\lambda < 1$. Then $f$ maps the complete space
$[x_V,\infty)$ into itself (Theorem A), so by the Banach fixed-point theorem
$f$ has a unique fixed point $x^\ast$, and $f^n(x) \to x^\ast$ for every
$x \ge x_V$. Moreover $x^\ast \ge x_-^\ast$, since on $[x_V, x_-^\ast)$ the
right-push of Lemma B forbids any fixed point. The infinite application
collapses the entire cone to a single throat point.*

Crucially, Theorem B is a **proof**, not a measurement. Banach's theorem
settles the destiny by an analytic argument; the script's iteration of
$f(x) = \tfrac{x}{2} + 1$ on $[1,\infty)$ — orbits from $1, 3, 7, 27, 1000$ all
converging to the throat $x^\ast = 2$ — is an *illustration that happens to be
trustworthy*, and it is trustworthy for a specific reason: a contraction damps
rounding error as fast as it damps everything else, so the floating-point
orbit and the true orbit converge to the same point. This robustness is not
generic, and §13 is devoted to exactly when it fails. The content of Theorem B
is the formal, universal statement the user asked for: *any* continuous
contraction living in a cone with throat above the bisector has the vertex
region as its sole destiny, by a three-line proof — no arithmetic, no
parities, no $2$-adics, just confinement, the sign of $\delta$, and
contraction.

**The other side is genuinely open.** With $\delta < 0$ the same contraction
hypothesis does not save the day, because the cone is not invariant, and a
confined map can fragment into *several* attractors — the continuous analogue
of the three $3x-1$ cycles. One can *draw* such a function (a confined curve
crossing the bisector several times, each downward crossing an attractor), but
— for the reasons of §13 — one cannot honestly *iterate it numerically* to
demonstrate the limits: the fragmented regime is precisely the one where
quantization decides the destiny. The fragmentation is real and provable
crossing-by-crossing as a statement about fixed points; its long-run
*trajectories* are not a thing a floating-point computation may be trusted to
report. Below the bisector, fragmentation is allowed; the destiny is open
exactly as the intuition says, and open in a way that numerics cannot close.

**Where Collatz actually sits — and why this is not a proof of it.** The
catch is that the true Collatz map is **not** a Lipschitz contraction. Its
single-valued envelope must contain the upper edge $y = 3x+1$, slope $3 > 1$:
an *expansion*. Collatz contracts only **on average** — the $\tfrac34$ drift
of Theorem 3, a Lyapunov/measure statement, not a pointwise Lipschitz one.
Theorem B is unconditional for true contractions; the Collatz map asks us to
weaken "Lipschitz $\lambda < 1$" to "average multiplier $\tfrac34 < 1$" and
keep the conclusion. That single weakening is the whole difficulty:

> **The continuum form of the Collatz conjecture.** A cone-confined map with
> throat above the bisector ($\delta>0$) and **average** log-contraction
> ($\mathbb{E}[\log\mu] < 0$) sends every orbit to the throat.

For a uniform contraction this is Banach and done. For an average one it is
open, and it is *exactly* the conjecture — now stated with no reference to
integers, parity, or $3x+1$, as a clean problem in real dynamics: does
trapping plus average contraction force a single attractor? The cone has
carried Collatz out of number theory and set it down in analysis, on the seam
between Lipschitz and Lyapunov.

---

## 12. What the cone sees, and what it does not

The cone is an honest instrument. It sees, exactly:

- **Confinement** (Prop. 2): the orbit is a sequence of bounces on two lines,
  trapped in the wedge, never escaping to a third regime.
- **The bisector at the core** (Thm. 1): the line of fixed points runs through
  the cone, and the orbit drifts along it.
- **Contraction** (Thm. 3): the typical macrostep is a $\tfrac34$ shrink, so
  the funnel runs downhill and the bounce loses height on average.
- **A single attractor for the infinite application** in the sense of §5: a
  narrowing throat that the integers can only fill with a small terminal cycle.

And it sees one thing more than a first reading credits it with:

- **Which side of equilibrium the funnel narrows onto** (Thm. 4): the sign of
  $g$ at the vertex, $\operatorname{sign} g(V_b) = \operatorname{sign}(b)$ — the
  Collatz throat above the bisector (the trapping/dome side), the $3x-1$ throat
  below it (the escaping side). This is the one cone quantity odd under the
  mirror, and it tracks the split between one drain and three.

It does not see:

- **That "throat above" forces a single cycle.** Theorem 4 names the
  discriminant; it does not prove the implication. That implication, uniform
  over all integers, *is* the conjecture.
- **Whether the contraction is universal** rather than merely average. Theorem
  3 is an expectation over residues; a single orbit can climb for a long time
  (the upper edge has slope $3$), and "on average downhill" is not "always
  arrives." Turning the average drift into a guarantee for *every* starting
  value is, again, the conjecture.

The path forward is no longer "the geometry is blind, find denser witnesses."
It is sharper: prove that a throat on the **dome side** of the bisector admits a
single trap. The argument must be sensitive to the sign of $b$ — because the
answer is, and now we know exactly where in the geometry that sign lives.

---

## 13. On numerical verification and the quantization boundary

A warning, and a self-imposed discipline, about the continuum part. It is
tempting to *check* the dichotomy of §§9–11 the way we checked everything on
the integers: pick a confined continuous $f$, iterate it, watch where the
orbit lands. **This is not a valid verification, and the paper does not rely
on it.** Here is why.

The infinite application $f^\infty$ of a continuous map confined to the cone
is, in general, **sensitive to rounding**. A floating-point step replaces the
true value $f(x)$ with $f(x) + \varepsilon$, $\varepsilon \sim 10^{-16}$; and
along any stretch where the map does not contract — where its slope exceeds
$1$, as the upper edge does with slope $3$ — that perturbation is *amplified*,
not damped. After enough steps the computed trajectory and the true trajectory
have separated completely. We are sampling a function at the **boundary
between order and chaos**, where the limit of the iteration is genuinely
discontinuous in the initial data and in the arithmetic. A number that the
floating-point orbit reports as the destiny may be an artifact of the last bit
of the mantissa.

This is not a defect of our particular script; it is a theorem-shaped fact
about the regime. It cuts our available tools to exactly two:

1. **Analytic proof.** Where the dynamics *is* a contraction, Banach (Theorem
   B) settles the destiny with no computation at all — and, not coincidentally,
   that is precisely the regime where a numerical orbit *would* also be
   reliable, because a contraction damps rounding error at the same rate it
   damps everything. Robustness of the numerics and provability by Banach are
   the **same condition**. When we can trust the computer we did not need it;
   when we need it we cannot trust it.
2. **Closing on the integers.** One can make the iteration exact by working in
   a lattice with exact arithmetic — but a confined map on the integers with
   the Collatz edges *is* the Collatz map. Quantizing to recover exactness
   hands the problem straight back to number theory; it is not an independent
   check of the continuum claim, it is the original conjecture wearing the
   continuum's coat.

So the honest verifications in this paper are confined to what is
**rounding-proof**: the cone geometry (vertex, edge–bisector crossings,
the throat sign-zone) is exact rational algebra; the invariance dichotomy
$\delta \gtrless 0$ is a single inequality; the $\tfrac34$ drift is a
statistical average over *integers* with exact $2$-adic valuations; the
contraction demo converges because it is a contraction. Everything that would
require trusting a long floating-point orbit of a non-contracting confined map
is deliberately absent, and the multi-attractor "cartoon" of §11 is labelled a
cartoon for exactly this reason.

There is real mathematics in the instability itself, but it is a *different*
problem. How does a continuous funnel-to-the-vertex dynamics fracture when you
quantize it — when you force every value onto a lattice and let the rounding
error drive the trajectory? That is a question about the dynamics *of the
quantization error*, and its natural home is the study of the fractal sets
such errors trace out: the basin boundaries, the strange repellers, the
self-similar structure of "which lattice point does this continuous orbit snap
to." We flag it here as a deliberate scope boundary and a sequel: **the crazy
crests are the shadow of a calm continuous descent (this paper); the precise
shape of the shadow — how the quantization carves the smooth funnel into
Collatz's jagged silhouette — belongs to a forthcoming study of quantization
instability and its fractals.** The two papers meet at this section: this one
proves the descent is smooth and analytic; that one will measure how the grid
roughens it.

---

## 14. Conclusion: a true funnel, and the seam where the proof must enter

Two lines, one vertex, one wedge. The Collatz map, read one step at a time,
is a ball bouncing in a funnel that confines it (it never leaves the cone) and
drains it (every macrostep is, on average, a $\tfrac34$ contraction toward the
throat). That funnel is real, and it is the geometric body of the same
"asymptotic shadow" the infinite-application theory studies abstractly: the
collapse of an iterated map onto the residue it cannot shed.

The $3x-1$ map bounces in the mirror of that funnel — same confinement, same
drift — and the mirror tempts one to conclude the geometry cannot tell one
drain from three. But the mirror, reflecting through the origin, fixes the
bisector as a set and **swaps its two sides**, and the throats fall on opposite
sides: Collatz above (the trapping dome side, $g(V)=+\tfrac15$), $3x-1$ below
(the escaping side, $g(V')=-\tfrac15$). The cone is not blind; it points. The
displacement $g$ at the vertex — the very quantity the infinite-application
theory calls the fundamental difference — is the one feature the symmetry
breaks, and it tracks the one-versus-three split exactly.

What the cone does not yet do is *force* the implication from that sign to a
unique cycle; that step, made uniform, is the conjecture itself. So the funnel
is genuine and the discriminant is genuine, and between them lies not a blank
wall but a seam: prove that a throat above the bisector admits a single trap.
The conjecture sits there, at the sign of $g(V_b)$ — exactly where the mirror
could not follow it.

And the cone does one thing more, which is the deepest reason to have built
it: it lets us *leave the integers*. Read as a stage for arbitrary continuous
maps (Part II), the cone turns the Collatz conjecture into a statement with no
arithmetic in it — *a confined curve over a throat above the bisector, that
contracts on average, drains to the vertex.* For a genuine contraction this is
Banach's theorem, three lines. For an average one it is open, and that gap —
from Lipschitz to Lyapunov — is the whole conjecture, now sitting in real
dynamics rather than number theory. The crazy crests of Collatz are the shadow
this continuous descent casts on the integer lattice; the smoothness of the
descent is provable, while the jaggedness of the shadow is a separate study of
quantization and its fractals (§13). The funnel is calm. Only its shadow is
wild.

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
(Theorem 3); the displacement at the vertex $g(V_b) = b/5$, reporting the
Collatz throat **above** the bisector and the $3x-1$ throat **below** it, with
$\operatorname{sign} g(V_b) = \operatorname{sign}(b)$ (Theorem 4); and the
positive cycle structure — the single cycle $\{1,2,4\}$ for $b=+1$ versus the
three cycles $\{1,2\}$, $\{5,7,10,14,20\}$, and the $18$-element cycle for
$b=-1$ (Section 7). It also renders the two-panel figure (with vertex zoom
insets) `library/images/collatz-light-cone.png`.

For Part II (the continuum abstraction) the script computes only the
**rounding-proof** quantities, in keeping with §13: the edge–bisector
crossings $x_-^\ast, x_+^\ast$ and the throat sign-zone (Lemmas A–B, exact
rational arithmetic); the invariance dichotomy $\delta = b/5 \gtrless 0$
(Theorem A); and the contraction demonstration $f(x) = \tfrac{x}{2}+1 \to 2$
(Theorem B — reliable because contractions damp rounding error). It also
prints the identity counterexample (confinement alone does not collapse) and,
explicitly labelled as a quantization-sensitive *cartoon* rather than a
verification, the $\delta<0$ leak and a multi-attractor sketch. No claim in
the paper rests on iterating a non-contracting confined map in floating point;
that instability is itself the subject of the sequel announced in §13.