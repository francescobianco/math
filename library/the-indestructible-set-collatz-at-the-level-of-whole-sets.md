---
title: "The Indestructible Set: Collatz at the Level of Whole Sets"
type: paper
created: 2026-06-13T10:00:00+00:00
updated: 2026-06-13T10:00:00+00:00
---

# The Indestructible Set: Collatz at the Level of Whole Sets

*Apply the Collatz map to all the naturals at once and nothing happens: the
set is a fixed point. This paper proves the persistence, measures the
collisions it survives, establishes an exact halving law for tail sets, and
then dismantles — honestly — the proof of the conjecture that this picture
seems to offer.*

## Abstract

Take the whole set of positive integers and apply one Collatz step to every
element **simultaneously**. Collisions happen everywhere — a sixth of the
values are hit twice — so the new set looks like it should be smaller. It is
not. It is exactly $\mathbb{N}$ again, because every $m$ has the predecessor
$2m$: no number is missing after the transformation. By induction the set
survives any number of steps. The map demolishes nothing, ever, at the level
of sets, while (conjecturally) demolishing everything at the level of points.

This paper makes the set-level dynamics precise. We prove that $\mathbb{N}$
and the cycle $\{1,2,4\}$ are both fixed points of the induced map on
subsets; that the finite fixed points are **exactly the unions of cycles**
(so "no other finite invariant set" is a set-theoretic restatement of the
no-other-cycles third of the conjecture); and that the tail sets
$S_m = \{m, m+1, m+2, \ldots\}$ obey an **exact halving law**

$$
T^k(S_m) \;=\; S_{\lceil m/2^k \rceil},
$$

so that every tail floods back over all of $\mathbb{N}$ — including $1$ — in
exactly $\lceil \log_2 m \rceil$ steps, as if the $3n+1$ branch did not
exist. We measure the contrast with finite truncations: the segment
$[1, 2^{20}]$ collapses to exactly $\{1,2,4\}$ after $522$ steps, so the two
limits $k \to \infty$ and $N \to \infty$ do not commute — the infinity of the
source is the only thing keeping the set alive.

Finally we examine the argument the picture suggests: *every tail $S_m$
floods back and touches $1$; since $m$ is arbitrary, numbers with destiny
$1$ exist beyond every bound; are they not all of them?* We locate the exact
logical gap (an $\exists$ where the conjecture needs a $\forall$) and prove
the obstruction is fundamental: the $3n-1$ map satisfies **identical**
set-level laws while having three cycles instead of one, so no argument
expressible purely at the level of set images can decide the conjecture.

Throughout, $T$ denotes the Collatz map

$$
T(n) =
\begin{cases}
n/2 & n \text{ even},\\[2pt]
3n+1 & n \text{ odd},
\end{cases}
$$

on the positive integers $\mathbb{N} = \{1, 2, 3, \ldots\}$, and
$\sigma(n)$ the total stopping time (number of steps to reach $1$). All
computational claims are reproduced by the companion script (see
*Reproducing the results*).

## 1. One Step Applied to Everything at Once

For a subset $A \subseteq \mathbb{N}$ write

$$
\widehat{T}(A) \;=\; T(A) \;=\; \{\, T(n) : n \in A \,\},
$$

the **induced map on subsets**. The whole paper is the study of
$\widehat{T}$, the dynamics of Collatz when the moving object is a set
rather than a number.

**Theorem 1 (Persistence).** $T(\mathbb{N}) = \mathbb{N}$, and hence
$T^k(\mathbb{N}) = \mathbb{N}$ for every $k \ge 0$. The set of naturals is a
fixed point of $\widehat{T}$.

*Proof.* Every $m \in \mathbb{N}$ is the image of $2m$, which is even and
maps to $m$. So the image contains every natural, and it is contained in
$\mathbb{N}$ trivially. Induction on $k$ does the rest. $\blacksquare$

One line — and yet the statement deserves a pause, because it collides with
a strong intuition. The map is far from injective: distinct numbers crash
onto the same value constantly (next section: a sixth of all values are hit
twice). A non-injective map applied to a finite set strictly shrinks it.
Applied to $\mathbb{N}$ it shrinks nothing, because the infinite reservoir
of larger numbers refills every hole: this is Hilbert's hotel run as a
dynamical system. Whatever the map destroys by collision, the tail of the
set has already replaced.

