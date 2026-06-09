#!/usr/bin/env python3
"""
Quant Guru Desk — GF-DMA Health Index Calculator

Scores whether a stock's price trend is supported by fundamental growth.
Combines fundamental speed (revenue/EPS growth) with technical structure
(moving-average alignment) to produce a 0-100 health score.

Usage:
    python3 gf_dma.py input.json
    python3 gf_dma.py input.json --output report.md
    python3 gf_dma.py --example

Requirements: Python 3.9+, zero external dependencies.
"""

import json
import math
import sys
from pathlib import Path

EXAMPLE_INPUT = {
    "ticker": "NVDA",
    "date": "2026-06-05",
    "fundamentals": {
        "revenue_growth_yoy": 122.0,
        "gross_profit_growth_yoy": 135.0,
        "eps_growth_yoy": 168.0,
        "analyst_revision_3m": 12.5,
    },
    "technicals": {
        "price_current": 138.20,
        "dma_20": 135.50,
        "dma_50": 130.80,
        "dma_100": 122.40,
        "dma_200": 108.60,
        "price_5d_ago": 134.00,
        "dma_50_5d_ago": 129.90,
    },
}


def validate_input(data: dict) -> list[str]:
    errors = []
    if "ticker" not in data:
        errors.append("Missing: 'ticker'")
    if "fundamentals" not in data:
        errors.append("Missing: 'fundamentals'")
    else:
        for key in ["revenue_growth_yoy", "gross_profit_growth_yoy", "eps_growth_yoy"]:
            if key not in data["fundamentals"]:
                errors.append(f"Missing fundamentals.{key}")
    if "technicals" not in data:
        errors.append("Missing: 'technicals'")
    else:
        for key in ["price_current", "dma_20", "dma_50", "dma_100", "dma_200"]:
            if key not in data["technicals"]:
                errors.append(f"Missing technicals.{key}")
    return errors


def calc_fundamental_speed(fund: dict) -> dict:
    """Calculate blended fundamental growth speed (0-100 scale)."""
    rev = fund.get("revenue_growth_yoy", 0)
    gp = fund.get("gross_profit_growth_yoy", 0)
    eps = fund.get("eps_growth_yoy", 0)
    revision = fund.get("analyst_revision_3m", 0)

    def growth_to_score(g: float) -> float:
        if g <= 0:
            return max(0, 10 + g)
        elif g <= 20:
            return 10 + g * 2
        elif g <= 50:
            return 50 + (g - 20) * 1.0
        elif g <= 100:
            return 80 + (g - 50) * 0.3
        else:
            return min(100, 95 + (g - 100) * 0.05)

    def revision_to_score(r: float) -> float:
        if r < -10:
            return 0
        elif r < 0:
            return 30 + r * 3
        elif r <= 10:
            return 30 + r * 5
        else:
            return min(100, 80 + (r - 10) * 2)

    rev_score = growth_to_score(rev)
    gp_score = growth_to_score(gp)
    eps_score = growth_to_score(eps)
    rev_adj_score = revision_to_score(revision)

    blended = (
        0.35 * rev_score
        + 0.25 * gp_score
        + 0.30 * eps_score
        + 0.10 * rev_adj_score
    )

    return {
        "revenue_score": round(rev_score, 1),
        "gross_profit_score": round(gp_score, 1),
        "eps_score": round(eps_score, 1),
        "revision_score": round(rev_adj_score, 1),
        "blended": round(blended, 1),
    }


def calc_dma_alignment(tech: dict) -> dict:
    """Score DMA alignment (price > 20 > 50 > 100 > 200 = perfect)."""
    price = tech["price_current"]
    dma20 = tech["dma_20"]
    dma50 = tech["dma_50"]
    dma100 = tech["dma_100"]
    dma200 = tech["dma_200"]

    order = [price, dma20, dma50, dma100, dma200]
    pairs = list(zip(order, order[1:]))
    aligned_count = sum(1 for a, b in pairs if a >= b)

    alignment_score = aligned_count * 25

    above_200 = (price - dma200) / dma200 * 100 if dma200 > 0 else 0
    above_50 = (price - dma50) / dma50 * 100 if dma50 > 0 else 0

    return {
        "alignment_score": alignment_score,
        "aligned_pairs": aligned_count,
        "price_vs_200dma_pct": round(above_200, 2),
        "price_vs_50dma_pct": round(above_50, 2),
    }


