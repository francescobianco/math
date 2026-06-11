---
title: The Elementary Theory of the Infinite Application of a Function
type: book
created: 2026-06-03T09:00:00+00:00
updated: 2026-06-12T11:00:00+00:00
color: #b8336a
section_prefix: nodot
author: F. Bianco
release: EDIZIONE 2026
---

# The Elementary Theory of the Infinite Application of a Function

A speculative treatise on what a function *becomes* once it is applied an
infinite number of times — on the asymptotic shadow that survives iteration.

> "Classical mathematics studies objects. This theory studies their destiny."

## Preface

Classical mathematics studies *objects*. This theory proposes instead to study
their **destiny**.

Not

$$
f(x)
$$

but

$$
f^{\infty}(x),
$$

where $f^{\infty}$ denotes the result of applying a function infinitely many
times.

The central philosophical hypothesis is the following:

> The observable mathematical objects may be the stable shadows of deeper
> iterative processes.

Throughout these notes we treat $f^{\infty}$ not as a formal limit alone but as
an object in its own right — the *fate* of $f$ — and we ask what algebra,
geometry, and arithmetic look like when destiny, rather than formula, becomes
the identity of a function.

---

# Part I — The Infinite Operator

## Chapter 1 — Definition

Given a function

$$
f : X \to X,
$$

we define the **orbit** of a point $x$ as the sequence

$$
x,\ f(x),\ f^{2}(x),\ f^{3}(x),\ \dots
$$

where $f^{n}$ denotes the $n$-fold composition $f \circ f \circ \cdots \circ f$.

We then introduce the object

$$
f^{\infty}
$$

as the **asymptotic behaviour** of the function: the limiting structure to which
the orbit tends, whenever such a structure exists.

## Chapter 2 — The Fundamental Classes

The fate of an orbit falls into a small number of qualitative classes.

### Point attractor

$$
f^{\infty}(x) = L,
$$

a single limit independent of the starting point. For instance

$$
f(x) = \sin(x) \quad\Longrightarrow\quad \sin^{\infty}(x) = 0.
$$

### Non-trivial fixed point

$$
f^{\infty}(x) = L, \qquad L = f(L).
$$

The classical example is the **Dottie constant**:

$$
\cos^{\infty}(x) = 0.739085\ldots
$$

### Cycle

$$
f^{\infty}(x) = \{a_1, a_2, \dots, a_k\}.
$$

The orbit settles onto a finite periodic set, as in the Collatz tail

$$
1 \to 4 \to 2 \to 1.
$$

### Multiple attractor

The result depends on the initial point: the space $X$ splits into **basins**,
each draining into its own attractor.

### Strange attractor

The limit set has non-trivial geometric structure: **chaos**.

### Escape

$$
f^{\infty}(x) = \infty,
$$

as for the iterated exponential $e^{x}$.

---

# Part II — The Attractor as an Object

## Chapter 3 — The Asymptotic Attractor

We define

$$
\mathcal{A}(f)
$$

as the **asymptotic attractor** of $f$: the set of limit points common to the
orbits. Examples:

$$
\mathcal{A}(\sin) = \{0\}, \qquad
\mathcal{A}(\cos) = \{0.739085\ldots\}, \qquad
\mathcal{A}(\mathrm{Collatz}) = \{1, 4, 2\}.
$$

The operator $\mathcal{A}$ is the central object of the theory: it maps a
function to its destiny.

## Chapter 4 — Equivalence Classes

We declare two functions equivalent,

$$
f \sim g,
$$

precisely when they share the same attractor:

$$
f \sim g \iff \mathcal{A}(f) = \mathcal{A}(g).
$$

Under this relation the **formula** is no longer the identity of a function.
The **destiny** is.

Two wildly different expressions may collapse to the same limit set, and so
belong to the same class; the theory is, in part, the study of these classes.

---

# Part III — Onion Functions

## Chapter 5 — Emergent Objects

We advance a hypothesis: the **familiar functions are not primitive**. They are
the collapse — the stable residue — of iterative processes.

For example, $\log(x)$ might be the shadow of some unknown operator $\mathrm{GOL}$:

$$
\mathrm{GOL}^{\infty}(x) = \log(x).
$$

The named function is the visible outer layer; underneath lie hidden iterative
strata, like the layers of an onion.

