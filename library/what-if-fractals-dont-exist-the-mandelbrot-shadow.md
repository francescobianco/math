---
title: "What If Fractals Don't Exist? The Mandelbrot Set as the Shadow of an Undecidable Edge"
type: paper
created: 2026-06-13T18:30:00+00:00
updated: 2026-06-13T18:30:00+00:00
---

# What If Fractals Don't Exist? The Mandelbrot Set as the Shadow of an Undecidable Edge

*A deliberately provocative study. We suspect that the lacy filaments we draw
at the edge of the Mandelbrot set are not an approximation of a real object but
an **artifact of quantization we cannot avoid** — a controlled hysteresis whose
shape is set by the precision of our machines. We retrace the simple algorithm,
measure how the boundary "breathes" with iteration depth and flips with the
mantissa, and then land the provocation honestly: the **set** exists and is
provably wild, but the **image** is a negotiation with an edge that finite
computation cannot resolve. The right object to draw is not a curve but a
**mesh of shadow zones** — a three-state map of what the machine can and cannot
decide.*

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
$N=50$, still falling to $51{,}555$ at $N=2000$, never settling: the picture is
always an overcount, breathing inward with every extra iteration. Switching
float32 → float64 at fixed depth flips the verdict of dozens of boundary
pixels. And the **shadow zone** — pixels whose in/out verdict changes when you
nudge a machine parameter — does *not* shrink as the grid refines: its share of
the boundary band *grows*, $0.09 \to 0.17 \to 0.28$ from $300^2$ to $1200^2$.

We then correct the provocation with the theorems. $M$ is connected
(Douady–Hubbard), and its boundary has **Hausdorff dimension $2$**
(Shishikura) — the wildness is a theorem about the true object, no computer
involved. So fractals *exist* as sets. Where the provocation bites is one level
down: the boundary $\partial M$ is exactly where membership is **undecidable in
finite time**, local connectivity of $M$ (MLC) is a famous open conjecture, and
genuine non-computability theorems exist for related Julia sets
(Braverman–Yampolsky). The honest conclusion is neither "the fractal is real"
nor "the fractal is fake," but a **three-state object**: certified-out,
certified-in, and an irreducible shadow skin the machine cannot resolve. We
argue that the correct rendering — and the correct *epistemology* of fractals
— is a refining **mesh** that paints that shadow explicitly rather than lying
in crisp black and white. This is the Mandelbrot face of the same thesis as
*The Light Cone of Collatz*: the wild thing we see is the shadow a finite
machine casts on an edge it cannot decide.

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
a single boundary parameter $c$ belongs to $M$ can require following an orbit
forever. So we cannot answer the provocation pixel by pixel. We can do two
better things. We can **measure** how much the picture depends on the machine
(§§2–5), and we can **bound** the provocation with what is actually proven
(§§6–7) — and the gap between those two is where the real, surprising answer
lives (§8).

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

The rendered "set" **shrinks at every step and never stops**. Each increase of
$N$ exposes another ring of pretenders — pixels that looked bounded only because
the machine gave up too early — and peels them off the black body. The losses
shrink ($1446 \to 67$) but stay positive: at $N=2000$ we are still losing
dozens of pixels per refinement, with no sign of a final value. The boundary
**breathes inward** with computational patience. Whatever crisp curve you think
you saw, you saw a frame of an animation that never ends, frozen at whatever $N$
your renderer happened to use.

This is the first concrete sense in which the picture is machine-made: its very
*area* is a function of $N$, not a property of $M$.

---

## 5. The mantissa decides

Now hold the depth fixed at $N=1000$ and change only the arithmetic. On the
same $600 \times 600$ grid, the float32 render and the float64 render disagree
on the in/out verdict of **$72$ pixels** — about $0.02\%$ of the frame, and a
much larger fraction of the boundary band. These are not random pixels
scattered over the plane; they sit in a thin seam along $\partial M$, exactly
where the script's third experiment localizes the shadow.

Seventy-two pixels sounds small until you say what it means: *there exist
parameters whose membership in the picture is decided by the $24$th versus the
$53$rd bit of the mantissa.* For those parameters, "is it in the Mandelbrot
set?" has the answer "depends which floating-point type you compiled with."
That is not approximation error in the usual sense — a slightly wrong position
of a real edge. It is the edge itself being *constituted* by the precision. The
provocation's word for this was **hysteresis**, and it is apt: like a magnet
that remembers its history, the rendered boundary remembers the machine that
drew it.

---

## 6. But the set exists — and is provably wild

