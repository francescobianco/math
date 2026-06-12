---
title: "The Three-Phase Key: Self-Verifying Watermarks from the Incompressible Collatz Phase"
type: paper
created: 2026-06-12T23:55:00+00:00
updated: 2026-06-12T23:55:00+00:00
---

# The Three-Phase Key: Self-Verifying Watermarks from the Incompressible Collatz Phase

*A theoretical-CS and applied-algorithms study of what the three Collatz
phase functions are good for, and — just as carefully — what they are not.
The honest thesis: the structure that makes the phase word **useless as a
cipher keystream** is exactly what makes it a **good fragile watermark**.*

## 0. The Toy, Stated Plainly

The phase program ([The Phases of Collatz](library/the-phases-of-collatz.md))
produced an object with a rare combination of properties:

- **Deterministic and public.** $\phi(n) = \sigma(n)\bmod 3$ is fixed; anyone
  can compute it.
- **Sequentially computable, not compressible.** You get $\phi(n)$ by walking
  the trajectory; there is no closed form, no finite-state generator
  (subword complexity is exponential), no congruence rule (proved). Predictable
  by travelling the road, incompressible off it.
- **Grammar-constrained.** The phase word over $\{0,1,2\}$ refuses exactly
  $72$ hexagrams (and a regenerating frontier of longer words), with $36$
  forcing rules — a non-trivial, partly-understood language strictly between
  regular and free.
- **Self-coupled in three pieces.** Three projections of one trajectory —
  the value trace, the phase $\phi=\sigma\bmod 3$, the halving-parity
  $\pi = \sigma_T\bmod 2$ — are linked by exact arithmetic and must agree.
- **Verifiable by re-walking.** A claimed value is checked by recomputing it;
  forging a *consistent* trace means exhibiting a *real* Collatz trajectory.

Francesco's instinct: this looks like a key in three pieces that can
self-verify, and like a removable watermark — a background bias an honest
party can strip and a forger cannot. This paper takes that instinct, sweeps
the design space (signatures, counter-signatures, unlock keys, obfuscation
watermarks), measures the constructions that survive scrutiny, and is blunt
about the ones that do not. Everything numerical is reproduced by
`library/scripts/collatz_watermark_experiments.py` (measured at $n<2^{20}$).

## 1. The Honest Thesis: Structure Is the Signature, Not the Secret

The first temptation is to use the phase word as a **keystream**: generate a
pseudo-random-looking stream from a secret seed $n_0$, add it to data,
subtract it to decrypt. This is **wrong, and instructively so.** A good cipher
keystream must be statistically flat and unpredictable. The phase word is
neither:

- neighbours are correlated far above chance ($P(\phi(n)=\phi(n+1))=0.622$,
  decaying slowly — *local rigidity*);
- $47.7\%$ of consecutive pairs share an *exact* stopping time;
- the language has forbidden words and forcing rules.

Every one of these is a **distinguisher** — a statistical handle an adversary
uses to predict the stream and peel it off. As a confidentiality primitive the
Collatz phase is a non-starter, and no amount of engineering fixes it, because
the weakness *is* the mathematics.

But invert the lens. The same structure — rigidity, forbidden words, three-way
coupling — is precisely what a **watermark** wants: a recognizable, hard-to-
counterfeit fingerprint that an edit disturbs. You do not *hide* data with the
phase word; you *authenticate* data against it. This reframing is the spine of
the paper:

> **Thesis.** The Collatz phase functions are a *fragile-watermark and
> tamper-evidence* gadget, not an encryption primitive. Confidentiality, where
> needed, must come from standard cryptography; the phase layer contributes
> cheap, self-describing, incompressible, three-way-redundant *integrity and
> provenance*.

Stating this up front is not modesty — it is the security model. The rest of
the paper builds only on what survives it.

## 2. The Three-Piece Self-Verifying Tag

Francesco's "key in three pieces, self-verified" has a precise and honest
realization, and it is *not* the conservation law.

**What does not work: the constant-sum law.** The phase paper's identity
$A_0(n)+A_1(n)+A_2(n)=a_0+a_1+a_2$ (e.g. $=7$ for the cycle values) is true of
*any* ternary sequence stacked with its rotations. As the forbidden-words
notes warn, it is *identity, not rigidity*: it forbids nothing, so it detects
no tampering. A forger satisfies it for free. The three rotated phase variants
$\phi\circ T^0,\phi\circ T^1,\phi\circ T^2$ are likewise the *same word
rotated* — given one, the other two are determined — so they carry no
independent verification. Stacking rotations is bookkeeping, not security.

**What does work: three coupled projections of one trajectory.** Take the
seed $n_0$ and its genuine Collatz trajectory. It yields three streams of
different *kinds*:

