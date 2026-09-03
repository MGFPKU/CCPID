#!/usr/bin/env python3
"""Run the full CCPID export-and-validate pipeline in one command.

Usage:
    python scripts/run_pipeline.py              # export + validate
    python scripts/run_pipeline.py --skip-isic  # skip ISIC normalization
    python scripts/run_pipeline.py --check-urls # also verify URL reachability
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run(args: list[str], description: str, allow_warnings: bool = False) -> int:
    print(f"\n{'=' * 60}")
    print(f"  {description}")
    print(f"{'=' * 60}", flush=True)
    result = subprocess.run([sys.executable, *args], cwd=str(ROOT))
    if result.returncode != 0:
        if allow_warnings:
            print(f"  (warnings found — review {ROOT / 'logs' / 'validation_report.md'})")
            return 0
        print(f"FAILED: {description} (exit {result.returncode})")
    return result.returncode


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Run full CCPID export + validate pipeline.")
    parser.add_argument("--skip-isic", action="store_true", help="Skip ISIC normalization step.")
    parser.add_argument("--check-urls", action="store_true", help="Check URL reachability during validation.")
    args = parser.parse_args()

    steps = []

    steps.append(([str(SCRIPTS / "normalize_cn_outputs.py")], "Normalize Chinese outputs", False))

    if not args.skip_isic:
        steps.append(([str(SCRIPTS / "normalize_isic_economic_sector.py")], "ISIC economic sector normalization", False))

    steps.append(([str(SCRIPTS / "export_workbooks.py"), "--lang", "all"], "Export Excel workbooks", False))

    validate_args = [str(SCRIPTS / "validate_dataset.py")]
    if args.check_urls:
        validate_args.append("--check-urls")
    steps.append((validate_args, "Validate outputs", True))  # warnings are non-fatal

    steps.append(([str(SCRIPTS / "generate_webpage.py")], "Generate data-overview webpage", False))

    failed = 0
    for step_args, description, allow_warnings in steps:
        rc = run(step_args, description, allow_warnings)
        if rc != 0:
            failed += 1

    print(f"\n{'=' * 60}")
    print(f"  Pipeline complete: {len(steps) - failed}/{len(steps)} steps passed")
    print(f"{'=' * 60}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
