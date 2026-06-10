va ---
title: The Phases of Collatz
type: paper
created: 2026-06-10T21:30:00+00:00
updated: 2026-06-11T00:30:00+00:00
---

# The Phases of Collatz

*An exact calculus of synchronization toward the terminal oscillator, with
verified transport laws, measured phase statistics, and the precise cost of a
closed phase formula.*

## Abstract

Every Collatz trajectory that reaches the terminal cycle

$$
1 \to 4 \to 2 \to 1
$$

ends up oscillating with period three. Each integer $n$ therefore arrives at
the oscillator with a definite **phase**: the residue, modulo three, of the
time it takes to get there. This paper makes the phase structure explicit. It
defines the phase $\phi(n)$, gives the fundamental wave of the cycle in closed
harmonic form, establishes an exact **phase transport calculus** (a set of
identities, each verified computationally on at least $2\times 10^5$ cases,
that propagate the phase through the Collatz tree), measures the statistical
laws of the phase (global uniformity, local rigidity), constructs an explicit
**phase compensator** that synchronizes all integers onto a single wave, and
states precisely what a closed formula for the phase would cost: the phase
function is total if and only if the Collatz conjecture is true.

Throughout, $T$ denotes the Collatz map

$$
T(n) =
\begin{cases}
n/2 & n \text{ even},\\[2pt]
3n+1 & n \text{ odd},
\end{cases}
$$

and $\sigma(n)$ denotes the total stopping time: the number of applications of
$T$ needed to reach $1$ (so $\sigma(1)=0$, $\sigma(2)=1$, $\sigma(4)=2$).

## The Phase of an Integer

Once a trajectory reaches $1$, it cycles forever:

$$
1,\ 4,\ 2,\ 1,\ 4,\ 2,\ \ldots
$$

Let $w$ be the periodic sequence with $w(0)=1$, $w(1)=4$, $w(2)=2$ and
$w(t+3)=w(t)$. If $n$ reaches $1$ at time $\sigma(n)$, then for **all** later
times

$$
T^{t}(n)=w\bigl(t-\sigma(n)\bigr), \qquad t\ge \sigma(n).
$$

Two remarks. First, the residue of the trajectory relative to the wave is not
merely vanishing in the limit: it is **exactly zero after finite time**. The
locking onto the oscillator is finite-time, which is stronger than the
asymptotic hypothesis $\varepsilon(t)\to 0$ proposed in the companion survey.
Second, the only memory of $n$ that survives in the eternal oscillation is the
residue class

$$
\phi(n)=\sigma(n) \bmod 3,
$$

which we call the **phase** of $n$. Two integers $a$ and $b$ are
**synchronized** (in phase) when

$$
\phi(a)=\phi(b);
$$

otherwise they are out of phase by $1$ or by $2$. Synchronized integers,
launched at the same instant, eventually beat on the cycle in perfect unison;
integers out of phase by $k$ beat with a lag of $k$ ticks forever.

Since $\sigma(n)$ is exactly the depth of $n$ in the inverse Collatz tree
rooted at $1$, the synchronization classes have a clean combinatorial meaning:

> The phase classes are the levels of the Collatz tree taken modulo three.

The first values:

| $n$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $\sigma(n)$ | $0$ | $1$ | $7$ | $2$ | $5$ | $8$ | $16$ | $3$ | $19$ | $6$ |
| $\phi(n)$ | $0$ | $1$ | $1$ | $2$ | $2$ | $2$ | $1$ | $0$ | $1$ | $0$ |

## The Fundamental Wave in Closed Form

The wave $w$ is a function on three points, so it is exactly representable by
a finite Fourier sum — one constant plus one harmonic:

$$
w(t)=\frac{7}{3}
-\frac{4}{3}\cos\!\left(\frac{2\pi t}{3}\right)
+\frac{2\sqrt{3}}{3}\sin\!\left(\frac{2\pi t}{3}\right).
$$

One checks directly that $w(0)=1$, $w(1)=4$, $w(2)=2$ (verified numerically to
machine precision). In amplitude–phase form,

