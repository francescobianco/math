---
title: "What If Fractals Don't Exist? The Mandelbrot Set Between a Wild Edge and a Finite Machine"
type: paper
created: 2026-06-13T18:30:00+00:00
updated: 2026-06-13T20:30:00+00:00
---

# What If Fractals Don't Exist? The Mandelbrot Set Between a Wild Edge and a Finite Machine

*A deliberately provocative essay with a serious core. The title is a goad, not
a thesis: the Mandelbrot **set** certainly exists, and we will lean on theorems
that prove how wild it is. The real question is narrower and sound — what is the
relationship between the mathematical set and the **picture** a finite machine
draws of it, given that the picture is always squeezed through a grid, a finite
iteration depth, and a finite precision? We retrace the simple algorithm,
measure (on the standard window) how the rendered region shrinks with iteration
depth and flips with the mantissa, and keep three registers strictly apart —
what is **proven**, what our **script measures**, and what is **metaphor**. The
constructive proposal that survives is a three-state rendering: certified-out,
certified-in, and an undecided band best drawn explicitly rather than papered
over.*

## Abstract

The Mandelbrot set is

$$
M \;=\; \bigl\{\, c \in \mathbb{C} : \text{the orbit of } 0 \text{ under }
z \mapsto z^2 + c \text{ stays bounded} \,\bigr\}.
$$

This is a clean, precise definition: $M$ is a perfectly real set. But *no
computer ever draws it.* What a machine draws is the level set of a finite
procedure governed by three quantizations — a **grid** (one pixel for a whole
square of parameters), a **depth cap** $N$ (we declare "bounded" anything that
has not escaped $|z|>2$ within $N$ steps), and a **precision** (float32,
float64, …). We measure the consequences on the standard window. The rendered
"inside" *shrinks monotonically* as $N$ grows — $54{,}318$ black pixels at
$N=50$, still falling to $51{,}555$ at $N=2000$, with no final value reached
within the depths we ran: the picture is an overcount, breathing inward with
every extra iteration. Switching float32 → float64 at fixed depth flips the
verdict of dozens of boundary pixels. And the **shadow zone** — pixels whose
in/out verdict changes when you nudge a machine parameter — does not shrink in
our experiment as the grid refines: its measured share of the boundary band
*rises*, $0.09 \to 0.17 \to 0.28$ from $300^2$ to $1200^2$ (an observed trend
over three resolutions, not a proven limit).

We then bound the provocation with the theorems. $M$ is connected
(Douady–Hubbard), and its boundary has **Hausdorff dimension $2$**
(Shishikura) — the wildness is a theorem about the true object, no computer
involved. So fractals *exist* as sets. Where the provocation has real bite is
one level down, and stated carefully: on the boundary $\partial M$ membership
is **not settled by the finite escape-time test** (only escapes are ever
certified in finite time; "never escapes" is not); local connectivity of $M$
(MLC) is a famous open conjecture; and genuine non-computability theorems exist
for related quadratic Julia sets (Braverman–Yampolsky). The honest conclusion
is neither "the fractal is real" nor "the fractal is fake," but a **three-state
object**: certified-out, certified-in, and an undecided band the finite render
must choose how to treat. We argue that the right rendering — and the right way
to *talk* about fractals — is a refining **mesh** that paints that band
explicitly, ideally with interval/ball arithmetic so the "certified" labels are
rigorous, rather than a crisp black-and-white that hides the choice.

