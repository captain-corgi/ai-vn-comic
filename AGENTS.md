# AGENTS.md

## Cursor Cloud specific instructions

This is a content/creative writing repository (Vietnamese Comic Universe), not a traditional software application. The "application" is a **MkDocs Material documentation site** that renders 37 Vietnamese superhero stories and 568 AI image-generation prompts.

### Services

| Service | Command | Notes |
| --- | --- | --- |
| Structural linter | `python3 tools/check_structure.py` | Pure stdlib, no pip deps. Exits non-zero on errors; warnings are expected for legacy content. |
| MkDocs dev server | `python3 tools/build_docs.py && mkdocs serve -a 0.0.0.0:8000` | Requires `pip install -r requirements-docs.txt`. Must stage content before serving. |
| MkDocs build | `python3 tools/build_docs.py && mkdocs build --strict` | Used in CI for GitHub Pages deployment. |
| Markdown lint | `markdownlint-cli2 '**/*.md' '!node_modules' '!site'` | Requires `npm install -g markdownlint-cli2`. Pre-existing MD060 violations exist in repo. |

### Non-obvious caveats

- **PATH for pip-installed binaries**: `mkdocs` installs to `~/.local/bin` which may not be on `PATH`. Either use `python3 -m mkdocs` or `export PATH="$HOME/.local/bin:$PATH"`.
- **Content staging is required before serving/building**: `tools/build_docs.py` copies stories, prompts, and images from the repo root into `docs/` subdirectories. The staged directories (`docs/stories/`, `docs/prompts/`, `docs/images/`) are gitignored. Always run `python3 tools/build_docs.py` before `mkdocs serve` or `mkdocs build`.
- **Structural linter warnings are normal**: The 17 warnings about missing epilogues, post-credit sections, and short stories are known legacy content issues. Only errors (exit code 1) indicate problems.
- **markdownlint pre-existing violations**: ~101 MD060 (table column style) violations exist in `.claude/`, `.factory/`, and `docs/` files. These are pre-existing and not blocking in CI (CI uses `DavidAnson/markdownlint-cli2-action@v16`).
- For story/prompt format conventions and content guidelines, see `CLAUDE.md`.