$$
w(t)=\frac{7}{3}+\frac{2\sqrt{7}}{3}
\cos\!\left(\frac{2\pi t}{3}+\psi\right),
\qquad
\psi=\pi+\arctan\frac{\sqrt{3}}{2}.
$$

The mean value of the Collatz oscillator is $7/3$ and its amplitude is
$2\sqrt{7}/3$. Every trajectory of every integer ends, verbatim, as a shifted
copy $w(t-\sigma(n))$ of this single harmonic.

## The Phase Transport Calculus

The phase is unknown in general, but it **transports exactly** along the
arithmetic of the tree. Each law below has a one-line proof and has been
verified by direct computation on all applicable $n$ up to $2\times 10^5$ (and
the statistical laws on $10^6$).

**Law 1 (step law).** One application of $T$ retards the phase by one:

$$
\phi(T(n))=\phi(n)-1 \pmod 3 .
$$

*Proof:* $\sigma(T(n))=\sigma(n)-1$. In particular

$$
\phi(2n)=\phi(n)+1,
\qquad
\phi\!\left(\frac{3n+1}{2}\right)=\phi(n)+1 \quad (n \text{ odd}),
$$

the latter because an odd step followed by the forced halving consumes two
ticks, and $-2\equiv 1 \pmod 3$.

**Law 2 (octave law).** Multiplication by $8$ is phase-transparent:

$$
\phi(8n)=\phi(n).
$$

*Proof:* three halvings. Consequently the registers $n$, $2n$, $4n$ realize
all three phases, and each class $\{2^{3k}m\}_{k\ge 0}$ is fully synchronized:
$n,\ 8n,\ 64n,\ 512n,\ \ldots$ all beat together.

**Law 3 (the $4n+1$ law).** For odd $n$,

$$
\phi(4n+1)=\phi(n)+2.
$$

*Proof:* $4n+1 \to 12n+4 \to 6n+2 \to 3n+1$ takes three steps to the point
that $n$ reaches in one step, so $\sigma(4n+1)=\sigma(n)+2$.

**Law 4 (coalescence law).** For every $k\ge 1$,

$$
\sigma(8k+4)=\sigma(8k+5),
$$

so the consecutive integers $8k+4$ and $8k+5$ are not merely synchronized —
they have *identical* stopping times. *Proof:* both trajectories meet at
$6k+4$ in exactly three steps:

$$
8k+4 \to 4k+2 \to 2k+1 \to 6k+4,
\qquad
8k+5 \to 24k+16 \to 12k+8 \to 6k+4.
$$

This gives an infinite arithmetic progression of synchronized consecutive
pairs: $(12,13),\ (20,21),\ (28,29),\ \ldots$

**Law 5 (predecessor law).** The predecessors of $m$ in the tree — namely
$2m$ always, and $(m-1)/3$ when $m\equiv 4 \pmod 6$ — share the same phase
$\phi(m)+1$. Sibling branches of the tree are born synchronized.

The calculus is closed under composition: any path through the tree has a
phase shift computable by summing the laws, without knowing any stopping time
along the way. What the calculus transports is *differences* of phase; what it
cannot produce is the *absolute* phase of a single integer. That asymmetry is
quantified in the closed-formula section below.

## The Statistical Laws of the Phase

Two empirical laws emerge from exhaustive computation on $n\le 10^6$.

**Global uniformity.** The three phases are equidistributed,

| phase $0$ | phase $1$ | phase $2$ |
|---:|---:|---:|
| $33.286\%$ | $33.331\%$ | $33.383\%$ |

and the phase is statistically independent of $n \bmod 3$ (all nine joint
cells lie within $0.05$ points of $1/9$). The phase carries no congruential
information: no congruence class of $n$ predicts it.

**Local rigidity.** Globally uniform does not mean locally random. The
probability that $n$ and $n+d$ are synchronized decays slowly from far above
chance:

| gap $d$ | $1$ | $2$ | $3$ | $4$ | $8$ | $16$ | $100$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| $P(\phi(n)=\phi(n+d))$ | $0.622$ | $0.551$ | $0.481$ | $0.503$ | $0.468$ | $0.440$ | $0.375$ |

with chance level $1/3$. At distance $1$ the lag distribution is

$$
P(\Delta\phi=0)=62.2\%,\qquad
P(\Delta\phi=1)=18.9\%,\qquad
P(\Delta\phi=2)=18.9\%,
$$

and fully $47.7\%$ of consecutive pairs have *exactly equal* stopping times.
The mechanism is coalescence: trajectories of nearby integers merge after few
steps (Law 4 is the simplest instance), and merged trajectories are
synchronized forever after if they merged at equal times. The picture is that
of a **locally rigid, globally uniform** field of phases: stiff at short
range, structureless at long range.

## The Cost of a Closed Phase Formula

Is there a closed formula deciding whether $a$ and $b$ are in phase? The
question has an exact price.

Write the trajectory of $n$ as $b$ odd steps and $a$ halvings, with
$\sigma(n)=a+b$, and let $n_1,\dots,n_b$ be the odd values visited. Telescoping
the trajectory gives the standard exact identity

$$
2^{a}=3^{b}\, n \prod_{i=1}^{b}\left(1+\frac{1}{3n_i}\right),
$$

hence

$$
\sigma(n)=\bigl(1+\log_2 3\bigr)\,b(n)+\log_2 n+\delta(n),
\qquad
\delta(n)=\log_2\prod_{i=1}^{b}\left(1+\frac{1}{3n_i}\right).
$$

The phase is therefore an exact function of the odd-step count $b(n)$ and of
the correction $\delta(n)$ — but both are defined through the trajectory
itself. No closed form is known for either, and the following observation
shows this is not an accident of technique.

**The totality obstruction.** The function $\phi$ is defined at $n$ exactly
when $\sigma(n)$ is finite, that is, exactly when $n$ reaches the cycle. Hence

> the phase function is total on $\mathbb{N}$ **if and only if** the Collatz
> conjecture is true.

A closed formula for $\phi$, together with a proof that it is defined for
every $n$, *is* a proof of the conjecture. The phase formula problem does not
approximate the conjecture; it contains it.

The obstruction has a clean dynamical form. Let $\omega=e^{2\pi i/3}$ and

$$
Z(n)=\omega^{\sigma(n)}.
$$

Then Law 1 reads

$$
Z(T(n))=\omega^{-1}\,Z(n):
$$

the phase is an **eigenfunction of the Koopman operator** of the Collatz map,
with eigenvalue $e^{-2\pi i/3}$. Finding the closed phase formula means
exhibiting this eigenfunction in closed form on all of $\mathbb{N}$ — a
spectral reformulation of the conjecture, not a shortcut around it.

### What "No Closed Formula" Does and Does Not Mean

A logical caution is in order, because the obstruction above is easily
over-read. The phase is **predictable** in the algorithmic sense: iterate $T$
and count — nothing more is needed. What is missing is **compression**:
evaluating $\phi(n)$ *without travelling the trajectory*. And "closed form"
is not an absolute notion; it is relative to a class of allowed expressions.
The classes form a ladder, and this paper locates the frontier on it exactly.

**Rung 1 — residue formulas** $\phi(n)=F(n \bmod m)$: impossible, by the
one-line theorem of the periodicity section (the residue $0$ alone would need
three values).

**Rung 2 — finite-state formulas** (automatic sequences: $\phi$ computed by a
finite automaton reading the digits of $n$; this rung contains every
eventually periodic rule and every digit-pattern rule): excluded empirically
with a wide margin. An automatic sequence has subword complexity at most
linear, $p(L)\le C\,L$, where $p(L)$ counts the distinct blocks of length $L$
occurring in the sequence. The measured complexity of the phase word
$\phi(1)\phi(2)\phi(3)\cdots$ on $n<2^{22}$ is exponential:

