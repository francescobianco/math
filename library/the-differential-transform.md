---
title: The Differential Transform
type: paper
created: 2026-05-23T12:00:00+00:00
updated: 2026-05-23T12:30:00+00:00
---

# The Differential Transform

## Abstract

Let $f$ be a differentiable function such that $f(x) \neq 0$ on an interval
$I$. We define the differential transform of $f$ as the ratio

$$\mathcal{D}[f](x) = \frac{f'(x)}{f(x)}.$$

This quantity measures the instantaneous relative rate of change of $f$. It is
also the logarithmic derivative of $f$, since

$$\mathcal{D}[f](x) = \frac{d}{dx}\log |f(x)|.$$

The exponential function $e^x$ plays a central role: its differential transform
is identically equal to $1$. We also examine $x^x$ and introduce an
iterative relation connecting the transform with higher derivatives.

## Definition

Let $f:I \to \mathbb{R}$ be differentiable and nonzero on $I$. The differential
transform of $f$ is

$$\mathcal{D}[f](x) = \frac{f'(x)}{f(x)}.$$

Equivalently,

$$\mathcal{D}[f](x) = (\log |f(x)|)'.$$

Thus the differential transform converts ordinary variation into relative
variation.

## Fundamental Properties

If $f$ and $g$ are differentiable and nonzero, then

$$\mathcal{D}[fg](x) = \mathcal{D}[f](x) + \mathcal{D}[g](x).$$

Indeed,

$$
\frac{(fg)'(x)}{f(x)g(x)}
= \frac{f'(x)g(x) + f(x)g'(x)}{f(x)g(x)}
= \frac{f'(x)}{f(x)} + \frac{g'(x)}{g(x)}.
$$

Similarly,

$$\mathcal{D}\left[\frac{f}{g}\right](x)
= \mathcal{D}[f](x) - \mathcal{D}[g](x),$$

and, for a real constant $\alpha$,

$$\mathcal{D}[f^\alpha](x) = \alpha \mathcal{D}[f](x).$$

These identities show that the differential transform behaves like a derivative
after taking logarithms: products become sums, quotients become differences, and
powers become scalar multiples.

## The Exponential Function

Consider

$$f(x) = e^x.$$

Since

$$f'(x) = e^x,$$

we obtain

$$\mathcal{D}[e^x](x) = \frac{(e^x)'}{e^x} = \frac{e^x}{e^x} = 1.$$

Therefore,

$$\mathcal{D}[e^x](x) = 1.$$

This is a notable result: $e^x$ has constant relative growth equal to $1$ at
every point.

More generally, for

$$f(x) = e^{kx},$$

where $k$ is a constant, we have

$$f'(x) = ke^{kx},$$

and so

$$\mathcal{D}[e^{kx}](x) = \frac{ke^{kx}}{e^{kx}} = k.$$

Thus the exponential functions $Ce^{kx}$, with $C \neq 0$, are exactly the
functions whose differential transform is constant.

## Characterization

Suppose that

$$\mathcal{D}[f](x) = k,$$

where $k$ is constant. Then

$$\frac{f'(x)}{f(x)} = k,$$

so

$$f'(x) = kf(x).$$

Solving this first-order differential equation gives

$$f(x) = Ce^{kx},$$

with $C \neq 0$. Hence a differentiable nonzero function has constant
differential transform if and only if it is exponential.

## The Function $x^x$

A particularly interesting example is

$$f(x)=x^x,$$

with $x>0$. Since

$$x^x = e^{x\log x},$$

we obtain

$$\log f(x) = x\log x.$$

Therefore,

$$\mathcal{D}[x^x](x)
= \frac{d}{dx}(x\log x)
= \log x + 1.$$

This means that the relative rate of change of $x^x$ is not constant, as in the
case of $e^{kx}$, but grows logarithmically. Consequently,

$$f'(x)=x^x(\log x+1).$$

The equation

$$\mathcal{D}[x^x](x)=\log x+1$$

shows how the differential transform can simplify functions whose exponent also
depends on the variable: instead of differentiating $x^x$ directly, one studies
the derivative of its logarithm.

## Examples

For $f(x)=x^n$ with $x>0$,

$$\mathcal{D}[x^n](x) = \frac{nx^{n-1}}{x^n} = \frac{n}{x}.$$

For $f(x)=\sin x$, where $\sin x \neq 0$,

$$\mathcal{D}[\sin x](x) = \frac{\cos x}{\sin x} = \cot x.$$

For $f(x)=\cos x$, where $\cos x \neq 0$,

$$\mathcal{D}[\cos x](x) = \frac{-\sin x}{\cos x} = -\tan x.$$

## Second Derivative and Iterative Relations

The differential transform also gives a useful way to relate the first and
second derivatives of a function. Let

$$T_1(x)=\mathcal{D}[f](x)=\frac{f'(x)}{f(x)}.$$

Then

$$f'(x)=T_1(x)f(x).$$

Differentiating again gives

$$f''(x)=T_1'(x)f(x)+T_1(x)f'(x).$$

Since $f'(x)=T_1(x)f(x)$, we obtain

$$f''(x)=\left(T_1'(x)+T_1(x)^2\right)f(x).$$

Thus

$$\frac{f''(x)}{f(x)}=T_1'(x)+T_1(x)^2.$$

This formula connects the second derivative with the differential transform. It
shows that the normalized second derivative is determined by the transform and
by the derivative of the transform.

This idea can be iterated. Define

$$T_n(x)=\frac{f^{(n)}(x)}{f(x)}.$$

Then $T_0(x)=1$ and $T_1(x)=\mathcal{D}[f](x)$. Since

$$f^{(n)}(x)=T_n(x)f(x),$$

differentiating gives

$$f^{(n+1)}(x)=T_n'(x)f(x)+T_n(x)f'(x).$$

Using $f'(x)=T_1(x)f(x)$, we get the iterative relation

$$T_{n+1}(x)=T_n'(x)+T_1(x)T_n(x).$$

The first cases are

$$T_1=\mathcal{D}[f],$$

$$T_2=T_1'+T_1^2,$$

and

$$T_3=T_2'+T_1T_2.$$

For $f(x)=e^x$, we have $T_1=1$. The recurrence gives

$$T_{n+1}=T_n,$$

so $T_n=1$ for every $n$. This recovers the classical fact that every derivative
of $e^x$ is again $e^x$.

For $f(x)=x^x$, the first transform is

$$T_1=\log x+1.$$

Hence

$$T_2=T_1'+T_1^2=\frac{1}{x}+(\log x+1)^2,$$

and therefore

$$f''(x)=x^x\left(\frac{1}{x}+(\log x+1)^2\right).$$

This illustrates the iterative nature of the method: once $T_1$ is known, higher
normalized derivatives can be generated recursively.

## Conclusion

The differential transform

$$\mathcal{D}[f](x) = \frac{f'(x)}{f(x)}$$

is a compact way to study the relative instantaneous change of a function. Its
main rules are

$$\mathcal{D}[fg] = \mathcal{D}[f] + \mathcal{D}[g],$$

$$\mathcal{D}\left[\frac{f}{g}\right] = \mathcal{D}[f] - \mathcal{D}[g],$$

and

$$\mathcal{D}[f^\alpha] = \alpha \mathcal{D}[f].$$

The most important example is

$$\mathcal{D}[e^x] = 1,$$

which expresses the defining feature of the natural exponential function: its
absolute rate of change is exactly equal to its current value.
