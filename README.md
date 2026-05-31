# RoboScholar Skills

Reusable Codex skills for research workflows.

## Included Skills

### `journal-finder`

`journal-finder` is a privacy-preserving Codex skill for selecting academic journals and open special issues for manuscripts. It is designed for tasks such as:

- finding SCI/SCIE, JCR, CAS-ranked journals;
- checking journal aims and scope, impact factor, ranking, article types, and author requirements;
- finding open special issues and confirming whether their deadlines are still valid;
- identifying similar papers in candidate journals;
- recommending manuscript improvements, including baselines, statistics, reproducibility, and hardware or experiment needs;
- avoiding leakage of unpublished manuscript details during public web search.

The skill first inspects manuscripts locally, then searches only with broad field terms, journal names, and generic topic labels. It explicitly instructs Codex not to paste unpublished titles, abstracts, hypotheses, exact claims, unique method names, tables, figures, or result sentences into public search engines.

## Installation

Install from this repository with the Codex skill installer:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo clockyee/RoboScholar-Skills \
  --path journal-finder
```

Restart Codex after installation so the skill is discovered.

## Usage

```text
Use $journal-finder to recommend suitable SCI journals and open special issues for my manuscript, with revision gaps and source links.
```

You can provide a manuscript PDF or a brief private description. For unpublished manuscripts, prefer attaching the local file and let the skill extract signals locally.

## Example

### Input

```text
Use $journal-finder to help me find suitable journals for this unpublished manuscript:
/path/to/manuscript.pdf

Requirements:
- SCI/SCIE only
- CAS Q1 or Q2 preferred
- strong recognition in robotics or embodied AI
- check whether there are still-open special issues
- rank by topical fit first, then impact factor
- tell me whether a physical robot experiment is needed
- provide a Chinese report and an XLSX summary

Privacy requirement:
Do not search the manuscript title, abstract, exact claims, or result sentences on public platforms.
```

### Expected Output

```text
Recommendation summary:
1. Journal A - main target; strong topical fit; SCIE, JCR Q1, CAS Q1/Q2; physical robot not mandatory.
2. Journal B - robotics-recognized target; better if a small hardware prototype is added.
3. Journal C - high-impact stretch target; requires stronger baselines and statistical validation.

For each journal:
- journal name, publisher, SCI/SCIE status, CAS partition, JCR quartile, latest impact factor;
- aims and scope summary with source link;
- fit assessment and submission risk;
- 2-4 similar articles from the same journal with links;
- whether a physical robot or hardware experiment is expected;
- revision workload before submission.

Open special issues:
- list only still-open calls that satisfy the user's hard requirements;
- mark expired or weak-fit calls as backup/reference only.

Revision checklist:
- remove template placeholders;
- rewrite abstract, keywords, and contribution statement;
- add baselines, ablations, statistical tests, and reproducibility notes;
- add hardware or real-world validation if targeting robotics-first venues.

Deliverables:
- a concise report in the requested language;
- optional XLSX workbook with sheets: Summary Ranking, Journal Details, Similar Articles,
  Open Special Issues, Revision Checklist, Sources.
```

## Privacy Notes

This repository does not include manuscripts, drafts, source data, generated journal reports, spreadsheets, API keys, or credentials.

Before pushing changes, run:

```bash
git status --short
grep -RInE "BEGIN (RSA|OPENSSH|PRIVATE) KEY|api[_-]?key|secret|token|password|Bearer " \
  --exclude="README*" --exclude=".gitignore" --exclude-dir=".git" . || true
find . -type f \( -name "*.pdf" -o -name "*.docx" -o -name "*.xlsx" -o -name "*.csv" -o -name "*.tex" -o -name "*.bib" \) -print
```

The second command should print nothing unless you intentionally added public sample files.

## License

Apache License 2.0. See [LICENSE](LICENSE).
