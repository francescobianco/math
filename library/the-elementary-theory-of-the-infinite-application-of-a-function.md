---
title: The Elementary Theory of the Infinite Application of a Function
type: book
created: 2026-06-03T09:00:00+00:00
updated: 2026-06-11T01:30:00+00:00
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