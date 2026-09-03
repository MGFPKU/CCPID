#!/usr/bin/env python3
"""Suggest canonical official-source searches for a policy title or URL.

This helper is intentionally offline-friendly: it does not depend on network
access. Use the printed queries in a browser/search engine before accepting
public-comment portals, reposts, or broad policy pages as source URLs.
"""

from __future__ import annotations

import argparse
import re
from urllib.parse import parse_qs, urlparse


NDRC_NOTICE_PATHS = (
    "site:ndrc.gov.cn/xwdt/tzgg",
    "site:ndrc.gov.cn/xxgk/zcfb/tz",
    "site:ndrc.gov.cn/xxgk/zcfb/ghxwj",
)

OTHER_OFFICIAL_DOMAINS = (
    "site:nea.gov.cn",
    "site:gov.cn",
)

CONSULTATION_OR_LEAD_HOSTS = {
    "yyglxxbsgw.ndrc.gov.cn": (
        "NDRC public-comment / opinion-solicitation system. Treat as a lead; "
        "search for the final notice on ndrc.gov.cn before coding Legal document, "
        "Last revisions, or Other weblinks."
    ),
}


def article_id_timestamp_hint(url: str) -> str:
    query = parse_qs(urlparse(url).query)
    article_id = "".join(query.get("articleId", []))
    compact = re.sub(r"[^0-9a-fA-F]", "", article_id)
    match = re.search(r"019[0-9a-fA-F]{9}", compact)
    if not match:
        return ""
    try:
        from datetime import datetime, timezone

        millis = int(match.group(0), 16)
        return datetime.fromtimestamp(millis / 1000, tz=timezone.utc).strftime("%Y-%m")
    except (OverflowError, ValueError):
        return ""


def quoted(value: str) -> str:
    return f'"{value.strip()}"'


def build_queries(title: str, document_number: str = "") -> list[str]:
    title_q = quoted(title)
    queries = [f"{scope} {title_q}" for scope in NDRC_NOTICE_PATHS]
    queries.extend(f"{scope} {title_q}" for scope in OTHER_OFFICIAL_DOMAINS)
    if document_number:
        doc_q = quoted(document_number)
        queries.extend(f"{scope} {doc_q}" for scope in NDRC_NOTICE_PATHS)
        queries.append(f"site:ndrc.gov.cn {doc_q} {title_q}")
    queries.append(f"site:ndrc.gov.cn {title_q}")
    queries.append(f"site:nea.gov.cn {title_q}")
    return list(dict.fromkeys(queries))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="Exact Chinese or English policy title to search.")
    parser.add_argument("--url", default="", help="Candidate URL already found.")
    parser.add_argument("--document-number", default="", help="Document number, e.g. 发改办能源〔2025〕669号.")
    args = parser.parse_args()

    if args.url:
        host = urlparse(args.url).netloc.lower().split("@")[-1].split(":")[0]
        note = CONSULTATION_OR_LEAD_HOSTS.get(host)
        if note:
            print(f"URL review: {note}")
        hint = article_id_timestamp_hint(args.url)
        if hint:
            print(f"URL timestamp hint: articleId appears to point around {hint}; search that month on official notice pages.")
        print()

    print("Recommended official-source searches:")
    for query in build_queries(args.title, args.document_number):
        print(f"- {query}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