## Chapter 6 — Mathematical Archaeology

Two problems present themselves.

The **direct problem** is to compute the fate of a known generator:

$$
f \longrightarrow f^{\infty}.
$$

The **inverse problem** is archaeological — given an observed function $F$, to
recover the primordial generator that produces it:

$$
F \longrightarrow \;?
$$

The inverse problem is, in general, far harder, and is the deeper concern of
this theory.

---

# Part IV — The Diagonal

## Chapter 7 — The Identity Function

The fundamental object of the geometry of iteration is the identity

$$
I(x) = x,
$$

whose graph, the diagonal

$$
y = x,
$$

represents **absolute equilibrium**: every point on it is fixed.

## Chapter 8 — The Fundamental Difference

We study the displacement

$$
g(x) = f(x) - x.
$$

The zeros of $g$ are exactly the **fixed points** of $f$,

$$
f(x) = x,
$$

i.e. the intersections of the graph of $f$ with the diagonal. The sign of $g$
tells us whether the orbit is pushed up or down at each step.

## Chapter 9 — Dynamics of the Zeros

The structure of $g(x) = f(x) - x$ governs the fate of the orbit.

### Exponential

$$
e^{x} - x > 0 \quad \text{everywhere}.
$$

The graph never meets the diagonal: there is no fixed point, and the orbit
**escapes**.

### Logarithm

$$
\log(x) - x < 0 \quad \text{everywhere}.
$$

Again no fixed point, but now the orbit is pushed below the diagonal: it
**collapses**.

### Cubic

$$
x^{3} - x = x(x-1)(x+1),
$$

with zeros

$$
-1,\ 0,\ 1.
$$

These three fixed points **separate the dynamical basins**: the cubic shows, in
the simplest algebraic setting, how zeros of $g$ partition the line into regions
of distinct destiny.

---

# Part V — Harmonic Collatz

## Chapter 10 — Removing the `if`

The Collatz map is usually defined by a conditional. We replace the branch by a
single analytic expression — its **harmonic** form:

$$
f(x) = \frac{7x + 2}{4} - \frac{5x + 2}{4}\cos(\pi x).
$$

On the integers $\cos(\pi n) = (-1)^{n}$, and the formula reproduces Collatz
exactly: even $n$ gives $n/2$, odd $n$ gives $3n+1$.

## Chapter 11 — Complex Form

Parity can be lifted into the complex plane:

$$
(-1)^{n} = e^{i\pi n}.
$$

What was a discrete distinction — even versus odd — becomes a continuous
**phase**.

## Chapter 12 — The Fundamental Cycle

The terminal cycle

$$
1 \to 4 \to 2 \to 1
$$

is reinterpreted as an **oscillator**. The conjecture is then read not as

> all trajectories converge to $1$,

but as

> all trajectories converge to the same **rhythm**.

## Chapter 13 — The Phases

Define the phase of an integer through its stopping time $s(n)$:

$$
\phi(n) = s(n) \bmod 3.
$$

The trajectories collapse into **three phases**, mirroring the period-three
length of the terminal cycle.

## Chapter 14 — The Fundamental Wave

Interpolate the repeating tail

$$
1, 4, 2, 1, 4, 2, \dots
$$

by a continuous periodic function with period three:

$$
w(t + 3) = w(t).
$$

Collatz then decomposes as a wave plus a residue:

$$
x(t) = w(t + \phi) + \varepsilon(t).
$$

## Chapter 15 — The Residue

The residue is what the wave fails to capture:

$$
\varepsilon(t) = x(t) - w(t + \phi).
$$

The **central hypothesis** of this part is that the residue vanishes
asymptotically:

$$
\varepsilon(t) \to 0,
$$

so that, in the limit, every trajectory *is* the fundamental wave.

---

# Part VI — Harmonic Analysis of Arithmetic

## Chapter 16 — Taylor Expansion

Expanding the cosine that carries the parity,

$$
\cos(\pi x) = \sum_{m=0}^{\infty} (-1)^{m}\frac{(\pi x)^{2m}}{(2m)!},
$$

turns harmonic Collatz into an **infinite series** — an analytic object built
from a single power series.

## Chapter 17 — Numbers as Resonances

Hypothesis: the integers are **synchronisation points** of the phase. Since

