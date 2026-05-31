#!/usr/bin/env python3
"""Extract local manuscript signals without network access.

Usage:
  python extract_manuscript_signals.py manuscript.pdf --max-pages 8

The script prints JSON with broad manuscript signals, placeholder risks,
section headings, and simple term counts. It intentionally does not call
external services.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


TERMS = [
    "robot",
    "robotics",
    "simulation",
    "physical",
    "hardware",
    "experiment",
    "baseline",
    "ablation",
    "statistical",
    "p-value",
    "confidence interval",
    "bootstrap",
    "code",
    "data",
    "reproduc",
    "energy",
    "morphology",
    "evolution",
    "embodied",
]

PLACEHOLDER_PATTERNS = [
    r"First Author",
    r"Second Author",
    r"email@",
    r"Keywords:\s*one,\s*two",
    r"This is a L\s*A\s*T\s*E\s*X template",
    r"TODO",
    r"\[TODO\]",
]


def extract_pdf_text(path: Path, max_pages: int | None) -> tuple[str, int]:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - environment dependent
        raise SystemExit(
            "Missing pypdf. Use the bundled Codex Python runtime or install pypdf."
        ) from exc

    reader = PdfReader(str(path))
    limit = len(reader.pages) if max_pages is None else min(max_pages, len(reader.pages))
    text = "\n".join(reader.pages[i].extract_text() or "" for i in range(limit))
    return text, len(reader.pages)


def headings(text: str) -> list[str]:
    found: list[str] = []
    for line in text.splitlines():
        item = line.strip()
        if len(item) > 120:
            continue
        if re.match(r"^(\d+\.?\s+[A-Z][A-Za-z0-9 ,:;()\-–]+|[A-Z][A-Za-z ]{3,}:)$", item):
            found.append(item)
    return found[:60]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf")
    parser.add_argument("--max-pages", type=int, default=None)
    args = parser.parse_args()

    path = Path(args.pdf).expanduser()
    text, page_count = extract_pdf_text(path, args.max_pages)
    lowered = text.lower()

    result = {
        "file": str(path),
        "pages": page_count,
        "extracted_pages": args.max_pages or page_count,
        "char_count": len(text),
        "section_headings": headings(text),
        "term_counts": {term: lowered.count(term.lower()) for term in TERMS},
        "placeholder_hits": [
            pattern for pattern in PLACEHOLDER_PATTERNS if re.search(pattern, text, re.I)
        ],
        "references_present": "references" in lowered,
        "likely_needs_attention": [],
    }

    if result["placeholder_hits"]:
        result["likely_needs_attention"].append("template_or_placeholder_text")
    if result["term_counts"]["baseline"] == 0:
        result["likely_needs_attention"].append("baseline_discussion_missing_or_sparse")
    if result["term_counts"]["ablation"] == 0:
        result["likely_needs_attention"].append("ablation_discussion_missing_or_sparse")
    if result["term_counts"]["p-value"] == 0 and result["term_counts"]["confidence interval"] == 0:
        result["likely_needs_attention"].append("statistical_testing_missing_or_sparse")
    if result["term_counts"]["physical"] == 0 and result["term_counts"]["hardware"] == 0:
        result["likely_needs_attention"].append("physical_validation_not_detected")
    if result["term_counts"]["code"] == 0 and result["term_counts"]["data"] == 0:
        result["likely_needs_attention"].append("reproducibility_statement_missing_or_sparse")

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