| $L$ | $4$ | $5$ | $6$ | $8$ | $10$ | $12$ | $14$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| $p(L)$ | $81$ | $243$ | $657$ | $4173$ | $23018$ | $108029$ | $336443$ |
| $3^L$ | $81$ | $243$ | $729$ | $6561$ | $59049$ | $531441$ | $4782969$ |

Every possible block occurs up to length $5$; the first forbidden words
appear at length $6$ ($72$ of the $729$ blocks never occur in four million
samples — the local rigidity laws forbid them); thereafter the language grows
by a factor $\approx 2.2$–$2.4$ per symbol. Positive entropy, far beyond any
finite-state device, yet strictly below the full shift: the phase language is
neither regular nor free.

**Rung 3 — elementary and analytic closed forms**: here nothing is deduced,
in either direction. The nonexistence of such a formula is **not** a
consequence of anything in this paper, and proving an impossibility theorem
at this rung is beyond current technique for any natural Collatz quantity.
The frontier of knowledge runs between rungs 2 and 3.

**Rung 4 — computable expressions**: existence is trivial modulo the
conjecture, e.g.

$$
\sigma(n)=\sum_{t=0}^{\infty}\mathbf{1}\bigl[T^{t}(n)\neq 1\bigr],
$$

a perfectly well-formed expression — which is the road itself, written as a
sum. It compresses nothing.

The licensed deduction is therefore conditional, not existential: **a formula
at any rung, together with a proof of its totality, proves the conjecture.**
The phase is predictable but, as far as anyone knows, incompressible — and
"as far as anyone knows" is a statement about proofs we lack, not a theorem
we own.

## Phase Compensation: the Synchronized Collatz

Although the absolute phase is conjecture-hard, *compensating* it is easy once
$\sigma(n)$ is computable, and the compensated system is exactly what the
title of this section promises: a Collatz dynamics in which **all integers
have the same phase**.

Define the compensating delay

$$
c(n)=\bigl(-\sigma(n)\bigr) \bmod 3 \in \{0,1,2\},
$$

so that $\sigma(n)+c(n)\equiv 0 \pmod 3$ for every $n$ (verified). For
integer arguments the residue can itself be written harmonically,

$$
m \bmod 3
=1+\frac{2}{\sqrt{3}}\sin\!\left(\frac{2\pi (m-1)}{3}\right),
$$

so the compensator is one sine away from the stopping time:

$$
c(n)=1+\frac{2}{\sqrt{3}}
\sin\!\left(\frac{2\pi\,(-\sigma(n)-1)}{3}\right).
$$

Now launch each integer with its own delay: hold the value $n$ for $c(n)$
ticks, then iterate,

$$
\tilde{x}_n(t)=
\begin{cases}
n & 0\le t< c(n),\\[2pt]
T^{\,t-c(n)}(n) & t\ge c(n).
\end{cases}
$$

Then every compensated trajectory reaches $1$ at a time divisible by three,
and therefore, for all $t\ge \sigma(n)+c(n)$,

$$
\tilde{x}_n(t)=w(t).
$$

Not approximately: identically. After a finite transient, **every integer
rides the same wave**

$$
w(t)=\frac{7}{3}
-\frac{4}{3}\cos\!\left(\frac{2\pi t}{3}\right)
+\frac{2\sqrt{3}}{3}\sin\!\left(\frac{2\pi t}{3}\right),
$$

with residue $\tilde{x}_n(t)-w(t)$ of finite support. The whole of
$\mathbb{N}$ becomes a single synchronized oscillator with individual
finite-length transients.

One honest impossibility result delimits the construction. The phase
$\phi(n)$ is determined by the integer orbit alone, so it **cannot be altered
by any modification of the harmonic interpolation off the integers**: no
choice of continuous extension $f(x)=\frac{7x+2}{4}-\frac{5x+2}{4}\cos(\pi x)
+ (\text{anything vanishing on }\mathbb{Z})$ changes a single phase. Phase
compensation must act on *time* (delays, as above) or on *initial conditions*
— never on the map. A "phase-compensating harmonic Collatz function" exists,
but it is a time reparametrization, not a new map; and its formula requires
$\sigma(n)$, which is the conjecture's own currency.

