# Regime Scorecard — Dalio Agent

A quantitative scoring system for assessing the macro environment. Unlike stock-level scorecards, this evaluates the ENVIRONMENT that all assets operate in. The output is a regime classification + confidence level that drives asset allocation.

## Macro factors (8 factors, 0-5 each, weighted to 100)

### 1. Debt cycle position (weight: 16%)

Where in the short-term debt cycle are we?

- 5: Early expansion — rates just cut, credit thawing, PMI inflecting upward, best time to own risk assets
- 4: Mid expansion — growth above trend, healthy credit, rates stable, equities grind higher
- 3: Neutral — mixed signals, neither clearly expanding nor contracting
- 2: Late expansion — full employment, credit loose, speculation rising, tightening underway, be cautious
- 1: Tightening — curve inverted, credit tightening, PMI declining, recession approaching
- 0: Active recession/deleveraging — demand collapsing, defaults rising, maximum caution

### 2. Liquidity conditions (weight: 15%)

Is money flowing into or out of the system?

- 5: Global easing — multiple central banks cutting, QE active, M2 growing, credit expanding
- 4: Net easing — Fed cutting or paused after cuts, global liquidity positive
- 3: Neutral — tightening ending but not yet easing, M2 flat, credit stable
- 2: Net tightening — QT active, rates still rising or high, bank lending tightening
- 1: Aggressive tightening — emergency hikes, liquidity withdrawal, credit crunch emerging
- 0: Liquidity crisis — funding markets frozen, interbank stress, central bank emergency facilities activated

### 3. Growth trajectory (weight: 14%)

Not just the level but the DIRECTION of growth.

- 5: Growth accelerating from a low base — the best environment for risk assets
- 4: Growth solid and stable — above-trend GDP, strong employment, consumer healthy
- 3: Growth stable but decelerating — still positive but losing momentum
- 2: Growth stalling — nearing trend, mixed data, leading indicators turning
- 1: Growth contracting — negative GDP prints, rising unemployment, capex cuts
- 0: Deep recession — multi-quarter contraction, systemic risk

### 4. Inflation regime (weight: 14%)

The type and direction of inflation matters more than the level.

- 5: Disinflation from high levels — the "Goldilocks glide path," best for bonds + stocks together
- 4: Low stable inflation (1.5-2.5%) — price stability, central bank can be accommodative
- 3: Inflation moderating but above target (2.5-4%) — progress but not resolved
- 2: Inflation sticky/re-accelerating (>4%) — policy tension, bonds under pressure
- 1: Inflation high and broadening (>5%) — wage-price dynamics, aggressive tightening needed
- 0: Hyperinflationary or deflationary spiral — extreme regime, portfolio must be defensive

### 5. Credit spreads / financial stress (weight: 12%)

The health of the financial system's plumbing.

- 5: Spreads at tights, no stress anywhere — credit freely available, risk-on environment
- 4: Spreads low and stable — occasional volatility absorbed quickly
- 3: Spreads widening moderately — early caution signals, monitoring needed
- 2: Spreads elevated — risk aversion rising, weaker credits losing market access
- 1: Spreads spiking — crisis dynamics emerging, flight to quality underway
- 0: Credit market seizure — no new issuance, funding markets frozen, systemic risk

### 6. Currency / dollar dynamics (weight: 10%)

The dollar as the global reserve currency creates unique dynamics.

- 5: Dollar weakening orderly — global risk-on, EM assets benefit, commodities rally
- 4: Dollar stable — no major tailwind or headwind from currency
- 3: Dollar strengthening moderately — headwind for commodities and EM, but manageable
- 2: Dollar strengthening aggressively — tightening global financial conditions, EM stress
- 1: Dollar shortage — offshore funding crisis, global deleveraging via dollar strength
- 0: Dollar crisis (either direction) — loss of reserve status concerns OR global funding seizure

### 7. Geopolitical risk (weight: 10%)

Events that can override all other factors.

- 5: Geopolitical calm — no major conflicts, trade flowing freely, globalization intact
- 4: Low-level tensions — manageable disputes, sanctions limited, supply chains adapting
- 3: Elevated but contained — active conflict(s) but not escalating, trade tensions moderate
- 2: Significant disruption — major trade war, key supply routes threatened, energy weaponized
- 1: Acute crisis — military escalation near critical infrastructure, sanctions on major economies
- 0: Systemic geopolitical rupture — major power conflict, global supply chains broken, reserve currency under attack

### 8. Paradigm shift probability (weight: 9%)

Is the market consensus about to break?

- 5: Strong consensus, no contradictions — paradigm stable, follow the trend
- 4: Consensus holding but cracks appearing — watch for early movers
- 3: Growing divergence between market pricing and fundamental reality
- 2: Clear contradictions — market acting "wrong" relative to data, shift likely within 6-12 months
- 1: Paradigm actively breaking — old rules failing, high uncertainty, repositioning underway
- 0: New paradigm unclear — old one dead, new one not yet established, maximum uncertainty

## Regime classification output

After scoring all 8 factors, classify the regime:

### Step 1: Quadrant determination

| Growth score (factor 3) | Inflation score (factor 4) | Quadrant |
|------------------------|-----------------------------|----------|
| ≥ 3 (growth positive) | ≥ 4 (inflation low/falling) | **Goldilocks** |
| ≥ 3 (growth positive) | ≤ 2 (inflation high/rising) | **Reflation** |
| ≤ 2 (growth weak) | ≤ 2 (inflation high/rising) | **Stagflation** |
| ≤ 2 (growth weak) | ≥ 4 (inflation low/falling) | **Deflation** |

### Step 2: Confidence level

| Total score (sum all 8) | Confidence in allocation |
|-------------------------|------------------------|
| 32-40 | High confidence — lean into tactical tilts |
| 24-31 | Moderate confidence — stay close to All-Weather base |
| 16-23 | Low confidence — maximize diversification, raise cash |
| < 16 | Crisis — defensive posture, gold + cash + short-duration bonds |

### Step 3: Transition risk flag

If paradigm shift probability (factor 8) ≤ 2 OR credit stress (factor 5) ≤ 2:
→ Flag "REGIME TRANSITION RISK" — raise cash buffer by 10%, reduce tactical tilts

## Regime-to-allocation mapping

| Quadrant | Stocks | Long bonds | TIPS | Gold | Commodities | Cash |
|----------|--------|-----------|------|------|-------------|------|
| **Goldilocks** | 40% | 25% | 5% | 5% | 10% | 15% |
| **Reflation** | 30% | 10% | 15% | 10% | 25% | 10% |
| **Stagflation** | 15% | 10% | 15% | 25% | 15% | 20% |
| **Deflation** | 15% | 35% | 5% | 15% | 5% | 25% |
| **Transition/uncertain** | 20% | 20% | 10% | 15% | 10% | 25% |

These are starting points. Tactical tilts of ±10% on any category are permitted with high-conviction evidence.
