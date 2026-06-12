---
title: Notes on the Forbidden Words of the Collatz Phases
type: notes
created: 2026-06-10T23:35:00+00:00
updated: 2026-06-12T21:00:00+00:00
---

# Notes on the Forbidden Words of the Collatz Phases

Working notes for the sharpest open question produced by the phase program
of [The Phases of Collatz](library/the-phases-of-collatz.md): the **72
length-6 words that the phase language never speaks**. This is the one
falsifiable, attackable research thread in the Collatz material; these notes
record what is known, the data, and the plan of attack.

## The Finding

The phase word is $\phi(1)\phi(2)\phi(3)\cdots$ with $\phi(n)=\sigma(n)\bmod
3$. Its subword complexity saturates completely up to length $5$ (every one
of the $3^5=243$ blocks occurs) and then drops:

$$
p(6)=657=729-72.
$$

The $72$ missing blocks are **stable under data growth**:

| sample | missing length-6 words |
|---|---:|
| $n<2^{20}$ | $72$ |
| $n<2^{22}$ | the same $72$ |
| $n<2^{24}$ ($16.7$M) | the same $72$, zero new appearances |

If they were merely rare, quadrupling the sample should have revealed some.

## Structure of the Forbidden Set

Verified facts about the set $\mathcal{F}$ of the $72$ words:

1. **Closed under letter rotation** $w\mapsto w+1 \pmod 3$: the set splits
   into $24$ rotation orbits of size $3$. Consistent with the dyadic
   covariance (doubling rotates all phases).
2. **Closed under reversal** $w\mapsto \tilde{w}$. This is *not* explained by
   any symmetry we have proved — the Collatz dynamics has no obvious
   time-reversal on the integer line. Worth understanding.
3. **Not the zigzag explanation**: only $24$ of the $72$ are pure zigzag
   (no equal adjacent letters), and $72$ of the $96$ possible zigzag words
   *do* occur. Excessive alternation is not the mechanism.
4. **The twelve trigram squares**: $\mathcal{F}$ contains the square $xx$ of
   every zigzag trigram $x$:

   $$
   010010,\ 012012,\ 020020,\ 021021,\ 101101,\ 102102,
   $$
   $$
   120120,\ 121121,\ 201201,\ 202202,\ 210210,\ 212212.
   $$

   An immediate repetition of a three-letter zigzag figure never happens:
   six consecutive integers never realize a zigzag phase pattern of exact
   period three. This sub-family looks like the most provable corner of
   $\mathcal{F}$.
5. Since $p(5)=243$, every length-5 word occurs — in particular the prefix
   and suffix of each forbidden word. Every word in $\mathcal{F}$ is
   therefore a *minimal* forbidden word.

## The Full List

```
010010 010012 010020 010021 010210 010212 012010 012012 012201 012202
012210 012212 020010 020012 020020 020021 020120 020121 021020 021021
021101 021102 021120 021121 101101 101102 101120 101121 101201 101202
102101 102102 102201 102202 102210 102212 120010 120012 120020 120021
120120 120121 121020 121021 121101 121102 121120 121121 201101 201102
201120 201121 201201 201202 202101 202102 202201 202202 202210 202212
210010 210012 210020 210021 210210 210212 212010 212012 212201 212202
212210 212212
```

## The Forcing Contexts (measured 2026-06-12)

The $72$ words are not sprinkled: **the holes come in pairs**. Grouping
$\mathcal{F}$ by its length-5 prefixes:

- every 5-context touched by $\mathcal{F}$ loses **exactly 2** of its 3
  children — never 1, never 3: $36$ prefixes $\times\ 2 = 72$;
- symmetrically for suffixes: $36$ suffix contexts $\times\ 2 = 72$.

Losing 3 children is impossible (the pentagram itself would be forbidden,
against $p(5)=243$). But *always exactly 2, never 1* is not forced by
anything known — it is a discovery: after each of these $36$ windows the
next letter is **determined**. The phase language contains $36$ forward
forcing rules (and $36$ backward ones), in $12$ rotation orbits:

```
01001->1  01002->2  01021->1  01201->1  01220->0  01221->1
02001->1  02002->2  02012->2  02102->2  02110->0  02112->2
10110->0  10112->2  10120->0  10210->0  10220->0  10221->1
12001->1  12002->2  12012->2  12102->2  12110->0  12112->2
20110->0  20112->2  20120->0  20210->0  20220->0  20221->1
21001->1  21002->2  21021->1  21201->1  21220->0  21221->1
```

Verified: reversal maps each forward rule to a backward rule **with the
same forced letter**.

