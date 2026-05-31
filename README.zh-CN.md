# RoboScholar Skills

面向科研工作流的可复用 Codex skills。

## 已包含的 Skills

### `journal-finder`

`journal-finder` 是一个注重隐私保护的 Codex skill，用于为论文草稿寻找合适的投稿期刊和仍开放的特刊。适用于：

- 筛选 SCI/SCIE、JCR、中科院分区期刊；
- 检查期刊 aims and scope、影响因子、分区、文章类型和投稿要求；
- 查找仍未截止的特刊，并核验截止日期是否有效；
- 查找候选期刊中与你稿件主题相近的已发表文章；
- 给出稿件需要补强的内容，例如 baseline、消融实验、统计检验、可复现性、实物或实验需求；
- 在公开检索时避免泄漏未发表论文内容。

这个 skill 会先在本地读取稿件，再只使用宽泛领域词、期刊名和通用主题词进行公开检索。它明确要求 Codex 不要把未发表论文的题名、摘要、独有假设、精确结论、独有方法名、表格、图片或结果句子粘贴到公开搜索引擎。

## 安装

用 Codex skill installer 从本仓库安装：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo clockyee/RoboScholar-Skills \
  --path journal-finder
```

安装后重启 Codex，新的 skill 才会被自动发现。

## 使用

```text
Use $journal-finder to recommend suitable SCI journals and open special issues for my manuscript, with revision gaps and source links.
```

你可以提供本地论文 PDF 或简短的私有说明。对于未发表稿件，建议优先提供本地文件，让 skill 在本地抽取主题和短板。

## 隐私与安全

本仓库不应包含论文原稿、草稿、实验数据、生成的期刊筛选报告、Excel 表格、API key 或任何凭据。

推送前建议运行：

```bash
git status --short
grep -RInE "BEGIN (RSA|OPENSSH|PRIVATE) KEY|api[_-]?key|secret|token|password|Bearer " \
  --exclude="README*" --exclude=".gitignore" --exclude-dir=".git" . || true
find . -type f \( -name "*.pdf" -o -name "*.docx" -o -name "*.xlsx" -o -name "*.csv" -o -name "*.tex" -o -name "*.bib" \) -print
```

第二条命令正常情况下不应输出任何文件，除非你明确要上传公开示例文件。

## 许可证

MIT License。见 [LICENSE](LICENSE)。