If the paper stopped here it would be sensational and wrong. So now the
correction, and it is decisive. The Mandelbrot set is *not* a computational
mirage. Two theorems, proved with no computer anywhere in them:

- **Connectedness (Douady–Hubbard, 1982).** $M$ is connected — in fact its
  complement is conformally a disk. The body is one piece, rigorously.
- **The boundary has Hausdorff dimension $2$ (Shishikura, 1991).**
  $\dim_H \partial M = 2$ — the maximum possible in the plane. The boundary is
  not a thin curve that we are failing to resolve; it is genuinely, provably,
  *area-filling in its complexity.*

Shishikura's theorem is the hinge of this paper. It says the wildness we see is
**real**, a property of the true set, independent of every machine. The lace is
not invented by the renderer — there really is structure at every scale, more
than any curve could hold. So "fractals don't exist" is **false** as a
statement about the object: $M$ exists, it is connected, and its edge is as
intricate as mathematics allows.

What Shishikura *also* tells us, though, is why §§4–5 had to happen. A boundary
of dimension $2$ is the worst possible case for a finite grid: it cannot be
covered efficiently, it never thins, and any pixelation straddles infinite
detail forever. The realness of the wildness and the unavoidability of the
quantization are **the same fact** seen from two sides. The set is real
*because* it is wild; the picture is machine-dependent *because* it is wild.

---

## 7. Where the provocation is actually true: the undecidable edge

So the body is real and the wildness is real. Is anything left of "fractals
don't exist"? Yes — and it is the sharp part. It survives not as a statement
about the *set* but about the *decision procedure* at its edge.

**Undecidability in finite time.** For $c$ in the interior of $M$ the orbit is
trapped near an attracting cycle and you can certify "inside" in finite time
(once you have located the cycle). For $c$ outside, the orbit escapes and you
certify "outside" the moment $|z|>2$. But for $c \in \partial M$ exactly, the
orbit neither escapes nor settles — it lives on the Julia set's knife-edge, and
**no finite computation can return a verdict.** The boundary is precisely the
locus of non-termination. A renderer must, by construction, *guess* there.

**Local connectivity is open (MLC).** Whether $M$ is locally connected — whether
the boundary behaves "tamely" enough that the filaments connect up the way the
pictures suggest — is the **central open conjecture** of the field. If MLC
holds, hyperbolic parameters are dense and the picture is, in a precise sense,
"what you think it is." If it fails, the edge hides behavior no finite zoom has
shown us. We do not know. The thing the pictures most strongly assert — that
the lace is a connected, locally-tame curtain — is *unproven*.

**Genuine non-computability nearby.** This is not idle worry. Braverman and
Yampolsky proved that there exist **quadratic Julia sets that are not
computable**: no algorithm, at any precision, can decide them to guaranteed
accuracy. The Julia sets are the per-$c$ companions of the Mandelbrot picture,
and the result shows that "draw the filled dynamics of $z^2+c$" can be, for
some parameters, a *formally uncomputable task*. The computability of $M$
itself is tied to MLC and the hyperbolicity conjecture and is not the trivial
"yes" the easy rendering suggests.

Put together: the **edge of the Mandelbrot set is where membership stops being
a finite question.** The provocation, properly aimed, is true of the boundary
*as a decision problem*: there is a precise sense in which what lives there
cannot be resolved by any machine, and our renders cope by quietly substituting
"hasn't escaped yet at this precision" for "is in the set." The lace is the
record of that substitution.

---

## 8. The honest object: a mesh of shadow zones

The two halves now fit. The set is real (§6); the edge is undecidable and our
arithmetic is finite (§§3–5, 7). The correct response is not to draw a crisp
black-and-white lie, nor to despair, but to draw **what the machine actually
knows** — a three-state map:

- **OUT** — certified: the orbit has escaped (rigorously, once $|z|>2$).
- **IN** — certified: the cell provably contains an attracting cycle / lies in a
  known hyperbolic component (certifiable in finite time).
- **SHADOW** — undecided at this budget: the machine cannot yet tell.

Operationally we define the shadow as the set of cells whose verdict **flips
under a change of machine parameter** — raise the depth cap, or change the
precision, and watch who changes their mind. Those are exactly the parameters
the render is guessing about. The figure paints them red.

![The Mandelbrot set as a three-state object on the standard window. Near-white is the certified-ish interior, dark blue-black is the certified exterior, and the red skin is the SHADOW zone: pixels whose in/out verdict flips when the iteration cap or the floating-point precision is changed. The shadow is not scattered noise — it is a coherent membrane clinging to the boundary, the visible locus of what the machine cannot decide.](library/images/mandelbrot-shadow-zones.png)

