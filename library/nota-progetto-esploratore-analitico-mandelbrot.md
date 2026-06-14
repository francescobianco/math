---
title: "Nota di progetto: esploratore analitico del Mandelbrot (web / JS)"
type: notes
created: 2026-06-14T20:00:00+00:00
updated: 2026-06-14T20:00:00+00:00
---

# Nota di progetto: esploratore analitico del Mandelbrot (web / JS)

Dedichiamo questo strumento alla **parte di studio analitico** dei lavori
*What If Fractals Don't Exist?* e del trittico interno/esterno/bordo. È il
contrario di un fractal-renderer: non disegna $M$ a pixel, disegna **solo ciò
che è dimostrato**, e lascia vuoto ciò che non lo è.

## Principio (cosa NON fa)

- **Niente rendering a pixel.** Niente escape-time che riempie un blob nero,
  niente colorazione continua del piano.
- **Niente interpolazione.** Tra due punti non si "indovina" mai cosa c'è in
  mezzo.

## Cosa fa

Un **foglio bianco** su cui compaiono **punti colorati e staccati** (non
contigui), ciascuno un **verdetto certificato**:

- **punto "fuori per definizione"** — certificato di fuga: l'orbita supera
  $|z|>2$ a un passo finito (esiste sempre per i punti esterni, esatto per $c$
  algebrico). Un colore.
- **punto "dentro per definizione"** — certificato di attrattore: esibito un
  ciclo attrattore, $|\text{moltiplicatore}|<1$ (gli strati iperbolici). Altro
  colore.
- **sul resto: niente.** Bordo / indecidibile / non ancora certificato =
  **bianco**, vuoto.

## La regola d'oro: punti staccati, mai contigui

I punti devono restare **distanziati**, mai a riempire una regione piena. Così
chi guarda ha *continuamente* la sensazione corretta:

> se vuoi sapere come si comporta *tra* due punti, devi **zoommare**.

Lo zoom non "riempie" il bianco per interpolazione: ricalcola i certificati
nella nuova finestra e fa comparire **nuovi punti certificati** più fitti. Il
bianco tra i punti non è "ancora da colorare": è *ciò che a questa scala non è
deciso*. Il **bordo resta vuoto a ogni livello di zoom** — non è certificabile,
e il vuoto lo dice onestamente. È l'epistemologia resa visibile: l'immagine non
mente mai di sapere ciò che non sa.

## Legenda (esplicita, sempre visibile)

- 🟦 dentro per definizione (ciclo attrattore esibito)
- 🟥 fuori per definizione (fuga certificata)
- ⬜ il resto: niente — da zoommare

## Note di implementazione (JS)

- **Certificato dentro**: itera, rileva ciclo di periodo $\le P_{\max}$ e
  verifica $|\lambda|<1$ ($\lambda=\prod 2z_i$ sul ciclo). Per la cardioide e i
  bulbi principali si può usare la forma chiusa esatta ($|1-\sqrt{1-4c}|<1$ ecc.).
- **Certificato fuori**: itera fino a $|z|>2$ (bailout); per i punti esterni
  termina sempre.
- **Campionamento staccato**: NON un punto per pixel. Griglia rada (eventualmente
  con jitter) o set sparso; lo zoom aumenta la densità ma lascia sempre gap
  visibili. Mai `fill`, mai aree piene.
- **Rendering**: canvas / WebGL, dot piccoli su sfondo bianco; due soli colori +
  bianco; legenda fissa.
- **Onestà sulla precisione** (cfr. §9 del paper): in `double` i certificati di
  bordo non sono fidati; l'upgrade rigoroso è **aritmetica di intervalli / ball
  arithmetic** — allora 🟦 e 🟥 diventano prove, e ⬜ è "nessuna prova, per ora".
  Versione 1 in double con il caveat; versione 2 con intervalli.

## Perché vale la pena

È l'incarnazione visiva della tesi: si vede **solo il certificabile** (dentro =
attrattori, fuori = fughe), il bordo frattale/indecidibile è letteralmente
**spazio bianco**, e "zoommare per sapere" diventa l'unico gesto possibile —
non una comodità, ma la verità del problema. Lo strumento non disegna il
frattale: disegna *quello che sappiamo*, e mostra dove smettiamo di saperlo.
