# Chokepoint Scorecard

A quantitative scoring system for ranking supply-chain bottleneck candidates. Adapted from [muxuuu/serenity-skill](https://github.com/muxuuu/serenity-skill).

## Positive factors (8 factors, 0-5 each, weighted to 100)

### 1. Demand inflection (weight: 15%)
- 5: Structural demand shift proven by multiple quarters of data (e.g., AI optical interconnect demand doubling YoY)
- 4: Clear inflection with 1-2 quarters of accelerating demand
- 3: Demand growing but not yet inflecting
- 2: Demand steady, no acceleration signal
- 1: Demand declining or uncertain
- 0: No identifiable demand driver

### 2. Architecture coupling (weight: 10%)
- 5: Designed into next-gen architecture as sole/primary source, certified, reference design
- 4: Designed in as one of two suppliers, certified
- 3: In evaluation/qualification phase with named customers
- 2: Claims relevance but no named customer or certification evidence
- 1: Peripheral to the architecture, easily substituted
- 0: No architectural coupling

### 3. Chokepoint severity (weight: 15%)
- 5: Physical monopoly — no alternative technology or supplier exists in the near term
- 4: Near-monopoly with one weak alternative that's years from qualification
- 3: One of 2-3 suppliers with meaningful differentiation
- 2: Commodity-like with some differentiation
- 1: Commodity, many interchangeable suppliers
- 0: Oversupplied market

### 4. Supplier concentration (weight: 12%)
- 5: Single supplier globally (e.g., ASML for EUV)
- 4: 2 suppliers, one dominant (>60% share)
- 3: 3-4 suppliers, fragmented but with a leader
- 2: 5+ suppliers, competitive market
- 1: Many suppliers, buyer's market
- 0: No concentration at all

### 5. Expansion difficulty (weight: 12%)
- 5: 5+ years to add meaningful capacity (specialized equipment, rare materials, extreme purity requirements)
- 4: 3-5 years (heavy capex, long qualification)
- 3: 2-3 years (moderate capex, some qualification needed)
- 2: 1-2 years (manageable capex)
- 1: <1 year (capacity can be added quickly)
- 0: No capacity constraint

### 6. Evidence quality (weight: 15%)
- 5: Multiple strong sources (SEC filings + earnings transcripts + customer contracts + government recognition)
- 4: 2-3 strong sources corroborating
- 3: 1 strong source + multiple medium sources
- 2: Medium sources only (media, trade publications)
- 1: Weak sources only (social media, KOL posts)
- 0: No evidence, pure speculation

### 7. Valuation disconnect (weight: 11%)
- 5: Market cap <10% of the addressable opportunity, no analyst coverage
- 4: Market cap <25% of opportunity, minimal coverage
- 3: Market cap 25-50% of opportunity
- 2: Market cap roughly reflects the opportunity
- 1: Market cap exceeds the near-term opportunity
- 0: Massively overvalued relative to fundamentals

### 8. Catalyst timing (weight: 10%)
- 5: Dated catalyst within 1-2 quarters (earnings, index inclusion, government filing, M&A close)
- 4: Catalyst within 2-4 quarters
- 3: Catalyst exists but timing uncertain (1-2 years)
- 2: Vague catalyst ("when demand ramps")
- 1: No identifiable catalyst
- 0: Negative catalyst approaching (dilution, lawsuit, competition)

## Penalty factors (8 factors, 0-5 each, multiplied by 2.0x weight)

Each penalty reduces the total score. A score of 5 on a penalty factor deducts 10 points from the total.

### 1. Dilution/financing
- ATM offering active or recently completed
- Convertible notes, secondary raises
- Dilution amount > 20% of market cap

### 2. Governance
- Insider selling at current levels
- Related-party transactions
- Opaque corporate structure

### 3. Geopolitics
- Jurisdiction with high regulatory/sovereignty risk
- Export control exposure
- Subsidy dependence (removal risk)

### 4. Liquidity
- Average daily volume < $1M
- Small float, delisting risk
- OTC/pink sheet listing

### 5. Hype risk
- Stock price primarily driven by social media mentions
- Meme-stock characteristics
- No fundamental backing for recent price action

### 6. Accounting quality
- Revenue recognition concerns
- Receivables/inventory growing faster than revenue
- Frequent restatements or auditor changes

### 7. Cyclicality
- End-demand highly cyclical (auto, consumer electronics)
- Customer capex cycle risk
- Pricing power erodes in downturns

### 8. Alternative design
- Technology substitution risk (copper replacing optics, etc.)
- New architecture could bypass the bottleneck
- R&D breakthroughs at competitors

## Rating thresholds

| Score | Rating | Action |
|-------|--------|--------|
| 85+ | Top research priority | Strong conviction position (20-30%) |
| 70-84 | High research priority | Core position (10-15%) |
| 55-69 | Worth tracking | Exploratory position (5-8%) |
| <55 | Early lead / low priority | Monitor only, do not hold |

## Quick scoring example

**$SIVE (hypothetical):**
- Demand inflection: 4 (CPO ramp accelerating)
- Architecture coupling: 5 (sole-source laser for multiple CPO platforms)
- Chokepoint severity: 4 (near-monopoly, one weak alternative)
- Supplier concentration: 4 (dominant supplier)
- Expansion difficulty: 4 (3-5 years for competitors)
- Evidence quality: 3 (customer references but no public contracts)
- Valuation disconnect: 4 (~$2B MC vs large TAM)
- Catalyst timing: 4 (MSCI inclusion approaching)

**Positive subtotal: (4×15 + 5×10 + 4×15 + 4×12 + 4×12 + 3×15 + 4×11 + 4×10) / 5 = 82.6**

- Dilution: 1 (minimal)
- Hype risk: 3 (social media driven, NINGI short report)
- Liquidity: 2 (moderate volume)

**Penalty: (1 + 3 + 2) × 2.0 = 12**

**Final score: 82.6 - 12 = 70.6 → High research priority**