Two threads deepen the essay past "approximation error." First, the machine
never iterates $f(z)=z^2+c$; it iterates a map reperturbed each step,
$\tilde z_{n+1}=\mathrm{fl}(\tilde z_n^2+c)$, so what it follows is a
**pseudo-orbit**, not the analytic orbit. *Shadowing theory* says a pseudo-orbit
faithfully tracks a true orbit in **hyperbolic** systems — the reason the bulk
of the picture is trustworthy — but the boundary is precisely the
**non-hyperbolic** locus where no such guarantee holds: there we have the least
right to claim the computed trajectory reflects a real one. Second, an
escape-time render asks, per pixel, a **Collatz question** ("does this infinite
orbit stay bounded?") and answers it by finite iteration — accepting for
Mandelbrot exactly the finite-trial evidence we reject for Collatz. That
**double pessimism** is justified only by the global theorems $M$ enjoys and
Collatz lacks; the honest residue of the provocation is that the hyperbolic
("trivial-destiny") parameters are what we can *certify*, the boundary is what we
mostly *infer*, and how much of the famous structure we have truly *observed*
rather than *deduced* is far less than the images suggest. This is the
Mandelbrot face of the same picture as *The Light Cone of Collatz*: the wild
thing we see owes part of its wildness to the finite machine that draws it.

All numerical claims are reproduced by
`library/scripts/mandelbrot_shadow_zones.py`.

---

## 1. The provocation

Here is a sentence designed to irritate: *the Mandelbrot set you have seen does
not exist.* Not the famous beetle-shaped body — that is solid and real — but
the thing everyone actually means by "the fractal": the infinitely fine lace at
the edge, the seahorse valleys, the dust of mini-brots, the filaments that keep
unfolding as you zoom. The claim of this paper, stated at its most extreme so
we can then measure exactly how much of it survives, is:

> What we render at the boundary may not be an approximation of a real curve.
> It may be a **hysteresis** — a smeared, machine-dependent skin — produced by a
> quantization of arithmetic we cannot escape, because the frontier is unstable
> and complex precisely where our numbers run out. Change the precision and the
> lace moves. Maybe there is nothing underneath it to approximate; maybe the
> lace *is* the finitude of the machine, made visible.

A pure point-by-point analytic settlement is not on the table: deciding whether
a single boundary parameter $c$ belongs to $M$ by escape-time alone can require
following an orbit without bound. So we cannot answer the provocation pixel by
pixel. We can do two better things. We can examine how much the picture depends
on the machine (§§2–6) — including the subtle point that the computer never even
follows the true orbit (§6) — and we can **bound** the provocation with what is
actually proven (§§7–8). The gap between those two is where the real content
lives (§9).

### A note on register

Because this is a provocative essay about a precise object, it is easy to slide
from a metaphor into an apparent claim. To prevent that, the paper keeps three
registers explicitly separated, and we tag which is which throughout:

- **Theorem** — what is mathematically proven, with attribution (Douady–Hubbard
  connectedness; Shishikura $\dim_H \partial M = 2$; Braverman–Yampolsky
  non-computability of certain Julia sets). These stand independent of any
  computation.
- **Experiment** — what the companion script *measures* on a specific window,
  grid, depth, and precision. These are observations over a finite range, not
  laws; where a trend appears (e.g. the shadow share rising with resolution) it
  is reported as a measured trend, and we do **not** claim a proven limit.
- **Metaphor** — the narrative images ("breathes," "shadow," "the lace is the
  machine"). These carry intuition and nothing more; no argument rests on them.

Whenever the three could be confused, the sentence says which one it is.

---

## 2. The algorithm, retraced honestly

The construction is famously simple. Fix a parameter $c \in \mathbb{C}$. Start
at $z_0 = 0$ and iterate

$$
z_{n+1} \;=\; z_n^2 + c.
$$

There is one classical fact that makes the picture computable at all: if ever
$|z_n| > 2$, the orbit escapes to infinity and $c \notin M$. So the rule is:

```
   z = 0
   repeat up to N times:
       z = z*z + c
       if |z| > 2:  return "ESCAPED at step n"   # c is OUTSIDE, color by n
   return "still bounded"                         # paint c BLACK = INSIDE
```

Read that last line slowly, because it is the whole problem. **"Paint it
black" is not a measurement; it is a confession of ignorance.** It does not
say "$c$ is in the set." It says "$c$ has not escaped *yet*, within $N$ steps,
at this precision." Every black pixel is a *hypothesis that the machine ran out
of patience before disproving*. The interior of $M$ is full of points that
genuinely never escape — those hypotheses are true. But the black band hugging
the boundary is full of points that *would* escape at step $N+1$, or $N+1000$,
or that escape in exact arithmetic but not in float64. The black is a mixture
of knowledge and fatigue, and from the image alone you cannot tell which pixel
is which.

So the picture we call "the Mandelbrot set" is really the set

$$
M_N^{(p)} \;=\; \bigl\{\, c \text{ on the grid} : |z_n| \le 2 \text{ for all }
n \le N, \text{ computed in precision } p \,\bigr\},
$$

a three-parameter family of finite approximations. The mathematical $M$ is a
limit these never reach: $M = \bigcap_N \{ c : |z_n|\le 2\ \forall n \le N \}$,
an intersection of *infinitely many* shrinking sets. We draw one term of the
sequence and call it the limit. The rest of this paper is about how badly that
substitution behaves at the edge.

---

## 3. Three quantizations we cannot avoid

Every rendered fractal is squeezed through three finite sieves.

**Grid.** A pixel is not a point; it is a little square of parameter values, and
the renderer samples *one* representative. Where the set is smooth (deep
interior, deep exterior) the representative is honest — its neighbours agree.
Where the boundary is intricate, a single pixel straddles structure finer than
itself, and the one sample it took is a coin flip among disagreeing neighbours.
Since (we will see) the boundary has dimension $2$, *no* pixel size ever makes
the boundary "thin": at every zoom the boundary fills area, and the grid is
always too coarse for it.

**Depth.** $N$ is finite. Points that escape just after the cap are misfiled as
inside. As $N \to \infty$ the black thins toward the true $M$ — but it thins
*forever*, never arriving, and §4 shows it is still visibly moving at
$N=2000$.

**Precision.** Floating point replaces $z_{n+1} = z_n^2 + c$ with
$z_{n+1} = \mathrm{fl}(z_n^2 + c)$, an error of order $10^{-16}$ per step.
On the boundary the dynamics is *chaotic in $c$* — the boundary of $M$ is,
locally, where the parameter sits on the Julia set's bifurcation locus, and
nearby orbits separate exponentially. A rounding error of $10^{-16}$, amplified
exponentially, decides escape-or-not within a few dozen steps. §5 measures the
flips.

None of the three is removable. You cannot render with infinite grid, infinite
depth, or infinite precision. The question is not *whether* the picture is
quantized — it always is — but *how much of what we see is the set and how much
is the sieve.*

---

## 4. The boundary breathes with depth

Run the escape-time render on the standard window
$[-2.5, 1] \times [-1.5, 1.5]$ at a $600 \times 600$ grid and count the black
("inside") pixels as the depth cap $N$ climbs:

| $N$ | $50$ | $100$ | $200$ | $500$ | $1000$ | $2000$ |
|---|---:|---:|---:|---:|---:|---:|
| black pixels | $54{,}318$ | $52{,}872$ | $52{,}180$ | $51{,}768$ | $51{,}622$ | $51{,}555$ |
| lost since previous | — | $1446$ | $692$ | $412$ | $146$ | $67$ |

(*Experiment.*) The rendered "set" shrinks at every increase of $N$ across the
range we ran, and has not settled by $N=2000$. Each increase exposes another
ring of pretenders — pixels that looked bounded only because the machine gave up
too early — and peels them off the black body. The per-step losses shrink
($1446 \to 67$) but remain positive: at $N=2000$ we are still losing dozens of
pixels per refinement. We do not claim the count never converges — monotone
bounded sequences do converge, and on the true interior it converges to the
genuine area; the measured fact is only that *within the depths we tested it is
still visibly moving.* (*Metaphor.*) The boundary "breathes inward" with
computational patience: the crisp curve you remember was a single frame, frozen
at whatever $N$ your renderer happened to use.

This is the first concrete sense in which the rendered area is machine-made: at
finite $N$ it is an overcount that depends on $N$, not yet a property of $M$.

---

## 5. The mantissa decides

Now hold the depth fixed at $N=1000$ and change only the arithmetic. On the
same $600 \times 600$ grid, the float32 render and the float64 render disagree
on the in/out verdict of **$72$ pixels** — about $0.02\%$ of the frame, and a
much larger fraction of the boundary band. These are not random pixels
scattered over the plane; they sit in a thin seam along $\partial M$, exactly
where the script's third experiment localizes the shadow.

Seventy-two pixels sounds small until you say what it means: *there exist grid
parameters whose classification by the renderer is decided by the $24$th versus
the $53$rd bit of the mantissa.* For those pixels, "does the program call it
inside?" has the answer "depends which floating-point type you compiled with."
Note the careful phrasing: this is a statement about the **render's verdict**,
not about true membership in $M$ — the true $c$ either is or is not in $M$,
independent of arithmetic; what flips is the machine's report. That report is
still what every published image *is*, so the dependence is real where it
matters. (*Metaphor, the provocation's word.*) One might call this a
**hysteresis** — like a magnet that remembers its history, the rendered boundary
remembers the machine that drew it — but the literal content is just the $72$
measured flips.

---

## 6. The deeper problem: we never iterate the orbit, only a pseudo-orbit

The depth cap and the mantissa flips are still, in a sense, *bookkeeping* errors
— wrong verdicts about the right object. There is a deeper issue, and it is the
real heart of the worry, distinct from the three-state problem of §9. It is not
that we might mislabel a point. It is that **the trajectory the computer follows
is not the mathematical orbit at all.**

The dynamics is $z_{n+1} = f(z_n)$ with $f(z) = z^2 + c$. But the machine does
not iterate $f$. At each step it computes

$$
\tilde z_{n+1} \;=\; \mathrm{fl}\!\left(\tilde z_n^{\,2} + c\right)
\;=\; f(\tilde z_n) + \varepsilon_n,
\qquad |\varepsilon_n| \sim 10^{-16},
$$

a *different, freshly perturbed map at every step*. In most numerical tasks this
is harmless: evaluate $\sin(1)$ and the rounding error stays where it is, a
final-digit nuisance. **Iteration is the exception**, because the error of today
becomes the input of tomorrow: $\varepsilon_n$ is fed back in and propagated by
all subsequent steps. What the machine produces is therefore not a sampled orbit
but a **pseudo-orbit** — the exact term from dynamical-systems theory — a
sequence $(\tilde z_n)$ in which every term carries the compounded history of
every rounding before it.

So the honest description of an escape-time render is brutal: *for each pixel we
follow a pseudo-orbit of a map that changes every step, and report whether
**that** stays bounded* — and then we attribute the answer to the analytic orbit
of $f$, which we never computed.

When is this attribution safe? This is exactly the subject of **shadowing
theory**. A pseudo-orbit is said to be *shadowed* if there exists a true orbit
(of a possibly slightly different starting point) that stays uniformly close to
it. The **shadowing lemma** guarantees this in *hyperbolic* (uniformly
expanding/contracting) systems: there, the computed pseudo-orbit, though not the
orbit you asked for, faithfully tracks *some* genuine orbit, and the picture is
trustworthy. For $c$ in the exterior or in a hyperbolic interior component, the
dynamics of $z^2+c$ is hyperbolic and shadowing applies — which is the rigorous
reason the *bulk* of the Mandelbrot picture is reliable.

On $\partial M$, however, hyperbolicity fails. The boundary is precisely the
non-hyperbolic locus — neutral cycles, parabolic points, Siegel disks, the
infinitely renormalizable parameters — where local expansion can amplify the
$10^{-16}$ seed without the compensating structure that the shadowing lemma
needs. There is no general theorem that boundary pseudo-orbits are shadowed.
So at the very place where the picture is most intricate and most celebrated, we
have the least right to claim the computed trajectory reflects a real one.

This sharpens the provocation into its strongest defensible form — and we state
it as a careful claim, not a slogan:

> The mathematical fractal exists (§7). But **no numerical image follows the
> analytic orbits of the boundary points**; it follows pseudo-orbits produced by
> an infinite succession of quantizations. It is open, in general, how much of
> the fine boundary structure we observe is a property of the analytic object
> and how much is a *robust property of the quantized dynamics* that approximates
> it — robust enough to survive rounding (and thus reproducible across machines)
> without being a faithful shadow of any single true orbit.

That last possibility is the genuinely interesting one, and it is *not* the same
as "the boundary is noise." A feature can be **reproducible across precisions
and machines** — everyone's renderer shows the same seahorse — and still be a
property of the *family* of quantized maps rather than of the exact map $f$. The
shadowing question is precisely: are the reproducible features we see the
fingerprints of the analytic object, or the stable artifacts of approximating it
with finite arithmetic? In the hyperbolic bulk, theorems say the former. On the
boundary, the question is open, and this paper's contribution is to insist it be
asked rather than assumed away.

This is the same move as everywhere in this notebook's Collatz work: an infinite
iteration observed through a finite machine confronts us with a choice between
the object and its **computational shadow**, and the honest stance is to mark
which one a given pixel, or a given orbit, actually reports.

---

## 7. But the set exists — and is provably wild

If the paper stopped here it would be sensational and wrong. So now the
correction, and it is decisive. The Mandelbrot set is *not* a computational
mirage. Two theorems, proved with no computer anywhere in them:

- **Connectedness (Douady–Hubbard, 1982).** $M$ is connected — in fact its
  complement is conformally a disk. The body is one piece, rigorously.
- **The boundary has Hausdorff dimension $2$ (Shishikura, 1991).**
  $\dim_H \partial M = 2$ — the maximum possible in the plane. The boundary is
  not a thin curve we are merely failing to resolve; its complexity is genuinely
  $2$-dimensional. (One thing this does *not* settle: whether $\partial M$ has
  positive Lebesgue *area* is a separate, still-open question — dimension $2$ is
  weaker than positive area. We claim only the dimension.)

Shishikura's theorem is the hinge of this paper. It says the wildness we see is
**real**, a property of the true set, independent of every machine. The lace is
not invented by the renderer — there really is structure at every scale, more
than any curve could hold. So "fractals don't exist" is **false** as a
statement about the object: $M$ exists, it is connected, and its edge is as
intricate as mathematics allows.

What Shishikura *also* tells us, though, is why §§4–6 had to happen. A boundary
of dimension $2$ is the worst possible case for a finite grid: it cannot be
covered efficiently, it never thins, and any pixelation straddles infinite
detail forever. The realness of the wildness and the unavoidability of the
quantization are **the same fact** seen from two sides. The set is real
*because* it is wild; the picture is machine-dependent *because* it is wild.

---

## 8. Where the provocation has real bite: the edge as a decision problem

So the body is real and the wildness is real. Is anything left of the goad in
the title? Yes — but it must be stated with care, because the strong version
("membership is undecidable") would be false, and the careful version is what is
actually true.

**What the escape-time test can and cannot settle.** For $c$ outside $M$ the
orbit crosses $|z|>2$ at some finite step, and the renderer certifies "outside"
the moment it does. For $c$ in a hyperbolic interior component the orbit is
attracted to a cycle and one can certify "inside" in finite time *once the cycle
is located*. But the plain escape-time loop — the one everybody runs — never
certifies "inside": it only ever runs out of patience. For $c$ on $\partial M$
the orbit neither escapes nor settles to an attracting cycle, so the escape-time
test **returns no verdict at any finite $N$**. This is a statement about *that
algorithm*, not a claim that membership is logically undecidable in the
Turing sense; $M$ as a whole is widely expected to be computable in the sense of
computable analysis (it would follow from MLC). The precise, defensible claim
is: *the finite escape-time procedure decides the exterior and the hyperbolic
interior, and is silent on the boundary, where it substitutes "hasn't escaped
yet" for an answer.*

**Local connectivity is open (MLC).** Whether $M$ is locally connected — whether
the boundary behaves tamely enough that the filaments connect up the way the
pictures suggest — is a **major open conjecture** (it would imply density of
hyperbolicity for the quadratic family). If MLC holds, the picture is, in a
precise sense, "what you think it is." If it fails, the edge hides behavior no
finite zoom has shown us. We do not know. The thing the pictures most strongly
assert — that the lace is a connected, locally-tame curtain — is *unproven*.

**Genuine non-computability nearby.** This is not idle worry. Braverman and
Yampolsky proved that there exist **quadratic Julia sets that are not
computable**: no algorithm computes them to guaranteed accuracy. The Julia sets
are the per-$c$ companions of the Mandelbrot picture, so "draw the filled
dynamics of $z^2+c$" is, for some parameters, a *formally uncomputable task*.
This is a theorem about Julia sets, not directly about $M$ — the computability
of $M$ itself is a separate, subtler question tied to MLC — but it shows the
neighbourhood of the problem genuinely contains non-computable objects, so the
worry is not rhetorical.

Put together, carefully: the **edge of the Mandelbrot picture is where the
standard finite procedure stops giving answers**, where a major tameness
conjecture is open, and where provably non-computable cousins live next door.
That is the sound residue of the provocation — not "the set is undecidable,"
but "the *edge* is exactly where finite rendering must guess, and where the
mathematics declines to promise it guessed right."

---

## 9. The honest object: a mesh of shadow zones

The two halves now fit. The set is real (§7); on the boundary the finite
escape-time procedure gives no answer (§8), our arithmetic is finite, and the
trajectory itself is only a pseudo-orbit (§§3–6).
The constructive response — and this is the part of the paper closest to a usable
technique — is not to draw a crisp black-and-white that hides the guess, but to
draw **what the machine actually knows** — a three-state map:

- **OUT** — certifiable: the orbit has escaped (rigorously, once $|z|>2$; with
  interval arithmetic, once the whole cell escapes).
- **IN** — certifiable: the cell provably lies in a known hyperbolic component
  (an attracting cycle can be exhibited in finite time).
- **SHADOW** — undecided at this budget: neither certificate is in hand.

In the script we use a *sampled* proxy for the shadow — cells whose verdict
**flips under a change of machine parameter** (raise the depth cap, or change
the precision). That is a cheap stand-in, not a rigorous certificate; the
rigorous version replaces point sampling with interval/ball arithmetic, where
OUT and IN become genuine proofs and SHADOW is "no proof either way yet." The
figure below paints the sampled shadow red.

![The Mandelbrot set as a three-state picture on the standard window. Near-white is the (sampled) interior, dark blue-black is the certified exterior, and the red skin is the SHADOW: pixels whose in/out verdict flips when the iteration cap or the floating-point precision is changed. Measured, the red is not scattered noise but a coherent band clinging to the boundary — the locus where this render's verdict is parameter-dependent. The interior/shadow split here is sampled, not interval-rigorous; see the text.](library/images/mandelbrot-shadow-zones.png)

(*Experiment.*) The interesting measurement is what the sampled shadow does as
you **refine the grid**. Naively, finer pixels should resolve more, so the
undecided fraction should fall. Over the three resolutions we ran it does the
opposite. Taking the shadow's share of the boundary band (so the trivial
interior and exterior do not dilute it):

| grid | shadow pixels | boundary-band pixels | shadow / boundary |
|---|---:|---:|---:|
| $300^2$ | $146$ | $1614$ | $0.09$ |
| $600^2$ | $670$ | $3901$ | $0.17$ |
| $1200^2$ | $2697$ | $9485$ | $0.28$ |

The undecided skin's share of the boundary band *rises* across these three
samples, $9\% \to 17\% \to 28\%$: refining the grid revealed *more* undecided
boundary, not less. We state this as an observation, not a law — three points
do not establish a limit, and the trend surely depends on the fixed depth and
precision used to define the proxy. What we will say is the weaker, defensible
thing: the measurement gives **no sign** that the undecided band is a transient
that finer pixels dissolve, and that is consistent with — though it does not
prove — the theorem that $\partial M$ has dimension $2$ (Shishikura), under
which there is always more boundary to resolve at finer scales. The honest
reading is that the shadow band behaves like a feature of the picture, not like
noise to be polished away; whether its share has a positive limit is left open.

This is the constructive proposal the provocation leads to. Replace the
fictional crisp curve with a **refining mesh of shadow zones**: a quadtree that
certifies OUT and IN cells (ideally with interval / ball arithmetic, so the
certificates are rigorous rather than sampled), and recurses *only* into the
shadow, painting it honestly at each depth. Such a render never lies about a
boundary pixel; it says "undecided, here is how much budget it would take to
try." It is the cartographer's discipline applied to a coastline of dimension
$2$: draw the land, draw the sea, and draw — in a third color — the tide.

---

## 10. Mandelbrot is a continuous Collatz — and the double pessimism

This is not an isolated provocation; it is the second instance of a single
thesis, and the comparison repays being made exact. In *The Light Cone of
Collatz* we argued that the "crazy crests" of Collatz — orbits soaring to
thousands before collapsing — are the **shadow** a finite integer lattice casts
on a smooth continuous descent to the vertex of a cone; the descent is provably
calm, only its sampling is jagged. There, too, the infinite application of a
confined map is *sensitive to quantization*, so numerical iteration of the
continuous model is not a valid verification — only analysis is.

Now look at what an escape-time render actually does. For each parameter $c$ it
launches the orbit

$$
0,\ c,\ c^2 + c,\ (c^2+c)^2 + c,\ \ldots
$$

and asks the one question: *does this stay bounded?* That is structurally a
**Collatz question, one per pixel**. Each $c$ carries its own infinite iteration
with its own unknown fate; the Mandelbrot set is, quite literally, a *continuous
Collatz parametrized by $c$* — a whole plane of "does this orbit settle or run
away?" conjectures, decided in parallel. And we decide each one the way we are
told *not* to decide Collatz: by running finitely many steps and trusting the
trend.

This exposes a real asymmetry of attitude — call it the **double pessimism**.
For Collatz we are rigorists: a verification to $2^{68}$ is "not a proof," and
we are right to say so. For Mandelbrot we are credulists: we run a few hundred
iterations per pixel, in float64, along a pseudo-orbit (§6), and frame the
result. The same epistemic move — finite iteration of an infinite process,
reported as the truth about its limit — is treated as worthless in one place and
as a poster in the other. The user's sharp question follows naturally:

> If we will not accept verified Collatz cases as proof, why do we accept the
> rendered Mandelbrot boundary as an object? Could $M$ "exist" only on its
> trivial points — the certifiable hyperbolic interior — while the whole
> filigree edge is a computational illusion?

Here is where intellectual honesty requires us to *part* from the strong form of
the provocation, and to say exactly why. The cases are **not** symmetric, and
the asymmetry is not prejudice — it is the presence or absence of theorems:

| | Collatz | Mandelbrot |
|---|---|---|
| definition | a *conjecture* about iterates ("all orbits reach $1$") | a *definition* of a set ("$c$ with bounded orbit") |
| global theorems | essentially none — we do not know if another cycle exists, or a divergent orbit | many: connectedness, $\dim_H\partial M=2$, infinitely many mini-copies, classified hyperbolic components |
| source of confidence | finite verification only | decades of complex analysis, *not* the colored pictures |
| status of the wild part | wholly open | constrained by proof, though MLC keeps part of it open |

For Collatz the wildness is genuinely unconstrained: there could be a second
cycle, a divergent ray, an infinite set of counterexamples, and nothing we have
forbids it. For Mandelbrot the wildness is *fenced in by proofs that used no
computer*: the boundary's dimension, the connectivity of the body, the infinite
cascade of mini-Mandelbrots are theorems. So "$M$ exists only on the trivial
points" is very hard to maintain — the non-trivial structure is guaranteed to
be there whether or not any pixel is honest about it.

But — and this is the version of the user's idea that *survives*, and it is
worth more than the slogan — there is a precise sense in which the boundary is
"the place where the trivial points run out." The interior is a union of
**hyperbolic components**, each certifiable in finite time by exhibiting an
attracting cycle; those are the "universal-destiny" parameters, the analogue of
Collatz's numbers with a known fate. The boundary is exactly the **non-
hyperbolic locus** — neutral, parabolic, Siegel, infinitely renormalizable —
where no such finite certificate exists and where, by §6, even our trajectory is
only a pseudo-orbit. So the honest restatement of "maybe only the trivial points
exist" is:

> The hyperbolic (trivial-destiny) parameters are the part we can *certify*; the
> boundary is the part we mostly *infer*. Whether hyperbolic parameters are even
> dense in the boundary is the content of MLC — still open. The structure is
> real (theorems), but how much of it we have genuinely *observed*, as opposed to
> *deduced*, is far less than the glossy images suggest.

And that is the most defensible and most interesting thing to say. Strip away
the theorems and keep only the renders, and the user's scepticism would be very
hard to refute: our confidence in the Mandelbrot boundary rests almost entirely
on complex analysis, hardly at all on the pictures — which, as §§4–6 show, are
machine-dependent pseudo-orbit reports at exactly the place that matters.

The discipline, in both worlds, is therefore the same: separate the provable
body from the quantization skin; refuse to iterate quantization-sensitive
dynamics in floating point and call the result truth; mark each pixel and each
orbit with which register it belongs to. (*Metaphor.*) The Mandelbrot lace and
the Collatz crest are two shadows of one sun — a line to remember the idea by,
not to prove anything with.

---

## 11. Conclusion

Do fractals exist? The honest answer is a careful *yes — but the picture is not
the set.* (*Theorem.*) The Mandelbrot set exists, is connected, and has a
boundary of the maximal dimension $2$: its wildness is proven, not a rendering
bug. (*Experiment.*) And yet no image of it is the set: every render is a
three-parameter object $M_N^{(p)}$ whose area shrinks with the depth cap
(still moving at $N=2000$ in our runs), whose boundary pixels can be decided by
the mantissa ($72$ flips between float32 and float64), and whose sampled
undecided band did not shrink but rose as a share of the boundary across the
three resolutions we tried ($9\% \to 28\%$ — a measured trend, not a limit).
The lace is neither pure object nor pure artifact; it is the **negotiation**
between a provably wild edge and an unavoidably finite machine.

Two things deepen this past the easy "approximation error." First, the machine
never even follows the orbit it claims to: it follows a **pseudo-orbit** of a
map reperturbed at every step (§6), and only in the hyperbolic bulk does
shadowing theory promise that pseudo-orbit tracks a real one. On the boundary —
the interesting part — that promise is absent. Second, the operation we perform
is, per pixel, a **Collatz question** — "does this infinite orbit stay bounded?"
— answered by finite iteration; and we accept for Mandelbrot exactly the
finite-trial evidence we reject for Collatz (§10). The asymmetry is justified
only by the global theorems $M$ enjoys and Collatz lacks; strip the theorems and
keep the pictures, and the scepticism would be hard to answer.

The goad in the title resolves like this: "fractals don't exist" is false about
the set and only *half* true about the picture — what we call the fractal is, at
its edge, partly the record of a finite computation following a pseudo-orbit and
guessing where its standard procedure goes silent. The remedy is not more pixels
but more honesty: draw the certified land, the certified sea, and — in a third
colour — the band between them, with interval arithmetic so the two certified
colours are proofs; and never confuse a reproducible feature of the *quantized*
dynamics with a property of the analytic object until shadowing says you may.
(*Metaphor, to close.*) The fractal we can draw truthfully is a map of our own
resolution; the one underneath, real and dimension-$2$ and perhaps not even
locally connected, keeps its own counsel just past the last bit of the mantissa.

---

## Reproducing the Results

All numerical claims are reproduced by:

```
python3 library/scripts/mandelbrot_shadow_zones.py
```

The script measures, on the standard window $[-2.5,1]\times[-1.5,1.5]$: the
depth-breath of the black region (inside-pixel count versus the iteration cap
$N$, monotonically shrinking and still moving at $N=2000$); the float32-versus-
float64 verdict flips at fixed depth ($72$ pixels on a $600^2$ grid); and the
shadow-zone fraction — pixels whose in/out verdict changes under a change of
depth or precision — relative to the boundary band, across grids $300^2$,
$600^2$, $1200^2$ (share growing $0.09 \to 0.17 \to 0.28$). It also renders the
three-state figure `library/images/mandelbrot-shadow-zones.png` (out / in /
shadow). The reported share rise $0.09 \to 0.17 \to 0.28$ is a measured trend
over three resolutions, not a proven limit. The "certified" labels here are
sampled, not interval-rigorous; a fully certified mesh would replace point
sampling with interval / ball arithmetic, turning the OUT and IN colours into
genuine proofs. The measurements give no sign that the undecided band is a
transient that finer pixels dissolve, which is consistent with — but does not by
itself prove — Shishikura's $\dim_H \partial M = 2$.
