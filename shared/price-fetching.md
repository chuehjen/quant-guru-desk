# Stock-Price Fetching (shared discipline)

Every guru uses this same price-fetching method so quotes are consistent across the desk.

## Fallback chain (try each until success)

1. **CNBC quote page** — `https://www.cnbc.com/quotes/TICKER` — most reliable; returns last, prev close, day range. Fetch **one ticker at a time** (batch fetches of macrotrends/google/stockanalysis tend to fail).
2. **Google Finance** — `https://www.google.com/finance/quote/TICKER:EXCHANGE`
3. **Yahoo Finance** — `https://finance.yahoo.com/quote/TICKER/` (often returns 403)
4. **Search snippet fallback** — WebSearch `"TICKER stock price today"`; use the snippet price, label `[estimated]`.

## Quality checks

- **Price conflict detection:** if 2+ sources differ by >15%, flag `[DATA CONFLICT]`, list sources + timestamps, default to the most recent.
- **Ticker validation:** if a ticker maps to a different company than expected, flag `[TICKER UNCONFIRMED]` and skip — do not silently drop or substitute it.
- **Abnormal-price check:** before treating a >$1,000 share price as an error, search the ticker's stock-split history. High-flyers (e.g., MU at times, certain names) can genuinely trade above $1,000 without having split.
- **Multi-currency:** for any non-USD quote, note the currency and FX rate, convert to USD for portfolio math. (Most competition-eligible US tickers are USD.)

## Output

Always include a small price-reference table in the decision so the user can audit:

```
### 参考股价
| Ticker | 价格 | 货币 | 来源 | 时间 |
|--------|------|------|------|------|
```

Prices are delayed/snapshot — label the source and treat as best-effort, not real-time market data.