$$
V = (n_0, T(n_0), T^2(n_0),\dots) \ \text{(value trace)}, \quad
\Phi = \phi(\cdot)\ \text{(phase, mod 3)}, \quad
\Pi = \pi(\cdot)\ \text{(halving-parity, mod 2)} ,
$$

linked by exact arithmetic: $\sigma_C = a+b$, $\sigma_T = a$, hence
$\Phi = (a+b)\bmod 3$ and $\Pi = a\bmod 2$, where $a,b$ count the halvings and
odd steps of $V$. The three pieces are **mutually consistent if and only if
they come from a real trajectory.** A verifier holding all three recomputes
$\Phi,\Pi$ from $V$ and checks equality and grammar compliance; a forger who
alters any piece must alter $V$ into another *bona fide* Collatz orbit to stay
consistent. This is an **algebraic-manipulation-detection-*flavoured*** tag:
not an information-theoretic AMD code (we claim no bound), but a tamper-evident
triple whose redundancy is arithmetic, not appended.

This is the correct reading of "three pieces": not three rotations of one word,
but three *projections of one road*, cross-checking each other. It is good for
**counter-signatures and audit** — three parties each custody one projection;
all three must agree for the tag to validate — and for **integrity of a
reconstructed key**, where the triple certifies that the reassembled secret
is the genuine one and not a manipulated near-miss.

## 3. The Fragile Watermark: Tamper-Evidence, Measured

The phase word's forbidden-word grammar is a *fragile watermark*: a genuine
trace never contains a forbidden window, so an edit that produces one is
detected by anyone, with no secret. We measured the detection rate at
$n<2^{20}$ (counts of forbidden windows: $72$ of $729$ at length $6$, $456$ of
$2187$ at length $7$, $2390$ of $6561$ at length $8$).

**Single-symbol substitution** (random position, flipped to a random other
symbol), probability some covering window becomes forbidden:

| grammar window length | $6$ | $7$ | $8$ |
|---|---:|---:|---:|
| $P(\text{detected})$ | $0.199$ | $0.219$ | $0.260$ |

**Burst of $k$ substitutions** in a 32-symbol block (length-8 grammar):

| $k$ | $1$ | $2$ | $3$ | $5$ | $8$ |
|---|---:|---:|---:|---:|---:|
| $P(\text{detected})$ | $0.260$ | $0.458$ | $0.572$ | $0.741$ | $0.860$ |

Read honestly: a *single* random edit is caught only about a quarter of the
time by one window grammar — this is a **weak per-symbol** fragile watermark.
But tampering is rarely one symbol, and detection compounds fast: eight edits
are caught $86\%$ of the time, and across a whole message of thousands of
symbols a genuine-vs-tampered decision is essentially certain (a real edit
must avoid every forbidden window over its entire span). Stacking the three
window lengths, and the binary $\pi$-grammar on top, raises the single-edit
rate further. The watermark's strength is *cumulative and free*: zero key,
zero stored side-information, detection by re-walking.

The phrase "removable only if you know how" gets its precise meaning here.
To *clean* an edit — change the data and restore a compliant trace — an
adversary must (i) know which map's grammar is in force, and (ii) re-derive
the trace, which requires the seed $n_0$. Without $n_0$ they can *detect-proof*
nothing and *repair* nothing: any edit they make trips the grammar at the
measured rate, and they cannot regenerate the legitimate mark. The watermark is
strippable by the issuer (who holds $n_0$) and fragile to everyone else.

## 4. Capacity: Where Payload Can Hide

If forced positions carry the watermark, the *free* positions can carry
payload — a covert channel. We measured the split (context length $5$,
$n<2^{20}$):

- $243$ distinct $5$-contexts occur (all of them);
- $36$ are **forcing** (one child — the next symbol is determined);
- $0$ are two-child; $207$ are **full** (all three children occur);
- position-weighted, only **$2.3\%$** of symbols sit after a forcing context;
- mean conditional entropy $H(\text{next}\mid 5\text{-context}) = 1.206$ bits,
  against the maximum $\log_2 3 = 1.585$.

So the channel offers about **$1.2$ payload bits per symbol**, while the
watermark is carried by the sparse $2.3\%$ forced positions plus the global
$1.2$-vs-$1.585$ entropy deficit that *any* compliant stream must exhibit. The
"never 1, never 3 children" pairing of the forbidden-words notes shows up here
as the clean $36 + 207$ split with no two-child contexts: the forcing is sharp
where it acts and absent elsewhere. A steganographic encoder fills free
positions with payload and lets the forced positions fall where the grammar
dictates; the carrier remains a valid phase trace, and the entropy deficit is
the watermark a censor cannot remove without making the stream *more* random
than any genuine trace — itself a detectable anomaly.