$$
e^{i\pi n} = \pm 1,
$$

the integers see only the extreme values of the wave — its crests and troughs.
Between them lies a continuum the integers never sample.

## Chapter 18 — Spectral Connection

We can now chain three viewpoints:

$$
(-1)^{n} \;\longrightarrow\; e^{i\pi n} \;\longrightarrow\; \cos(\pi n).
$$

Parity becomes phase, phase becomes wave. **Arithmetic becomes a harmonic
phenomenon**.

---

# Part VII — Infinite Differentiation

## Chapter 19 — The Onion, Again

Where iteration follows a trajectory, **differentiation removes layers**:

$$
f \;\longrightarrow\; f' \;\longrightarrow\; f'' \;\longrightarrow\; \cdots
$$

Each derivative peels away one stratum of structure.

## Chapter 20 — Double Infinity

Two infinite operators act on a function in orthogonal directions.

### Iteration

$$
f^{\infty}
$$

follows the **trajectory** — the horizontal, dynamical fate.

### Differentiation

$$
D^{\infty}(f)
$$

strips the **structure** — the vertical, analytic skeleton.

## Chapter 21 — Fixed Points of Differentiation

The derivative operator $D = \dfrac{d}{dx}$ has its own fixed points. Since

$$
\frac{d}{dx} e^{x} = e^{x},
$$

the exponential is a **fixed point of $D$**: differentiation, applied infinitely,
leaves it unchanged. The exponential is to $D$ what the Dottie constant is to
$\cos$.

---

# Part VIII — Philosophy of the Infinite

## Chapter 22 — The Multimirror

Each iteration is a **mirror**:

$$
x \;\longrightarrow\; f(x) \;\longrightarrow\; f^{2}(x) \;\longrightarrow\; \cdots
$$

The attractor is the **vanishing point** of this infinite perspective — the
place where all reflections converge.

## Chapter 23 — Compression of Information

Just as

$$
7 + 5 = 12
$$

loses the information about which addends were used, so the passage

$$
f \;\longrightarrow\; f^{\infty}
$$

**loses the information about the dynamics**. The attractor remembers the
destination but forgets the road.

## Chapter 24 — Fundamental Principle

> The observable mathematical objects may not be primitive.
>
> They may be the stable residue of infinite iterative processes.

---

# Part IX — The Destiny Field

## Chapter 25 — From Attractor to Field

The attractor $\mathcal{A}(f)$ of Part II was a single set. But destiny varies
with the starting point. Define the **destiny field** of $f$ as the function

$$
x \;\longmapsto\; \mathcal{A}_x(f),
$$

assigning to each point the limit behaviour of *its own* orbit. The theory of
infinite applications becomes the study of this field: not one destiny, but
the geography of all destinies.

For the cosine the field is constant:

$$
\mathcal{A}_x(\cos) = \{0.739085\ldots\} \quad \text{for every } x.
$$

One value compresses the whole field. Information content: zero. The
compression of Chapter 23 is total.

## Chapter 26 — The Anomaly of Stability

For the harmonic Collatz map of Part V the destiny field is a dichotomy:

$$
\mathcal{A}_x(f) =
\begin{cases}
\{1,4,2\} & x \in B,\\[2pt]
\infty & \text{for most other } x,
\end{cases}
$$

where $B$ is a thin dust of slivers concentrated around the integers.
Measured: only $2.5\%$ of the reals in $[1,50]$ belong to $B$; the sliver
around the integer $n$ has thickness collapsing with the peak $M(n)$ of the
trajectory,

$$
r(n) \approx \frac{n}{\pi^{2}M(n)^{2}}
$$

(the sliver at $27$, whose flight reaches $9232$, is $10^{-8}$ wide). This
field is **incompressible**: its geometry around $n$ stores the entire
trajectory of $n$.

The two examples are the poles of a classification axis: functions ranked by
the complexity of their destiny field. At one end the constant field
(cosine, closed form, zero memory); at the other the fractal field (Collatz,
total memory, no formula). Where the destiny field develops anomalously thin
stable sets, iteration theory touches arithmetic — and problems become hard.

## Chapter 27 — The Two Completions