The striking measurement is what the shadow does as you **refine the grid**.
Naively, finer pixels should resolve more, so the undecided fraction should
fall. It does the opposite. Taking the shadow's share of the boundary band
(so the trivial interior and exterior do not dilute it):

| grid | shadow pixels | boundary-band pixels | shadow / boundary |
|---|---:|---:|---:|
| $300^2$ | $146$ | $1614$ | $0.09$ |
| $600^2$ | $670$ | $3901$ | $0.17$ |
| $1200^2$ | $2697$ | $9485$ | $0.28$ |

The undecided skin's share of the boundary **grows** as we look closer:
$9\% \to 17\% \to 28\%$. Refinement does not dissolve the shadow; it *reveals
more of it*, exactly as a dimension-$2$ boundary (Shishikura) must — the finer
the mesh, the more boundary there is to be undecided about. The shadow is not a
transient artifact to be polished away with a better GPU. It is a **stable
feature of the honest picture**, and it converges (in share) not to $0$ but to
the genuine, theorem-backed wildness of the edge.

This is the constructive proposal the provocation leads to. Replace the
fictional crisp curve with a **refining mesh of shadow zones**: a quadtree that
certifies OUT and IN cells (ideally with interval / ball arithmetic, so the
certificates are rigorous rather than sampled), and recurses *only* into the
shadow, painting it honestly at each depth. Such a render never lies about a
boundary pixel; it says "undecided, here is how much budget it would take to
try." It is the cartographer's discipline applied to a coastline of dimension
$2$: draw the land, draw the sea, and draw — in a third color — the tide.

---

## 9. The same shadow as Collatz

This is not an isolated provocation; it is the second instance of a single
thesis. In *The Light Cone of Collatz* we argued that the "crazy crests" of
Collatz — orbits soaring to thousands before collapsing — are the **shadow** a
finite integer lattice casts on a smooth continuous descent to the vertex of a
cone; the descent is provably calm, only its sampling is jagged. There, too,
the infinite application of a confined map was shown to be *sensitive to
quantization*, so that numerical iteration of the continuous model is not a
valid verification — only analysis is. The Mandelbrot edge is the same
phenomenon with the roles vivid in the other direction:

| | Collatz crests | Mandelbrot lace |
|---|---|---|
| the smooth/real thing | continuous funnel to the vertex (provable) | the set $M$, connected, $\dim_H\partial M = 2$ (provable) |
| the wild thing we see | jagged integer crests | filigree boundary at zoom |
| the source of the jaggedness | quantization onto the integer lattice | quantization onto grid + depth + mantissa |
| the honest verification | analytic, not floating-point iteration | three-state mesh, not crisp black/white |

In both, a finite machine meets an edge it cannot resolve and produces a
**controlled hysteresis** that we then mistake for the object. The discipline is
the same: separate the provable smooth body from the quantization skin, refuse
to iterate non-contracting / undecidable dynamics in floating point and call
the result truth, and render the uncertainty explicitly. The fractal and the
Collatz crest are two shadows of one sun.

---

## 10. Conclusion

Do fractals exist? The honest answer is a careful *yes, but not the one you
drew.* The Mandelbrot set exists, is connected, and has a boundary of the
maximal dimension $2$ — its wildness is a theorem, not a rendering bug. And yet
**no image of it is the set**: every render is a three-parameter approximation
$M_N^{(p)}$ whose area breathes with the depth cap (still moving at $N=2000$),
whose boundary pixels are decided by the mantissa ($72$ flips between float32
and float64), and whose undecided shadow does not shrink but *grows* as a share
of the boundary under refinement ($9\% \to 28\%$). The lace is neither pure
object nor pure artifact; it is the **negotiation** between a provably wild edge
and an unavoidably finite machine.

The provocation "fractals don't exist" is therefore false about the set and
true about the *picture*: what we have been calling the fractal is, at its edge,
the shadow a finite computation casts on a region where membership stops being a
finite question. The remedy is not more pixels but more honesty: draw the
certified land, the certified sea, and — in red — the shadow tide between them,
refining the mesh into the undecidable rather than pretending to have crossed
it. The fractal we can draw truthfully is a map of our own resolution. The one
underneath, real and dimension-$2$ and possibly not even locally connected,
keeps its own counsel just past the last bit of the mantissa.

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
shadow). The "certified" labels here are sampled, not interval-rigorous; a
fully certified mesh would replace point sampling with interval / ball
arithmetic, which only sharpens the same conclusion: the shadow band is a
stable, theorem-backed feature, not a transient to be polished away.
