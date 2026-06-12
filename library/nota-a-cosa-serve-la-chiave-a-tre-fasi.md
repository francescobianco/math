---
title: "Nota: a cosa serve la chiave a tre fasi (in parole semplici)"
type: notes
created: 2026-06-13T00:30:00+00:00
updated: 2026-06-13T01:15:00+00:00
---

# Nota: a cosa serve la chiave a tre fasi (in parole semplici)

Spiegazione semplice del paper
[The Three-Phase Key](library/the-three-phase-key-watermarks-from-the-incompressible-collatz-phase.md).
Niente formule: solo cosa fa lo strumento, cosa si può farci, e cosa **non**
si può farci.

## L'idea in una frase

Le fasi di Collatz producono una sequenza che è **facile da ricalcolare ma
impossibile da indovinare con una formula**, e che parla una "lingua" con
regole precise (alcune combinazioni di simboli non compaiono mai). Questa
lingua è una **impronta**: se qualcuno tocca i dati, rompe una regola della
lingua e te ne accorgi. Lo strumento non serve a *nascondere* i dati — serve
a *certificarli e proteggerli da manomissioni*.

## La scoperta più importante (e controintuitiva)

Verrebbe da usare questa sequenza per **cifrare** (come rumore segreto da
sommare ai dati). **Non funziona**, e il paper lo dimostra: la sequenza è
troppo "regolare" (i vicini si somigliano, certe parole sono vietate), quindi
un attaccante la riconosce e la toglie. Come cifratura è inutile.

Ma proprio quella regolarità la rende perfetta come **filigrana (watermark)**:
è un'impronta riconoscibile che una modifica disturba. Quindi:

> Non si **nascondono** i dati *con* le fasi. Si **autenticano** i dati
> *contro* le fasi.

## Cosa si può fare (concreto)

1. **Watermark anti-manomissione (l'uso più solido).**
   Intrecci l'impronta di Collatz nei tuoi dati. Se qualcuno li modifica,
   con buona probabilità rompe una regola della lingua e la manomissione
   viene scoperta — **da chiunque, senza bisogno di chiavi**. Più sono le
   modifiche, più è certo l'allarme (8 ritocchi → scoperti nell'86% dei casi;
   su un file intero la manomissione è praticamente sempre rilevata).

2. **"Rimovibile solo se sai come".**
   Solo chi possiede il **seme segreto** (il numero di partenza) può
   rigenerare l'impronta esatta e quindi rimuoverla o spostarla pulitamente.
   Chi non ce l'ha può *accorgersi* che c'è, ma non può modificarla né
   ricrearla senza far scattare l'allarme. Esattamente la filigrana che volevi:
   togliibile solo da chi sa come.

3. **Chiave / firma in tre pezzi che si autoverifica.**
   Da un'unica traiettoria nascono tre "viste" diverse (i valori, la fase
   mod 3, la parità mod 2). Le tre viste **combaciano solo se provengono da
   una traiettoria vera**. Quindi tre custodi possono tenere un pezzo ciascuno
   e il sistema verifica da solo che nessuno abbia barato: una controfirma /
   audit a prova di manomissione.

4. **Canale nascosto (steganografia leggera).**
   In una traccia valida restano posizioni "libere": ci puoi infilare un
   messaggio (circa 1,2 bit per simbolo) mentre la traccia continua a sembrare
   una normale impronta di Collatz.

5. **Puzzle anti-abuso (rate limiting).**
   Calcolare la traccia richiede di "percorrere la strada", passo dopo passo,
   senza scorciatoie: utile per imporre un costo a chi fa troppe richieste.

## Lo streaming in tempo reale (la casa naturale)

Lo strumento è fatto apposta per i flussi in tempo reale: la verifica costa
**pochissimo per simbolo**, a memoria costante, e si fa **mentre i dati
arrivano** (non serve avere tutto il file). Il marchio viaggia *dentro* il
flusso, non è un'etichetta separata da staccare.

Attenzione però a un numero: una **singola** manomissione strutturale (tagliare
e incollare un pezzo, riordinare, reinserire un blocco) viene scoperta solo
circa **1 volta su 4**. Quindi da solo è una *spia probabilistica economica*,
non una garanzia: va messo **sopra** strumenti standard (HMAC, hash chain,
firme) quando serve certezza. Con questo in mente, i casi pratici:

- **Anti-cheat (client che inviano comandi/mosse)** — *debole da solo.* Se chi
  bara controlla il proprio software, possiede il seme e falsifica il flusso:
  non c'è scampo. Contro un intermediario, una hash chain è più adatta. Il
  valore vero è la **coerenza lato server** (le mosse valgono solo se coerenti
  con la simulazione del server), e lì la parte Collatz è quasi decorativa.
- **Trust di payload HTTP / integrità di flussi** — *layer complementare.* Per
  "è autentico?" un HMAC vince. Collatz aggiunge ciò che l'HMAC non dà: sigillo
  *dentro* i dati, **localizzazione** del punto manomesso, e canale nascosto.
- **Flussi di token di agenti di coding** — *il caso più promettente.* Il ~25%
  per singolo ritocco **diventa quasi certezza su output lunghi** (chi manomette
  dovrebbe evitare *ogni* regola proibita per migliaia di simboli). Unito al
  canale nascosto puoi incorporare provenienza/versione/identità del modello
  nel flusso stesso. Diverso dai watermark LLM classici: quelli marcano la
  *generazione*, questo sigilla un flusso *già esistente*.
- **Side-channel per controllo dispositivi** — *reale ma di nicchia.* Puoi far
  viaggiare comandi/heartbeat a basso rateo dentro un flusso che *al tempo
  stesso* certifica sé stesso. È offuscamento, non segretezza.

**Il vantaggio davvero unico: la localizzazione.** Un HMAC su tutto il messaggio
dice "manomesso", ma non *dove*. Qui la regola si rompe *vicino* al punto
toccato (entro ~8 simboli), e puoi verificare anche solo un **frammento** del
flusso. Per il tempo reale — verifica parziale, guasto localizzato,
degradazione graduale — è esattamente ciò che un'etichetta appiccicata in fondo
non può fare.

## Cosa NON si può fare (importante)

- **Non cifra.** Per la segretezza vera serve crittografia standard; le fasi
  aggiungono solo l'**integrità** (capire se i dati sono autentici o toccati).
- **Non è una funzione "a senso unico".** Calcolare la fase è facile; "non
  comprimibile" vuol dire *senza formula chiusa*, non *difficile da calcolare*.
- **La lingua non è segreta.** Tentare di renderla segreta cambiando il modo
  di leggerla **non funziona** (lo abbiamo misurato: leggere a salti distrugge
  l'impronta). Il segreto vero è il **seme di partenza**, non la grammatica.
- **Niente garanzie matematiche di sicurezza.** È uno strumento di integrità
  *misurato sul campo*, da appoggiare sopra primitive crittografiche che le
  garanzie ce le hanno.

## In sintesi

È un **sigillo intelligente**: economico, autodescrittivo, con ridondanza a
tre pezzi incorporata. Lo metti sui dati per dire "questo è autentico e non è
stato toccato" — e solo tu, che conosci il seme, puoi rimuoverlo o rifarlo.
Per tenere i dati *segreti* serve altro; per tenerli *integri e tracciabili*,
questo giocattolo funziona davvero.