## Splitting the Phases: Primitives in Superposition

The three phase classes

$$
\Phi_k=\{n\in\mathbb{N}:\phi(n)=k\},
\qquad k=0,1,2,
$$

can be split off exactly by superposing three **phase primitives**. Let
$\omega=e^{2\pi i/3}$ and recall the Koopman eigenfunction
$Z(n)=\omega^{\sigma(n)}$. The primitives are the powers

$$
Z^0=1,\qquad Z,\qquad Z^2=\bar{Z},
$$

and the indicator of each class is their discrete Fourier superposition over
$\mathbb{Z}/3$:

$$
\mathbf{1}_{\Phi_k}(n)
=\frac{1}{3}\sum_{j=0}^{2}\omega^{-jk}\,Z(n)^{j}
=\frac{1}{3}
+\frac{2}{3}\cos\!\left(\frac{2\pi\bigl(\sigma(n)-k\bigr)}{3}\right).
$$

The check is immediate: the cosine equals $1$ when $\sigma(n)\equiv k$ and
$-1/2$ otherwise, giving exactly $1$ and $0$. The three **phase waves**

$$
P_k(n)=\frac{1}{3}
+\frac{2}{3}\cos\!\left(\frac{2\pi(\sigma(n)-k)}{3}\right)
$$

form a partition of unity, $P_0+P_1+P_2=1$, and they are *one single wave
read at three shifts*: each class is the uniform background $1/3$ plus the
same oscillation $\tfrac{2}{3}\cos(2\pi\sigma/3)$ sampled at offset $k$. The
splitting of the phases is therefore entirely carried by the one primitive
$Z$; the background $1/3$ is exactly the long-range uniform density measured
earlier.

The transport calculus now becomes a group action. Doubling multiplies the
primitive by $\omega$,

$$
Z(2n)=\omega\,Z(n),
$$

and the $4n+1$ law multiplies it by $\omega^{2}$,

$$
Z(4n+1)=\omega^{2}\,Z(n) \qquad (n\ \text{odd}).
$$

The two elementary tree moves thus realize, by explicit arithmetic maps, the
full cyclic group $\mathbb{Z}/3$ acting on the phase splitting: $n\mapsto 2n$
rotates the three classes one notch forward, $n\mapsto 4n+1$ one notch
backward.

## The Periodicity of the Distinct Phases

Where does the phase partition repeat? The answer, verified both exactly and
statistically, is: **never along $n$, exactly along scale**.

### No translational period

Along the integer line the phases admit no period and no drift. The lag
distribution is symmetric at every tested gap (computed on $n<2^{22}$):

$$
P(\Delta\phi=1)\approx P(\Delta\phi=2)
$$

to four decimal places at gaps $1,2,3,5,7$ — the correlation between
neighbours decays without any directional bias — and no congruence class of
$n$ predicts the phase (the joint distribution with $n\bmod 3$ is uniform to
$0.05$ points). In fact, congruential prediction is impossible by a one-line
theorem, not merely by measurement.

**Theorem (no congruence formula).** For no modulus $m$ is the phase a
function of $n \bmod m$ — not even allowing finitely many exceptions.
*Proof:* the multiples $m, 2m, 4m, 8m, \ldots$ are all congruent to $0$
modulo $m$, yet by the step law their phases

$$
\phi(m),\ \phi(m)+1,\ \phi(m)+2,\ \phi(m),\ \ldots
$$

cycle through all three values, each infinitely often. A function of the
residue would have to take three different values at the single residue $0$.
$\square$

A translational period $p$ would make $\phi$ a function of $n \bmod p$; hence
no translational period exists, for any modulus — a theorem, not a
measurement.

### Exact dyadic period: three octaves

The step law $\phi(2n)=\phi(n)+1$ says that the doubling map **permutes the
three classes cyclically**:

$$
2\,\Phi_k=\Phi_{k+1}\cap 2\mathbb{N},
\qquad
8\,\Phi_k=\Phi_k\cap 8\mathbb{N}.
$$