The anomaly seems to say that the integers are special points of the
continuum. But the harmonic canvas was *built* to resonate with them: the
carrier $\cos(\pi x)$ equals $\pm 1$ exactly on $\mathbb{Z}$, giving
$f'(\text{even})=1/2$ and $f'(\text{odd})=3$. The analytic continuum is a
biased court.

A fair court exists. It is the **formal completion**

$$
\mathbb{Z}_2=\varprojlim\; \mathbb{Z}/2^{k}\mathbb{Z},
$$

an inverse limit — a categorical construction, intrinsic to the parity
structure of the map, with no interpolation chosen. There the Collatz map is
continuous without artifice, conjugate to the shift, and the integers are
**dense and in no way special**.

The two courts pass the same sentence in dual forms. In $\mathbb{R}$ the
integers are a topologically isolated dust of stability; in $\mathbb{Z}_2$
they are metrically negligible (Haar measure zero). In both, the arithmetic
question lives on a thin set invisible to the ambient theory. The difficulty
does not depend on the courtroom.

## Chapter 28 — The Transferable Colour

Every analytic function vanishing on the integers is divisible by
$\sin(\pi x)$. Hence the analytic extensions of the Collatz map form the
affine space

$$
g = f + \sin(\pi x)\,h, \qquad h \text{ entire}:
$$

infinitely many **canvases**, one **colour** — all restrict to the same map
on $\mathbb{Z}$.

Measured: the multiplier of the terminal cycle $1\to 4\to 2$ is $+0.75$
(attracting) on the minimal canvas, $+4.28$ and $-1.88$ (repelling) on
others. The basin, the slivers, the stability itself: **paint**, not
pigment. What travels intact through every transfer is the conjugacy class
of $(\mathbb{N},T)$ — stopping times, phases, forbidden words, entropy
deficits. That is the colour.

Hence a conservation law:

> **Conservation of difficulty.** The conjecture is an invariant of the
> colour. No canvas can dissolve it; every "relaxing angle" merely moves it
> into the paint.

And a method:

> Canvases do not solve; they **compute**. Each canvas makes a different
> invariant of the colour legible — the drift becomes a multiplier on the
> harmonic canvas, the parity becomes a shift on the 2-adic canvas, the
> trajectory becomes a thickness on the basin canvas. Choose the canvas for
> the invariant you need to read, and never mistake the paint for the
> pigment.

---

# Part X — The Bell on the Diagonal

## Chapter 29 — A Gaussian Laid on the Diagonal

Every Gaussian bell we have ever drawn rests on the horizontal axis. Lay it
instead on the diagonal — slightly *below* the diagonal — and it becomes a
dynamical system:

$$
f(x) = x - \delta + A\,e^{-(x-c)^{2}/2\sigma^{2}},
\qquad A > \delta > 0,\quad c > 0.
$$

The graph is the line $y = x - \delta$, a copy of the diagonal shifted down
by $\delta$, with a Gaussian bump of height $A$ riding on it. Both tails run
**below the diagonal**, at the constant distance $\delta$. Only the dome
pierces it: on the interval where the bump exceeds $\delta$, the graph rises
above $y = x$. The peak sits at $x = c$ — not above zero, but a little to the
right.

The visible part of the bell — the **dome** peeking over the diagonal — is

$$
\{\,x : f(x) > x\,\} = (x_-,\ x_+),
\qquad
x_{\pm} = c \pm \sigma\sqrt{2\ln(A/\delta)}.
$$

In the language of Chapter 8 this is simply the positive region of the
fundamental difference $g(x) = f(x) - x = A\,e^{-(x-c)^{2}/2\sigma^{2}} - \delta$:
a Gaussian lowered by $\delta$, whose two zeros $x_{\pm}$ are the rims of the
dome. The claim of this Part is that the dome is the **attractor** — and that
the infinite application of $f$ is not a limit but an *oscillation upon it*.

Throughout we fix the concrete bell

$$
A = 3,\qquad \delta = 1,\qquad c = 1,\qquad \sigma = \tfrac{3}{5},
$$

so that $x_- \approx 0.1106$ and $x_+ \approx 1.8894$.

![The bell on the diagonal and its phase stripes](library/images/bell-on-diagonal.png)

## Chapter 30 — The Dome as a Trap

Off the dome the dynamics is a uniform drift. For $x$ far in either tail,

$$
f(x) \approx x - \delta:
$$

