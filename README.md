# Math Wiki

Un wiki matematico statico: una single-page app (`index.html`) pubblicabile su
GitHub Pages. Ogni documento è un file Markdown dentro `content/`, quindi **la
repository è sia l'applicazione sia il contenitore dei contenuti**.

I documenti sono di tre tipi — **libro**, **paper**, **note** — e compaiono
nell'albero a sinistra. Il foglio centrale è impaginato come un A4, a mo' di
anteprima PDF. Il rendering matematico usa [KaTeX](https://katex.org) e il
Markdown è gestito da [marked](https://marked.js.org) (entrambi via CDN).

## Sviluppo locale

Serve solo Python 3 (nessuna dipendenza esterna).

```bash
make start          # avvia http://127.0.0.1:8080
make start PORT=9000
make build          # rigenera content/index.json dai file .md
make help
```

Il server locale (`server.py`) serve `index.html` ed espone una piccola API che
**scrive davvero** i documenti: premendo *Salva* viene creato il file `.md` in
`content/` e il manifesto `content/index.json` viene rigenerato.

## Flusso di lavoro

1. **+ Nuovo** → scegli *Paper*, *Libro* o *Note*: nasce una **bozza** in memoria
   (autosalvata nel browser, ma non ancora su disco).
2. Scrivi in Markdown; usa `$...$` per la matematica inline e `$$...$$` per il
   display. Il pulsante *Anteprima* mostra il foglio impaginato.
3. **Salva** → in locale scrive `content/<slug>.md`; committa il file per
   pubblicarlo.

## Pubblicazione su GitHub Pages

Abilita Pages dalla repo (branch `main`, cartella root). Il file `.nojekyll`
disattiva Jekyll così i `.md` in `content/` sono serviti come file raw.

Su Pages non c'è backend: il *Salva* non può scrivere su disco, quindi fa da
*fallback* scaricando il file `.md`, che poi metti in `content/`, committi e
infine rigeneri il manifesto con `make build`.