## 5. Keying: A Negative Result That Reshapes the Design

The attractive idea is a **secret grammar**: let the key choose which forbidden
language is in force, so an attacker who does not know the key cannot tell
compliant from tampered. We tested the most natural version — read the phase
word along a secret arithmetic progression $n \equiv r \pmod m$ — and it
**fails**:

- across $14$ scans ($m\in\{2,3,4,5\}$, all residues), only **$2$** distinct
  forbidden-hexagram sets arise: the original $72$, or the **empty set**;
- subsampling by $m>1$ destroys the rigidity — the thinned word realizes *all*
  $729$ hexagrams, so it forbids nothing.

The lesson is sharp and worth stating as a finding: **the forbidden-word
watermark lives on the consecutive-integer scan.** It is a property of reading
$n, n+1, n+2,\dots$, driven by trajectory coalescence between *neighbours*
(Law 4, $\sigma(8k+4)=\sigma(8k+5)$, and its hierarchy). Subsample, and the
coalescence correlations break, the rigidity evaporates, and the watermark is
gone. You cannot key the scan; the grammar is canonical to the consecutive
reading.

Consequently the grammar is **public**, not secret (indeed we published the
$72$ words). The genuine secret must live elsewhere:

- the **seed** $n_0$ and the **starting offset** — *where* in the line the
  legitimate trace sits;
- the **embedding schedule** $K$ — which positions of the data carry the mark
  — derived from a standard PRF;
- optionally the **map** ($3n+1$ full, the shortcut, an $a n+b$ variant with
  $a\le 3$ so $\sigma$ stays usable; recall $a>3$ diverges) — a small,
  low-entropy selector, at best a few bits of grammar choice ($72$ ternary
  words vs $2$ binary words vs the joint $\mathbb{Z}/6$ language).

So security reduces to standard secret-key authentication keyed by $(n_0,K)$;
the Collatz layer adds a self-describing, incompressible, three-way-redundant
mark, *not* a new hardness assumption. This is the honest perimeter, and the
failed scan-keying is what draws it.

## 6. Sequentiality: A Client Puzzle, Not a VDF

Computing $\sigma(n)$ is inherently **sequential** — walk the trajectory, no
known shortcut or parallelization — and the running time is *data-dependent*
and *unpredictable in closed form* (the $27\to 9232$ excursion is the famous
case). This is the shape of a **proof-of-sequential-work / client puzzle**:
hand out a seed, demand $\sigma$ and the three-piece tag, rate-limit by the
sequential cost.

It is **not a Verifiable Delay Function**, and the reason is exactly the
asymmetry a VDF needs and this lacks: VDF verification must be *fast* (much
cheaper than evaluation), but here verification is *also* sequential — the
verifier re-walks the same road. Without a succinct proof of the trajectory
(a SNARK over the Collatz step, which is possible but moves all the cost into
standard machinery), the gadget is a symmetric puzzle: useful for crude rate
limiting and for tying work to a specific seed, useless where cheap
verification is the point. Stated so no one mistakes it for more.

## 7. A Concrete Protocol: Fragile Provenance Watermark

Putting the survivors together, end to end.

**Setup.** Issuer holds a long-lived secret $n_0$ (a large seed) and a key
$K$ for a standard PRF $F_K$.

**Mark (per data stream $D$).**
1. Generate the phase trace $\Phi$ from $n_0$ (and its $\pi$ companion).
2. $F_K(\text{stream-id})$ selects an embedding schedule: a sparse set of
   positions in $D$ that will carry the mark, and an interleaving order.
3. At marked positions, weave in $\Phi$ (and $\pi$) so the marked subsequence
   is a genuine phase trace; payload occupies the free positions (Section 4).
4. Publish $D$ with the three-piece tag of Section 2 over the marked trace.