every application slides the point **left** by $\delta$. From the right tail
the orbit marches down the diagonal toward the dome. From the left of $x_-$
it marches away forever:

$$
f^{\infty}(x) = -\infty \qquad (x < x_-).
$$

The two rims are the fixed points, and both **repel** — but in opposite
styles. The multipliers are

$$
f'(x_{\pm}) = 1 \mp \frac{\delta}{\sigma}\sqrt{2\ln(A/\delta)},
$$

which for our bell gives

$$
f'(x_-) \approx +3.47, \qquad f'(x_+) \approx -1.47.
$$

The left rim repels by **amplification**: a positive multiplier greater than
$1$, pushing neighbours straight out — outward to the abyss, inward onto the
dome. The right rim repels by **reflection**: a multiplier less than $-1$,
which throws every neighbour to the *opposite side* of $x_+$ at each step.
Repulsion with a negative sign is the seed of oscillation.

And the orbit, once near the dome, can never leave it behind. Since
$f(x) \ge x - \delta$ everywhere, no application moves a point left by more
than $\delta$; and since

$$
\delta < x_+ - x_- ,
$$

no orbit can leap *over* the dome from right to left. On the dome itself
$f(x) > x \ge x_-$. Hence the half-line $[x_-, \infty)$ is **forward
invariant**: the wall at $x_-$ can be approached from the right but never
crossed. The dome is a trap — a point pushed right whenever it stands on the
dome, pulled left whenever it stands beyond it.

## Chapter 31 — The Oscillating Destiny

A point trapped at the right rim, thrown alternately on and off the dome,
must negotiate a compromise. The compromise is a **2-cycle**: solving
$f(f(x)) = x$ beside $x_+$ gives the pair

$$
a \approx 1.6014, \qquad b = f(a) \approx 2.4167, \qquad f(b) = a,
$$

astride the rim — $a$ *on* the dome, where the bell kicks the point up and
right; $b$ *off* it, where the drift pulls the point back down and left. Its
multiplier is

$$
f'(a)\,f'(b) \approx -0.555,
$$

of modulus less than one: the cycle **attracts**. Every orbit starting right
of the wall — except the countable scaffold of preimages of the two rims —
slides into this bounce. The cobweb in the figure shows the whole story: the
long staircase down the right tail, then the lock onto the rectangle
$a \to b \to a$.

Here the theory meets a destiny it has not seen since the Collatz tail. The
infinite application

$$
f^{\infty}
$$

is **not a function**. The even and odd iterates converge separately,

$$
\lim_{n\to\infty} f^{2n}(x) = E(x),
\qquad
\lim_{n\to\infty} f^{2n+1}(x) = f(E(x)),
$$

to *two* functions, each taking only the values $a$ and $b$, exchanged by one
further application of $f$. The infinite application of the bell is this
pair — a beat of period two, living on the rim of the dome:

> The destiny of the Gaussian laid on the diagonal is not a point, not a
> formula, but a **rhythm**: an oscillation upon the dome.

## Chapter 32 — The Field with One Wall

The destiny field of Chapter 25 reads, for the bell:

$$
\mathcal{A}_x(f) =
\begin{cases}
-\infty & x < x_-,\\[2pt]
\{x_-\} & x = x_-,\\[2pt]
\{a, b\} & x > x_-.
\end{cases}
$$

On the classification axis of Chapter 26 this field sits exactly between the
poles. It is not constant, like the cosine: it has a wall. It is not fractal,
like Collatz: it has *only* a wall — one discontinuity, two destinies, one
bit of information.

But look closer and the field acquires a finer grain. The limit function
$E(x)$ of the even iterates is a **step function**: the basin $(x_-,\infty)$
splits into countably many stripes, alternately assigned to $a$ and to $b$ —
the *phase* of the point, which of the two beats of the rhythm it lands on.
The stripe boundaries are the preimages of the reflecting rim $x_+$, and they
accumulate against the wall: approaching $x_-$ from the right, the stripes
thin without bound, the phase flickering faster and faster — a one-wall
miniature of the slivers of Chapter 26.

The bell thus completes a small taxonomy of destinies. The cosine forgets
everything. Collatz remembers everything. The bell on the diagonal remembers
exactly two things about its origin: *whether* the point beat the wall, and
*on which beat* it arrived.

---

# Part XI — The Bell on the Anti-Diagonal

