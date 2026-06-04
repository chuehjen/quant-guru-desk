# ARK 6-Metric Scoring System

ARK's actual bottom-up scoring framework. Score each candidate **1-10** on six dimensions, aggregate to a composite, then rank all candidates against each other across platforms. The composite drives portfolio weight.

## The six metrics

### 1. Company / People & Culture (1-10)
Quality, vision, and mission-alignment of management and the organization. ARK favors visionary, mission-driven founders.

### 2. Execution of Objectives (1-10)
Track record of hitting milestones and delivering on stated goals. Has the company done what it said it would?

### 3. Moat / Barriers to Entry (1-10)
Defensibility: network effects, proprietary technology, proprietary data, scale advantages.

### 4. Product & Service Leadership (1-10)
Product superiority and innovation leadership *within the platform*. Is it the best-in-class disruptor?

### 5. Thesis Risk (1-10, higher = lower risk)
Risks to the investment thesis: regulatory, competitive, execution, dilution. A high score means the thesis is robust to these.

### 6. Valuation (1-10)
Bottom-up 5-year model **targeting ~15% minimum annual return** over the horizon. Higher score = more attractive expected 5-year CAGR. *This is where buy-the-dip mechanics enter:* a lower price raises the expected CAGR, raising this score, raising the weight.

## Aggregation & ranking

- Composite = (weighted or simple) average of the six. Debate and adjust in "stock meetings."
- Rank **every security against every other** across all five platforms — a single conviction-ordered list.
- Composite → conviction → portfolio weight. Highest scores get the largest weights (top name ~10-12%, top 10 ≈ 50%+).
- **Re-validate continuously.** New cost data, milestones, or fundamentals change scores → rankings → weights. ARK trades daily as a result.

## Buy-the-dip / trim-winners mechanics

- **Stock sells off, thesis intact** → price down → expected 5-year CAGR up → Valuation score up → composite up → **add to position**. Mechanical.
- **Stock runs up** → expected forward CAGR down → Valuation score down → **trim and recycle** into higher-scored names.

## Worked example (illustrative — Tesla)

| Metric | Score (1-10) | Note |
|--------|-------------|------|
| People & Culture | 9 | visionary founder, mission-driven |
| Execution | 7 | delivers, but timelines slip |
| Moat | 8 | data/scale/vertical integration |
| Product Leadership | 9 | autonomy + energy + manufacturing |
| Thesis Risk | 6 | regulatory/competition/key-person risk |
| Valuation (5yr) | 8 | EV model: ~60% of value from robotaxi; base case well above the 15% hurdle |
| **Composite** | **≈7.8** | flagship weight (~10%) |

ARK's published Tesla base case ≈ $2,600/share by 2029 (Monte Carlo; robotaxi ≈ 60% of expected value). *Targets change frequently — rebuild from cited figures each run.*

## Competition adaptation

The 6-metric scoring, 15%/5-yr hurdle, conviction concentration, buy-the-dip, and trim-winners logic transfer directly. The only change: express the blockchain platform through crypto-*equities* (COIN/HOOD/CRCL/XYZ), never tokens or spot-crypto ETFs (see `competition-format.md`).
