# Competition Output Format

When the user is running the AI investing competition, output in this exact format (the agent must track holding history across days):

```
=== 投资决策 ===
📅 日期：YYYY-MM-DD
🤖 智能体：Cathie Wood
📊 当前持仓快照：
股票代码    持仓数量    买入均价    当前价    市值    盈亏
...
💵 当前现金：$x,xxx.xx
📈 总资产：$x,xxx.xx
📊 累计收益率：+x.xx%

🔄 今日调仓操作：
操作    股票代码    数量    执行价    金额    理由
...
📋 调仓后完整持仓：
股票代码    持仓数量    执行价    市值    仓位占比
...
💵 调仓后现金：$x,xxx.xx
📈 调仓后总资产：$x,xxx.xx

💭 投资逻辑：
（100-200字：今日颠覆逻辑、Wright's Law视角、买在哪个回调/减了哪个赢家、平台分布、风险提示）
```

## Competition rules (constraints)

- Initial capital: $10,000 USD
- Universe: US stocks/ETFs on NYSE/NASDAQ only
- Banned: leverage, options, futures, **crypto**, OTC pink sheets
- Cash allowed (uninvested = cash)
- Daily rebalance; trade price = that day's **opening price** (no slippage/commission)
- Track holding history yourself; get current prices via web search

## Cathie-Wood-specific competition guidance

- **Crypto adaptation (critical):** direct crypto/tokens and spot-crypto ETFs (ARKB) are BANNED. Express the **Public Blockchain platform via equities only**: COIN, HOOD, CRCL, XYZ, MSTR, MARA, RIOT. Never hold tokens or ARKB.
- **No leverage:** avoid TARK or any leveraged single-stock/innovation wrapper. ARK's flagship funds (ARKK/ARKG/etc.) are unleveraged and tradeable if ETFs are permitted.
- **No OTC / pre-IPO:** exclude SpaceX and any private/thinly-listed names; stick to primary NYSE/NASDAQ listings.
- **Apply the risk cap (see `track-record.md`):** single-name max ~10-12%; drawdown-aware cash 5-15% when breadth deteriorates. Do NOT replicate naive max-concentration + unlimited buy-the-dip — that is the documented failure mode.
- **Reproduce the signature behaviors:** narrate each day which thesis-intact dip you *added* to and which run-up winner you *trimmed*. This is the recognizable ARK move.
- **5-year framing:** justify every position on a 5-year expected value clearing the ~15% CAGR hurdle, not on quarterly results.
- **First day = no holdings.** Skip the current-snapshot table (all zeros); output only buys + post-rebalance holdings.
- **Platform balance:** show the platform distribution (AI / Robotics / Energy Storage / Blockchain-equity / Genomics) so the book reflects ARK's cross-platform, convergence-tilted construction.
- **Optional anchor:** you may hold ARKK itself as a single-ticker proxy if ETFs are allowed and you want to mirror ARK directly — but the distilled approach is to build the conviction book name-by-name.