So the picture is this. Pointwise — conjecturally — everything dies into the
cycle $1 \to 4 \to 2$. Set-wise, nothing dies at all. The system is
**pointwise dissipative and set-wise conservative**, and the entire content
of this paper is the tension between those two adjectives.

## 2. The Collisions It Survives

How wasteful is the map, exactly?

**Proposition 2 (Collision census).** A value $m$ has two $T$-preimages
($2m$ and $(m-1)/3$) exactly when $m \equiv 4 \pmod 6$, and one preimage
($2m$ alone) otherwise. The doubly-covered values have natural density
$\tfrac16$.

*Proof.* The even preimage $2m$ always exists. An odd preimage $j$ requires
$3j + 1 = m$ with $j = (m-1)/3$ a positive odd integer, which holds iff
$m \equiv 1 \pmod 3$ and $(m-1)/3$ is odd, i.e. $m \equiv 4 \pmod 6$.
$\blacksquare$

Verified on $[1, 2^{20}]$: $174763$ doubly-covered values, fraction
$0.166667$. So at every single step, one value in six absorbs two
predecessors — the map loses a sixth of its injectivity everywhere, forever
— and the image is still everything. (On a finite segment the loss is
visible: the first image of $[1, N]$ has size $\tfrac{11}{12}N$, because the
$N/2$ halved evens and the $N/2$ tripled odds overlap in exactly $N/12$
collisions. On $\mathbb{N}$ the loss is exactly $0$.)

## 3. The Exact Halving Law for Tails

Now the heart of the intuition. Take the tail set

$$
S_m \;=\; \{\, n \in \mathbb{N} : n \ge m \,\},
$$

all the naturals from $m$ onward, and push it forward. The droplets fall;
where do the splashes land?

**Theorem 3 (Halving law).** $T(S_m) = S_{\lceil m/2 \rceil}$ exactly, and
therefore

$$
T^k(S_m) \;=\; S_{\lceil m/2^k \rceil}
\qquad\text{for all } k \ge 0.
$$

*Proof.* Two inclusions.

*Everything above $\lceil m/2 \rceil$ is hit:* if $x \ge \lceil m/2 \rceil$
then $2x \ge m$, so $2x \in S_m$ and $T(2x) = x$.

*Nothing below it is hit:* let $x = T(n)$ with $n \ge m$. If $n$ is even,
$x = n/2 \ge m/2$, so $x \ge \lceil m/2 \rceil$. If $n$ is odd,
$x = 3n + 1 > n \ge m$. Either way $x \ge \lceil m/2 \rceil$.

The iterated form follows by induction using
$\lceil \lceil m/2 \rceil / 2 \rceil = \lceil m/4 \rceil$. $\blacksquare$

This is stronger than the qualitative "the tail comes back": the family of
tails is **invariant** under the dynamics, and the front advances by exactly
a factor of $2$ per step. Read the proof again and notice what it says about
the two branches: the $3n+1$ branch only throws numbers *upward*, deeper
into the tail, so it is **completely invisible** at this level. Watching
tail sets evolve, Collatz is indistinguishable from the trivial map
$n \mapsto \lceil n/2 \rceil$. All the famous turbulence — $27$ climbing to
$9232$ — happens strictly behind a front that marches down at speed $2$,
metronome-steady, indifferent to everything.

**Corollary 4 (Flooding time).** $T^k(S_m) = \mathbb{N}$ exactly when
$k \ge \lceil \log_2 m \rceil$. In particular $1 \in T^k(S_m)$ from that
moment on: every tail, no matter how far out it starts, floods back over
the entire set of naturals — splashes covering the whole floor — in
logarithmic time.

The theorem is verified computationally by backward search: for each $x$ in
a window and each tested $(m, k)$ up to $m = 10^6$, the script checks that
$x$ has a depth-$k$ preimage $\ge m$ precisely when
$x \ge \lceil m/2^k \rceil$. All cases agree with the formula.

Here is the droplets-and-splashes picture made exact. The subsets of
$\mathbb{N}$ interpenetrate and scatter; every tail spreads back over the
whole floor; and yet — Theorem 1 — the floor as a whole never moves. Every
single droplet is (conjecturally) on its way to the drain at $1$, while the
wet surface remains, eternally, all of $\mathbb{N}$.

## 4. Cut the Source and the Beast Starves

Where does the persistence come from? At every step, the large numbers in
the image are images of *even larger* numbers. The set survives because the
source is bottomless: there are always new numbers upstream to feed the
beast. The cleanest way to see this is to **truncate the source** and watch
the difference.

