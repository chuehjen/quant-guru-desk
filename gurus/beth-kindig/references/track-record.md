# Track Record & Verification Caveats

## Reported performance (I/O Fund primary sources, Feb 2026)

| Metric | Value |
|--------|-------|
| Cumulative return since May 2020 launch | **326%** |
| Annualized | **29.2%/yr** |
| 2025 audited (blended/hedged) | **37%** |
| 2025 equity-only | **56%** |
| Outperformance vs Nasdaq-100 | ~152% |
| Outperformance vs tech ETFs | ~294% |
| $10,000 at inception → | ~$42,552 (vs $13,192 for institutional tech portfolios) |
| Ranking claim | top-tier "among Wall Street's best" (one cite: 8th among US hedge funds in 2025) |

## The NVIDIA call

- First entry **$3.15 (split-adjusted), December 2018** (NVIDIA ~$100B cap then).
- Cumulative NVIDIA gain cited ~**3,280%** (≈900% for the 2023-25 leg).
- Public forecasts: NVIDIA to **$10T** (Bloomberg, May 2024); **$20T by 2030** thesis.

## Verification posture (pro)

- Emphasizes **third-party audited returns**; claims >$210,000 spent on "accountability and transparency" (audits) since inception.
- Explicitly positions against unverified guru claims: "Institutional investors don't take claims at face value — they require proof."
- Covered by Bloomberg, Forbes (she's a contributor), Seeking Alpha, Yahoo Finance.

## Caveats to model honestly (con)

1. **Marketing-framed source.** Headline figures come predominantly from the firm's own (self-commissioned, audited) reporting and press releases, not a regulated fund filing. It's a *research/model portfolio*, not a public mutual fund with a regulated NAV.
2. **Single-position vs portfolio.** The NVIDIA "+3,280%" is one early entry, not the whole-portfolio return — do not treat it as the strategy's return.
3. **Hedge drag in up years.** The blended/hedged return (37% in 2025) materially lags equity-only (56%) in strong years. Model the **blended ~29% annualized as the realistic full-strategy benchmark**, and treat equity-only / single-stock numbers as upper-bound components.

## How to use this in the agent

- Quote performance with the "self-reported/audited" qualifier, never as independently regulated fact.
- Benchmark the strategy to ~29% annualized, not to the single-stock or equity-only headline.
- The verification discipline itself is part of the method — demand cited, gradeable evidence before assigning conviction.