Two consequences. First, the attack value: proving a single forcing rule
proves *two* forbidden words at once — a better first target than the
trigram squares. Second, no contradiction with the exponential subword
complexity that kills finite-state formulas: these are *partial* local
rules (36 special windows), not a total automaton — exactly the shape of
outcome (c).

## The Variants Share the Missing Words (identity versus rigidity)

The step law is pointwise: $\phi(T(n)) = \phi(n) - 1 \pmod 3$. Hence the
phase variants $\phi\circ T$ and $\phi\circ T^{2}$, as sequences over $n$,
are the original word with all letters rotated — no horizontal
rescrambling. Their forbidden sets are $\mathcal{F}-1$ and
$\mathcal{F}-2$, and by rotation closure these are **the same 72 words**.
In fact the two statements are equivalent:

> the three phase variants share their missing words
> $\iff$ $\mathcal{F}$ is closed under letter rotation.

Stacking the three variants, every *column* is a permutation of
$\{0,1,2\}$ (a Latin structure); the constant-sum law
$A_0+A_1+A_2 = 1+4+2 = 7$ of the phase paper is the vertical shadow of
these permutation columns. Mutually compensating missing words between
variants are therefore impossible by construction: rows two and three
carry no new horizontal information.

**Methodological warning (identity versus rigidity).** The conservation
law is an *identity*: any ternary sequence whatsoever, stacked with its
rotations, sums to a constant. It forbids nothing — the same epistemic
situation as the mod-8 coalescence law below. The $72$ paired holes are
*rigidity*: an empirical theorem still awaiting its arithmetic cause. The
cause must live in the transport calculus (coalescence hierarchies at
higher moduli), not in the harmonic bookkeeping. Do not mistake the paint
for the pigment.

## The Frontier at Lengths 7 and 8 (measured 2026-06-12, $n<2^{22}$)

**Length 7.** Missing words: $456 = 408$ *inherited* (containing a
forbidden hexagram) $+\ 48$ **genuinely new** ($16$ rotation orbits). All
$48$ persistent from quarter range to full range, zero appearances. The
pairing law repeats exactly: the new words sit in $24$ fresh forcing
6-contexts, each losing exactly $2$ of $3$ children.

**The cascade is not propagation.** None of the $24$ new forcing
6-contexts is an old 5-context extended by its forced letter ($0$ of
$24$). Each length brings *genuinely new* deterministic windows: the
rigidity is not the shadow of the previous level — it regenerates.

**Reversal breaks at length 7.** Of the $48$ genuinely new missing
words, exactly $24$ have reversals that **occur**:

```
0110210 missing, 0120110 occurs     0112010 missing, 0102110 occurs
0220120 missing, 0210220 occurs     0221020 missing, 0201220 occurs
1001201 missing, 1021001 occurs     1002101 missing, 1012001 occurs
...                                  (24 in all, 8 orbits)
```

So the reversal closure of $\mathcal{F}$ (fact 2, the orphan) is **exact
at length 6 and half-broken at length 7**: reversal is *not* a symmetry
of the phase language. The mystery is reframed — what needs explaining is
no longer a deep time-reversal of the dynamics, but why the breaking is
invisible at length 6 and exactly half at length 7.

**Length 8.** Missing: $2388$, of which $372$ genuinely new (all
persistent from quarter range, rotation-closed; $192/372$ reversals
occur). Pairing *almost* holds: $180$ forcing 7-contexts lose $2$
children — and **12 contexts lose only 1**, the first deviation from
perfect pairing:

```
0112120 0112121 0221210 0221212 1002020 1002021
1220201 1220202 2001010 2001012 2110101 2110102
```

All $12$ persistent at this sample, but length-8 statistics are thinner;
stress-test at $2^{24}$–$2^{26}$ before believing the deviation.

**Complexity growth.**

| $L$ | $p(L)$ | $3^L$ | $p(L)/p(L-1)$ |
|---|---:|---:|---:|
| 5 | 243 | 243 | 3.000 |
| 6 | 657 | 729 | 2.704 |
| 7 | 1731 | 2187 | 2.635 |
| 8 | 4173 | 6561 | 2.411 |

The growth ratio falls steadily below $3$: the entropy of the phase
language is strictly below $\log 3$ and, at these scales, still
descending. No limit claim — the ratios are not yet stable.

## Why the Known Laws Cannot Explain This

