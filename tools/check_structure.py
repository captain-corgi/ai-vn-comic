"""Structural / consistency lint for the Vietnamese Comic Universe repo.

This is a *content* linter, not a code linter. It keeps the
documentation claims (counts, file pairings, image references,
required sections) in sync with the actual markdown files and
exits non-zero on CI when anything drifts.

Run locally:

    python3 tools/check_structure.py

Or with the ``--json`` flag to get machine-readable output:

    python3 tools/check_structure.py --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

STORY_RE = re.compile(r"^(\d{2})-[a-z0-9-]+\.md$")
PROMPT_RE = re.compile(r"^(\d{2})-[a-z0-9-]+-prompts\.md$")
IMAGE_REF_RE = re.compile(r"!\[[^\]]*\]\((images/[^)\s]+)\)")
CHAPTER_HEADING_RE = re.compile(r"^#{1,3}\s*Chương\s+\d+", re.MULTILINE)
# Stories in this repo use several different closers:
#   "## EPILOGUE: ...", "## LỜI KẾT", "## Kết Thúc", or just a
# trailing scene with no named section. We accept any of these.
EPILOGUE_RE = re.compile(
    r"^#{1,3}\s*(EPILOGUE|LỜI\s+KẾT|Lời\s+Kết|KẾT\s+THÚC|Kết\s+Thúc|ĐOẠN\s+KẾT)",
    re.MULTILINE | re.IGNORECASE,
)
POST_CREDIT_RE = re.compile(
    r"^#{1,3}\s*(POST[- ]CREDIT|SAU\s+CREDIT|HẬU\s+CREDIT)",
    re.MULTILINE | re.IGNORECASE,
)
PROMPT_LINE_RE = re.compile(r"^\*\*Prompt:\*\*", re.MULTILINE)


@dataclass
class Findings:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    stats: dict[str, object] = field(default_factory=dict)

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def list_story_files() -> list[Path]:
    out = []
    for p in sorted(REPO_ROOT.glob("*.md")):
        if STORY_RE.match(p.name):
            out.append(p)
    return out


def list_prompt_files() -> list[Path]:
    prompts_dir = REPO_ROOT / "prompts"
    if not prompts_dir.is_dir():
        return []
    return sorted(p for p in prompts_dir.glob("*.md") if PROMPT_RE.match(p.name))


def check_story_prompt_pairing(f: Findings) -> None:
    stories = {STORY_RE.match(p.name).group(1): p for p in list_story_files()}  # type: ignore[union-attr]
    prompts = {PROMPT_RE.match(p.name).group(1): p for p in list_prompt_files()}  # type: ignore[union-attr]

    f.stats["story_count"] = len(stories)
    f.stats["prompt_file_count"] = len(prompts)

    for num, path in stories.items():
        if num not in prompts:
            f.err(
                f"Story {path.name} has no matching prompt file "
                f"(expected prompts/{num}-*-prompts.md)"
            )
    for num, path in prompts.items():
        if num not in stories:
            f.err(
                f"Prompt file {path.relative_to(REPO_ROOT)} has no matching "
                f"story file (expected {num}-*.md at repo root)"
            )


def check_required_sections(f: Findings) -> None:
    short_story_threshold_lines = 120
    short_chapter_threshold = 4
    for story_path in list_story_files():
        text = story_path.read_text(encoding="utf-8")
        chapters = CHAPTER_HEADING_RE.findall(text)
        has_epilogue = bool(EPILOGUE_RE.search(text))
        has_post_credit = bool(POST_CREDIT_RE.search(text))
        # POST-CREDIT is documented as required, but a handful of early
        # Bamboo-arc stories (02–06) close with an inline "câu chuyện tiếp
        # tục trong The Bamboo Council" scene instead of a named section.
        # We flag the missing header as a warning so the linter is honest
        # about legacy content without failing CI on it (use --strict to
        # escalate).
        if not has_post_credit:
            f.warn(
                f"{story_path.name}: no explicit POST-CREDIT / Sau Credit "
                f"heading. Consider adding one so the universe connector "
                f"is discoverable."
            )
        if not has_epilogue and has_post_credit:
            f.warn(
                f"{story_path.name}: no explicit EPILOGUE / Lời Kết section "
                f"(closes directly on POST-CREDIT). Consider adding one."
            )
        chapter_count = len(chapters)
        line_count = text.count("\n") + 1
        if chapter_count < short_chapter_threshold:
            f.warn(
                f"{story_path.name}: only {chapter_count} chapter headings "
                f"(target is 10+ for new stories)"
            )
        if line_count < short_story_threshold_lines:
            f.warn(
                f"{story_path.name}: only {line_count} lines "
                f"(target is 300+ for new stories)"
            )


def check_image_refs(f: Findings) -> None:
    images_dir = REPO_ROOT / "images"
    existing = {p.name for p in images_dir.glob("*")} if images_dir.is_dir() else set()
    f.stats["image_file_count"] = len(existing)

    referenced: set[str] = set()
    stories_with_images = 0
    for story_path in list_story_files():
        text = story_path.read_text(encoding="utf-8")
        refs = IMAGE_REF_RE.findall(text)
        if refs:
            stories_with_images += 1
        for rel in refs:
            referenced.add(Path(rel).name)
            target = REPO_ROOT / rel
            if not target.is_file():
                # Warn rather than error: fixing this either means generating
                # the image or rewording the story, both of which are
                # content-author decisions. The linter's job is to surface
                # the dangling reference; strict mode (--strict) promotes it.
                f.warn(
                    f"{story_path.name}: references missing image "
                    f"`{rel}` (not found at {target.relative_to(REPO_ROOT)})"
                )

    f.stats["stories_with_image_refs"] = stories_with_images
    f.stats["unique_images_referenced"] = len(referenced)

    orphaned = sorted(existing - referenced - {".gitkeep"})
    if orphaned and len(orphaned) > 5:
        f.warn(
            f"images/ contains {len(orphaned)} files that are not "
            f"referenced by any story (e.g. {', '.join(orphaned[:5])}, ...). "
            f"That's fine if they're shared character sheets, but consider "
            f"documenting that in prompts/README.md."
        )


def count_prompts(f: Findings) -> int:
    total = 0
    per_file_counts: dict[str, int] = {}
    for p in list_prompt_files():
        count = len(PROMPT_LINE_RE.findall(p.read_text(encoding="utf-8")))
        per_file_counts[p.name] = count
        total += count
    f.stats["total_prompts"] = total
    if per_file_counts:
        f.stats["min_prompts_per_file"] = min(per_file_counts.values())
        f.stats["max_prompts_per_file"] = max(per_file_counts.values())
    return total


# Patterns that *may* appear in documentation announcing the prompt count.
# Any integer that matches one of these gets compared against the real total.
# A mismatch is an error; if none of the patterns match in a file we stay
# silent (the doc simply doesn't make that claim).
DOC_CLAIM_PATTERNS: list[tuple[Path, list[re.Pattern[str]], str]] = [
    (
        REPO_ROOT / "CLAUDE.md",
        [
            re.compile(r"\*\*Total Prompts\*\*:\s*(\d+)"),
            re.compile(r"\*\*(\d+)\+?\s+total prompts\*\*"),
        ],
        "CLAUDE.md prompt-count claim",
    ),
    (
        REPO_ROOT / "prompts" / "README.md",
        [
            re.compile(r"\*\*Tổng số prompts:\*\*\s*\**\s*(\d+)"),
        ],
        "prompts/README.md prompt-count claim",
    ),
]


def check_doc_claims(f: Findings, total_prompts: int) -> None:
    for path, patterns, label in DOC_CLAIM_PATTERNS:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for pat in patterns:
            for m in pat.finditer(text):
                claimed = int(m.group(1))
                if claimed != total_prompts:
                    f.err(
                        f"{label}: claims {claimed} prompts but repo "
                        f"actually has {total_prompts}. Update the docs "
                        f"(or the prompts) to match."
                    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit JSON report")
    parser.add_argument(
        "--strict",
        action="store_true",
        help=(
            "Exit non-zero if any warnings are present. Turn this on once "
            "the known legacy warnings (short stories, missing POST-CREDIT "
            "headers in stories 02–06, missing images/23.png) have been "
            "addressed."
        ),
    )
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="Deprecated alias for --strict.",
    )
    args = parser.parse_args(argv)

    f = Findings()
    check_story_prompt_pairing(f)
    check_required_sections(f)
    check_image_refs(f)
    total = count_prompts(f)
    check_doc_claims(f, total)

    if args.json:
        print(
            json.dumps(
                {"errors": f.errors, "warnings": f.warnings, "stats": f.stats},
                indent=2,
                ensure_ascii=False,
            )
        )
    else:
        print("== ai-vn-comic structural lint ==")
        print()
        for key, val in sorted(f.stats.items()):
            print(f"  {key}: {val}")
        print()
        if f.warnings:
            print(f"WARNINGS ({len(f.warnings)}):")
            for w in f.warnings:
                print(f"  - {w}")
            print()
        if f.errors:
            print(f"ERRORS ({len(f.errors)}):")
            for e in f.errors:
                print(f"  - {e}")
            print()
        else:
            print("No structural errors found.")

    if f.errors:
        return 1
    if (args.strict or args.warnings_as_errors) and f.warnings:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
