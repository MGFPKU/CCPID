#!/usr/bin/env python3
"""Detect new/updated national policies in the China Carbon Neutrality Tracker (ccnt.igdp.cn).

The CCND action database exposes its policy list as JSON at
https://ccnt.igdp.cn/api/v1/policies/all?locale=zh. This script compares the
national subset (region_type == "国家") against review/ccnt/tracking.csv and
downloads the original document of every new/updated entry into
review/ccnt/docs/ for the review round.

Usage:
    python scripts/check_ccnt_updates.py [--catchup-days N] [--mark-seen] [--force-fetch]

Default run: detect candidates, download originals, write review/ccnt/candidates.json.

--catchup-days N: only has an effect on the run that creates the tracking
    baseline (first run); includes entries whose date_updated falls within
    the last N days as candidates.
--mark-seen: mark every entry listed in candidates.json as processed by
    updating review/ccnt/tracking.csv. No network access needed.
--force-fetch: ignore the cached API response and refetch.
"""

import argparse
import csv
import html as html_mod
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
import zipfile
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import urlparse

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

ROOT = Path(__file__).resolve().parent.parent
CCND_DIR = ROOT / "review" / "ccnt"
TRACKING_CSV = CCND_DIR / "tracking.csv"
REPORTS_DIR = CCND_DIR / "reports"
DOCS_DIR = CCND_DIR / "docs"
CANDIDATES_JSON = CCND_DIR / "candidates.json"
API_CACHE = CCND_DIR / "api_cache.json"
API_URL = "https://ccnt.igdp.cn/api/v1/policies/all?locale=zh"
CACHE_MAX_AGE = 6 * 3600
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) CCPID-update-checker"}


def log(msg):
    print(msg)
    sys.stdout.flush()


def fetch_policies(force=False):
    if not force and API_CACHE.exists():
        age = time.time() - API_CACHE.stat().st_mtime
        if age < CACHE_MAX_AGE:
            return json.loads(API_CACHE.read_text(encoding="utf-8"))
    req = urllib.request.Request(API_URL, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=120) as resp:
        raw = resp.read()
    API_CACHE.write_bytes(raw)
    return json.loads(raw.decode("utf-8"))


def national_policies(policies):
    return [p for p in policies if p.get("region_type") == "国家" and p.get("id")]


def load_tracking():
    if not TRACKING_CSV.exists():
        return None
    with TRACKING_CSV.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return {r["id"]: r for r in rows}


def write_tracking(rows):
    fields = ["id", "file_name", "organization", "year_published", "month_published", "date_updated", "last_seen"]
    with TRACKING_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})


def baseline_rows(national, today):
    rows = [
        {
            "id": p["id"],
            "file_name": p.get("file_name", ""),
            "organization": p.get("organization", ""),
            "year_published": p.get("year_published", ""),
            "month_published": p.get("month_published", ""),
            "date_updated": (p.get("date_updated") or "")[:10],
            "last_seen": today,
        }
        for p in national
    ]
    rows.sort(key=lambda r: r["date_updated"], reverse=True)
    return rows


def sanitize(name):
    name = re.sub(r"[^\w\-]+", "_", name, flags=re.UNICODE)
    return name.strip("_")[:60] or "doc"


def html_to_text(raw):
    text = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
    text = re.sub(r"(?s)<[^>]+>", "\n", text)
    text = html_mod.unescape(text)
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    return text.strip()


