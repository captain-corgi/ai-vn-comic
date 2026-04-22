"""Stage repo content into `docs/` for MkDocs Material.

Stories, prompts and images live at the repo root so they can be read
directly on GitHub. For the MkDocs site we copy them into `docs/stories/`,
`docs/prompts/` and `docs/images/` right before running `mkdocs build`.

The staged directories are gitignored; only the hand-authored meta pages
(`docs/index.md`, `docs/characters.md`, etc.) and this script live in
source control.

Run via:

    python3 tools/build_docs.py            # stage
    mkdocs build                           # build the site
    python3 tools/build_docs.py --serve    # convenience wrapper

Or simply `python3 tools/build_docs.py && mkdocs serve` for local preview.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
STAGED_STORIES = DOCS_DIR / "stories"
STAGED_PROMPTS = DOCS_DIR / "prompts"
STAGED_IMAGES = DOCS_DIR / "images"

STORY_RE = re.compile(r"^(\d{2})-[a-z0-9-]+\.md$")
PROMPT_RE = re.compile(r"^(\d{2})-[a-z0-9-]+-prompts\.md$")


def clean(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


IMAGE_REF_RE = re.compile(r"!\[([^\]]*)\]\(images/([^)\s]+)\)")


def copy_stories() -> list[tuple[str, str]]:
    """Copy NN-*.md into docs/stories/ and return (num, title) pairs.

    Story files live at the repo root and reference images via
    `images/N.png`. Once we move them into `docs/stories/`, that relative
    path would resolve to `docs/stories/images/N.png` — so rewrite to
    `../images/N.png`. Dangling references (e.g. `images/23.png` that
    doesn't exist) are replaced with an admonition so mkdocs strict mode
    doesn't trip on them; the structural linter already surfaces them.
    """
    images_dir = REPO_ROOT / "images"
    entries: list[tuple[str, str]] = []
    for src in sorted(REPO_ROOT.glob("[0-9][0-9]-*.md")):
        if not STORY_RE.match(src.name):
            continue
        dst = STAGED_STORIES / src.name
        text = src.read_text(encoding="utf-8")

        def _rewrite(match: re.Match[str]) -> str:
            alt, rel = match.group(1), match.group(2)
            if (images_dir / rel).is_file():
                return f"![{alt}](../images/{rel})"
            return (
                f"<!-- missing image: images/{rel} (alt: {alt or '-'}) -->"
            )

        text = IMAGE_REF_RE.sub(_rewrite, text)
        dst.write_text(text, encoding="utf-8")
        title = _first_h1(text) or src.stem
        entries.append((src.name, title))
    return entries


def copy_prompts() -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    prompts_dir = REPO_ROOT / "prompts"
    for src in sorted(prompts_dir.glob("[0-9][0-9]-*-prompts.md")):
        if not PROMPT_RE.match(src.name):
            continue
        dst = STAGED_PROMPTS / src.name
        text = src.read_text(encoding="utf-8")
        dst.write_text(text, encoding="utf-8")
        title = _first_h1(text) or src.stem
        entries.append((src.name, title))
    return entries


def copy_images() -> int:
    images_dir = REPO_ROOT / "images"
    if not images_dir.is_dir():
        return 0
    count = 0
    for src in images_dir.iterdir():
        if src.is_file():
            shutil.copy2(src, STAGED_IMAGES / src.name)
            count += 1
    return count


def _first_h1(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def write_index(
    path: Path, heading: str, intro: str, entries: list[tuple[str, str]]
) -> None:
    lines = [f"# {heading}", "", intro.strip(), ""]
    for name, title in entries:
        lines.append(f"- [{title}]({name})")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--serve",
        action="store_true",
        help="after staging, exec `mkdocs serve` for a live preview",
    )
    parser.add_argument(
        "--build",
        action="store_true",
        help="after staging, exec `mkdocs build --strict`",
    )
    args = parser.parse_args(argv)

    clean(STAGED_STORIES)
    clean(STAGED_PROMPTS)
    clean(STAGED_IMAGES)

    stories = copy_stories()
    prompts = copy_prompts()
    images = copy_images()

    write_index(
        STAGED_STORIES / "index.md",
        "Truyện",
        "Danh sách toàn bộ truyện trong vũ trụ, theo số thứ tự. "
        "Dùng thanh tìm kiếm ở đầu trang để tìm theo nhân vật, vũ trụ "
        "hoặc khái niệm.",
        stories,
    )
    write_index(
        STAGED_PROMPTS / "index.md",
        "Prompts tạo hình minh họa",
        "Mỗi truyện có một file prompt đi kèm để tạo hình minh họa AI. "
        "Tổng cộng khoảng 568 prompts trong toàn bộ vũ trụ.",
        prompts,
    )

    print(
        f"[build_docs] staged {len(stories)} stories, "
        f"{len(prompts)} prompt files, {images} images into {DOCS_DIR}"
    )

    if args.serve:
        return subprocess.call(["mkdocs", "serve"], cwd=REPO_ROOT)
    if args.build:
        return subprocess.call(["mkdocs", "build", "--strict"], cwd=REPO_ROOT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