Each class is invariant under multiplication by $8$ and the three classes are
exchanged by the cycle $(0\,1\,2)$ under multiplication by $2$. The phase
partition is therefore **log-periodic**: periodic in the variable $\log_2 n$
with period exactly $3$. Every geometric ray

$$
n,\ 8n,\ 64n,\ 512n,\ \ldots
$$

is mono-phase, and the rays of ratio $2$ step through the phases in strict
rotation. The periodicity of the distinct phases is a periodicity of *scale*,
not of *position*: the natural axis of the phase field is the octave, not the
integer line.

### Octave spectroscopy

The exact rotation law constrains only the dyadic rays; whether the rotation
is visible in the *bulk* statistics is an empirical question. Define the mean
phase vector of each octave,

$$
M_j=\frac{1}{2^{j}}\sum_{2^{j}\le n<2^{j+1}}Z(n).
$$

If the classes were perfectly balanced in every octave, $M_j$ would vanish;
if the doubling rotation acts coherently on the bulk, $M_j$ should rotate by
one unit of $2\pi/3$ per octave. The measurement on $n<2^{22}$ gives, for the
argument of $M_j$ in units of $2\pi/3$:

| $j$ | $4$ | $5$ | $6$ | $7$ | $8$ | $14$ | $15$ | $16$ | $20$ | $21$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $\lvert M_j\rvert$ | $0.225$ | $0.219$ | $0.154$ | $0.087$ | $0.045$ | $0.011$ | $0.010$ | $0.010$ | $0.006$ | $0.004$ |
| $\arg M_j$ | $+0.38$ | $+1.50$ | $-0.37$ | $+0.93$ | $-0.96$ | $+0.22$ | $+1.30$ | $-0.55$ | $+0.68$ | $-1.31$ |

The octave-to-octave rotation $\arg M_{j+1}-\arg M_j \pmod 3$ across all
seventeen consecutive pairs is

$$
1.12,\ 1.13,\ 1.30,\ 1.11,\ 1.11,\ 1.07,\ (2.09),\ 0.96,\ 0.90,\
1.06,\ 1.08,\ 1.15,\ 1.13,\ 1.02,\ 1.03,\ 1.05,\ 1.01,
$$

with mean $\approx 1.08$ excluding the single outlier, which occurs exactly
where $\lvert M\rvert\approx 0.006$ falls to noise level. The prediction is
confirmed: **each doubling rotates the collective phase vector by one notch**.
The mechanism is transparent — the even half of octave $j+1$ is the doubled
copy of octave $j$ and contributes $\tfrac{1}{2}\omega M_j$ exactly; the
measurement shows that the odd half does not destroy the rotation.

Two refinements complete the picture honestly. The magnitude $\lvert M_j\rvert$
decays with scale (from $0.225$ at $j=4$ to $0.004$ at $j=21$): the rotation
is coherent but the *polarization* of the octaves washes out as $n$ grows —
the bulk drifts toward perfect three-way balance, consistent with the global
uniformity law. And the correlation of $Z(n)$ with the continuous
log-periodic carrier $e^{2\pi i\log_2(n)/3}$ is $\approx 0.0008$: the field
is rotation-covariant octave by octave, but it is *not* phase-locked to a
continuous wave in $\log_2 n$. The dyadic rotation is a symmetry of the
partition, not a melody one can hum along the real line.

## The Continuous Phase: the Basin Program

The deepest objection to induction on Collatz is that trajectories jump out
of range: no local, contained, expandable theory survives the excursion of
$27$ to $9232$. The phase, by contrast, lives in a *finite* space — three
values — which suggests a program: find a continuous function covering the
phase function, and run the inverse Collatz expansively on the continuum,
hoping to show that the expansion swallows all of $\mathbb{N}$. This section
makes the program rigorous, proves the part of it that is true, measures the
part of it that is hard, and locates exactly where the difficulty resurfaces.

### The Oscillator Is Attracting

Work with the harmonic interpolation

$$
f(x)=\frac{7x+2}{4}-\frac{5x+2}{4}\cos(\pi x),
$$

