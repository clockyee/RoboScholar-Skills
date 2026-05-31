---
name: journal-finder
description: Privacy-preserving academic journal and special-issue selection for manuscripts, PDFs, abstracts, or paper drafts. Use when Codex needs to recommend SCI/SCIE/JCR/CAS-ranked journals, open special issues, similar published articles, fit/risk, required manuscript improvements, experiment or hardware needs, and source-backed submission strategy without leaking unpublished manuscript details into public search.
---

# Journal Finder

## Core Rule

Protect unpublished work. Inspect manuscript files locally first, then search the web only with broad field terms, journal names, and generic topic labels. Do not paste the manuscript title, abstract, hypotheses, exact claims, unique method names, tables, figures, or result sentences into public search engines or external tools.

## Workflow

1. **Local manuscript pass**
   - Use `scripts/extract_manuscript_signals.py` for PDFs when available.
   - Run it with the bundled Codex Python runtime when system Python lacks `pypdf`.
   - Identify broad domains, methods, article type, evidence type, placeholders, missing statistics, missing baselines, data/code statements, and whether physical experiments are present.
   - Summarize internally as generic search terms, for example `evolutionary robotics`, `embodied evolution`, `morphology control co-adaptation`, not as exact manuscript wording.

2. **Clarify only high-impact preferences**
   - Ask only for preferences that cannot be inferred: required index/ranking system, priority between fit/impact/acceptance probability, whether hardware experiments can be added, and desired deliverable format.
   - If not specified, default to: fit and field recognition first, then impact factor; include spreadsheet if the user asks for tabular deliverables.

3. **Search current journal evidence**
   - Browse for current metrics and policies; journal IF, CAS/JCR partition, special issues, APCs, and author guidelines change over time.
   - Prefer official publisher/journal pages, Web of Science/JCR or institutional sources when available, then reputable metric aggregators only as cross-checks.
   - Read `references/search-playbook.md` before searching for detailed source priorities and query patterns.

4. **Score and rank venues**
   - Require the user's hard constraints first, such as SCI/SCIE and CAS 1/2.
   - Use the default score unless the user gives weights: topical fit 35%, field recognition 25%, metrics/ranking 20%, workload/risk 15%, open special issue 5%.
   - Separate `main targets`, `stretch targets`, `backup targets`, and `excluded/not recommended` instead of forcing all venues into one list.

5. **Find similar articles**
   - For each strong candidate, find 2-4 related articles from the same journal.
   - Record title, link/DOI, why it is similar, and what the user's manuscript must add or change relative to it.
   - Use generic terms and journal-name searches; avoid exact manuscript phrases.

6. **Check open special issues**
   - Check official journal special issue/call-for-papers pages first.
   - Record only calls still open on the current date. Put expired calls in a separate reference-only section if useful.
   - Verify that each special issue also satisfies the user's index/ranking requirements; do not promote an open special issue in a weak journal as a main target.

7. **Report manuscript improvement gaps**
   - Include venue-specific revision needs: article type, scope framing, baseline/ablation/statistics, real robot or hardware needs, data/code policy, length/page limits, figure/video requirements, and review style.
   - Explicitly flag desk-reject risks such as template placeholders, missing abstract/keywords, unclear contribution, weak related work, missing statistical support, and missing reproducibility.

## Deliverables

Use `references/output-template.md` for the recommended report shape. If a spreadsheet is requested, use the Spreadsheets skill and create sheets for:

- `Summary Ranking`
- `Journal Details`
- `Similar Articles`
- `Open Special Issues`
- `Revision Checklist`
- `Sources`

Every metric, scope claim, special issue, and similar article must have a source URL. Mark CAS partition from public sources as "needs institutional confirmation" unless it came from an authoritative subscription source available in the session.

## Domain Notes

For robotics, embodied AI, evolutionary robotics, artificial life, morphology-control co-design, bio-inspired systems, or soft robotics manuscripts, read `references/robotics-venue-notes.md` before ranking venues.
