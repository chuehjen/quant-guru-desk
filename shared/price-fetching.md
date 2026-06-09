# Stock-Price Fetching (shared discipline)

Every guru uses this same price-fetching method so quotes are consistent across the desk.

## Fallback chain (try each until success)

1. **Twelve Data (preferred)** — `https://api.twelvedata.com/price?symbol=TICKER1,TICKER2&apikey=KEY`
   - Returns `{"TICKER": {"price": "215.98"}}` (price is a STRING, must `parseFloat`)
   - Free tier: 8 credits/min, 800 credits/day. Each symbol = 1 credit.
   - Batch up to 8 symbols per request. For > 8 symbols, split into batches with 62-second delay between.
   - For historical close prices: `/time_series?symbol=TICKER&interval=1day&outputsize=3&apikey=KEY`
   - **No CORS proxy needed** — works directly from browser.
   - API key management: user provides their own key. Sign up at https://twelvedata.com (free tier sufficient for daily use).

2. **CNBC quote page** — `https://www.cnbc.com/quotes/TICKER` — reliable; returns last, prev close, day range. Fetch **one ticker at a time**.

3. **Google Finance** — `https://www.google.com/finance/quote/TICKER:EXCHANGE` — requires HTML parsing; good for verification.

4. **Search snippet fallback** — WebSearch `"TICKER stock price today"`; use the snippet price, label `[estimated]`.

## Deprecated / unreliable (do NOT use)

- ~~Yahoo Finance~~ — returns 403/429/520 consistently since 2025
- ~~Alpha Vantage demo key~~ — 5 req/min hard limit, often timeout
- ~~FMP free tier~~ — expired keys return empty responses
- ~~Finnhub demo~~ — rate limited to unusable levels

## Quality checks

- **Price conflict detection:** if 2+ sources differ by >15%, flag `[DATA CONFLICT]`, list sources + timestamps, default to the most recent.
- **Ticker validation:** if a ticker maps to a different company than expected, flag `[TICKER UNCONFIRMED]` and skip — do not silently drop or substitute it.
- **Abnormal-price check:** before treating a >$1,000 share price as an error, search the ticker's stock-split history. High-flyers (e.g., MU at times, certain names) can genuinely trade above $1,000 without having split.
- **Multi-currency:** for any non-USD quote, note the currency and FX rate, convert to USD for portfolio math. (Most competition-eligible US tickers are USD.)

## Twelve Data batch strategy

For a portfolio scan involving N symbols:

```
Total symbols: N
Batch size: 8 (max per request on free tier)
Batches: ceil(N / 8)
Delay between batches: 62 seconds (safety margin over 60s credit reset)
Total time: (batches - 1) × 62 seconds
```

Example: 32 symbols → 4 batches → ~3 minutes total.

## Output

Always include a small price-reference table in the decision so the user can audit:

```
### 参考股价
| Ticker | 价格 | 货币 | 来源 | 时间 |
|--------|------|------|------|------|
```

Prices are delayed/snapshot — label the source and treat as best-effort, not real-time market data.
