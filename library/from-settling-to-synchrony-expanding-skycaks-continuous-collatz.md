---
title: "From Settling to Synchrony: Expanding Skycak's Continuous Collatz"
type: paper
created: 2026-06-12T22:30:00+00:00
updated: 2026-06-12T22:30:00+00:00
---

# From Settling to Synchrony: Expanding Skycak's Continuous Collatz

*An expansion of J. P. Skycak's "Continuous Extension of the 3n+1 Problem"
(advisor J. Diller, Notre Dame): what his numerics already saw, what they
could not see, and how the phase program — including the forbidden words —
is the natural next chapter of his paper.*

## Abstract

Skycak extends the accelerated Collatz map $T(n) = \frac{3n+1}{2} \mid
\frac{n}{2}$ to a continuous map $f_S$ on $\mathbb{R}^{+}$, observes
numerically that orbits settle onto the attracting cycles $(1,2)$ and
$(1.193\ldots, 2.139\ldots)$, generalizes to an $an+b$ family with an area
crossover at $a = 3$, and closes with a random-walk analogy for why
fluctuations proportional to $x$ produce settling. This paper takes each of
those numerical findings seriously and continues it, using the machinery of
[The Phases of Collatz](library/the-phases-of-collatz.md). Four expansions,
all verified at script level. **(1)** The multiplier $3/4$ he computes at the
cycle $(1,2)$ is not generic: it is the Lagarias drift appearing as a literal
eigenvalue, the same number our full-map canvas produces at $(1,4,2)$, and it
is an invariant of the *integer* dynamics on the minimal canvas — whereas his
ghost cycle, and the basin geometry around it, are properties of the chosen
interpolation and evaporate under repainting (measured; we also correct the
ghost multiplier from his $-0.632$ to $-0.2308$). **(2)** His final plots of
$f^{400}$ are, unnamed, the first pictures of a **continuous phase field**:
the basin of the cycle splits into pieces permuted cyclically by the map, the
phase is a Koopman eigenfunction, and the conjecture becomes
$\mathbb{N}\subset B$. **(3)** His settling analysis — areas, expected
values — is *destiny-level* and therefore phase-blind. Measuring the phase
language of his own map $T$ (the parity word $\sigma_T(n) \bmod 2$), we find
it saturates to length $5$ and then refuses exactly **two hexagrams**,
$010010$ and $101101$ — precisely the two words of our $72$ ternary forbidden
words that are writable over $\{0,1\}$, and precisely the squares of the two
binary zigzag trigrams. The rigidity discovered in the full map's mod-3
language is present, in miniature, in Skycak's own clock. **(4)** His $a=3$
area crossover is an arithmetic-mean criterion; iteration compounds
multiplicatively, and the geometric-mean criterion puts the critical dial at
$a = 4$. The integer family ($a$ odd) cannot sample the window $(3,4)$; his
continuous family can, and measurement shows the settling boundary smeared
across exactly that window. The continuous extension is not just a curiosity
that mimics the discrete map: it is an instrument that sees between the
integers.

## 1. The Paper Being Expanded

Skycak's paper does four things, all numerical by his own honest declaration:

1. **Construction.** Bound $T$ between the lines $u(x) = \frac{3x+1}{2}$ and
   $\ell(x) = \frac{x}{2}$, run a sinusoid of period $2$ along the
   equilibrium, and obtain

   $$
   f_S(x) = \frac{4x+1}{4} - \frac{2x+1}{4}\cos(\pi x),
   $$

   which restricts to $T$ on $\mathbb{N}$ (a slice of the
   Letherman–Schleicher–Wood extension to $\mathbb{C}$).

2. **Settling.** Orbits of $f_S$ that were tested settle into one of two
   attracting $2$-cycles: the integer cycle $(1,2)$ with multiplier $3/4$,
   and a non-integer cycle near $(1.193, 2.139)$.

3. **The dial.** Generalize to $T_{a,b}$ and $F_{a,b}$; the signed area of
   $F_{a,1}$ above the diagonal is $\frac{a-3}{8}t^{2} + O(t)$, and contour
   plots locate the crossover from settling to divergence at $a = 3$.

