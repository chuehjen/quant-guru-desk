# Changelog

All notable changes to Quant Guru Desk will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.0.0] - 2026-06-08

### Added
- `shared/market-sources.md` — Cross-market information source playbook covering 7 markets (US, A-shares, HK, Taiwan, Japan, Korea, Europe) with per-market source tables, evidence grading, and 5 cross-market intelligence tips
- `shared/bayesian-valuation.md` — Bayesian intrinsic growth valuation shared tool: 6 hypotheses (H0 contraction to H5 exponential), 6-step Bayesian update process, FOMO separation methodology, price-growth divergence interpretation, per-guru integration guide
- `scripts/gf_dma.py` — GF-DMA technical health index calculator (Python 3.9+, zero deps): fundamental speed × DMA alignment × divergence analysis × trend parallelism → 0-100 score with 6 health states
- `dashboard/index.html` — Competition visualization dashboard (Chart.js): paste JSON data to render cumulative return curves, guru comparison cards, and portfolio snapshot table

### Changed
- Root SKILL.md shared resources table expanded with market-sources and bayesian-valuation entries
- Root SKILL.md version bumped to 2.0.0

## [1.2.0] - 2026-06-08

### Added
- `shared/dialogue-protocol.md` — Structured 5-level teaching ladder for Learn mode, with per-guru L1 mapping, dialogue flow template, and transition triggers
- `scripts/scorecard.py` — Local Python scoring tool (zero dependencies, Python 3.9+); input JSON → weighted score + Markdown report with visual bar and warnings
- `examples/daily-run-serenity.md` — Complete Serenity daily-run output example with evidence map
- `examples/panel-mode-amd.md` — Three-guru panel debate example showing distinct voices and explicit divergence
- `examples/competition-day5.md` — Competition Day 5 output example with arithmetic identity check demonstrated
- Minimum completion standards added to all three gurus' Daily Run / Theme Scan modes

### Changed
- Root SKILL.md: Learn mode instruction expanded to reference dialogue-protocol; shared resources table updated
- Serenity SKILL.md: Step B now includes minimum standards (≥3 layers, ≥5 candidates, ≥1 Strong source/candidate)
- Beth Kindig SKILL.md: Step B now includes minimum standards (≥5 candidates, ≥1 Strong source/model, kill-switch check)
- Cathie Wood SKILL.md: Step B now includes minimum standards (≥5 candidates, platform tag, ≥1 Strong source/cost-curve)
- Root SKILL.md version bumped to 1.2.0

## [1.1.0] - 2026-06-08

### Added
- `shared/evidence-standards.md` — Three-tier evidence ladder (Strong/Medium/Weak) with mandatory citation rules, red flag checklist, and evidence map template
- `evals/test-cases.md` — 10 behavioral test cases covering: no buy/sell instructions, no hallucinated financials, arithmetic identity, data conflict detection, universe boundary, panel mode voice preservation, evidence downgrade, output language, learn mode, and competition first-day format
- `CHANGELOG.md` — Version history tracking
- `CONTRIBUTING.md` — Contribution guidelines for the project
- Evidence-grading requirements added to all three gurus' Hard Rules sections
- `shared/evidence-standards.md` referenced in root SKILL.md shared resources table

### Changed
- Root `SKILL.md` version bumped to 1.1.0
- Serenity SKILL.md Hard Rules expanded with evidence-grading constraints (rules 8-11)
- Beth Kindig SKILL.md Hard Rules expanded with evidence-grading constraints (rules 10-13)
- Cathie Wood SKILL.md Hard Rules expanded with evidence-grading constraints (rules 10-13)
- Root SKILL.md Hard Rules expanded with evidence-grading constraint (rule 8)
- README updated with version badge, new file descriptions, and evals section

## [1.0.0] - 2026-06-04

### Added
- Initial release with three gurus: Serenity, Beth Kindig, Cathie Wood
- Root SKILL.md with request router, smart-recommendation mapping, and panel mode
- `shared/competition-rules.md` — Unified competition format
- `shared/price-fetching.md` — Price fallback chain and quality checks
- Per-guru SKILL.md with full methodology, scoring, persona, and hard rules
- Per-guru references (framework, scoring-system, holdings, track-record, glossary, competition-format)
- Serenity-specific: supply-chain-map, exemplars, controversies, market-sources
- README with bilingual documentation (English + Chinese)
- MIT License