def calc_divergence(fund_speed: float, tech: dict) -> dict:
    """Score divergence between fundamental speed and price trend."""
    price = tech["price_current"]
    dma50 = tech["dma_50"]
    dma200 = tech["dma_200"]

    price_momentum = (price - dma200) / dma200 * 100 if dma200 > 0 else 0
    fund_annualized = fund_speed

    divergence = price_momentum - fund_annualized

    if divergence > 30:
        score = max(0, 50 - (divergence - 30) * 2)
        state = "stretched_above"
    elif divergence > 10:
        score = 70 - (divergence - 10)
        state = "slightly_hot"
    elif divergence >= -10:
        score = 80
        state = "healthy_match"
    elif divergence >= -30:
        if fund_annualized > 20:
            score = 90
            state = "opportunity"
        else:
            score = 60
            state = "weak_fundamentals"
    else:
        if fund_annualized > 20:
            score = 85
            state = "deep_opportunity"
        else:
            score = 30
            state = "broken"

    return {
        "price_momentum_pct": round(price_momentum, 1),
        "divergence": round(divergence, 1),
        "divergence_score": round(score, 1),
        "state": state,
    }


def calc_trend_parallel(tech: dict) -> dict:
    """Score whether short-term price slope parallels the 50DMA slope."""
    price = tech["price_current"]
    price_5d = tech.get("price_5d_ago", price)
    dma50 = tech["dma_50"]
    dma50_5d = tech.get("dma_50_5d_ago", dma50)

    price_slope = (price - price_5d) / price_5d * 100 if price_5d > 0 else 0
    dma50_slope = (dma50 - dma50_5d) / dma50_5d * 100 if dma50_5d > 0 else 0

    if dma50_slope == 0:
        escape_ratio = 0 if price_slope == 0 else 999
    else:
        escape_ratio = price_slope / dma50_slope if dma50_slope != 0 else 0

    if 0.5 <= escape_ratio <= 1.5:
        score = 85
    elif 0.2 <= escape_ratio <= 2.0:
        score = 65
    elif escape_ratio > 2.0:
        score = 40
    elif escape_ratio < 0:
        score = 30
    else:
        score = 50

    return {
        "price_slope_5d": round(price_slope, 3),
        "dma50_slope_5d": round(dma50_slope, 3),
        "escape_ratio": round(escape_ratio, 2),
        "parallel_score": round(score, 1),
    }


def calculate_health(data: dict) -> dict:
    """Main calculation: combine all modules into final health score."""
    fund = data["fundamentals"]
    tech = data["technicals"]

    fund_speed = calc_fundamental_speed(fund)
    alignment = calc_dma_alignment(tech)
    divergence = calc_divergence(fund_speed["blended"], tech)
    parallel = calc_trend_parallel(tech)

    final_score = (
        0.40 * ((fund_speed["blended"] + alignment["alignment_score"]) / 2)
        + 0.25 * divergence["divergence_score"]
        + 0.20 * parallel["parallel_score"]
        + 0.15 * fund_speed["revision_score"]
    )
    final_score = round(min(100, max(0, final_score)), 1)

    if final_score >= 85:
        state = "Healthy Momentum"
        action = "Strong trend supported by fundamentals. Hold/add on pullbacks."
    elif final_score >= 75:
        state = "Strong but Watch"
        action = "Good alignment; monitor for divergence signals."
    elif final_score >= 65:
        state = "Hot but Supported"
        action = "Price running ahead slightly; tighten stops, don't chase."
    elif final_score >= 55:
        state = "Damaged"
        action = "Fundamental support weakening. Reduce exposure on bounces."
    elif final_score >= 40:
        state = "High Risk"
        action = "Major divergence. Only hold with strong catalyst thesis."
    else:
        state = "Broken"
        action = "No fundamental support for current trend. Exit or avoid."

    return {
        "ticker": data.get("ticker", "UNKNOWN"),
        "date": data.get("date", ""),
        "final_score": final_score,
        "state": state,
        "action": action,
        "fundamental_speed": fund_speed,
        "dma_alignment": alignment,
        "divergence": divergence,
        "trend_parallel": parallel,
        "_raw_rev": fund.get("revenue_growth_yoy", "N/A"),
        "_raw_gp": fund.get("gross_profit_growth_yoy", "N/A"),
        "_raw_eps": fund.get("eps_growth_yoy", "N/A"),
        "_raw_revision": fund.get("analyst_revision_3m", "N/A"),
    }


