# Contributing to Quant Guru Desk

Thank you for your interest in contributing! This document explains how to propose changes, add new gurus, and ensure quality.

## Ways to contribute

1. **Improve an existing guru** — Refine methodology, add references, fix inaccuracies
2. **Add a new guru** — Distill a public investment methodology into the desk format
3. **Improve shared infrastructure** — Evidence standards, competition rules, price fetching
4. **Add test cases** — Propose new behavioral tests in `evals/test-cases.md`
5. **Fix documentation** — Typos, clarifications, better examples

## Adding a new guru

1. Create `gurus/<new-guru>/SKILL.md` with:
   - YAML frontmatter (`name`, `description`, `version`)
   - Request router (Daily Run / Theme Scan / Analyze / Compare / Learn modes)
   - Full methodology workflow
   - Quantitative scoring system
   - Portfolio construction rules
   - Persona notes
   - Hard rules (must include evidence-standards compliance)
   - Bundled references table

2. Create `gurus/<new-guru>/references/` with at minimum:
   - `framework.md` — The full analytical framework
   - `scoring-system.md` — Quantitative scoring rubric with weights
   - `track-record.md` — Honest assessment including criticisms
   - `glossary.md` — Domain-specific term definitions
   - `competition-format.md` — Competition-specific adaptations

3. Update root files:
   - Add row to roster table in `SKILL.md`
   - Add row to smart-recommendation mapping in `SKILL.md`
   - Add entry in `README.md` (both English and Chinese sections)
   - Add entry in `CHANGELOG.md` under `[Unreleased]`

4. Quality bar:
   - Methodology must be from **public sources** (books, interviews, published research, public filings)
   - Must include honest track-record AND criticism — no hagiography
   - Must cite sources for all methodology claims
   - Must pass all existing evals (new guru should not break any test case)

## Code style

- Markdown files: ATX headings (`#`), one blank line before lists, fenced code blocks with language tags
- YAML frontmatter: `name` (lowercase-hyphenated), `description` (quoted string), `version` (semver)
- Tables: aligned pipes, header separator row
- No trailing whitespace, single newline at EOF
- Keep individual files focused — prefer multiple small files over one monolithic file

## Commit messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(serenity): add NINGI short report context to controversies
fix(shared): correct arithmetic identity formula in evidence-standards
docs: update README with v1.1.0 changes
test(evals): add TC-11 for multi-day competition continuity
```

## Pull request process

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/new-guru-buffett`)
3. Make your changes
4. Run through `evals/test-cases.md` mentally (or with an agent) to verify no regressions
5. Update `CHANGELOG.md` under `[Unreleased]`
6. Submit a pull request with:
   - Clear description of what changed and why
   - Which test cases are affected
   - For new gurus: sources used for distillation

## Quality principles

1. **Faithful distillation** — Reproduce the real methodology, not a blend or improvement. If you disagree with a guru's method, note it in track-record, don't "fix" the method.
2. **Evidence over narrative** — Every claim about a methodology should be traceable to a public source.
3. **Honest limitations** — Include criticisms, failure modes, and known biases for every guru.
4. **Distinct voices** — Each guru must sound and reason differently. The value is in contrast, not consensus.
5. **No financial advice** — This is research infrastructure. Never produce actionable buy/sell instructions.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
