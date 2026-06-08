# Bayesian Intrinsic Growth Valuation (shared tool)

A supplementary analytical framework for any guru to separate **intrinsic growth** from **FOMO/narrative-driven multiple expansion**. Not a standalone guru — a shared valuation lens that any guru can invoke when the question is "is this growth rate real or hype?"

## When to use

- User asks "is the growth priced in?" or "is this a bubble?"
- A candidate has extreme revenue growth but unclear sustainability
- Stock price moved 50%+ on narrative alone (no new fundamental data)
- You need to separate intrinsic-growth conviction from momentum/FOMO

## The six growth hypotheses

| Hypothesis | Growth rate (3-5yr CAGR) | Description |
|-----------|-------------------------|-------------|
| H0: Contraction | < 0% | Revenue shrinking; structural decline |
| H1: Stagnation | 0-5% | GDP-like; no differentiated growth |
| H2: Moderate growth | 5-15% | Healthy but not exceptional |
| H3: Strong growth | 15-30% | Clear leader in expanding market |
| H4: Hyper growth | 30-50% | Dominant position in explosive TAM |
| H5: Exponential | > 50% | Unprecedented; requires new market creation |

## The Bayesian update process

### Step 1: Establish prior distribution

Before looking at the latest data, assign a probability to each hypothesis based on:
- Historical growth rate (last 4-8 quarters)
- Industry base rate (what % of companies sustain this growth?)
- Company's track record of hitting guidance

**Example prior (a strong AI company):**
```
H0: 2%  H1: 5%  H2: 15%  H3: 35%  H4: 30%  H5: 13%
```

### Step 2: Classify new information

For each new data point, classify its type:
- **Fundamental** — revenue beat, margin change, new contract, guidance raise
- **Narrative** — analyst upgrade, KOL mention, media hype, "theme rotation"
- **Technical** — price breakout, volume surge, short squeeze

**Key rule:** Only Fundamental data updates intrinsic-growth probabilities. Narrative and Technical data update FOMO/sentiment, not the growth hypothesis.

### Step 3: Bayesian update (for fundamental data only)

For each fundamental data point:
1. Estimate the **likelihood** — how probable is this observation under each hypothesis?
2. Multiply prior × likelihood → unnormalized posterior
3. Normalize (sum to 100%)

**Simplified likelihood guide:**

| Observation | Most supports | Moderately supports | Weakly supports |
|-------------|--------------|--------------------|-----------------| 
| Revenue beat >20% | H4, H5 | H3 | — |
| Revenue beat 5-20% | H3, H4 | H2 | — |
| Revenue miss | H1, H2 | H0 | — |
| Guidance raised substantially | H4, H5 | H3 | — |
| Major new customer win | H3, H4 | H2 | — |
| Customer loss / churn increase | H0, H1 | H2 | — |
| Margin expansion + growth | H3, H4 | H5 | — |
| Growth deceleration (still positive) | H2, H3 | H1 | — |

### Step 4: Calculate weighted intrinsic growth

```
Weighted Growth = Σ (midpoint of hypothesis range × posterior probability)
```

Midpoints: H0=-5%, H1=2.5%, H2=10%, H3=22.5%, H4=40%, H5=65%

### Step 5: Reverse-engineer market-implied growth

From the current stock price, work backward:
1. Take current EV/Revenue or P/E
2. Assume the market's required return (10-12%)
3. Solve for the growth rate implied by the current multiple

**Rough shortcut:** `Market-implied growth ≈ (Forward P/E - 15) × 2%` for tech companies. If P/E = 50, implied growth ≈ 70%.

### Step 6: Compare and assess

```
Price-Growth Divergence = Market-implied growth − Weighted intrinsic growth
```

| Divergence | Interpretation | Action |
|-----------|---------------|--------|
| < -10pp | Market underestimates growth → Undervalued | Consider adding |
| -10pp to +10pp | Fairly priced | Hold; no urgency |
| +10pp to +25pp | Some optimism priced in | Monitor for de-rating risk |
| > +25pp | FOMO/narrative premium large | Caution; trim if evidence doesn't catch up |

## FOMO separation (the key innovation)

Track separately:
- **Intrinsic growth confidence** — changes ONLY on fundamental data (Steps 1-4)
- **FOMO/narrative premium** — the gap between market-implied and intrinsic (Step 6)

A stock can have HIGH intrinsic growth confidence AND high FOMO premium — meaning the growth is real but the price already reflects it. This distinction prevents both:
- Selling a genuinely high-growth company just because it "feels expensive"
- Holding a narrative-driven bubble because "growth is high"

## Output template (when invoked)

```
### 贝叶斯估值评估 — $TICKER

**后验概率分布：**
| H0 | H1 | H2 | H3 | H4 | H5 |
|----|----|----|----|----|----| 
| X% | X% | X% | X% | X% | X% |

**加权内在增速：** XX% CAGR
**市场隐含增速：** XX% CAGR  
**价格-增长偏离：** ±XXpp

**关键更新事件：**
| 数据点 | 类型 | 最支持假设 | 对增速判断的影响 |
|--------|------|-----------|----------------|

**FOMO 分离：**
- 内在增长信心变化：[unchanged / strengthened / weakened]
- 叙事/情绪溢价变化：[expanding / stable / contracting]

**结论：** [undervalued / fairly priced / FOMO premium present / caution]
```

## Integration with each guru

| Guru | When to invoke Bayesian tool | How it informs their decision |
|------|----------------------------|------------------------------|
| **Serenity** | A chokepoint candidate has run up 100%+ — is the growth real? | If FOMO premium > 25pp, reduce position sizing regardless of chokepoint score |
| **Kindig** | Forward-model validation — does the market already price in the forward revenue? | Directly feeds the "opportunity-cost test" — high FOMO premium = capital better deployed elsewhere |
| **Cathie** | A 5-year EV model shows huge upside — but is the cost-curve thesis priced in? | If market-implied growth already > 50%, the 15% CAGR hurdle may not be met from current price |

## Limitations

- This tool requires **quantitative inputs** (revenue growth, P/E, guidance). Without financial data, it cannot run.
- The simplified likelihood guide is a starting point — experienced users should adjust based on context.
- Not a substitute for fundamental due diligence — it organizes thinking about growth probability, not about quality/moat/risk.
