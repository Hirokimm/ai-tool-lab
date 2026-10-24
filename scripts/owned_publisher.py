#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
from pathlib import Path
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen

DEFAULT_MANIFEST_URL = "https://factory-social-control-plane.vercel.app/owned_manifest.json"
SITE = "ai-tool-lab"
PUBLIC_BASE = "https://aiventurefactory117.com"
TRACKER_BASE = "https://factory-social-control-plane.vercel.app/api/r"
ALLOWED_MANIFEST_HOSTS = {"factory-social-control-plane.vercel.app"}
ALLOWED_CTA_TARGETS = {"ai-search-audit", "hub", "split2ai"}


def _load_json_url(url: str) -> dict:
    parts = urlsplit(url)
    if parts.scheme != "https" or parts.hostname not in ALLOWED_MANIFEST_HOSTS:
        raise ValueError("manifest URL is not allowlisted")
    req = Request(url, headers={"User-Agent": "AI-Tool-Lab-Owned-Publisher/1.0"})
    with urlopen(req, timeout=15) as response:
        if response.status != 200:
            raise RuntimeError(f"manifest HTTP {response.status}")
        return json.loads(response.read().decode("utf-8"))


def _load_manifest(args: argparse.Namespace) -> dict:
    if args.manifest_file:
        return json.loads(Path(args.manifest_file).read_text(encoding="utf-8"))
    return _load_json_url(args.manifest_url)


def _safe_slug(value: str) -> str:
    if not value or any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-" for c in value):
        raise ValueError(f"unsafe slug: {value!r}")
    return value


def _safe_source_url(value: str) -> str:
    parts = urlsplit(value)
    if parts.scheme != "https" or not parts.hostname:
        raise ValueError("source URL must be https")
    return value


def _tracker_url(item: dict) -> str:
    target = item.get("cta_target", "")
    if target not in ALLOWED_CTA_TARGETS:
        raise ValueError(f"CTA target is not allowlisted: {target!r}")
    params = {
        "t": target,
        "utm_source": "ai_tool_lab",
        "utm_medium": "owned",
        "utm_campaign": item.get("campaign", "owned_media"),
        "utm_content": item.get("content_id", item["id"]),
        "avf_venture": item.get("venture", "FACTORY"),
    }
    return f"{TRACKER_BASE}?{urlencode(params)}"


def _item_hash(item: dict) -> str:
    canonical = json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _render_page(item: dict) -> str:
    title = html.escape(item["title"])
    description = html.escape(item["description"])
    slug = _safe_slug(item["slug"])
    canonical = f"{PUBLIC_BASE}/insights/{slug}/"
    published_at = html.escape(item.get("published_at", ""))
    cta = html.escape(_tracker_url(item), quote=True)
    cta_label = html.escape(item.get("cta_label", "無料でチェックする"))

    sections = []
    for section in item.get("sections", []):
        heading = html.escape(section.get("heading", ""))
        paragraphs = "".join(f"<p>{html.escape(str(p))}</p>" for p in section.get("paragraphs", []))
        sections.append(f"<section><h2>{heading}</h2>{paragraphs}</section>")

    sources = []
    for source in item.get("sources", []):
        url = html.escape(_safe_source_url(source["url"]), quote=True)
        label = html.escape(source.get("label", source["url"]))
        sources.append(f'<li><a href="{url}" rel="noopener noreferrer">{label}</a></li>')
    source_block = f"<section><h2>参考</h2><ul>{''.join(sources)}</ul></section>" if sources else ""

    article_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": item["title"],
        "description": item["description"],
        "datePublished": item.get("published_at", ""),
        "dateModified": item.get("published_at", ""),
        "mainEntityOfPage": canonical,
        "publisher": {"@type": "Organization", "name": "AI Tool Lab", "url": PUBLIC_BASE + "/"},
    }, ensure_ascii=False).replace("</", "<\\/")

    return f'''<!doctype html>
<html lang="ja"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{canonical}">
<title>{title}｜AIツール研究所</title>
<meta name="description" content="{description}">
<style>
:root{{font-family:system-ui,-apple-system,sans-serif;color:#161616;background:#f7f7f5}}*{{box-sizing:border-box}}body{{margin:0}}main{{max-width:760px;margin:auto;padding:42px 18px 72px}}a{{color:#174ea6}}.eyebrow{{font-size:.78rem;font-weight:800;letter-spacing:.09em;color:#666}}h1{{font-size:clamp(2rem,7vw,3rem);line-height:1.18;margin:.35em 0}}.lead{{font-size:1.08rem;line-height:1.8;color:#555}}.meta{{font-size:.82rem;color:#777;margin:16px 0 32px}}section{{margin:34px 0}}h2{{font-size:1.3rem}}p,li{{line-height:1.8}}.cta{{background:#fff;border:1px solid #222;border-radius:16px;padding:20px;margin:34px 0}}.btn{{display:inline-block;background:#161616;color:#fff;text-decoration:none;font-weight:800;padding:12px 15px;border-radius:10px}}.fine{{font-size:.8rem;color:#777}}nav{{margin-bottom:28px}}nav a{{color:#555;text-decoration:none}}
</style>
<script type="application/ld+json">{article_json}</script>
</head><body><main>
<nav><a href="/">← AIツール研究所</a></nav>
<div class="eyebrow">AI SEARCH / PRACTICAL CHECK</div>
<h1>{title}</h1><p class="lead">{description}</p><div class="meta">更新: {published_at}</div>
{''.join(sections)}
<div class="cta"><h2>自社サイトで確認する</h2><p>公開URLだけでAI検索・引用の技術準備度を無料確認できます。問題がなければ有料対応は不要です。</p><a class="btn" href="{cta}">{cta_label}</a><p class="fine">掲載や順位を保証するものではありません。</p></div>
{source_block}
</main></body></html>'''