Apply $\widehat{T}$ to the finite segment $[1, N]$ with $N = 2^{20}$:

| $k$ | $0$ | $1$ | $5$ | $20$ | $100$ | $300$ | $400$ | $500$ | $522$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $\bigl|T^k([1,N])\bigr|$ | $1048576$ | $961195$ | $633515$ | $285321$ | $30837$ | $502$ | $50$ | $7$ | $3$ |

At $k = 522$ the set is exactly $\{1, 2, 4\}$ and stays there forever. (The
number $522$ is no accident: the slowest starter below $2^{20}$ is
$n = 837799$ with $\sigma = 524$, and two steps before touching $1$ its
trajectory sits on $4$, already inside the cycle-set. Hence the collapse
lands at $\sigma_{\max} - 2$.)

So:

$$
\lim_{k \to \infty} T^k\bigl([1, N]\bigr) = \{1, 2, 4\}
\quad\text{(verified for } N = 2^{20}\text{)},
\qquad\text{but}\qquad
T^k\Bigl(\lim_{N \to \infty} [1, N]\Bigr) = \mathbb{N}
\ \ \forall k.
$$

**The two limits do not commute.** Every finite truncation of the world is
demolished down to the terminal cycle; the whole world is indestructible.
The strangeness the persistence provokes — *it should be getting smaller!* —
is precisely the intuition trained on finite sets, applied where finiteness
fails. The infinite tail is not a technicality here; it is the entire
mechanism.

## 5. The Finite Fixed Points Are Exactly the Cycles

$\widehat{T}$ has at least two fixed points: $\mathbb{N}$ (Theorem 1) and
the cycle-set $\{1, 2, 4\}$, since $T(\{1,2,4\}) = \{4, 1, 2\}$ — the same
set, internally rotated. This is not a coincidence of this particular cycle:

**Theorem 5 (Finite invariant sets).** A finite nonempty set
$A \subseteq \mathbb{N}$ satisfies $T(A) = A$ if and only if $A$ is a union
of cycles of $T$.

*Proof.* A union of cycles is clearly invariant. Conversely, if $T(A) = A$
with $A$ finite, then $T$ restricted to $A$ is a surjection of a finite set
onto itself, hence a bijection, hence a permutation of $A$ — and every
permutation of a finite set decomposes into cycles. Each element of $A$
therefore lies on a genuine cycle of $T$. $\blacksquare$

This gives the set-level dynamics a precise stake in the conjecture. The
Collatz conjecture splits classically into two halves — *no other cycles*
and *no divergent trajectories* — and Theorem 5 translates the first half
perfectly:

> $\{1, 2, 4\}$ is the **only** finite nonempty fixed point of
> $\widehat{T}$ $\iff$ $1 \to 4 \to 2$ is the only cycle of $T$.

The fixed-point landscape of $\widehat{T}$, as conjectured, is austere:
$\varnothing$, the cycle $\{1,2,4\}$, the indestructible $\mathbb{N}$, and
nothing else finite. (A divergent trajectory, if one existed, would
contribute infinite forward-invariant sets strictly between the cycle and
$\mathbb{N}$ — but never a finite one.)

## 6. The Argument That Almost Proves the Conjecture

Now the reasoning the whole picture whispers in your ear. Spelled out:

1. Take any tail $S_m = \{m, m+1, \ldots\}$, with $m$ as enormous as you
   like.
2. By Corollary 4, $T^k(S_m) = \mathbb{N}$ for $k \ge \lceil \log_2 m
   \rceil$. The expansion of $S_m$ *must* return to cover all of
   $\mathbb{N}$ — and to cover $\mathbb{N}$ it must touch $1$.
3. So $1 \in T^k(S_m)$: some element of $S_m$ has destiny $1$.
4. Since $m$ was arbitrary, numbers with destiny $1$ exist beyond every
   bound... *but then are they not all the numbers?*

Steps 1–3 are theorems. Step 4 is the trap, and it deserves to be sprung in
slow motion rather than waved away.

The statement $1 \in T^k(S_m)$ unfolds to

$$
\exists\, n \ge m : \; T^k(n) = 1,
$$

an **existential** statement. The conjecture is

$$
\forall\, n : \; \exists k : \; T^k(n) = 1,
$$