4. **The closing analogy.** Random walks $r(x) = (1+\delta)x$ with
   $\delta = \pm\lambda$ satisfy $E[r^{k}(x)] = x(1-\lambda^{2})^{k/2} \to
   0$: fluctuations proportional to position produce contraction even when
   the *area* balance is neutral.

Each of the four is the beginning of something the paper does not yet have
the machinery to finish. This paper supplies the machinery — the phase
calculus, the gauge analysis, and the language of forbidden words — and runs
the measurements. Notation throughout: $C$ is the full Collatz map
($n/2$ odd $\mapsto 3n+1$), $T$ is Skycak's accelerated map, $f_S$ is his
canvas, and

$$
f_H(x) = \frac{7x+2}{4} - \frac{5x+2}{4}\cos(\pi x)
$$

is the harmonic canvas of the full map used in the phase paper. All new
measurements below are reproduced by
`library/scripts/skycak_bridge_experiments.py`.

## 2. Two Clocks, One Arithmetic

The two maps tell the same trajectories with two clocks. Write a trajectory
as $b$ odd steps and $a$ halvings. Every $3n+1$ produces an even number, so
each odd step of $T$ absorbs exactly one halving, and

$$
\sigma_C(n) = a + b,
\qquad
\sigma_T(n) = a :
$$

**the accelerated stopping time is exactly the number of halvings.** The two
terminal cycles are the same orbit read on the two clocks: $1 \to 4 \to 2$
(period three) collapses to $1 \to 2$ (period two). And the multipliers
agree:

$$
\underbrace{\tfrac{3}{2}\cdot\tfrac{1}{2}}_{f_S \text{ at } (1,2)}
\;=\;
\underbrace{3\cdot\tfrac{1}{2}\cdot\tfrac{1}{2}}_{f_H \text{ at } (1,4,2)}
\;=\;\frac{3}{4}.
$$

This is the first expansion of Skycak's observation: the $3/4$ he computed
by the chain rule is not an accident of his interpolation. On any *minimal*
canvas (no $\sin(\pi x)$ term) the derivative at an integer equals the slope
of the arithmetic step itself, so the multiplier of any integer cycle is the
**discrete cycle ratio** $3^{p}/2^{q}$ — and for the terminal cycle that
ratio is $3/4$, the Lagarias drift, the classical heuristic contraction rate
of the conjecture, here appearing as a literal eigenvalue. The same
computation shows (as in the phase paper) that *every* integer cycle of
either map — including any undiscovered one — is automatically attracting on
its minimal canvas, since the exact cycle identity forces $3^{p}/2^{q} =
1/\prod(1 + \frac{1}{3n_i}) < 1$.

**A correction.** Skycak reports the ghost cycle multiplier as $\approx
-0.632$, computed from the three-digit cycle values $(1.193, 2.139)$.
Locating the cycle to ten digits,

$$
(x_1, x_2) = (1.1925319070,\ 2.1386563355),
\qquad
f_S'(x_1)\,f_S'(x_2) = (-0.100519)(2.295612) = -0.23075,
$$

