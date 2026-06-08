#!/usr/bin/env python3
"""
Quant Guru Desk — Chokepoint Scorecard Calculator

A local, deterministic scoring tool for Serenity-style supply-chain bottleneck
analysis. Input a JSON file with factor scores, get a weighted total + Markdown
report.

Usage:
    python3 scorecard.py input.json
    python3 scorecard.py input.json --output report.md
    python3 scorecard.py --example  # Print an example input JSON

Requirements: Python 3.9+, zero external dependencies.
"""

import json
import sys
from pathlib import Path

POSITIVE_WEIGHTS = {
    "demand_inflection": 15,
    "architecture_coupling": 10,
    "chokepoint_severity": 15,
    "supplier_concentration": 12,
    "expansion_difficulty": 12,
    "evidence_quality": 15,
    "valuation_disconnect": 11,
    "catalyst_timing": 10,
}

PENALTY_MULTIPLIER = 2.0

PENALTY_FACTORS = [
    "dilution_financing",
    "governance",
    "geopolitics",
    "liquidity",
    "hype_risk",
    "accounting_quality",
    "cyclicality",
    "alternative_design",
]

RATING_BANDS = [
    (85, "Top research priority", "Strong conviction position (20-30%)"),
    (70, "High research priority", "Core position (10-15%)"),
    (55, "Worth tracking", "Exploratory position (5-8%)"),
    (0, "Early lead / low priority", "Monitor only, do not hold"),
]

EXAMPLE_INPUT = {
    "ticker": "SIVE",
    "guru": "serenity",
    "date": "2026-06-08",
    "notes": "CPO laser sole-source thesis",
    "positive_factors": {
        "demand_inflection": 4,
        "architecture_coupling": 5,
        "chokepoint_severity": 4,
        "supplier_concentration": 4,
        "expansion_difficulty": 4,
        "evidence_quality": 3,
        "valuation_disconnect": 4,
        "catalyst_timing": 4,
    },
    "penalty_factors": {
        "dilution_financing": 1,
        "governance": 0,
        "geopolitics": 1,
        "liquidity": 2,
        "hype_risk": 3,
        "accounting_quality": 0,
        "cyclicality": 1,
        "alternative_design": 1,
    },
}


def validate_input(data: dict) -> list[str]:
    """Validate input JSON structure. Returns list of error messages."""
    errors = []

    if "ticker" not in data:
        errors.append("Missing required field: 'ticker'")

    if "positive_factors" not in data:
        errors.append("Missing required field: 'positive_factors'")
    else:
        for key in POSITIVE_WEIGHTS:
            if key not in data["positive_factors"]:
                errors.append(f"Missing positive factor: '{key}'")
            else:
                val = data["positive_factors"][key]
                if not isinstance(val, (int, float)) or val < 0 or val > 5:
                    errors.append(f"'{key}' must be a number between 0 and 5, got: {val}")

    if "penalty_factors" not in data:
        errors.append("Missing required field: 'penalty_factors'")
    else:
        for key in PENALTY_FACTORS:
            if key not in data["penalty_factors"]:
                errors.append(f"Missing penalty factor: '{key}'")
            else:
                val = data["penalty_factors"][key]
                if not isinstance(val, (int, float)) or val < 0 or val > 5:
                    errors.append(f"'{key}' must be a number between 0 and 5, got: {val}")

    return errors


def calculate_score(data: dict) -> dict:
    """Calculate the weighted score from input data."""
    positive = data["positive_factors"]
    penalties = data["penalty_factors"]

    # Weighted positive score (each factor 0-5, weighted to 100 total)
    # Formula: sum(score * weight) / 5 (since max per factor is 5)
    positive_total = sum(
        positive[key] * weight for key, weight in POSITIVE_WEIGHTS.items()
    ) / 5.0

    # Penalty deduction: each penalty point * multiplier
    penalty_total = sum(penalties[key] for key in PENALTY_FACTORS) * PENALTY_MULTIPLIER

    # Final score
    final_score = max(0, positive_total - penalty_total)

    # Rating band
    rating = ""
    position_guidance = ""
    for threshold, label, guidance in RATING_BANDS:
        if final_score >= threshold:
            rating = label
            position_guidance = guidance
            break

    # Per-factor breakdown
    factor_scores = {}
    for key, weight in POSITIVE_WEIGHTS.items():
        factor_scores[key] = {
            "raw": positive[key],
            "weighted": positive[key] * weight / 5.0,
            "weight": weight,
        }

    penalty_scores = {}
    for key in PENALTY_FACTORS:
        penalty_scores[key] = {
            "raw": penalties[key],
            "deduction": penalties[key] * PENALTY_MULTIPLIER,
        }

    return {
        "ticker": data.get("ticker", "UNKNOWN"),
        "guru": data.get("guru", "serenity"),
        "date": data.get("date", ""),
        "notes": data.get("notes", ""),
        "positive_total": round(positive_total, 1),
        "penalty_total": round(penalty_total, 1),
        "final_score": round(final_score, 1),
        "rating": rating,
        "position_guidance": position_guidance,
        "factor_scores": factor_scores,
        "penalty_scores": penalty_scores,
    }


