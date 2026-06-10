#!/usr/bin/env python3
"""
Quant Guru Desk — Calls Tracker

The deterministic grading layer for the desk. Every signal card the gurus
emit is appended to ``calls.json``; this script grades calls 30 / 90 days
later against actual prices from Twelve Data, and prints per-guru hit
rates and conviction-weighted scores.

Why this script matters
-----------------------
Without this, the desk is just role-play. With it, every guru has a public
batting average. The LLM never grades itself — only this script does.

Usage
-----
    # one-off: see the desk's standing
    python3 scripts/track_calls.py summary

    # cron-friendly: grade calls that aged past 30 / 90 days
    TWELVEDATA_API_KEY=xxx python3 scripts/track_calls.py score

    # the LLM uses this to add a row when emitting a signal card
    python3 scripts/track_calls.py append --json '{ ... }'

    # human review of a single guru
    python3 scripts/track_calls.py summary --guru minervini

    # show recent calls
    python3 scripts/track_calls.py list --limit 10

Schema
------
Documented in shared/calls-schema.md. This script is the only authority
that writes the ``scored_30d`` / ``scored_90d`` fields.

Requirements
------------
Python 3.9+. Standard library only (``urllib``, ``json``, ``argparse``).
TWELVEDATA_API_KEY env var only required for ``score``.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
CALLS_PATH = REPO_ROOT / "calls.json"
TWELVEDATA_BASE = "https://api.twelvedata.com"

VALID_GURUS = {"buffett", "dalio", "kindig", "cathie", "serenity", "minervini", "panel-consensus"}
VALID_ACTIONS = {"BUY", "HOLD", "SELL", "WATCH", "AVOID"}
VALID_VERDICTS = {"correct", "neutral", "wrong", "unscorable"}


# ---------- I/O ---------------------------------------------------------------


def load_calls() -> list[dict]:
    if not CALLS_PATH.exists():
        return []
    text = CALLS_PATH.read_text(encoding="utf-8").strip()
    if not text:
        return []
    return json.loads(text)


def save_calls(calls: list[dict]) -> None:
    CALLS_PATH.write_text(json.dumps(calls, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# ---------- Validation --------------------------------------------------------


REQUIRED_FIELDS = {
    "id",
    "created_at",
    "guru",
    "ticker",
    "action",
    "conviction",
    "entry",
    "horizon_days",
    "thesis",
    "competition_run",
}


def validate_record(record: dict) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_FIELDS - record.keys()
    if missing:
        errors.append(f"missing fields: {sorted(missing)}")
    if record.get("guru") not in VALID_GURUS:
        errors.append(f"invalid guru: {record.get('guru')!r}; allowed: {sorted(VALID_GURUS)}")
    if record.get("action") not in VALID_ACTIONS:
        errors.append(f"invalid action: {record.get('action')!r}")
    conviction = record.get("conviction")
    if not isinstance(conviction, int) or not 1 <= conviction <= 5:
        errors.append(f"conviction must be int 1-5, got {conviction!r}")
    horizon = record.get("horizon_days")
    if not isinstance(horizon, int) or horizon <= 0:
        errors.append(f"horizon_days must be positive int, got {horizon!r}")
    if record.get("ticker") != "MACRO-REGIME" and record.get("entry") in (None, ""):
        errors.append("entry price required unless ticker == MACRO-REGIME")
    return errors


# ---------- Append ------------------------------------------------------------


def cmd_append(args: argparse.Namespace) -> int:
    if args.json:
        try:
            record = json.loads(args.json)
        except json.JSONDecodeError as exc:
            print(f"error: invalid JSON ({exc})", file=sys.stderr)
            return 2
    elif args.file:
        record = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        print("error: provide --json or --file", file=sys.stderr)
        return 2

    record.setdefault("scored_30d", None)
    record.setdefault("scored_90d", None)
    record.setdefault("panel_id", None)
    record.setdefault("context", "")
    record.setdefault("stop", None)
    record.setdefault("target", None)

    errors = validate_record(record)
    if errors:
        for err in errors:
            print(f"error: {err}", file=sys.stderr)
        return 2

    calls = load_calls()
    if any(c["id"] == record["id"] for c in calls):
        print(f"error: duplicate id {record['id']}", file=sys.stderr)
        return 2

    calls.append(record)
    save_calls(calls)
    print(f"appended {record['id']} ({record['guru']} {record['action']} {record['ticker']} conv={record['conviction']})")
    return 0


# ---------- Twelve Data fetch -------------------------------------------------


@dataclass
class PriceLookup:
    api_key: str

    def close_on_or_before(self, ticker: str, target_date: datetime) -> tuple[float | None, str | None]:
        """Return (close_price, actual_date_iso) for the trading day on or before target_date."""
        end = target_date.strftime("%Y-%m-%d")
        # pull a 7-day window so we hit a trading day even on weekends/holidays
        start = (target_date - timedelta(days=10)).strftime("%Y-%m-%d")
        params = {
            "symbol": ticker,
            "interval": "1day",
            "start_date": start,
            "end_date": end,
            "order": "DESC",
            "outputsize": 10,
            "apikey": self.api_key,
        }
        url = f"{TWELVEDATA_BASE}/time_series?" + urllib.parse.urlencode(params)
        try:
            with urllib.request.urlopen(url, timeout=20) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
        except Exception as exc:  # noqa: BLE001 — we want to surface anything network-side
            return None, f"fetch_error: {exc}"
        if payload.get("status") == "error":
            return None, f"api_error: {payload.get('message', 'unknown')}"
        values = payload.get("values") or []
        if not values:
            return None, "no_data"
        for row in values:  # already DESC by date
            try:
                close = float(row["close"])
            except (KeyError, TypeError, ValueError):
                continue
            return close, row.get("datetime")
        return None, "no_close_field"


# ---------- Grading -----------------------------------------------------------


def compute_verdict(action: str, move_pct: float) -> str:
    if action == "BUY":
        if move_pct >= 10:
            return "correct"
        if move_pct <= -10:
            return "wrong"
        return "neutral"
    if action == "SELL":
        if move_pct <= -10:
            return "correct"
        if move_pct >= 10:
            return "wrong"
        return "neutral"
    if action == "HOLD":
        return "correct" if abs(move_pct) <= 10 else "neutral"
    if action == "AVOID":
        if move_pct >= 20:
            return "wrong"
        if move_pct <= 5:
            return "correct"
        return "neutral"
    if action == "WATCH":
        return "neutral"
    return "unscorable"


def parse_iso(ts: str) -> datetime:
    # python's fromisoformat handles "+08:00" since 3.11; be lenient for 3.9+
    try:
        return datetime.fromisoformat(ts)
    except ValueError:
        # strip trailing 'Z'
        if ts.endswith("Z"):
            return datetime.fromisoformat(ts[:-1]).replace(tzinfo=timezone.utc)
        raise


def grade_one(call: dict, horizon_days: int, lookup: PriceLookup) -> dict | None:
    if call.get("ticker") == "MACRO-REGIME":
        return {
            "scored_at": datetime.now(timezone.utc).isoformat(),
            "price_then": None,
            "move_pct": None,
            "verdict": "unscorable",
            "reasoning": "macro regime calls are tracked qualitatively only",
        }
    entry = call.get("entry")
    if entry in (None, "") or not isinstance(entry, (int, float)) or entry <= 0:
        return {
            "scored_at": datetime.now(timezone.utc).isoformat(),
            "price_then": None,
            "move_pct": None,
            "verdict": "unscorable",
            "reasoning": "entry price missing or invalid",
        }

    created = parse_iso(call["created_at"])
    target_date = created + timedelta(days=horizon_days)
    if target_date > datetime.now(target_date.tzinfo or timezone.utc):
        return None  # too early

    close, info = lookup.close_on_or_before(call["ticker"], target_date)
    if close is None:
        return {
            "scored_at": datetime.now(timezone.utc).isoformat(),
            "price_then": None,
            "move_pct": None,
            "verdict": "unscorable",
            "reasoning": info or "unknown fetch failure",
        }

    move_pct = round((close - entry) / entry * 100, 2)
    verdict = compute_verdict(call["action"], move_pct)

    # stop-out override for BUY
    stop = call.get("stop")
    if (
        call["action"] == "BUY"
        and isinstance(stop, (int, float))
        and stop > 0
        and close <= stop
    ):
        verdict = "wrong"
        reasoning = f"BUY @{entry:.2f}, stop ${stop:.2f} hit by close ${close:.2f} ({move_pct:+.2f}% over {horizon_days}d)"
    else:
        reasoning = f"{call['action']} @{entry:.2f}, {move_pct:+.2f}% over {horizon_days}d (threshold per schema)"

    return {
        "scored_at": datetime.now(timezone.utc).isoformat(),
        "price_then": close,
        "move_pct": move_pct,
        "verdict": verdict,
        "reasoning": reasoning,
        "actual_date": info,
    }


def cmd_score(args: argparse.Namespace) -> int:
    api_key = os.environ.get("TWELVEDATA_API_KEY") or args.api_key
    if not api_key:
        print("error: TWELVEDATA_API_KEY env var (or --api-key) required", file=sys.stderr)
        return 2

    lookup = PriceLookup(api_key=api_key)
    calls = load_calls()
    if not calls:
        print("no calls to score")
        return 0

    updated = 0
    for call in calls:
        for window in (30, 90):
            field = f"scored_{window}d"
            if call.get(field) is not None:
                continue
            result = grade_one(call, window, lookup)
            if result is None:
                continue  # not aged yet
            call[field] = result
            updated += 1
            print(
                f"  scored {window}d  {call['guru']:<8} {call['ticker']:<6} {call['action']:<5} → {result['verdict']:<10} {result['reasoning']}"
            )

    if updated:
        save_calls(calls)
    print(f"\ndone. {updated} verdict(s) written.")
    return 0


# ---------- Summary -----------------------------------------------------------


def cmd_summary(args: argparse.Namespace) -> int:
    calls = load_calls()
    if args.guru:
        calls = [c for c in calls if c["guru"] == args.guru]
    if not calls:
        print("no calls recorded yet")
        return 0

    # build per-guru aggregates
    Stat = lambda: {"total": 0, "correct": 0, "wrong": 0, "neutral": 0, "unscorable": 0, "weighted": 0, "pending": 0}
    per_guru: dict[str, dict] = defaultdict(Stat)

    scored_pool: list[tuple[dict, dict]] = []
    pending: list[dict] = []

    for call in calls:
        s = per_guru[call["guru"]]
        s["total"] += 1
        # prefer 90d verdict if available, else 30d
        graded = call.get("scored_90d") or call.get("scored_30d")
        if not graded:
            s["pending"] += 1
            pending.append(call)
            continue
        verdict = graded.get("verdict", "unscorable")
        s[verdict] = s.get(verdict, 0) + 1
        if verdict == "correct":
            s["weighted"] += call["conviction"]
            scored_pool.append((call, graded))
        elif verdict == "wrong":
            s["weighted"] -= call["conviction"]
            scored_pool.append((call, graded))

    # per-guru table
    print("\n📊 Quant Guru Desk — batting average\n")
    print(f"{'Guru':<18} {'total':>6} {'✅':>4} {'❌':>4} {'~':>4} {'?':>4} {'hit-rate':>10} {'weighted':>10} {'pending':>8}")
    print("-" * 72)
    for guru, s in sorted(per_guru.items()):
        decided = s["correct"] + s["wrong"]
        hit_rate = f"{s['correct'] / decided * 100:5.1f}%" if decided else "  n/a "
        print(
            f"{guru:<18} {s['total']:>6} {s['correct']:>4} {s['wrong']:>4} {s['neutral']:>4} {s['unscorable']:>4} {hit_rate:>10} {s['weighted']:>+10} {s['pending']:>8}"
        )

    # best / worst
    if scored_pool:
        scored_pool.sort(key=lambda cw: (cw[0]["conviction"] if cw[1]["verdict"] == "correct" else -cw[0]["conviction"]), reverse=True)
        best = [cw for cw in scored_pool if cw[1]["verdict"] == "correct"][:3]
        worst = [cw for cw in scored_pool if cw[1]["verdict"] == "wrong"]
        worst.sort(key=lambda cw: cw[0]["conviction"], reverse=True)
        worst = worst[:3]

        if best:
            print("\n🏆 best calls (by conviction-weighted impact):")
            for c, g in best:
                print(f"  {c['guru']:<10} {c['ticker']:<6} {c['action']:<5} conv={c['conviction']}  {g['reasoning']}")

        if worst:
            print("\n💀 worst calls (errors are the most valuable signal):")
            for c, g in worst:
                print(f"  {c['guru']:<10} {c['ticker']:<6} {c['action']:<5} conv={c['conviction']}  {g['reasoning']}")

    # pending tail
    if pending and args.show_pending:
        print(f"\n⏳ pending ({len(pending)}):")
        for c in pending[-10:]:
            print(f"  {c['created_at'][:10]} {c['guru']:<10} {c['ticker']:<6} {c['action']:<5} conv={c['conviction']}  horizon={c['horizon_days']}d")

    return 0


# ---------- List --------------------------------------------------------------


def cmd_list(args: argparse.Namespace) -> int:
    calls = load_calls()
    if args.guru:
        calls = [c for c in calls if c["guru"] == args.guru]
    if args.ticker:
        calls = [c for c in calls if c["ticker"].upper() == args.ticker.upper()]
    calls = list(reversed(calls))[: args.limit]
    if not calls:
        print("no matching calls")
        return 0
    for c in calls:
        graded = c.get("scored_90d") or c.get("scored_30d")
        verdict = graded["verdict"] if graded else "pending"
        entry = c.get("entry")
        entry_str = f"${entry:.2f}" if isinstance(entry, (int, float)) else "—"
        print(
            f"{c['created_at'][:10]} {c['guru']:<10} {c['ticker']:<6} {c['action']:<5} conv={c['conviction']} entry={entry_str:<8} horizon={c['horizon_days']:>3}d → {verdict}"
        )
    return 0


# ---------- Entry -------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="track_calls", description="Quant Guru Desk — calls tracker")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_append = sub.add_parser("append", help="append a new signal record")
    p_append.add_argument("--json", help="record as a JSON string")
    p_append.add_argument("--file", help="record from a JSON file")
    p_append.set_defaults(func=cmd_append)

    p_score = sub.add_parser("score", help="grade calls that aged past 30/90 days")
    p_score.add_argument("--api-key", help="Twelve Data API key (or set TWELVEDATA_API_KEY)")
    p_score.set_defaults(func=cmd_score)

    p_summary = sub.add_parser("summary", help="print the desk's batting average")
    p_summary.add_argument("--guru", help="filter to a single guru")
    p_summary.add_argument("--show-pending", action="store_true", help="also list pending tail")
    p_summary.set_defaults(func=cmd_summary)

    p_list = sub.add_parser("list", help="list recent calls")
    p_list.add_argument("--guru", help="filter by guru")
    p_list.add_argument("--ticker", help="filter by ticker")
    p_list.add_argument("--limit", type=int, default=20)
    p_list.set_defaults(func=cmd_list)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