def docx_to_text(raw):
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            xml = z.read("word/document.xml").decode("utf-8", errors="ignore")
    except Exception:
        return ""
    xml = re.sub(r"</w:p>", "\n", xml)
    text = re.sub(r"<[^>]+>", "", xml)
    text = html_mod.unescape(text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    return text.strip()


def doc_to_text(raw):
    """Extract text from a legacy OLE2 .doc/.wps file via antiword (best-effort)."""
    antiword = shutil.which("antiword")
    if not antiword:
        return ""
    fd, tmp = tempfile.mkstemp(suffix=".doc")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(raw)
        proc = subprocess.run([antiword, tmp], capture_output=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return ""
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass
    if proc.returncode != 0 or not proc.stdout.strip():
        return ""
    try:
        return proc.stdout.decode("utf-8").strip()
    except UnicodeDecodeError:
        return proc.stdout.decode("gbk", errors="ignore").strip()


def pdf_to_text(raw):
    try:
        from pdfminer.high_level import extract_text
    except ImportError:
        return None
    try:
        return extract_text(io.BytesIO(raw), maxpages=0)
    except Exception:
        return None


def download_doc(item, idx):
    """Download the original document of one policy; return (local_file, status)."""
    link = (item.get("link") or "").strip()
    if not link:
        return "", "no link"
    slug = sanitize(item.get("file_name", ""))
    ext = os.path.splitext(urlparse(link).path)[1].lower()
    req = urllib.request.Request(link, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            raw = resp.read()
            ctype = (resp.headers.get("Content-Type") or "").lower()
    except Exception as e:
        return "", f"download failed: {type(e).__name__}"
    if ctype.startswith("text/html") or ext in (".htm", ".html"):
        path = DOCS_DIR / f"{idx:03d}_{slug}.txt"
        path.write_text(html_to_text(raw.decode("utf-8", errors="ignore")), encoding="utf-8")
        return path.name, "ok (html)"
    if ctype.startswith("application/pdf") or ext == ".pdf":
        text = pdf_to_text(raw)
        if text is None:
            path = DOCS_DIR / f"{idx:03d}_{slug}.pdf"
            path.write_bytes(raw)
            return path.name, "ok (pdf, no pdfminer)"
        path = DOCS_DIR / f"{idx:03d}_{slug}.txt"
        path.write_text(text.strip(), encoding="utf-8")
        if len(text.strip()) < 200:
            return path.name, "ok (pdf, text extraction possibly incomplete)"
        return path.name, "ok (pdf)"
    if "wordprocessingml" in ctype or ext == ".docx":
        text = docx_to_text(raw)
        if not text:
            return "", "docx extraction failed"
        path = DOCS_DIR / f"{idx:03d}_{slug}.txt"
        path.write_text(text, encoding="utf-8")
        return path.name, "ok (docx)"
    if ext in (".doc", ".wps") or "application/msword" in ctype:
        # Some .wps files are OOXML zips renamed; antiword only handles OLE2.
        text = docx_to_text(raw) if raw[:2] == b"PK" else doc_to_text(raw)
        if text:
            path = DOCS_DIR / f"{idx:03d}_{slug}.txt"
            path.write_text(text, encoding="utf-8")
            if len(text) < 200:
                return path.name, "ok (doc, text extraction possibly incomplete)"
            return path.name, "ok (doc)"
        path = DOCS_DIR / f"{idx:03d}_{slug}{ext}"
        path.write_bytes(raw)
        return path.name, "doc extraction failed (saved raw)"
    path = DOCS_DIR / f"{idx:03d}_{slug}.bin"
    path.write_bytes(raw)
    return path.name, f"ok (unknown type {ctype or ext})"


def mark_seen():
    if not CANDIDATES_JSON.exists():
        log("错误：找不到 candidates.json，请先运行检测。")
        sys.exit(1)
    cands = json.loads(CANDIDATES_JSON.read_text(encoding="utf-8"))
    today = date.today().isoformat()
    tracking = load_tracking() or {}
    for c in cands:
        tracking[c["id"]] = {
            "id": c["id"],
            "file_name": c.get("file_name", ""),
            "organization": c.get("organization", ""),
            "year_published": c.get("year_published", ""),
            "month_published": c.get("month_published", ""),
            "date_updated": c.get("date_updated", ""),
            "last_seen": today,
        }
    rows = sorted(tracking.values(), key=lambda r: r.get("date_updated", ""), reverse=True)
    write_tracking(rows)
    log(f"已将 {len(cands)} 条候选标记为已处理 (last_seen={today})")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--catchup-days", type=int, default=0)
    ap.add_argument("--mark-seen", action="store_true")
    ap.add_argument("--force-fetch", action="store_true")
    args = ap.parse_args()

    for d in (CCND_DIR, REPORTS_DIR, DOCS_DIR):
        d.mkdir(parents=True, exist_ok=True)

    if args.mark_seen:
        mark_seen()
        return

    log("正在获取 ccnt.igdp.cn 政策数据 ...")
    policies = fetch_policies(force=args.force_fetch)
    national = national_policies(policies)
    today = date.today().isoformat()
    log(f"国家政策总数: {len(national)} (全部政策 {len(policies)})")

    tracking = load_tracking()
    baseline_created = False
    if tracking is None:
        write_tracking(baseline_rows(national, today))
        tracking = load_tracking()
        baseline_created = True
        log(f"首次运行：已建立基线 tracking.csv ({len(national)} 条国家政策, last_seen={today})")

    if baseline_created and args.catchup_days:
        cutoff = (date.today() - timedelta(days=args.catchup_days)).isoformat()
        candidates = [p for p in national if (p.get("date_updated") or "")[:10] >= cutoff]
        log(f"首次运行补课：date_updated >= {cutoff} 的候选 {len(candidates)} 条")
    else:
        candidates = [
            p for p in national
            if p["id"] not in tracking
            or (p.get("date_updated") or "")[:10] > tracking[p["id"]].get("date_updated", "")
        ]

    new_ids = {p["id"] for p in candidates} - set(tracking)
    log(f"候选政策: {len(candidates)} 条 (新增 {len(new_ids)}, 更新 {len(candidates) - len(new_ids)})")

    cands = []
    ordered = sorted(candidates, key=lambda x: (x.get("date_updated") or ""), reverse=True)
    for idx, p in enumerate(ordered, start=1):
        local_file, status = download_doc(p, idx)
        entry = {
            "idx": idx,
            "id": p["id"],
            "file_name": p.get("file_name", ""),
            "organization": p.get("organization", ""),
            "link": p.get("link", ""),
            "year_published": p.get("year_published"),
            "month_published": p.get("month_published"),
            "date_updated": (p.get("date_updated") or "")[:10],
            "category_1": p.get("category_1", []),
            "category_2": p.get("category_2", []),
            "note": p.get("note", ""),
            "local_file": local_file,
            "download_status": status,
        }
        cands.append(entry)
        name = (p.get("file_name") or "")[:40]
        log(f"[{idx:02d}] {entry['date_updated']} 发布{p.get('year_published')}-{p.get('month_published')} {name} | {status}")

    CANDIDATES_JSON.write_text(json.dumps(cands, ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"候选清单已写入 {CANDIDATES_JSON.relative_to(ROOT)}；原文位于 {DOCS_DIR.relative_to(ROOT)}")
    if not cands:
        log("本轮无候选，无需人工审核。")


if __name__ == "__main__":
    main()
