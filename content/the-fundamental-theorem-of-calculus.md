---
title: The Fundamental Theorem of Calculus
type: paper
created: 2026-05-22T10:00:00+00:00
updated: 2026-05-22T21:28:46.757Z
---

## Statement

Let $f$ be a function continuous on the interval $[a, b]$ and let $F$ be an
antiderivative of it, i.e. $F'(x) = f(x)$ for every $x \in [a, b]$. Then

$$\int_a^b f(x)\,dx = F(b) - F(a).$$

## Proof (sketch)

Define the integral function

$$G(x) = \int_a^x f(t)\,dt.$$

By the integral mean value theorem, for every $h \neq 0$ there exists
$\xi \in (x, x+h)$ such that

$$\frac{G(x+h) - G(x)}{h} = f(\xi).$$

Taking the limit $h \to 0$ and using the continuity of $f$ gives $G'(x) = f(x)$,
so $G$ is an antiderivative of $f$. Since two antiderivatives differ by a
constant, $F(x) = G(x) + c$, from which the claim follows by evaluating at
$a$ and $b$.

## Consequences

- It links differentiation and integration as inverse operations.
- It lets you compute areas and integrals via antiderivatives.
- It is the foundation of elementary integral calculus.