verified independently by finite differences. The cycle sits almost exactly
on a critical point of $f_S$ ($f_S'(x_1) \approx -0.1$), which makes the
multiplier exquisitely sensitive to the cycle location — three digits are
not enough. The cycle is even more attracting than reported; his conclusion
stands, strengthened.

## 3. The Census of the Basin, and What Is Paint

Skycak writes that every tested orbit settles. We ran the census: $20{,}000$
random seeds in $[1, 100]$, iterated to convergence.

| canvas | $\to (1,2)$ | $\to$ ghost | escape |
|---|---:|---:|---:|
| $f_S$ | $76.0\%$ | $24.0\%$ | $0\%$ |
| $f_S + 0.3\sin(\pi x)$ | $100\%$ | — | $0\%$ |
| $f_S + \sin(\pi x)$ | $0\%$ | $100\%$ (a *new* ghost) | $0\%$ |
| $f_H$ (full map, from the phase paper) | $2.5\%$ (to $(1,4,2)$) | — | $97.5\%$ |

His observation is confirmed and sharpened: on his canvas **nothing
escapes** — the continuum splits $76/24$ between the integer cycle and the
ghost. But the second and third rows are the expansion. Every analytic
extension of $T$ has the form $g = f_S + \sin(\pi x)h$ with $h$ entire; all
of them restrict to $T$ on $\mathbb{N}$, so all of them carry the
conjecture. Under repainting:

- at $c = 0.3$ the ghost cycle **evaporates** — the whole interval drains
  into $(1,2)$, whose multiplier shifts from $0.7500$ to $0.8042$ (the sine
  term tilts the derivative at the integers: $g'(n) = f_S'(n) + c\pi
  \cos(\pi n)$);
- at $c = 1$ the integer cycle itself turns **repelling** (multiplier
  $-5.978$) and a brand-new ghost at $(0.4926, 1.7309)$, multiplier
  $+0.3415$, captures everything.

And the fourth row shows that even the *minimal* canvas of the **full** map
behaves oppositely: there the basin is a dust of slivers around the tree
integers (local radius $r(n) \approx n/\pi^{2}M(n)^{2}$, where $M$ is the
trajectory peak — the excursion of $27$ to $9232$ reappears as a $10^{-8}$
sliver), and $97.5\%$ of the continuum diverges.

The lesson is the gauge lesson of the phase paper, now demonstrated *on
Skycak's own function*: the ghost cycle, the capture fractions, the
multiplier values, the basin geometry — all **paint**, properties of the
chosen interpolation. What survives every repainting is the orbit structure
on $\mathbb{Z}$ and the discrete cycle ratios $3^{p}/2^{q}$. A continuous
program built on these extensions must either fix a canonical canvas and
defend the choice, or work only with gauge-invariant quantities. Skycak's
$f_S$ is a *good* canonical candidate — it is minimal, and on it the
continuum is completely captured — but the case must be made, not assumed.

## 4. The Phase: What the Settling Forgets

Skycak's most striking plots are his last two: $f^{40}$ of three seeds
$0.01$ apart reaching values hundreds apart, then $f^{400}$ of an interval
of seeds collapsing onto the two cycles — but onto *different points of the
cycle at a given time*, in a fine interleaving along the seed axis. He reads
this as sensitivity followed by settling. It is more: **it is the first
picture of a continuous phase field.**

When an orbit settles onto a $2$-cycle, the destiny ("which cycle") forgets
everything about the road except one bit: the *parity of the arrival time*.
Two seeds landing on $(1,2)$ either beat in unison forever or beat in
opposition forever. For the integers this is the phase of the accelerated
clock,

$$
\phi_2(n) = \sigma_T(n) \bmod 2 = a(n) \bmod 2
$$

— the parity of the number of halvings — and it obeys the same transport
calculus as the mod-3 phase of the full map: every step flips it,
$\phi_2(T(n)) = \phi_2(n) + 1$; doubling flips it, $\phi_2(2n) = \phi_2(n) +
1$; $Z_2(n) = (-1)^{\sigma_T(n)}$ is a Koopman eigenfunction of $T$ with
eigenvalue $-1$.

On the continuum the structure is geometric. The basin $B$ of the cycle
$(1,2)$ under $f_S$ decomposes into two disjoint open pieces $B_0, B_1$ —
seeds tracking $1$ at even versus odd times — and $f_S$ **swaps them**. The
phase field $F: B \to \{0,1\}$ is locally constant, continuous, satisfies
$F\circ f_S = F + 1$, and restricts to $\phi_2$ on the tree integers. The
fine interleaving in Skycak's $f^{400}$ plot *is* the boundary structure of
$B_0$ and $B_1$ (and of the ghost's two pieces, fourfold in all). Measured:
the captured seeds split $7479 / 7716$ between even and odd arrival — the
two phase pieces have, to sampling accuracy, equal measure.

The conjecture then takes the same geometric form as in the phase paper:

> **Collatz $\iff$ $\mathbb{N} \subset B$** — every integer interior to the
> basin of the terminal cycle.

with one pleasant difference of canvas: on $f_H$ the basin is a pinched dust
in a diverging continuum, while on $f_S$ the basin appears to be (up to the
ghost's share and a measure-zero boundary) *the whole half-line*. On
Skycak's canvas the conjecture is not "the basin reaches every integer
against a hostile continuum" but "no integer falls into the ghost's
territory or the boundary". Whether that reformulation is easier or merely
repainted is exactly the gauge question of Section 3 — but it is a
reformulation his paper earns and does not state.

## 5. The Phase Language of Skycak's Map

Here is the genuinely new measurement, and the reason this paper exists.
The phase paper found that the full map's phase word $\phi(1)\phi(2)
\phi(3)\cdots$ over $\{0,1,2\}$ saturates all $243$ pentagrams and then
refuses exactly $72$ hexagrams — stable from $2^{20}$ to $2^{24}$, paired
into $36$ forcing rules, regenerating genuinely new forbidden words at every
length ([notes](library/notes-on-the-forbidden-words-of-the-collatz-phases.md)).

Does *Skycak's* clock speak such a language? Form the binary word
$\phi_2(1)\phi_2(2)\phi_2(3)\cdots$ and count subwords (measured at $n <
2^{22}$ and $n < 2^{24}$, identical results through length $12$):

| $L$ | $p(L)$ | $2^L$ | missing |
|---|---:|---:|---:|
| $4$ | $16$ | $16$ | $0$ |
| $5$ | $32$ | $32$ | $0$ |
| $6$ | $62$ | $64$ | $\mathbf{2}$ |
| $7$ | $120$ | $128$ | $8$ |
| $8$ | $230$ | $256$ | $26$ |
| $12$ | $2618$ | $4096$ | $1478$ |
| $20$ | $131112$ | $1048576$ | $917464$ |

The language is full through length $5$ and then refuses **exactly two
hexagrams**:

$$
010010 \qquad\text{and}\qquad 101101.
$$

Verified: persistent from quarter range to full range at both $2^{22}$ and
$2^{24}$ with zero appearances; the pair is closed under complement (the
binary letter rotation) and under reversal; the growth ratio
$p(20)/p(19) \approx 1.56 < 2$, so the entropy is strictly below $\log 2$ —
the binary phase language, like the ternary one, is neither regular nor
free, and the finite-state rung of the formula ladder is excluded for
$\sigma_T \bmod 2$ exactly as it was for $\sigma_C \bmod 3$.

Because the alphabet is binary, the forcing structure is as sharp as it can
be: a missing hexagram removes one of the *two* children of its pentagram
context, so each forbidden word is one deterministic rule. The whole bottom
level of the binary rigidity is **two forcing rules**:

$$
01001 \to 1,
\qquad
10110 \to 0.
$$

After five consecutive integers whose halving-counts have parities
$0,1,0,0,1$, the parity of the sixth is determined. This is the cheapest
provable target in the entire forbidden-words program — one congruence
statement about $a(n), \ldots, a(n+5)$, two letters, one rule by symmetry.

**The frontier differs from the ternary case.** At length $7$ all $8$
missing words are inherited (contain a forbidden hexagram): *zero* genuinely
new — where the ternary language produced $48$ new words at its length $7$.
The first genuinely new binary words appear at length $8$, and they are

$$
01010101 \qquad\text{and}\qquad 10101010 :
$$

the pure alternations. **The parity of the halving count never alternates
eight times in a row** along consecutive integers; the maximal zigzag run is
seven. At length $9$, eighteen genuinely new words appear. The binary
rigidity is thus *sparser* and *slower* than the ternary one — two words
against seventy-two, a silent length against forty-eight new words — which
is what makes it the right first battlefield: small enough to attack, alive
enough to matter.

## 6. The Trigram-Square Law

Now place the two languages side by side. The ternary forbidden set
$\mathcal{F}$ contains exactly two words writable over the alphabet
$\{0,1\}$ — scan the list of $72$ — and they are $010010$ and $101101$.
Measured, then:

$$
\mathcal{F}_{\text{binary}} \;=\; \mathcal{F}_{\text{ternary}} \cap \{0,1\}^{6}.
$$

The same two strings are refused by both clocks — by $\sigma_C \bmod 3$ read
along the integers, and by $\sigma_T \bmod 2$ read along the integers. And
both are **squares of zigzag trigrams**: $010\cdot 010$ and $101\cdot 101$.
The ternary language forbids the squares of all twelve of its zigzag
trigrams; the binary language forbids the squares of both of its two. Every
trigram square that *can* be forbidden, on either clock, *is* forbidden.

> **Conjecture (trigram-square law).** On either Collatz clock — the full
> map mod $3$, the accelerated map mod $2$ — the phase word never repeats a
> zigzag trigram immediately: no six consecutive integers realize a phase
> pattern of exact period three with no equal adjacent letters.

This is the unification the two papers were waiting for, and it has a clean
arithmetic home. The pair $(a(n), b(n))$ — halvings and odd steps — is the
common currency: $\phi_2 = a \bmod 2$ and $\phi_3 = (a + b) \bmod 3$ are two
linear shadows of the same two-dimensional additive data. The natural
object is the **joint phase word** over $\mathbb{Z}/2 \times \mathbb{Z}/3
\cong \mathbb{Z}/6$,

$$
\Phi(n) = \bigl(a(n) \bmod 2,\ (a(n)+b(n)) \bmod 3\bigr),
$$

whose forbidden structure must project onto both measured languages. If the
two shadows refuse the same squares, the obstruction plausibly lives
upstairs, in the joint word — one cause, two silhouettes. Measuring the
subword complexity of $\Phi$ (alphabet six, first interesting length
presumably six) is the immediate next experiment; proving the binary forcing
rule $01001 \to 1$ is the immediate next theorem-attempt.

## 7. The Dial $a$, and the Band Between Two Means

Skycak's area functional $G_{a,1}(t) = \frac{a-3}{8}t^{2} + O(t)$ vanishes
at $a = 3$, and his contour plots place the settling/divergence crossover
there. But he himself notices the puzzle: at $a = 3$ the area criterion is
neutral, yet the orbits settle — and his closing random-walk computation,
$E[r^{k}(x)] = x(1-\lambda^{2})^{k/2}$, is precisely the resolution
struggling to be named. The area above the diagonal is an **arithmetic
mean** of the step sizes. Iteration *compounds*; what governs compounding is
the **geometric mean**. For the $an+1$ walk the expected log-factor per
accelerated step is

$$
\tfrac{1}{2}\log\tfrac{a}{2} + \tfrac{1}{2}\log\tfrac{1}{2}
= \tfrac{1}{2}\log\tfrac{a}{4},
$$

which is negative — settling — until $a = 4$, not $3$. At $a = 3$ there is
no paradox to explain: the multiplicative drift is $\sqrt{3}/2 < 1$,
comfortably contracting; the vanishing area is simply the wrong average
going quiet.

The two criteria disagree exactly on the window $3 < a < 4$ — and here the
continuous extension stops being a mimic and becomes an instrument. The
integer family cannot sample the window: $T_{a,1}$ needs $a$ odd, so the
dial jumps from $3$ (settles) to $5$ (diverges, consistently with both
criteria). But $F_{a,1}$ is defined for every real $a$. The census ($400$
seeds in $[1,500]$, $400$ iterations, escape threshold $10^{8}$):

| $a$ | settled ($<10$) | escaped ($>10^{8}$) | median final |
|---:|---:|---:|---:|
| $2.8$ | $400$ | $0$ | $1.0$ |
| $3.0$ | $400$ | $0$ | $1.2$ |
| $3.2$ | $355$ | $4$ | $1.7$ |
| $3.4$ | $142$ | $92$ | $8569$ |
| $3.6$ | $34$ | $321$ | $10^{8}$ |
| $3.8$ | $9$ | $387$ | $10^{8}$ |
| $4.0$ | $0$ | $400$ | $10^{8}$ |
| $4.2$ | $0$ | $400$ | $10^{8}$ |

The crossover is not the line $a = 3$: it is a **band**, opening just above
$3.2$ and closing at $4.0$ — precisely the disputed window, with coexistence
of settling and escape in the middle (at $a = 3.4$, $142$ settle while $92$
escape and the rest wander). Skycak's isocline marks where the *area*
changes sign; the dynamics changes regime where the *geometric* mean does,
blurred across the band by the attracting cycles that survive a little past
their drift. His own closing analogy, taken quantitatively, predicts this —
the expansion here is only the measurement that confirms it.

At the other end of the dial sits the gift: $a = 1$. The map $T_{1,1}(n) =
\frac{n+1}{2} \mid \frac{n}{2}$ is strictly decreasing above $1$, so its
stopping time is **provably total** — in fact $\sigma_{T_{1,1}}(n) =
\lceil \log_2 n \rceil$, and the entire phase apparatus (word, complexity,
forbidden structure) can be computed *and proved* in closed form. The
$an+b$ family is thus a rigidity dial with a solvable end: every question
of Sections 5–6, asked at $a = 1$, has an answer by theorem; asked at $a =
3$, it is the research program. Comparing the two ends — does the solvable
end already show forbidden words, or is rigidity a creature of criticality?
— is the cleanest calibration experiment the program has.

## 8. Status, and the Continuation Program

In Skycak's spirit, the ledger. **Inherited theorems** (from the phase
paper, restated on his map): the transport calculus of $\phi_2$; the Koopman
eigenfunction $Z_2$ with eigenvalue $-1$; totality of $\phi_2$ $\iff$ the
conjecture; the gauge classification $g = f_S + \sin(\pi x)h$ of his
extensions; attractivity of every integer cycle on the minimal canvas, with
multiplier the discrete ratio $3^{p}/2^{q}$. **New measurements** (this
paper, all script-reproducible): the basin census of $f_S$ ($76/24/0$) and
its collapse under repainting; the corrected ghost multiplier $-0.2308$; the
equal measure of the two phase pieces; the binary phase language — full to
length $5$, exactly two forbidden hexagrams $010010, 101101$, persistent to
$2^{24}$, complement- and reversal-closed, entropy $< \log 2$; the silent
length $7$; the forbidden alternations at length $8$ (maximal zigzag run
seven); the identity $\mathcal{F}_{\text{binary}} = \mathcal{F}_{\text{ternary}}
\cap \{0,1\}^{6}$; the crossover band $(3.2, 4.0)$ of $F_{a,1}$.
**Conjectures**: the trigram-square law; criticality of the dial at $4$,
not $3$. **Not progress toward the conjecture**: all of the above, and
honesty requires saying so — the realistic product of this thread is
experimental mathematics, sharpened questions, and small provable targets.

The continuation program, ordered by attack value:

1. **Prove $01001 \to 1$.** One binary forcing rule; with complement
   symmetry it proves both binary forbidden words, the first theorem of the
   forbidden-words program, on Skycak's own map.
2. **Measure the joint word** $\Phi(n) \in \mathbb{Z}/6$ and locate the
   common ancestor of the two forbidden sets.
3. **Calibrate at $a = 1$**: compute the provable phase language of
   $T_{1,1}$ and compare its rigidity (if any) with the critical case.
4. **Map the band**: refine the census on $a \in (3.2, 4.0)$, where
   settling and escape coexist — basin boundaries, and whether the ghost
   cycles of $F_{a,1}$ persist or evaporate across the band.
5. **The gauge-invariant bound**: the expansion-stable lower bound on basin
   radii sought by the phase paper, now with a second canvas ($f_S$, which
   captures everything) to test any candidate against.

## Reproduction

```bash
python3 library/scripts/skycak_bridge_experiments.py 22   # all three experiments
python3 library/scripts/skycak_bridge_experiments.py 24   # phase language at 16.7M
```

Experiment A prints the basin census and gauge tests of Section 3 (and the
ghost-cycle multiplier of Section 2), Experiment B the binary phase language
of Section 5, Experiment C the crossover band of Section 7. The ternary
companion data come from `library/scripts/collatz_forbidden_words.py` and
`library/scripts/collatz_phase_frontier.py`.

## References

- Skycak, J. P. *Continuous Extension of the 3n+1 Problem.* University of
  Notre Dame (advisor J. Diller).
- Lagarias, J. C. "The 3x+1 problem and its generalizations." *Amer. Math.
  Monthly* 92, 3–23 (1985).
- Letherman, S.; Schleicher, D.; Wood, R. "The 3n+1-Problem and Holomorphic
  Dynamics." *Experimental Mathematics* 8:3, 241–252 (1999).
- Oliveira e Silva, T. "Empirical verification of the 3x+1 and related
  conjectures." In *The Ultimate Challenge: The 3x+1 Problem*, J. C.
  Lagarias, ed. AMS (2010).
- [The Phases of Collatz](library/the-phases-of-collatz.md) — the phase
  transport calculus, the basin program, the gauge classification.
- [Notes on the Forbidden Words of the Collatz Phases](library/notes-on-the-forbidden-words-of-the-collatz-phases.md)
  — the 72 ternary words, the 36 forcing rules, the frontier at lengths 7–8.