# Calls Schema — `calls.json`

The single source of truth for "what did this desk actually call, and was it right?"

`shared/reflection-protocol.md` defines the **natural-language memory** layer (free-text notes a guru can search). `calls.json` is the **machine-graded** layer — structured, deterministic, and not negotiable by the LLM.

The two coexist on purpose:

| Layer | What it stores | Who writes it | Who grades it |
|-------|----------------|---------------|---------------|
| `MEMORY.md` / `memory/*.md` | Free-text reasoning, context, lessons | The LLM | The LLM (subjective) |
| `calls.json` | Structured signals: action / entry / stop / horizon | The LLM (one row per signal card) | `scripts/track_calls.py` against Twelve Data prices (deterministic) |

If they ever disagree, **`calls.json` wins** — that's the public batting average.

---

## File location

`calls.json` lives at the **skill root**:

```
quant-guru-desk/
├── calls.json          ← here
├── SKILL.md
└── ...
```

The file is intentionally inside the repo (not the user's home) so anyone who clones the skill inherits the call history. Users running multiple installs should treat their own clone's `calls.json` as personal.

A starter `calls.json` ships with `[]`.

---

## Record schema

Every signal card emits exactly one record:

```json
{
  "id": "2026-06-09-minervini-NVDA-001",
  "created_at": "2026-06-09T13:30:00+08:00",
  "guru": "minervini",
  "ticker": "NVDA",
  "action": "BUY",
  "conviction": 4,
  "entry": 205.10,
  "stop": 190.00,
  "target": 250.00,
  "horizon_days": 30,
  "thesis": "VCP 3rd contraction complete, pivot $206 breakout on volume",
  "context": "Market Stage 2, AI capex cycle intact",
  "competition_run": false,
  "panel_id": null,
  "scored_30d": null,
  "scored_90d": null
}
```

### Field reference

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `id` | string | yes | `YYYY-MM-DD-{guru}-{ticker}-{seq}`. Sequence resets per day. |
| `created_at` | ISO-8601 string | yes | With timezone offset. Defines "day 0" for grading. |
| `guru` | enum | yes | `buffett` / `dalio` / `kindig` / `cathie` / `serenity` / `minervini` / `panel-consensus` |
| `ticker` | string | yes | Uppercase. Use `MACRO-REGIME` for Dalio macro calls without a ticker. |
| `action` | enum | yes | `BUY` / `HOLD` / `SELL` / `WATCH` / `AVOID`. Matches signal card. |
| `conviction` | integer 1–5 | yes | Higher conviction → grading penalty for wrong calls is larger (see scoring). |
| `entry` | number \| null | yes | The price the call was made at. Null only allowed for `MACRO-REGIME`. |
| `stop` | number \| null | optional | Price stop for Minervini/Kindig/Cathie/Serenity. `null` for Buffett (condition-based). |
| `target` | number \| null | optional | Price target. Null = no explicit target. |
| `horizon_days` | integer | yes | Expected holding period. Used to pick which day's price to score against. Typical: Minervini 30, Kindig 90, Cathie/Buffett 365. |
| `thesis` | string | yes | One-sentence core logic, ≤ 30 chars-equivalent. Mirrors the signal card. |
| `context` | string | optional | Macro/structural context one liner. |
| `competition_run` | boolean | yes | True if the call came from the daily AI investing competition (separates serious calls from the competition's forced-rebalance noise). |
| `panel_id` | string \| null | optional | If part of a panel verdict, the panel UUID. Lets `summary` group by panel. |
| `scored_30d` | object \| null | written by grader | See below. |
| `scored_90d` | object \| null | written by grader | See below. |

### Grading sub-record

After the horizon elapses, `track_calls.py score` fills in:

```json
{
  "scored_30d": {
    "scored_at": "2026-07-09T00:00:00+00:00",
    "price_then": 215.40,
    "move_pct": 5.02,
    "verdict": "neutral",
    "reasoning": "BUY @205.10, +5.0% over 30d (threshold ±10%)"
  }
}
```

#### Verdict rules (deterministic)

| Action | `move_pct` (close − entry) / entry | Verdict |
|--------|-------------------------------------|---------|
| `BUY`  | ≥ +10% | `correct` |
| `BUY`  | between −10% and +10% | `neutral` |
| `BUY`  | ≤ −10% | `wrong` |
| `SELL` | ≤ −10% | `correct` |
| `SELL` | between −10% and +10% | `neutral` |
| `SELL` | ≥ +10% | `wrong` |
| `HOLD` | absolute move ≤ 10% | `correct` (didn't move much, holding was fine) |
| `HOLD` | absolute move > 10% in either direction | `neutral` (HOLD wasn't a directional call; record but don't score harshly) |
| `AVOID`| ≤ +5% | `correct` |
| `AVOID`| ≥ +20% | `wrong` (you called it bad and it ran without you) |
| `AVOID`| between +5% and +20% | `neutral` |
| `WATCH`| any | `neutral` always (a non-call cannot be wrong) |

If the stop was hit before scoring date → action-aware override:
- `BUY` with stop hit → `wrong` regardless of final price
- `SELL` with stop hit (i.e., price went up past entry) → already covered by main rule

If the call sits inside `horizon_days` of a stock split / ticker change → mark verdict `unscorable` and write the reason in `reasoning`.

---

## Conviction-weighted score

`track_calls.py summary` reports two numbers per guru:

1. **Hit rate** — `correct / (correct + wrong)`. Neutrals and unscorables are excluded.
2. **Conviction-weighted score** — sum of `(conviction × +1)` for correct, `(conviction × −1)` for wrong, `0` for neutral. A guru that gets 5-conviction calls right is worth more than one who hedges everything at 2.

The summary also prints the worst three wrong calls (for honesty) and the best three right calls — by absolute conviction-weighted contribution.

---

## What the LLM must do

When emitting a signal card (any guru, any mode), the LLM appends to `calls.json` via `track_calls.py append` (preferred) or directly writes a JSON record with the schema above.

Hard rules:

1. **One signal card → one row.** Panel mode writes one row per participating guru plus one with `guru: panel-consensus`.
2. **Never edit a past row's grading fields.** Only the grader writes `scored_30d` and `scored_90d`.
3. **Never delete a wrong call.** Errors are the most valuable training signal.
4. If the user asks "how am I doing?" → run `track_calls.py summary` and quote it verbatim. Don't paraphrase numbers.

---

## Privacy

`calls.json` lives in the user's local clone of the repo. It only goes public if the user pushes it. The skill never auto-commits it. If a user wants to share their batting average, they push the file; if they want it private, they add `calls.json` to `.gitignore` in their clone.

The shipped repo's `calls.json` starts empty (`[]`) and is seeded only by maintainer-curated demo entries (clearly marked with `"context": "demo"`).