def generate_markdown(result: dict) -> str:
    """Generate a Markdown report from calculation results."""
    lines = []

    lines.append(f"## Scorecard — ${result['ticker']}")
    if result["date"]:
        lines.append(f"**Date:** {result['date']}")
    if result["notes"]:
        lines.append(f"**Notes:** {result['notes']}")
    lines.append(f"**Guru:** {result['guru'].title()}")
    lines.append("")

    # Summary
    lines.append("### Summary")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Positive subtotal | {result['positive_total']} / 100 |")
    lines.append(f"| Penalty deduction | -{result['penalty_total']} |")
    lines.append(f"| **Final score** | **{result['final_score']}** |")
    lines.append(f"| Rating | {result['rating']} |")
    lines.append(f"| Position guidance | {result['position_guidance']} |")
    lines.append("")

    # Positive factors breakdown
    lines.append("### Positive Factors")
    lines.append("")
    lines.append("| Factor | Raw (0-5) | Weight | Weighted |")
    lines.append("|--------|-----------|--------|----------|")
    for key, info in result["factor_scores"].items():
        display_name = key.replace("_", " ").title()
        lines.append(
            f"| {display_name} | {info['raw']} | {info['weight']}% | {info['weighted']:.1f} |"
        )
    lines.append(f"| **Total** | | | **{result['positive_total']}** |")
    lines.append("")

    # Penalty factors breakdown
    lines.append("### Penalty Factors")
    lines.append("")
    lines.append("| Factor | Raw (0-5) | Deduction |")
    lines.append("|--------|-----------|-----------|")
    for key, info in result["penalty_scores"].items():
        display_name = key.replace("_", " ").title()
        if info["raw"] > 0:
            lines.append(f"| {display_name} | {info['raw']} | -{info['deduction']:.1f} |")
        else:
            lines.append(f"| {display_name} | 0 | — |")
    lines.append(f"| **Total penalty** | | **-{result['penalty_total']}** |")
    lines.append("")

    # Visual bar
    score = result["final_score"]
    bar_len = int(score / 2)
    bar = "█" * bar_len + "░" * (50 - bar_len)
    lines.append("### Score Visual")
    lines.append("")
    lines.append(f"```")
    lines.append(f"[{bar}] {score}/100")
    lines.append(f"```")
    lines.append("")

    # Warnings
    warnings = []
    if result["factor_scores"]["evidence_quality"]["raw"] <= 2:
        warnings.append(
            "Evidence quality is low (<=2). Conclusions should be flagged as [未验证]."
        )
    for key, info in result["penalty_scores"].items():
        if info["raw"] >= 4:
            display_name = key.replace("_", " ").title()
            warnings.append(f"High penalty on '{display_name}' ({info['raw']}/5) — red flag.")
    if warnings:
        lines.append("### Warnings")
        lines.append("")
        for w in warnings:
            lines.append(f"- {w}")
        lines.append("")

    lines.append("---")
    lines.append("*Generated by quant-guru-desk/scripts/scorecard.py*")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scorecard.py <input.json> [--output report.md]")
        print("       python3 scorecard.py --example")
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

    # Validate
    errors = validate_input(data)
    if errors:
        print("Validation errors:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    # Calculate
    result = calculate_score(data)

    # Generate report
    report = generate_markdown(result)

    # Output
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

    # Also print JSON summary to stderr for programmatic use
    summary = {
        "ticker": result["ticker"],
        "final_score": result["final_score"],
        "rating": result["rating"],
        "positive_total": result["positive_total"],
        "penalty_total": result["penalty_total"],
    }
    print(json.dumps(summary), file=sys.stderr)


if __name__ == "__main__":
    main()
