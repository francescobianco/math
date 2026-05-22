---
title: Il Teorema Fondamentale del Calcolo
type: paper
created: 2026-05-22T10:00:00+00:00
updated: 2026-05-22T10:00:00+00:00
---

## Enunciato

Sia $f$ una funzione continua sull'intervallo $[a, b]$ e sia $F$ una sua
primitiva, cioè $F'(x) = f(x)$ per ogni $x \in [a, b]$. Allora

$$\int_a^b f(x)\,dx = F(b) - F(a).$$

## Dimostrazione (schizzo)

Definiamo la funzione integrale

$$G(x) = \int_a^x f(t)\,dt.$$

Per il teorema della media integrale, per ogni $h \neq 0$ esiste
$\xi \in (x, x+h)$ tale che

$$\frac{G(x+h) - G(x)}{h} = f(\xi).$$

Passando al limite $h \to 0$ e usando la continuità di $f$ si ottiene
$G'(x) = f(x)$, dunque $G$ è una primitiva di $f$. Poiché due primitive
differiscono per una costante, $F(x) = G(x) + c$, da cui la tesi valutando
in $a$ e $b$.

## Conseguenze

- Collega derivazione e integrazione come operazioni inverse.
- Permette di calcolare aree e integrali tramite le primitive.
- È la base del calcolo integrale elementare.