## Chapter 33 — The Pendulum

Rotate the support. Lay the same bell on the **anti-diagonal** — slightly
below $y = -x$, the dome still poking through it:

$$
f(x) = -x - \delta + A\,e^{-(x-c)^{2}/2\sigma^{2}},
\qquad A > \delta > 0.
$$

The change of one sign changes everything. On the diagonal, the tails were a
*drift*: each application slid the point left by $\delta$. On the
anti-diagonal the tails are a **swing**: far from the dome,

$$
f(x) \approx -x - \delta,
\qquad
f(f(x)) \approx x,
$$

and the support map $x \mapsto -x-\delta$ is an **involution** — its square
is the identity. Every distant point is a neutral 2-cycle: the orbit flips
endlessly between $x$ and $-x-\delta$, a pendulum swinging across the whole
line, around the pivot $-\delta/2$. No escape, no convergence: pure suspended
oscillation. The bell does not create the rhythm here — the support line
already *is* a rhythm. What the dome adds is friction.

## Chapter 34 — Gaussian Friction

The second iterate measures what one full swing fails to undo:

$$
f^{2}(x) = x + A\left[
e^{-(f(x)-c)^{2}/2\sigma^{2}} - e^{-(x-c)^{2}/2\sigma^{2}}
\right].
$$

The bracket compares the bump felt at the two ends of the swing, and for our
bell ($A=3$, $\delta=1$, $\sigma=3/5$, $c>0$) its sign is fixed: the right
turning point drifts **down**, the left turning point drifts **up**. Each
pass over the dome steals a little amplitude. The pendulum is damped — the
dome is the only source of friction in the system.

But the friction is a Gaussian tail, and a Gaussian tail vanishes faster
than anything. The number of swings needed to shrink the amplitude by one
half-unit, measured ($c = 1.2$):

$$
\begin{aligned}
3 \to 2.5 &: \quad \sim 4 \text{ swings},\\
4 \to 3.5 &: \quad \sim 1.6 \times 10^{3},\\
5 \to 4.5 &: \quad \sim 1.1 \times 10^{7},\\
6 \to 5.5 &: \quad \sim 1.3 \times 10^{12},\\
10 \to 9.5 &: \quad \sim 4.7 \times 10^{44}.
\end{aligned}
$$

Here the theory meets a new phenomenon. The bell on the diagonal had a wall:
two destinies, divided in *space*. The bell on the anti-diagonal has **no
wall at all**: every orbit, started anywhere, is destined for the same
attractor. The destiny field is constant, like the cosine's. But the *time*
of destiny diverges doubly exponentially with the starting amplitude — at
machine precision a pendulum of amplitude $6$ is already indistinguishable
from an eternal one. The geography of destinies is trivial; their **calendar**
is not. Beside the field $x \mapsto \mathcal{A}_x(f)$ the theory must place a
second field,

$$
x \;\longmapsto\; T_x(f),
$$

the time each point needs to reach its fate. The cosine compresses both
fields to nothing. The bell on the anti-diagonal compresses the *where* and
leaves the *when* incompressible.

![The bell on the anti-diagonal: damped pendulum and chaotic bounce](library/images/bell-on-antidiagonal.png)

## Chapter 35 — Where the Diagonal Cuts

And what is the fate, once the pendulum has spent its amplitude? Fixed
points obey $f(x) = x$, that is

$$
A\,e^{-(x-c)^{2}/2\sigma^{2}} = 2x + \delta:
$$

the destination is decided not by the line the bell **rests on**, but by
where it meets the line it **faces** — the main diagonal, which cuts across
the bell transversally. Three regimes, governed by the position of the peak
against the critical height $c^{*} = (A-\delta)/2$:

**The diagonal cuts the left tail** ($c > c^{*}$; we measure $c = 1.2$).
One fixed point, far from the dome, down on the tail:

$$
x_{*} \approx -0.4686, \qquad f'(x_{*}) \approx -0.709.
$$

A negative multiplier of modulus less than one: the pendulum spirals onto
$x_{*}$, overshooting alternately left and right, the swing decaying
geometrically at the end of its doubly-exponential approach. The destiny is
a **point** — and, for the first time in these notes, the dome is not where
the orbit ends. It is only the *engine*: the friction that made the ending
possible. The attractor and the mechanism have come apart.

