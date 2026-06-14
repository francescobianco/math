---
title: "Nota: c = 0.1 − 0.3i è dentro M (prova facile, analitica)"
type: notes
created: 2026-06-14T18:00:00+00:00
updated: 2026-06-14T18:00:00+00:00
---

# Nota: $c = 0.1 - 0.3i$ è dentro $M$ — prova facile e analitica

Mostriamo, **senza far girare l'orbita** e senza dipendere dall'arrotondamento,
che $c = 0.1 - 0.3i$ appartiene all'insieme di Mandelbrot. La prova è una
disuguaglianza algebrica, non un calcolo numerico iterato.

## L'idea in una riga

La **cardioide principale** di $M$ è l'insieme dei $c$ per cui la mappa
$f(z)=z^2+c$ ha un **punto fisso attrattore**. La cardioide è contenuta in $M$
(teorema). Quindi basta esibire il punto fisso attrattore: se c'è, $c$ è dentro.

## Passo 1 — i punti fissi (forma chiusa)

Un punto fisso risolve $z^2+c=z$, cioè $z^2-z+c=0$:

$$
z_\pm \;=\; \frac{1 \pm \sqrt{1-4c}}{2}.
$$

Nessuna iterazione: due valori esatti.

## Passo 2 — il moltiplicatore decide attrattore vs repulsore

Il moltiplicatore in un punto fisso è $\lambda = f'(z) = 2z$, quindi

$$
\lambda_\pm \;=\; 2z_\pm \;=\; 1 \pm \sqrt{1-4c}.
$$

Regola esatta: il punto fisso **attrae** se $|\lambda|<1$, **respinge** se
$|\lambda|>1$. Cerchiamo quello attrattore (il segno $-$):

$$
\lambda \;=\; 1 - \sqrt{1-4c}.
$$

## Passo 3 — sostituiamo $c = 0.1 - 0.3i$

Prima $1-4c$:

$$
1-4c \;=\; 1 - 4(0.1 - 0.3i) \;=\; 1 - 0.4 + 1.2i \;=\; 0.6 + 1.2i.
$$

Poi la radice $\sqrt{0.6 + 1.2i}$. Con la formula della radice complessa
$\sqrt{a+bi} = \sqrt{\tfrac{r+a}{2}} + i\,\sqrt{\tfrac{r-a}{2}}$ (segno $+$ perché
$b>0$), dove $r=\sqrt{a^2+b^2}$:

$$
r = \sqrt{0.6^2 + 1.2^2} = \sqrt{1.8} = 1.341640\ldots
$$

$$
\sqrt{0.6+1.2i}
= \sqrt{\tfrac{1.341640+0.6}{2}} + i\,\sqrt{\tfrac{1.341640-0.6}{2}}
= 0.985302\ldots + 0.608949\ldots\, i .
$$

## Passo 4 — il moltiplicatore e la disuguaglianza

$$
\lambda = 1 - \sqrt{1-4c}
= 1 - (0.985302 + 0.608949\,i)
= 0.014698 - 0.608949\,i .
$$

$$
|\lambda|
= \sqrt{0.014698^2 + 0.608949^2}
= \sqrt{0.000216 + 0.370819}
= \sqrt{0.371035}
= 0.609127\ldots
$$

Quindi

$$
\boxed{\,|\lambda| = 0.6091\ldots \;<\; 1\,}
$$

## Conclusione

$|\lambda|<1$: il punto fisso

$$
z_- = \frac{\lambda}{2} \approx 0.00735 - 0.30447\,i
$$

è **attrattore**. Dunque $f(z)=z^2+c$ ha un punto fisso attrattore, cioè $c$ sta
nella cardioide principale, che è contenuta in $M$. Perciò

$$
c = 0.1 - 0.3i \;\in\; M .
$$

## Perché è "analitica" e non "numerica"

- Il certificato è il **punto fisso in forma chiusa** e la disuguaglianza
  $|1-\sqrt{1-4c}|<1$ — un confronto fra **numeri algebrici**, deciso
  esattamente. I decimali qui sopra sono solo visualizzazione: la verità del
  $<1$ non dipende da quante cifre scrivi.
- **Non** abbiamo iterato $z\mapsto z^2+c$ all'infinito né aspettato che
  un'orbita "non scappi": niente cap di iterazioni, niente float, niente
  pseudo-orbita. La domanda infinita ("l'orbita resta limitata per sempre?") è
  collassata in un conto finito ed esatto.

Questo è esattamente ciò che rende il punto **banale** nel senso del paper *What
If Fractals Don't Exist?*: appartiene a uno degli **strati certificabili** (le
componenti iperboliche), dove il destino non si afferma soltanto — si *esibisce*.
La difficoltà vera non è qui: vive sul **bordo** $\partial M$, dove un certificato
finito così non esiste.