def _render_index(items: list[dict]) -> str:
    cards = []
    for item in sorted(items, key=lambda x: x.get("published_at", ""), reverse=True):
        slug = _safe_slug(item["slug"])
        cards.append(
            f'<a class="card" href="/insights/{slug}/"><b>{html.escape(item["title"])}</b>'
            f'<span>{html.escape(item["description"])}</span></a>'
        )
    return f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="index,follow"><link rel="canonical" href="{PUBLIC_BASE}/insights/"><title>AI検索・業務AIの実践ノート｜AIツール研究所</title><meta name="description" content="AI検索や業務AIを実際に検証する短い実践ノート。"><style>:root{{font-family:system-ui,-apple-system,sans-serif;color:#161616;background:#f7f7f5}}*{{box-sizing:border-box}}body{{margin:0}}main{{max-width:760px;margin:auto;padding:42px 18px 72px}}a{{color:inherit}}h1{{font-size:clamp(2rem,7vw,3rem)}}.sub{{color:#666;line-height:1.7}}.grid{{display:grid;gap:12px;margin-top:28px}}.card{{display:block;background:#fff;border:1px solid #ddd;border-radius:15px;padding:18px;text-decoration:none}}.card b{{display:block;margin-bottom:6px}}.card span{{color:#666;line-height:1.55}}</style></head><body><main><p><a href="/">← AIツール研究所</a></p><h1>実践ノート</h1><p class="sub">AI検索・業務AIについて、実際に確認できることを短くまとめます。</p><div class="grid">{''.join(cards)}</div></main></body></html>'''


def publish(manifest: dict, root: Path) -> tuple[int, list[str]]:
    if manifest.get("schema_version") != 1:
        raise ValueError("unsupported manifest schema")
    receipts_path = root / "data" / "owned_publish_receipts.json"
    receipts_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        receipts = json.loads(receipts_path.read_text(encoding="utf-8")) if receipts_path.exists() else {"items": {}}
    except json.JSONDecodeError:
        raise ValueError("invalid receipts JSON")
    receipt_items = receipts.setdefault("items", {})

    published_items: list[dict] = []
    changed: list[str] = []
    for item in manifest.get("items", []):
        if item.get("site") != SITE or item.get("status") != "READY":
            continue
        item_id = str(item.get("id", ""))
        slug = _safe_slug(str(item.get("slug", "")))
        digest = _item_hash(item)
        output = root / "insights" / slug / "index.html"
        published_items.append(item)
        if receipt_items.get(item_id, {}).get("sha256") == digest and output.exists():
            continue
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(_render_page(item), encoding="utf-8")
        receipt_items[item_id] = {"sha256": digest, "slug": slug, "published_at": item.get("published_at", "")}
        changed.append(item_id)

    if published_items:
        index_path = root / "insights" / "index.html"
        rendered_index = _render_index(published_items)
        if not index_path.exists() or index_path.read_text(encoding="utf-8") != rendered_index:
            index_path.parent.mkdir(parents=True, exist_ok=True)
            index_path.write_text(rendered_index, encoding="utf-8")

    receipts_path.write_text(json.dumps(receipts, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return len(changed), changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest-url", default=os.environ.get("OWNED_MANIFEST_URL", DEFAULT_MANIFEST_URL))
    parser.add_argument("--manifest-file")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    manifest = _load_manifest(args)
    count, changed = publish(manifest, Path(args.root))
    print(json.dumps({"published": count, "changed_ids": changed}, ensure_ascii=False, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