The only proved coalescence law in the phase paper is
$\sigma(8k+4)=\sigma(8k+5)$, which forces equal letters at window positions
$\equiv 4,5 \pmod 8$. But a length-6 window aligned at $5$, $6$ or $7$ modulo
$8$ contains no such pair, so **this law alone forbids nothing**: every
candidate word has escape alignments. Whatever kills the $72$ words must
operate at those alignments too — either an undiscovered hierarchy of merge
laws at higher moduli ($16, 32, 64, \ldots$), or a genuinely new constraint
on the phase language.

## Outcomes (all of them count as progress)

- **(a) Prove a word forbidden.** Even one. Then the phase language has
  explicit forbidden words and entropy strictly below $\log 3$ — a real,
  small theorem. The twelve trigram squares are the natural first target.
- **(b) A word eventually appears.** Then the local rigidity is softer than
  it looks and the complexity picture must be redrawn.
- **(c) Characterize the set.** Even empirically: if the $72$ words are
  generated by finitely many congruence merge-laws, those laws extend the
  transport calculus of the phase paper.

## Plan of Attack (re-prioritized 2026-06-12)

1. **Prove one forcing rule.** Each of the 36 rules
   (context $\to$ forced letter) proves *two* forbidden words at once;
   the rules are explicit congruence-flavoured statements about
   $\sigma(n),\ldots,\sigma(n+5)$. This replaces the trigram squares as
   the natural first target.
2. Enumerate the coalescence families at moduli $16, 32, 64$: pairs (or
   tuples) of residue classes provably reaching a common value in equal
   time. (Automatable: symbolic forward iteration of $ak+b$ classes.)
3. For each forbidden word, list its escape alignments and check which
   higher-modulus law blocks each one. A word is *proved* forbidden when
   every alignment in every residue class is blocked.
4. The trigram squares $xx$ remain a structured sub-target: a period-3
   zigzag phase pattern on six consecutive integers — look for an
   arithmetic obstruction to $\sigma(n+3)\equiv\sigma(n)\pmod 3$ holding
   three times in a row with zigzag profile.
5. **Reversal, reframed.** The old question ("what symmetry explains
   reversal closure?") is dead — reversal closure breaks at length 7.
   The new question: why is the breaking invisible at length 6 and
   exactly half ($24/48$) at length 7?
6. Push the sample to $2^{26}$–$2^{28}$ (needs a faster sieve, e.g. C or
   numba). Priority check: the 12 single-hole contexts at length 8 —
   do they stay single (pairing law genuinely broken) or close into
   pairs (one word of each pair merely rare)?

## Reproduction

```bash
python3 library/scripts/collatz_forbidden_words.py 22 6   # default analysis
python3 library/scripts/collatz_forbidden_words.py 24 6   # 16.7M check (minutes)
python3 library/scripts/collatz_forbidden_words.py 22 7   # length-7 frontier
python3 library/scripts/collatz_phase_frontier.py 22      # forcing contexts + frontier 7/8
```

The first script prints the complexity table, the persistence comparison,
the closure tests, and the decoded list of missing words. The second
reproduces the 2026-06-12 findings: the pairing of holes, the 36 forcing
rules, the genuinely-new frontier at lengths 7 and 8, the reversal
breaking, and the complexity ratios.

## Where the Collatz Program Stands (honest status)

For reuse, the state of the whole Collatz line in this library as of
2026-06-10:

- **Theorems (small but real):** phase transport calculus; no congruence
  formula for the phase at any modulus; dyadic log-periodicity (period three
  octaves); totality obstruction (a total closed phase formula proves the
  conjecture); finite-time locking onto the explicit wave
  $w(t)=\tfrac73-\tfrac43\cos\tfrac{2\pi t}{3}+\tfrac{2\sqrt3}{3}\sin\tfrac{2\pi t}{3}$.
- **Measurements:** global phase uniformity; local rigidity ($62\%$ at gap 1,
  slow decay); octave rotation $\approx +1$ per doubling with decaying
  polarization; exponential subword complexity (kills finite-state
  formulas); the $72$ forbidden words. Added 2026-06-12: the paired-hole
  law and the $36$ forcing rules; the genuinely-new frontier ($48$ at
  length 7, $372$ at length 8, all persistent); reversal closure breaking
  at length 7 ($24/48$); the 12 single-hole contexts at length 8 (to be
  stress-tested); complexity ratios falling ($2.70, 2.63, 2.41$) —
  entropy strictly below $\log 3$.
- **Open and attackable:** everything in these notes.
- **Not progress toward the conjecture:** all of the above. The proof
  distance is unchanged; the realistic ceiling of this thread is an
  experimental-mathematics note. Recorded here so future sessions do not
  re-inflate expectations.