**Verify (anyone, with the issuer's public commitment to the trace).**
Re-derive the marked subsequence, check (a) grammar compliance of $\Phi$ and
$\pi$, (b) mutual consistency of the three projections, (c) match against the
issuer's commitment. Tampering is caught at the measured rates, escalating to
near-certainty over the full stream.

**Strip / re-mark (issuer only).** With $n_0$ and $K$ the issuer regenerates
the exact trace, removes or relocates the mark, and re-issues — the "removable
only if you know how" property, where *knowing how* is *holding $n_0$*.

**What an adversary can and cannot do.** Without $(n_0,K)$: cannot locate the
mark, cannot regenerate it, cannot edit $D$ without tripping the grammar
(measured per-edit and burst rates), cannot forge a consistent three-piece tag
without exhibiting a real trajectory. *Can*, because the grammar is public,
recognize that *a* phase trace is present and, in principle, synthesize *some*
compliant trace of *their own* seed — which is why the issuer's commitment to
the specific trace (standard signature over $n_0$'s public trace digest) is
load-bearing. The Collatz layer is the fragile, cheap, redundant fingerprint;
the unforgeability of *whose* fingerprint it is rests on the standard signature.

## 8. The Design Space, Swept

Francesco's candidate applications, judged:

- **Unlock key in three pieces** — *realistic, as integrity not secrecy.* The
  three-piece tag certifies a reconstructed key is the genuine one; the
  *secrecy* of the shares is whatever the sharing scheme provides, not the
  phase. Good as a robustness layer over standard secret sharing.
- **Signature / counter-signature** — *realistic as audit.* Three custodians,
  one projection each, all must agree; tamper-evident by arithmetic coupling.
  Not a public-key signature (no trapdoor); a *co-validation* mechanism.
- **Removable obfuscation watermark** — *the strongest fit*, Section 7;
  fragile, issuer-strippable, measured tamper-evidence.
- **Encryption / keystream bias** — *rejected*, Section 1; the structure is a
  distinguisher. If a *bias* is wanted purely for obfuscation (not security),
  the phase word serves, but must never be relied on for confidentiality.

## 9. What This Is Not (the load-bearing disclaimers)

- **Not a one-way function.** $\phi$ is easy forward and there is no trapdoor;
  "incompressible" means *no closed form*, not *hard to evaluate*.
- **Not confidentiality.** The phase word is a statistical sieve; see Section 1.
- **Not a VDF.** Verification is sequential, not succinct; Section 6.
- **Not keyed by the grammar.** The grammar is canonical and public; keying is
  $(n_0,K)$ in standard machinery; Section 5.
- **No security reduction.** Nothing here rests on a proof that Collatz is hard
  — it is not hard, it is incompressible — so there is no theorem to lean on.
  The constructions are *engineering with measured tamper-evidence*, and must
  be deployed as integrity layers atop primitives that *do* carry proofs.

## 10. Status and Open Problems

**Real and measured:** the structure-is-signature thesis; the three-projection
tamper-evident tag; per-edit ($\approx 0.20$–$0.26$) and burst ($0.86$ at
$k=8$) detection rates of the fragile watermark; the $2.3\%$-forced /
$1.206$-bit covert-channel capacity; the negative scan-keying result (the
watermark lives on the consecutive scan only).

**Open and worth doing:**
1. **Stronger fragile watermark.** Combine the ternary, binary, and joint
   $\mathbb{Z}/6$ grammars and the forcing rules into one detector; measure
   the single-edit rate. Target: push per-edit detection toward $1$ using all
   three projections at once.
2. **Succinct verification.** A SNARK/STARK over the Collatz step turns the
   client puzzle into a real VDF-like object — but then the Collatz part is
   cosmetic; quantify what, if anything, the phase structure adds over a
   generic sequential function.
3. **The covert channel, formally.** The $1.206$-bit capacity is an empirical
   conditional entropy; characterize the channel of compliant phase streams as
   a constrained code (its capacity is the topological entropy of the phase
   language — the very quantity the forbidden-words program is bounding).
4. **AMD bound or refutation.** Is the three-projection tag an AMD code with a
   provable manipulation-detection probability, or only heuristic? Settling
   this is the one place the toy could earn a theorem rather than a measurement.
5. **The honest ceiling.** As with the rest of the Collatz line in this
   library, the realistic product is an experimental-algorithms note and a
   clean integrity gadget — not a cryptographic primitive with a hardness
   proof. Recorded so future work does not re-inflate the claim.

## Reproduction

```bash
python3 library/scripts/collatz_watermark_experiments.py 20   # all four experiments
```

E1/E3 prints the tamper-evidence rates of Section 3, E2 the capacity split of
Section 4, E4 the scan-keying negative result of Section 5. The grammar data
come from `library/scripts/collatz_forbidden_words.py`; the binary companion
and the $\mathbb{Z}/6$ joint word from
`library/scripts/skycak_bridge_experiments.py`.

## References

- [The Phases of Collatz](library/the-phases-of-collatz.md) — phase transport
  calculus, incompressibility, the Koopman eigenfunction.
- [Notes on the Forbidden Words of the Collatz Phases](library/notes-on-the-forbidden-words-of-the-collatz-phases.md)
  — the $72$ words, the $36$ forcing rules, identity-versus-rigidity.
- [From Settling to Synchrony](library/from-settling-to-synchrony-expanding-skycaks-continuous-collatz.md)
  — the binary phase language and the joint $\mathbb{Z}/6$ word.
- Cramer, Dodis, Fehr, Padró, Wichs. "Detection of Algebraic Manipulation."
  *EUROCRYPT* (2008) — for the AMD framing referenced in Sections 2 and 10.