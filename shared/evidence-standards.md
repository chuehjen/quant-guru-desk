# Evidence Standards (shared)

Every guru on the desk uses this same evidence-grading discipline. The goal: **prevent LLM hallucination of financial data** while maintaining analytical depth.

## The three-tier evidence ladder

### Strong

Verifiable primary sources with legal accountability:

- SEC / HKEX / exchange filings (10-K, 10-Q, 8-K, 20-F, proxy)
- Annual reports, quarterly earnings releases
- Earnings call transcripts (verbatim, timestamped)
- Official contracts, purchase orders, customer announcements
- Patent filings (USPTO, EPO, WIPO)
- Government/regulatory filings (CHIPS Act awards, FCC, NIST, DoC)
- Audited financial statements

### Medium

Reputable secondary sources with editorial standards:

- Major financial media (Bloomberg, Reuters, CNBC, FT, WSJ)
- Trade publications (Semiconductor Engineering, Lightwave, EE Times)
- Industry association data (SIA, SEMI, Yole, TrendForce)
- Company investor relations (IR decks, guidance slides)
- Sell-side research reports (Goldman, Morgan Stanley, etc.)
- Verified industry databases (Epoch AI, semiconstocks.com)

### Weak

Unverified or low-accountability sources:

- KOL posts (X/Twitter, Reddit, Substack)
- Social media discussions, forum threads
- Unsourced screenshots or rumor aggregators
- Anonymous tips, Telegram/Discord leaks
- Self-reported returns without third-party audit

## Mandatory citation rules

1. **Every data point must have a source.** Revenue figures, margins, customer names, market share, stock prices — all must be attributed. Format: `[Source: <name>, <date>]` or inline attribution.

2. **Grade every source.** When presenting evidence, label it: `[Strong]`, `[Medium]`, or `[Weak]`.

3. **No source = no claim.** If you cannot find a source for a data point, you MUST:
   - Mark it as `[未验证]` (unverified)
   - Downgrade any conclusion that depends on it
   - Suggest a verification path ("check the Q2 10-Q filing for this")

4. **Weak-only claims cannot support investment conclusions.** They can appear as "leads to investigate" but not as the basis for scoring, positioning, or conviction statements.

5. **Arithmetic identity check (mandatory every run):**
   ```
   Σ(持仓市值) + 现金 = 总资产
   ```
   Re-derive cash as `总资产 − Σ市值` to catch the most common LLM arithmetic error. If the identity fails, fix the numbers before outputting.

6. **Price source attribution.** Every stock price must include source + timestamp (see `price-fetching.md`). Never output a price without saying where it came from.

## Red flags (trigger mandatory risk disclosure)

If ANY of these are true for a candidate, the risk section MUST explicitly mention it:

| Red flag | Why it matters |
|----------|---------------|
| Thesis relies on a single unnamed customer rumor | Unverifiable → could be fabricated |
| Stock price primarily driven by social media posts | Signal vs noise indistinguishable |
| Company must raise capital before opportunity → revenue | Dilution risk + thesis not yet proven |
| Receivables/inventory growing faster than revenue | Potential channel-stuffing or accounting games |
| Claims scarcity but gross margin hasn't improved | Pricing power thesis contradicted by financials |
| Self-reported returns without audit | Track record unverifiable |
| Recent short report published | Bear case must be addressed, not ignored |
| Analyst coverage = 0 and volume < $1M/day | Liquidity risk + no independent verification |

## How gurus use this file

- **Before scoring:** Grade the evidence available for each candidate. A candidate with only Weak evidence cannot score above "Worth tracking" regardless of other factors.
- **During output:** Cite sources inline. The reader should be able to trace any claim back to a document.
- **After output:** Include a "证据地图" (evidence map) for high-conviction calls showing which claims have Strong/Medium/Weak support.

## Evidence map template (optional, for deep dives)

```
### 证据地图 — $TICKER

| 核心论点 | 证据 | 等级 | 来源 | 日期 |
|---------|------|------|------|------|
| 唯一供应商 | 10-K mentions sole-source | Strong | SEC 10-K FY2025 | 2026-03-15 |
| 需求翻倍 | CFO guidance on call | Strong | Q1 earnings transcript | 2026-04-28 |
| 客户是 NVDA | KOL post, no filing | Weak | @aleabitoreddit | 2026-05-10 |

**证据强度: 2 Strong + 0 Medium + 1 Weak → 中等可信度，需要 Q2 filing 验证客户身份**
```

## What this does NOT do

- This file does not replace each guru's methodology — it adds a universal quality floor.
- It does not ban Weak evidence — it bans Weak-only conclusions.
- It does not require perfection — it requires honesty about uncertainty.