which restricts to $T$ on the integers. Its derivative at integer points is
strikingly simple: the sine term vanishes and

$$
f'(n)=\frac{7}{4}-\frac{5}{4}\cos(\pi n)
=\begin{cases}
1/2 & n \text{ even},\\[2pt]
3 & n \text{ odd}.
\end{cases}
$$

Hence the cycle $1\to 4\to 2$ has multiplier

$$
f'(1)\,f'(4)\,f'(2)=3\cdot\frac{1}{2}\cdot\frac{1}{2}=\frac{3}{4}<1:
$$

**the terminal oscillator is an attracting cycle of the continuous Collatz
map**, and its attraction rate $3/4$ is the classical statistical drift of
the conjecture, appearing here not as a heuristic but as a literal
eigenvalue.

The same computation yields a curious corollary: a hypothetical integer
cycle with $a$ odd and $b$ even steps would have multiplier $3^{a}/2^{b}$,
and the exact cycle identity forces $3^{a}/2^{b}=1/\prod(1+\tfrac{1}{3n_i})<1$.
*Every* integer cycle of the Collatz map — including any undiscovered one —
is automatically attracting in the harmonic extension.

### The Continuous Phase Exists — on the Basin

Let $B$ be the basin of attraction of the cycle: the open set of reals whose
$f$-orbit converges to $\{1,4,2\}$. Because the cycle has period three, $B$
decomposes into three disjoint open pieces $B_0, B_1, B_2$ — the points
whose orbit tracks $1$ at times $\equiv 0, 1, 2 \pmod 3$ — and $f$ permutes
them cyclically. The function

$$
F:B\to\{0,1,2\},
\qquad
F\equiv k \text{ on } B_k,
$$

is locally constant, hence continuous, and satisfies the eigenfunction law
$F(f(x))=F(x)-1 \bmod 3$. For an integer $n$ in the Collatz tree the orbit
hits $1$ exactly at time $\sigma(n)$, so

$$
F(n)=\phi(n):
$$

**the continuous covering of the phase function exists**, canonically, on
the basin. Moreover every tree integer is an *interior* point of $B$ (its
finite orbit reaches the attracting cycle, and continuity propagates a
neighbourhood along it). The program is therefore well-posed, and the
conjecture acquires a clean geometric form:

> **Collatz $\iff$ $\mathbb{N}\subset B$.**

The expansive construction is the basin's own definition from below: if $U$
is a small neighbourhood of the cycle, then

$$
B=\bigcup_{k\ge 0} f^{-k}(U)
$$

— the continuous inverse Collatz, pulling the seed backward through all
preimages. The conjecture says this expansion eventually captures a
neighbourhood of every integer.

### Reconnaissance: the Measured Geometry of $B$

Numerical exploration (verified, script-level) gives the program its honest
contours.

*Continuity at the integers.* For $2\le n\le 30$, the points $n\pm 10^{-6}$
converge to the cycle with phase exactly $\phi(n)$ — with one instructive
exception: $27+10^{-6}$ **escapes to infinity**, and $27$ requires
$\varepsilon=10^{-8}$. The integer with the famous excursion is interior to
$B$, but barely.

*The pinching law.* The local basin radius $r(n)$ — the largest verified
$\varepsilon$ with $n\pm\varepsilon\subset B$ at phase $\phi(n)$ — collapses
with the trajectory peak $M(n)$:

| $n$ | $3$ | $6$ | $7$ | $9$ | $16$ | $27$ | $31$ | $41$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $M(n)$ | $16$ | $16$ | $52$ | $52$ | $16$ | $9232$ | $9232$ | $9232$ |
| $r(n)$ | $3{\cdot}10^{-4}$ | $10^{-3}$ | $10^{-4}$ | $10^{-4}$ | $3{\cdot}10^{-3}$ | $10^{-8}$ | $10^{-8}$ | $10^{-8}$ |

