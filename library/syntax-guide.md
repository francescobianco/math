---
title: Syntax Guide
type: page
created: 2026-05-23T12:00:00+00:00
updated: 2026-05-23T12:00:00+00:00
---

This page is a living reference for everything you can write in a Math Wiki document.

---

## Text formatting

| Syntax | Result |
|--------|--------|
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `` `inline code` `` | `inline code` |
| `~~strikethrough~~` | ~~strikethrough~~ |

---

## Headings

```
# Heading 1
## Heading 2
### Heading 3
```

Headings automatically appear in the Table of Contents sidebar. The numbering is hierarchical and normalised to the shallowest level present in the document.

---

## Inline math

Wrap a LaTeX expression in single dollar signs:

```
The area of a circle is $A = \pi r^2$.
```

Result: The area of a circle is $A = \pi r^2$.

---

## Display math (formulas)

Wrap a block expression in double dollar signs on their own line:

```
$$
\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}
$$
```

$$
\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}
$$

Each display formula receives a numbered counter on the right (e.g. `(1.1)`) and is **clickable** — clicking opens an editor so you can modify the LaTeX directly.

---

## Wiki links

Every document is assigned a **Reference Code** visible in the topbar badge (e.g. `B1` for the first book, `P1` for the first paper, `N1` for the first notes page). You can link to any document using this code inside a standard Markdown link:

```
See [Real Analysis](#B1) for the formal definition.
```

To link to a specific chapter (heading) within a document, append `/CN` where N is the heading index (1-based):

```
See [the convergence section](#B1/C3).
```

You can override or fix a document's reference code in its **Settings** (gear icon → Reference Code field).

---

## External links

Standard Markdown links to external URLs open in a new tab automatically:

```
[Anthropic](https://www.anthropic.com)
```

---

## Lists

**Unordered:**

```
- Item one
- Item two
  - Nested item
```

- Item one
- Item two

**Ordered:**

```
1. First
2. Second
3. Third
```

1. First
2. Second
3. Third

---

## Blockquotes

```
> A small truth, clearly stated, is worth more than a large truth left unsaid.
```

> A small truth, clearly stated, is worth more than a large truth left unsaid.

---

## Code blocks

Fenced with triple backticks. Optionally specify a language for syntax highlighting:

````
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```
````

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

---

## Horizontal rules

Three dashes on their own line:

```
---
```

---

## Tables

```
| Column A | Column B | Column C |
|----------|----------|----------|
| $\alpha$ | $\beta$  | $\gamma$ |
| 1        | 2        | 3        |
```

| Column A | Column B | Column C |
|----------|----------|----------|
| $\alpha$ | $\beta$  | $\gamma$ |
| 1        | 2        | 3        |

---

## Shareable URLs

Every document state is encoded in the URL hash. You can share the address bar URL and the recipient will land in exactly the same state — including which document is open, whether the TOC is showing, and whether the Settings panel is open.

Example URL shapes:

| URL | Meaning |
|-----|---------|
| `#doc=real-analysis` | Document open, tree sidebar |
| `#doc=real-analysis&toc=1` | Document open, TOC sidebar |
| `#doc=real-analysis&modal=settings` | Settings panel open |

---

## Document types

| Type | Reference prefix | Description |
|------|-----------------|-------------|
| `book` | `B` | Paginated, with a decorative cover page |
| `paper` | `P` | Paginated, starts with a title header |
| `notes` | `N` | Single scrollable page with TOC |
| `page` | `Pg` | Simple page, no TOC sidebar |

The type is set when creating a document and is visible in the topbar badge.
