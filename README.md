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
