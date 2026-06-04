# Competition Rules & Output Format (shared)

The single source of truth for the AI investing competition. Every guru on the desk uses this same format so results are comparable. The acting guru fills it with their own logic and voice.

## Rules / constraints

- Initial capital: **$10,000 USD**
- Universe: **US stocks/ETFs on NYSE/NASDAQ only**
- Banned: leverage, options, futures, **crypto**, OTC pink sheets
- Cash allowed (uninvested = cash)
- Daily rebalance; each US trading day you may adjust
- Trade price = that day's **opening price** (no slippage/commission)
- You must **track holding history yourself** across days
- Get current prices via web search (see `price-fetching.md`)

## Output format (use exactly)

```
=== 投资决策 ===
📅 日期：YYYY-MM-DD
🤖 智能体：[Guru name, e.g. Serenity / Beth Kindig / Cathie Wood]
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
（100-200字，用该大神的视角与口吻）
```

## Cross-guru conventions

- **First day = no holdings.** Skip the current-snapshot table (all zeros); output only buys + post-rebalance holdings.
- **Arithmetic identity check (mandatory).** Verify `Σ(持仓市值) + 现金 = 总资产` every run. This catches the most common error (mis-stated cash). Re-derive cash as `总资产 − Σ市值`.
- **Same-day re-run:** P&L = current price vs your buy average (not vs prev close). If buy price = current price (just bought), P&L ≈ $0.
- **Crypto adaptation:** direct crypto/tokens and spot-crypto ETFs (e.g., ARKB) are banned → express blockchain exposure via equities (COIN/HOOD/CRCL/XYZ/MSTR).
- **No leverage wrappers** (e.g., TARK). ARK's own unleveraged ETFs (ARKK etc.) are allowed if ETFs are permitted.
- **Foreign-listed names** (e.g., Stockholm/Euronext tickers) are NOT competition-tradeable — exclude or note `[不可交易]`.

## Guru-specific competition notes

Each guru folder has a `references/competition-format.md` with style-specific guidance (e.g., Kindig expresses risk via cash not options; Cathie applies a single-name cap + drawdown cash buffer; Serenity uses dynamic cash by volatility). Read it after this shared file.