**The diagonal grazes the peak** ($c = c^{*}$; here exactly $c = 1$, since
$A = 2c + \delta$). The peak itself is the fixed point, and its multiplier
is exactly

$$
f'(c) = -1:
$$

the knife edge of neutrality, where the spiral neither contracts nor
escapes.

**The diagonal cuts the dome's flank** ($c < c^{*}$; we measure $c = 0.8$).
The fixed point now sits on the falling flank of the dome,

$$
x_{*} \approx 0.952, \qquad f'(x_{*}) \approx -2.23,
$$

and the reflection is too violent to negotiate the compromise of
Chapter 31. No 2-cycle catches the orbit: it bounces on the dome **forever
and without period** — Lyapunov exponent $\approx 0.51$, trajectories
confined to the band $[-0.03,\ 1.26]$ inside the dome, never repeating. The
destiny is a **chaotic oscillation upon the dome**: the strange attractor of
Chapter 2, finally exhibited by the simplest bell.

One bell, two support lines, and the whole taxonomy of Part I returns: on
the diagonal, a wall and a rhythm; on the anti-diagonal, no wall — and a
destiny that is a point, a knife edge, or chaos, according to where the
*other* diagonal cuts the bell.

> Rotate the support of a function and its destiny migrates: from geography
> to calendar, from the dome to the tail, from rhythm to noise.

---

# Part XII — The Infinite Functions

## Chapter 36 — The Forgotten Road

Two sciences have been mixed in these notes, and the time has come to
separate them.

There is the science of the **road**: spirals, multipliers, basins, walls,
Gaussian friction, the calendar of convergence. Parts X and XI belong to it.
And there is the science of the **destination**: the object $f^{\infty}$
itself. The two must not be confused, because the infinite application is
precisely the operator that destroys the first to produce the second.

Consider the cosine. The road is rich: orbits that overshoot alternately
left and right, a multiplier of $-0.674$, a spiral tightening forever. But
$\cos^{\infty}$ retains none of it. It is

$$
\cos^{\infty}(x) = 0.739085\ldots \qquad \text{for every } x
$$

— **a constant function**. Not a dynamics of collapse, not a process seen
from afar: a static, total, completed object, defined at every point,
containing no spiral whatsoever. The Chapter 23 principle, taken at last to
its conclusion: the attractor was said to *remember the destination and
forget the road* — then the honest notation must forget it too.

So the word **attractor** is road-language, and applying it to the final
object is a category error. The Dottie number is not an attractor. It is the
*value of the constant function* $\cos^{\infty}$ — a **constant of
mathematics**, with the same citizenship as $e$ and $\pi$. And the
comparison is not a metaphor, because the classical constants have the same
birth certificate:

$$
e = \lim_{n\to\infty}\left(1+\frac{1}{n}\right)^{n}
$$

is the frozen destiny of compound interest; $\pi$ is the frozen destiny of
Archimedes' doubling polygons. Every constant of mathematics is the residue
left on the bottom when an infinite process evaporates.

> **A constant is a destiny whose road has been forgotten.**
>
> The Dottie number is not less of a constant than $e$. It is only younger.

## Chapter 37 — The Normalized Space of Destinies

To study destinations and nothing else, we need a space where *all* of them
fit — including the infinite ones. Normalize the line onto a finite
interval,

$$
h(x) = \frac{2}{\pi}\arctan(x), \qquad h : \overline{\mathbb{R}} \to [-1, 1],
$$

so that

$$
+\infty \mapsto 1, \qquad -\infty \mapsto -1.
$$

In this space **escape is no longer a separate kind of fate**. The orbit
that fled to $-\infty$ on the left of the wall now converges — to the
boundary constant $-1$. Divergence becomes convergence to the edge. The
three destinies that seemed different in the open line — $-\infty$,
$+\infty$, a finite value $c$ — collapse into one: *destiny with a single
value*.

And the normalization pays immediately. It predicts a destiny the open line
hides: the map $x \mapsto -2x$ flips sign at every step with growing
modulus — in $[-1,1]$ its orbit settles onto the pair $\{-1, +1\}$, an
**oscillation between the two infinities**. A 2-cycle whose two beats are
the edges of the world. No list of destinies drawn up in the open line would
have contained it.

