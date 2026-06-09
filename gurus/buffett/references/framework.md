# Buffett Value-Investing Framework

## The mental model

"I'm 85% Benjamin Graham and 15% Phil Fisher." The early Buffett bought cigar-butt cheap stocks; the mature Buffett (post-Munger, post-See's Candies) buys wonderful businesses at fair prices. This agent embodies the mature Buffett.

## The decision tree (every candidate must pass sequentially)

```
1. Circle of competence? → NO → STOP (no analysis, no opinion)
                         → YES ↓
2. Durable moat exists?  → NO → PASS (no matter how cheap)
                         → YES ↓
3. Honest, capable mgmt? → NO → PASS (moat erodes without good stewards)
                         → YES ↓
4. Intrinsic value calculable? → NO → WAIT (come back when earnings normalize)
                               → YES ↓
5. Margin of safety ≥25%? → NO → WATCHLIST (wonderful but too expensive today)
                          → YES ↓
6. BUY and hold until moat breaks or better opportunity at materially higher conviction.
```

## Owner earnings (the key metric)

Buffett's 1986 letter defines "owner earnings":

```
Owner earnings = Reported earnings
              + Depreciation & amortization
              + Other non-cash charges
              − Average annual maintenance capex
              − Working capital increases needed to maintain volume
```

This differs from:
- **GAAP net income** — distorted by non-cash, one-time items
- **EBITDA** — ignores capex entirely ("Does management think the tooth fairy pays for capital expenditures?")
- **Free cash flow** — close but uses total capex, not just maintenance capex

## Intrinsic value via discounted owner earnings

1. Calculate current owner earnings (use trailing 4 quarters, normalized for any one-timers)
2. Apply a growth rate:
   - Mature compounder (KO, JNJ): 4-8% perpetuity
   - Quality grower (AAPL, V): 8-12% for 10 years, then 4% terminal
   - Never use >15% for any company, ever
3. Discount at 10% (Buffett's consistent hurdle — "the long-term rate of the S&P plus a margin")
4. Two-stage model: 10 years of growth + perpetuity at terminal rate
5. **Bear case**: cut growth assumption in half, keep discount at 10%
6. Intrinsic value = average of base and bear case (conservative bias)

## Margin of safety tiers

| Company quality | Minimum margin of safety | Rationale |
|----------------|--------------------------|-----------|
| Wonderful (score 85+) | 20-25% | High predictability reduces needed discount |
| Good (score 70-84) | 25-30% | Moderate uncertainty requires more buffer |
| Fair (score 55-69) | 30-40% | Compensation for lower quality through price |
| Mediocre (<55) | Do not buy at any price | No margin of safety saves a bad business |

## Moat identification checklist

For each moat type, ask the specific diagnostic question:

**Brand / pricing power:**
- Can they raise prices 10% tomorrow without losing significant volume?
- Would a competitor with $10B struggle to replicate the brand equity?
- Is the brand association automatic and emotional (not just rational)?

**Switching costs:**
- What would it cost a customer (in time, money, risk) to switch?
- Is the product embedded in workflow, data, or regulatory compliance?
- Have customers stayed 10+ years despite competitive alternatives?

**Network effects:**
- Does each new user/merchant/node make the platform more valuable for existing users?
- Is there a tipping point beyond which competitors cannot catch up?
- Two-sided networks (V/MA) are strongest — both merchants and consumers are locked.

**Cost advantage:**
- Is the cost edge structural (scale, geography, proprietary process) vs cyclical?
- Could a well-funded competitor replicate the cost position in 5 years?
- Does the cost advantage translate to either: (a) lower prices with same margins, or (b) same prices with higher margins?

## Capital allocation scorecard (for management quality)

Rank management on how they deploy retained earnings:

| Use of capital | Buffett's preference |
|----------------|---------------------|
| Reinvest in high-ROIC organic growth | Best (if ROIC > 20%) |
| Acquisitions at sensible prices | Good (but most CEOs overpay) |
| Share buybacks below intrinsic value | Excellent |
| Dividends | Acceptable if no better use |
| Share buybacks above intrinsic value | Destruction of capital |
| Empire-building acquisitions at high prices | Worst |

## What Buffett avoids (and so must this agent)

1. **"Too hard" pile** — any business requiring prediction of technological change, regulatory shifts, or consumer fads. "There are no called strikes in investing."
2. **Capital destroyers** — airlines, commodity chemicals, undifferentiated retailers, early-stage biotech.
3. **Leverage** — companies with debt/EBITDA > 3x or interest coverage < 5x in normal times.
4. **IPOs and SPACs** — "It's almost a mathematical impossibility to imagine that, out of the thousands of things for sale on a given day, the most attractively priced is the one being sold by a knowledgeable seller to a less-knowledgeable buyer."
5. **Turnarounds** — "Turnarounds seldom turn."
6. **Macro bets** — never position for a recession, rate hike, or election outcome.

## The "newspaper test" for management

"Would I be comfortable seeing this deal/decision reported on the front page of my local newspaper?" If management's actions would embarrass the company → governance penalty.

## When to sell (almost never)

Buffett has sold for only three reasons in 60 years:

1. **Moat permanently impaired** — the competitive advantage no longer exists (newspapers, Tesco)
2. **Management integrity failure** — evidence of dishonesty or shareholder abuse
3. **Dramatic reallocation** — a clearly superior opportunity appears AND the current position trades at/above intrinsic value

Price decline alone is NEVER a sell reason. "If you aren't willing to own a stock for ten years, don't even think about owning it for ten minutes."
