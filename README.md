# Math Wiki

A static math wiki: a single-page app (`index.html`) you can publish on GitHub
Pages. Every document is a Markdown file under `content/`, so **the repository
is both the application and the content store**.

Documents have four standard types and appear in the tree on the left:

- 📃 **page** — the **home** page is always present and is the landing document.
- 📕 **book**
- 📄 **paper**
- 📝 **notes**

The central sheet is laid out like an A4 page, as a PDF-style preview. Math is
rendered with [KaTeX](https://katex.org) and Markdown is handled by
[marked](https://marked.js.org) (both via CDN).

## Saving (via the GitHub API)

There is no write backend. Pressing **Save** commits the matching `.md` file
straight to GitHub through the
[Contents API](https://docs.github.com/rest/repos/contents): one click for both
**new** and **existing** documents (for updates the file's current `sha` is
fetched first).

This needs a **token**: a fine-grained Personal Access Token with
*Contents: Read and write* on this repository. The first time you save you are
asked for it via a prompt; it is stored only in the browser's **sessionStorage**
(cleared when the tab closes) and never committed. Use the 🔑 button at the
bottom of the sidebar to set, replace, or remove it.

The target repo is configured at the top of the script in `index.html`
(`const GITHUB = …`); if the site runs on `<user>.github.io/<repo>/` it is
detected automatically.

When a `.md` file is committed, a **GitHub Action**
(`.github/workflows/manifest.yml`) rebuilds `content/index.json` (the tree) and
commits it back, so the site stays up to date with no manual step.

## Local development

The local server only serves files (read-only): it needs Python 3, no
dependencies. Saving still goes through GitHub, exactly like online.

```bash
make start          # serves on http://127.0.0.1:5040
make start PORT=9000
make build          # rebuild content/index.json from the .md files (the Action does this too)
make help
```

## Publishing on GitHub Pages

Enable Pages for the repo (branch `main`, root folder). The `.nojekyll` file
disables Jekyll, so the `.md` files under `content/` are served as raw files.