## Chapter 38 — The Four Destinies

In the normalized space, the destiny of a point is the set of values its
orbit keeps visiting forever. And here the theory meets a theorem — a
classical result of one-dimensional dynamics (the school of Sharkovskii):
for a continuous map of a compact interval, this set can be **only one of
four things**:

$$
\begin{array}{ll}
\textbf{1. a point} & \text{the constant destiny (including the edges } \pm 1\text{)},\\[2pt]
\textbf{2. a finite array} & \text{the oscillation — } k \text{ values in cyclic exchange},\\[2pt]
\textbf{3. a dust} & \text{infinitely many values, nowhere dense, visited in rigid order},\\[2pt]
\textbf{4. a band} & \text{a finite union of intervals — the continuous array: chaos.}
\end{array}
$$

Nothing else. Not a hope, not a taxonomy proposed: a closed list.

The deepest of the four is the second, because it marks a frontier of
*logic*, not of geometry. The function $f$ is single-valued; its infinite
composite need not be. The oscillation is exactly **the threshold where
$f^{\infty}$ ceases to be a function and becomes multivalued** — an array
of $k$ values where one value was expected. The four destinies are then the
four ranks of the multifunction $f^{\infty}$: rank one (a function — indeed
a constant function), rank $k$ (a finite array), rank infinity in two
species (dust and band).

The bells have already exhibited three of the four ranks, measured:

$$
\begin{array}{lll}
\text{rank } 1: & \cos^{\infty} = 0.739\ldots; \quad \text{anti-diagonal bell, } c=1.2 & (x_* \approx -0.4686)\\[2pt]
\text{rank } 2: & \text{diagonal bell} & (\{a, b\} \approx \{1.60,\ 2.42\})\\[2pt]
\text{rank } 3: & \text{Collatz} & (\{1, 4, 2\})\\[2pt]
\text{rank } \infty \text{ (band)}: & \text{anti-diagonal bell, } c=0.8 & ([-0.03,\ 1.26])
\end{array}
$$

One destiny is still missing from our collection: the **dust** — the
infinite oscillation that never repeats and never spreads into a band. The
classification guarantees its existence; no bell of ours has yet produced
it. It is the empty box of the table, and the next hunt.

A last accounting, of what survives the compression. At rank one the
dynamics evaporates totally: there remains a number, a constant, a new
citizen beside $e$. At rank $k$ exactly one memory survives: the integer
$k$, the rhythm — the only property of the road that becomes a property of
the object. At rank infinity the order of visiting survives. The infinite
application loses less and less, until — in chaos — it stops compressing
at all.

## Chapter 39 — The New Family

Now the mission of these notes can be stated without metaphor.

Mathematics has, a handful of times, admitted a new family of functions
into its foundations: the polynomials; then $\log$ and $\exp$; then
$\sin$ and $\cos$; then the special functions of analysis. Each admission
redrew what could be expressed.

This theory proposes the next family: the **infinite functions**

$$
F = f^{\infty},
$$

the destinies of all generators $f$ — constant functions carrying new
constants, finite arrays carrying rhythms, dusts and bands carrying the
two infinities. They form a closed world of exactly four kinds, living in
the normalized space $[-1,1]$, with their own equivalence (Chapter 4),
their own inverse problem (Chapter 6: which $f$ generates a given $F$?),
their own arithmetic still to be built.

And the dynamics — the spirals, the multipliers, the walls, the friction,
the calendars, everything Parts X and XI measured with such care? It is
**the bridge**. One bank is classical mathematics, where functions are
formulas. The other bank is the new base, where functions are destinies.
The roads are how one walks across; they are indispensable, and they are
not the destination. The theory studies them as the engineer studies the
scaffolding: rigorously, and in order to remove it.

> The mission is not to describe how orbits move.
>
> The mission is to found the family of infinite functions — the
> destinies — and to hand mathematics a new set of primitives, as it was
> once handed the logarithm.
>
> Process is the bridge. Destiny is the base.

---

## Epilogue

Traditional mathematics studies

$$
f.
$$

The theory of infinite applications studies

$$
f^{\infty}.
$$

Traditional mathematics asks:

> What is a function?

This theory asks:

> What does a function *become* after infinitely many applications?

and, more deeply still:

> Is the object we observe the function — or its asymptotic shadow?