The data fit a quantitative law. Linearizing along the orbit, a perturbation
$\varepsilon$ at $n$ is amplified to roughly $(M/n)\,\varepsilon$ at the
peak, while the nonlinearity of the cosine tolerates only
$\delta\lesssim 1/(\pi^{2}M)$ there; solving for $\varepsilon$ gives

$$
r(n)\;\approx\;\frac{n}{\pi^{2}\,M(n)^{2}},
$$

which matches the measurements across six decades (for $n=27$:
$27/(\pi^{2}\cdot 9232^{2})\approx 3{\cdot}10^{-8}$, measured $10^{-8}$).

*The capture fraction.* Of $20{,}000$ random reals in $[1,50]$, only
$2.5\%$ converge to the cycle (with phases uniform: $163/171/175$); $97.5\%$
escape to infinity; no other attractor was met by the sample. The basin is
a dust of slivers concentrated around the tree integers, in a continuum
that overwhelmingly diverges.

### Where the Advantage Goes, and Where the Dragon Sits

The program's premise is correct as organization: three labels instead of
unbounded trajectories, an open set instead of an induction that leaks. But
the measurements show with unusual clarity where the difficulty migrates.

First, **the infinity moves from height into pinching**. The excursion of
$27$ to $9232$, which destroys range-limited induction, reappears —
through the law $r\approx n/\pi^{2}M^{2}$ — as the $10^{-8}$ radius of the
basin sliver at $27$. The geometry of $B$ around $n$ *is* the trajectory of
$n$, written as a thickness. Nothing was lost; it changed coordinates.

Second, **the continuum cannot carry the phase globally**. Off the basin,
where the dynamics of $f$ is chaotic or divergent, a continuous solution of
$F\circ f=F-1$ cannot exist (mixing dynamics admits no continuous Koopman
eigenfunction with eigenvalue of modulus one). The phase is a resonance of
the integers; the continuous covering exists exactly on $B$ and can exist
nowhere else. Hence "cover the phase continuously" and "prove
$\mathbb{N}\subset B$" are the same demand — the program restates the
conjecture in geometric coordinates rather than approaching it.

What the restatement *does* buy is a precise target. The expansion
$B=\bigcup_k f^{-k}(U)$ captures each integer if and only if the local
radius survives the pullback, and each odd step stretches perturbations by
$3$ while the peaks tax them by the pinching law. The missing ingredient is
an **expansion-stable lower bound**: a quantity attached to the inverse
orbit, provably bounded below, that dominates $r$. No such bound is known;
finding one would be genuine progress — and would amount to the hidden
Lyapunov function in geometric clothing.

## Conclusion

The phase structure of Collatz is now explicit at three levels.

At the **exact** level, the phase obeys a transport calculus — step law,
octave law, the $4n+1$ law, the coalescence law, the predecessor law — that
propagates synchronization information through the tree without any knowledge
of stopping times, and the terminal oscillator is the explicit harmonic
$w(t)=\tfrac{7}{3}-\tfrac{4}{3}\cos(2\pi t/3)+\tfrac{2\sqrt 3}{3}\sin(2\pi
t/3)$ onto which every trajectory locks in finite time.

At the **statistical** level, the phase field is globally uniform and locally
rigid: no congruence class of $n$ predicts the phase, yet $62\%$ of
consecutive integers are synchronized and the correlation decays slowly with
distance, driven by trajectory coalescence.

At the **foundational** level, the boundary is sharp: relative phases are
computable by calculus, absolute phases are conjecture-hard. The phase
function is total exactly when the conjecture holds, and it is precisely a
Koopman eigenfunction of eigenvalue $e^{-2\pi i/3}$. The compensated, fully
synchronized continuous Collatz exists and is written above — but its
compensator is built from $\sigma(n)$ itself.

The phases of Collatz can be transported, measured, compensated — and even
predicted, by walking the trajectory. What they cannot yet be is
*compressed*: computed without travelling the road. Congruence formulas are
impossible by theorem, finite-state formulas are excluded by the exponential
complexity of the phase language, and beyond that nothing is known in either
direction. The distance between transporting the phase and compressing it is,
exactly, the Collatz conjecture.