def generate_markdown(result: dict) -> str:
    lines = []
    lines.append(f"## GF-DMA Health Index — ${result['ticker']}")
    if result["date"]:
        lines.append(f"**Date:** {result['date']}")
    lines.append("")

    lines.append("### Summary")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| **Health Score** | **{result['final_score']}** / 100 |")
    lines.append(f"| State | {result['state']} |")
    lines.append(f"| Action | {result['action']} |")
    lines.append("")

    score = result["final_score"]
    bar_len = int(score / 2)
    bar = "█" * bar_len + "░" * (50 - bar_len)
    lines.append(f"```")
    lines.append(f"[{bar}] {score}/100")
    lines.append(f"```")
    lines.append("")

    fs = result["fundamental_speed"]
    lines.append("### Fundamental Speed")
    lines.append("")
    lines.append("| Component | Growth % | Score (0-100) | Weight |")
    lines.append("|-----------|----------|---------------|--------|")
    lines.append(f"| Revenue | {result.get('_raw_rev', 'N/A')}% | {fs['revenue_score']} | 35% |")
    lines.append(f"| Gross Profit | {result.get('_raw_gp', 'N/A')}% | {fs['gross_profit_score']} | 25% |")
    lines.append(f"| EPS | {result.get('_raw_eps', 'N/A')}% | {fs['eps_score']} | 30% |")
    lines.append(f"| Analyst Revision | {result.get('_raw_revision', 'N/A')}% | {fs['revision_score']} | 10% |")
    lines.append(f"| **Blended** | | **{fs['blended']}** | |")
    lines.append("")

    al = result["dma_alignment"]
    lines.append("### DMA Alignment")
    lines.append("")
    lines.append(f"- Aligned pairs: {al['aligned_pairs']}/4 (score: {al['alignment_score']})")
    lines.append(f"- Price vs 200DMA: +{al['price_vs_200dma_pct']}%")
    lines.append(f"- Price vs 50DMA: +{al['price_vs_50dma_pct']}%")
    lines.append("")

    dv = result["divergence"]
    lines.append("### Divergence Analysis")
    lines.append("")
    lines.append(f"- Price momentum (vs 200DMA): +{dv['price_momentum_pct']}%")
    lines.append(f"- Fundamental speed (blended): {fs['blended']}")
    lines.append(f"- Divergence: {dv['divergence']}pp → **{dv['state']}** (score: {dv['divergence_score']})")
    lines.append("")

    tp = result["trend_parallel"]
    lines.append("### Trend Parallelism")
    lines.append("")
    lines.append(f"- 5-day price slope: {tp['price_slope_5d']}%")
    lines.append(f"- 5-day 50DMA slope: {tp['dma50_slope_5d']}%")
    lines.append(f"- Escape ratio: {tp['escape_ratio']} (ideal: 0.5-1.5)")
    lines.append(f"- Parallel score: {tp['parallel_score']}")
    lines.append("")

    lines.append("---")
    lines.append("*Generated by quant-guru-desk/scripts/gf_dma.py*")
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 gf_dma.py <input.json> [--output report.md]")
        print("       python3 gf_dma.py --example")
        sys.exit(1)

    if sys.argv[1] == "--example":
        print(json.dumps(EXAMPLE_INPUT, indent=2, ensure_ascii=False))
        sys.exit(0)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"Error: File not found: {input_path}")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    errors = validate_input(data)
    if errors:
        print("Validation errors:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    result = calculate_health(data)
    report = generate_markdown(result)

    output_path = None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = Path(sys.argv[idx + 1])

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Report written to: {output_path}")
    else:
        print(report)

    summary = {
        "ticker": result["ticker"],
        "health_score": result["final_score"],
        "state": result["state"],
    }
    print(json.dumps(summary), file=sys.stderr)


if __name__ == "__main__":
    main()