a **universal** one. Set images are unions over elements:
$x \in T^k(A)$ means *somebody* in $A$ lands on $x$ — it never says who, and
it never says *everybody*. Repeating an existential statement for every $m$
yields infinitely many existential statements, not a universal one. Indeed,
step 3 is witnessed by an old friend: the first power of two past $m$
satisfies it all by itself. The grand flooding of Corollary 4, restricted
to the claim "some element of $S_m$ reaches $1$," proves nothing that
$2^{\lceil \log_2 m \rceil}$ didn't already prove for free.

There is a sharper way to say what flooding *does* prove. It shows that the
inverse tree of $1$ — the set of numbers that eventually reach $1$ — is
**unbounded**: it has members beyond every horizon $m$. But the conjecture
asks that this tree be **spanning**: that it contain *every* natural. An
unbounded subtree can still be meager — the powers of two alone are an
unbounded subtree. Between *unbounded* and *spanning* lies the entire
difficulty of the problem, and set-level dynamics sees only the first.

## 7. The $3n-1$ Litmus Test

Could a cleverer set-level argument close the gap? No — and we can prove
it, by the strongest kind of evidence: a map for which every set-level
statement above holds *verbatim* and the conjecture's analogue is *false*.

Let $T'$ be the $3n-1$ map ($n/2$ if even, $3n-1$ if odd). Then:

* **Persistence.** $T'(\mathbb{N}) = \mathbb{N}$ — same one-line proof,
  $2m \mapsto m$.
* **Halving law.** $T'^k(S_m) = S_{\lceil m/2^k \rceil}$ — same proof: the
  even branch halves, the odd branch $3n - 1 > n$ only throws upward.
* **Flooding.** Every tail floods back over $\mathbb{N}$ and touches $1$ in
  $\lceil \log_2 m \rceil$ steps.

Identical laws, word for word. But $T'$ is the standard counterexample
factory: it has (at least) three cycles, and the finite collapse shows them
directly. Running the same truncation experiment on $[1, 2^{20}]$, the set
collapses at $k = 553$ not to a single cycle but to a $25$-element fixed
set —

$$
\{1, 2\} \;\cup\; \{5, 10, 7, 14, 20\} \;\cup\;
\{17, 50, 25, 74, 37, \ldots, 272\}
$$

— the union of the three known cycles of $T'$, exactly as Theorem 5
predicts (the theorem's proof never used the "$+1$").

The consequence is a genuine no-go principle:

> Any argument that uses only the set-level behaviour of the map —
> surjectivity, persistence, tail flooding, image densities — applies
> equally to $3n+1$ and to $3n-1$. Since the single-destiny conclusion is
> false for $3n-1$, no such argument can prove the Collatz conjecture.

This is the same litmus test that dispatches several strategies in the
companion survey, and it places the set-level picture honestly: it is a
true, clean, and *provable* layer of Collatz — and it is constitutionally
blind to the thing the conjecture asks.

## 8. Conclusion: Perfect Bookkeeping of Roads, Total Amnesia of Destinies

What the set-level dynamics knows, it knows exactly: $\mathbb{N}$ is a fixed
point (Theorem 1); collisions cost a sixth and the infinite source repays
them (Proposition 2); tails are eigensets of the dynamics with eigenvalue
"halve" (Theorem 3); finite invariant sets are precisely the unions of
cycles (Theorem 5); and the indestructibility of the whole is a pure
infinity effect, vanishing under every truncation (Section 4).

What it cannot know is *who went where*. The image $T(A)$ is the perfect
ledger of which places are occupied after one tick, and the perfect
forgetting of which occupant came from where. It bookkeeps the roads and
erases the destinies — and the conjecture is a statement about destinies:
one drain, every droplet. The droplets scatter, the splashes re-cover the
floor at each instant, the floor never changes; and the question of whether
every single drop eventually finds the drain at $1$ is exactly the part of
the picture that the picture, by construction, cannot show.

The set that cannot be demolished is real. The proof it seems to offer is
not. Between them lies the conjecture, intact.

## Reproducing the Results

All numerical claims are reproduced by:

```
python3 library/scripts/collatz_set_dynamics.py        # N = 2^20 (~1M, a few minutes)
python3 library/scripts/collatz_set_dynamics.py 18     # quicker, N = 2^18
```

The script verifies the finite collapse of $[1, N]$ to $\{1,2,4\}$ under
$3n+1$ (and to the $25$-element union of three cycles under $3n-1$), the
$1/6$ collision density, and the exact halving law
$T^k(S_m) = S_{\lceil m/2^k \rceil}$ by backward search on windows, for $m$
up to $10^6$.