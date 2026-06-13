---
title: Notes on the Music of the Collatz Phases
type: notes
created: 2026-06-10T23:30:00+00:00
updated: 2026-06-10T23:30:00+00:00
---

# Notes on the Music of the Collatz Phases

Working notes for the sonification of the phase sequence studied in
[The Phases of Collatz](library/the-phases-of-collatz.md). Kept as a
standalone work item so it can be picked up later.

## The Metaphor, Made Exact

The guiding image: the phase word $\phi(1)\phi(2)\phi(3)\cdots$ is background
music with a recognizable melody that cannot be compressed into a repeating
tune. Every clause of the image corresponds to an established fact:

| Musical clause | Mathematical fact |
|---|---|
| recognizable melody | local rigidity: $62\%$ of consecutive integers share a phase |
| rules of harmony | forbidden words: from length $6$ on, $72$ figures never occur |
| no repeating refrain | theorem: no translational period, for any modulus |
| no mechanical canon | finite-state formulas excluded: subword complexity is exponential |
| transposition canon | exact: $\times 2$ rotates the three phases, $\times 8$ is the identity |
| background pedal | the uniform $1/3$ density under the oscillating part $\tfrac{2}{3}\cos(2\pi\sigma/3)$ |

The transposition structure is precisely that of a **Shepard scale**: the
piece is periodic in pitch-space (period: three octaves of $n$), aperiodic in
time. The honest one-line description: *an improvisation obeying a rigorous
harmony and an exact transposition canon, whose score nobody has found — and
finding the score is worth the Collatz conjecture.*

## The Sonification

Mapping: the three phases go to the major triad,

$$
\phi=0 \mapsto \mathrm{C4},\qquad
\phi=1 \mapsto \mathrm{E4},\qquad
\phi=2 \mapsto \mathrm{G4}.
$$

Implementation: [`library/scripts/sonify_collatz_phases.py`](library/scripts/sonify_collatz_phases.py)
(numpy + stdlib `wave`, no other dependencies). Usage:

```bash
python3 library/scripts/sonify_collatz_phases.py            # n = 1..1024, 90 ms per note
python3 library/scripts/sonify_collatz_phases.py 256 80     # shorter sample
```

Output: `library/audio/collatz-phases.wav` (22050 Hz, mono). A 20-second
sample for $n\le 256$ is checked in.

## What to Listen For

1. **Repeated notes far beyond chance** — the local rigidity. Long plateaus
   of the same note are coalescing trajectories beating in unison.
2. **The absent figures** — by theorem-level statistics, twelve immediate
   repetitions of a three-note zigzag figure (such as C–E–C–C–E–C) never
   occur. See the companion note on forbidden words.
3. **No chorus** — wait as long as you like: the piece provably never enters
   a loop.

## Possible Extensions

- Render each octave $[2^j, 2^{j+1})$ as a separate voice to make the
  transposition canon audible (each octave should sound like the previous
  one rotated C→E→G→C).
- Sonify $\Delta\phi$ instead of $\phi$ (intervals instead of notes): the
  symmetry $P(\Delta\phi=1)=P(\Delta\phi=2)$ should make it directionless.
- Slow the tempo with $\log n$ so each octave takes equal time — the
  Shepard structure then becomes literal.