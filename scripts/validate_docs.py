#!/usr/bin/env python3
"""Lightweight docs validator for PT-base markdown content.

Checks:
1) Balanced code fences
2) Broken relative markdown links (outside code blocks)
3) Python snippet syntax (`python`/`py` fenced blocks)
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path


OPEN_RE = re.compile(r"^(\s*)```\s*([A-Za-z0-9_+\-/]*)\s*$")
CLOSE_RE = re.compile(r"^\s*```\s*$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


@dataclass
class ValidationIssue:
    path: Path
    line: int
    kind: str
    message: str


def iter_markdown_files(root: Path, include_enzo: bool) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        if not include_enzo and "Enzo" in path.parts:
            continue
        files.append(path)
    return sorted(files)


def strip_fence_base_indent(lines: list[str], base_indent: int) -> str:
    normalized: list[str] = []
    for line in lines:
        if line.startswith(" " * base_indent):
            normalized.append(line[base_indent:])
        else:
            normalized.append(line.lstrip("\t"))
    return textwrap.dedent("\n".join(normalized))


def check_file(path: Path) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    lines = path.read_text(encoding="utf-8").splitlines()

    in_block = False
    block_lang = ""
    block_start_line = 0
    block_base_indent = 0
    block_lines: list[str] = []
    non_code_lines: list[str] = []

    for i, line in enumerate(lines, start=1):
        if not in_block:
            open_match = OPEN_RE.match(line)
            if open_match:
                in_block = True
                block_base_indent = len(open_match.group(1))
                block_lang = (open_match.group(2) or "").lower()
                block_start_line = i
                block_lines = []
            else:
                non_code_lines.append(line)
            continue

        if CLOSE_RE.match(line):
            if block_lang in {"python", "py"}:
                code = strip_fence_base_indent(block_lines, block_base_indent)
                try:
                    ast.parse(code)
                except SyntaxError as exc:
                    issues.append(
                        ValidationIssue(
                            path=path,
                            line=block_start_line + 1,
                            kind="python-syntax",
                            message=f"{exc.msg} (line {exc.lineno})",
                        )
                    )

            in_block = False
            block_lang = ""
            block_start_line = 0
            block_base_indent = 0
            block_lines = []
            continue

        block_lines.append(line)

    if in_block:
        issues.append(
            ValidationIssue(
                path=path,
                line=block_start_line,
                kind="fence-balance",
                message="unterminated code fence",
            )
        )

    text_outside_code = "\n".join(non_code_lines)
    for match in LINK_RE.finditer(text_outside_code):
        raw_link = match.group(1).strip()
        if (
            not raw_link
            or raw_link.startswith("#")
            or raw_link.startswith("http://")
            or raw_link.startswith("https://")
            or raw_link.startswith("mailto:")
        ):
            continue

        if raw_link.startswith("<") and raw_link.endswith(">"):
            raw_link = raw_link[1:-1]

        rel_target = raw_link.split("#", 1)[0]
        if not rel_target:
            continue

        target_path = (path.parent / rel_target).resolve()
        if not target_path.exists():
            # Best-effort line hint based on character offset.
            line_hint = text_outside_code[: match.start()].count("\n") + 1
            issues.append(
                ValidationIssue(
                    path=path,
                    line=line_hint,
                    kind="broken-link",
                    message=f"missing target: {raw_link}",
                )
            )

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate markdown docs consistency.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root to validate (default: project root).",
    )
    parser.add_argument(
        "--include-enzo",
        action="store_true",
        help="Include Enzo translation folder in validation.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    files = iter_markdown_files(root, include_enzo=args.include_enzo)

    all_issues: list[ValidationIssue] = []
    for md_file in files:
        all_issues.extend(check_file(md_file))

    if not all_issues:
        scope = "PT base + Enzo" if args.include_enzo else "PT base"
        print(f"[ok] validate_docs: {len(files)} markdown files checked ({scope}).")
        return 0

    print(f"[fail] validate_docs: found {len(all_issues)} issue(s).")
    for issue in all_issues:
        rel = issue.path.relative_to(root)
        print(f"- {rel}:{issue.line} [{issue.kind}] {issue.message}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
