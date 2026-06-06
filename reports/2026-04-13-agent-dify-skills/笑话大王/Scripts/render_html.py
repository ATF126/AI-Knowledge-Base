import argparse
import datetime as _dt
import os
from dataclasses import dataclass
from typing import Iterable

from jinja2 import Template


def _read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def _write_text(path: str, content: str) -> None:
    out_dir = os.path.dirname(os.path.abspath(path))
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def _strip_prefix(line: str, prefix: str) -> str:
    s = (line or "").strip()
    if not s:
        return ""
    if s.startswith("-"):
        s = s.lstrip("-").strip()
    if s.startswith(prefix):
        return s.split(prefix, 1)[-1].strip()
    return s


def _extract_items_by_prefix(text: str, *, prefix: str) -> list[str]:
    items: list[str] = []
    current: list[str] = []
    saw_prefix = False
    for raw in (text or "").splitlines():
        line = (raw or "").rstrip()
        stripped = line.strip()
        if not stripped:
            if current:
                items.append(" ".join([x.strip() for x in current if x.strip()]).strip())
                current = []
            continue
        if stripped.startswith("-"):
            stripped = stripped.lstrip("-").strip()
        if prefix and stripped.startswith(prefix):
            saw_prefix = True
            if current:
                items.append(" ".join([x.strip() for x in current if x.strip()]).strip())
                current = []
            current.append(stripped.split(prefix, 1)[-1].strip())
            continue
        if prefix and saw_prefix:
            current.append(stripped)
            continue
        current.append(stripped)
    if current:
        items.append(" ".join([x.strip() for x in current if x.strip()]).strip())
    return [x for x in items if x]


def _extract_items_fallback(text: str) -> list[str]:
    items: list[str] = []
    current: list[str] = []
    for raw in (text or "").splitlines():
        s = (raw or "").strip()
        if not s:
            if current:
                items.append(" ".join(current).strip())
                current = []
            continue
        if s.startswith("-"):
            s = s.lstrip("-").strip()
        current.append(s)
    if current:
        items.append(" ".join(current).strip())
    return [x for x in items if x]


@dataclass(frozen=True)
class RenderInput:
    kind: str
    title: str
    source_path: str
    items: list[str]
    md_html: str


_TEMPLATE = Template(
    """<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{{ title }}</title>
  <style>
    :root {
      --bg: #0b1020;
      --card: rgba(255, 255, 255, 0.06);
      --text: rgba(255, 255, 255, 0.92);
      --muted: rgba(255, 255, 255, 0.65);
      --line: rgba(255, 255, 255, 0.12);
      --accent: #7aa2f7;
      --accent2: #9ece6a;
      --shadow: 0 12px 30px rgba(0, 0, 0, 0.35);
      --radius: 18px;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", Arial, sans-serif;
      background: radial-gradient(1200px 800px at 15% 10%, rgba(122, 162, 247, 0.30), transparent 55%),
                  radial-gradient(900px 600px at 80% 30%, rgba(158, 206, 106, 0.20), transparent 55%),
                  radial-gradient(1000px 700px at 50% 100%, rgba(187, 154, 247, 0.18), transparent 55%),
                  var(--bg);
      color: var(--text);
      padding: 40px 16px 56px;
    }
    .wrap { max-width: 860px; margin: 0 auto; }
    header {
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 18px;
    }
    h1 {
      margin: 0;
      font-size: 28px;
      letter-spacing: 0.2px;
    }
    .meta {
      color: var(--muted);
      font-size: 12px;
      line-height: 1.5;
      text-align: right;
      white-space: nowrap;
    }
    .card {
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      overflow: hidden;
    }
    .card .content { padding: 16px; }
    .tag {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 12px;
      border-radius: 999px;
      border: 1px solid var(--line);
      background: rgba(255,255,255,0.04);
      color: var(--muted);
      font-size: 13px;
      margin-bottom: 12px;
    }
    .tag b { color: var(--text); font-weight: 650; }
    ol {
      margin: 0;
      padding-left: 22px;
    }
    li {
      padding: 10px 8px;
      border-bottom: 1px dashed rgba(255,255,255,0.12);
      line-height: 1.7;
    }
    li:last-child { border-bottom: 0; }
    .pill {
      display: inline-block;
      margin-right: 8px;
      padding: 2px 10px;
      border-radius: 999px;
      font-size: 12px;
      color: rgba(255,255,255,0.86);
      background: rgba(122,162,247,0.18);
      border: 1px solid rgba(122,162,247,0.28);
      vertical-align: 1px;
    }
    .md {
      margin-top: 14px;
      padding-top: 14px;
      border-top: 1px solid var(--line);
      color: rgba(255,255,255,0.88);
      line-height: 1.8;
    }
    .md h1,.md h2,.md h3 { margin: 12px 0 8px; }
    .md a { color: var(--accent); }
    .md code { background: rgba(255,255,255,0.08); padding: 2px 6px; border-radius: 8px; }
    .md pre { background: rgba(0,0,0,0.25); padding: 12px; border-radius: 12px; overflow: auto; }
    footer {
      margin-top: 14px;
      color: var(--muted);
      font-size: 12px;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div>
        <h1>{{ title }}</h1>
      </div>
      <div class="meta">
        <div>类型：{{ kind_label }}</div>
        <div>生成时间：{{ generated_at }}</div>
      </div>
    </header>

    <section class="card">
      <div class="content">
        <div class="tag">
          <b>笑话大王</b>
          <span>·</span>
          <span>共 {{ count }} 条</span>
        </div>

        <ol>
          {% for it in items %}
            <li><span class="pill">{{ loop.index }}</span>{{ it }}</li>
          {% endfor %}
        </ol>

        {% if md_html %}
          <div class="md">{{ md_html | safe }}</div>
        {% endif %}
      </div>
    </section>

    <footer>source: {{ source_path }}</footer>
  </div>
</body>
</html>
"""
)


def _build_render_input(*, kind: str, title: str, in_path: str, raw_text: str) -> RenderInput:
    kind_norm = (kind or "").strip().lower()
    if kind_norm not in {"cold", "duanzi"}:
        raise ValueError("kind must be one of: cold, duanzi")

    if kind_norm == "cold":
        items = _extract_items_by_prefix(raw_text, prefix="冷笑话：")
        if not items:
            items = _extract_items_fallback(raw_text)
        return RenderInput(
            kind=kind_norm,
            title=title or "冷笑话",
            source_path=os.path.abspath(in_path),
            items=items,
            md_html="",
        )

    items = _extract_items_by_prefix(raw_text, prefix="段子：")
    if not items:
        items = _extract_items_fallback(raw_text)
    return RenderInput(
        kind=kind_norm,
        title=title or "段子",
        source_path=os.path.abspath(in_path),
        items=items,
        md_html="",
    )


def render_html(*, kind: str, in_path: str, out_path: str, title: str) -> str:
    raw_text = _read_text(in_path)
    payload = _build_render_input(kind=kind, title=title, in_path=in_path, raw_text=raw_text)
    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    kind_label = "冷笑话" if payload.kind == "cold" else "段子"
    html = _TEMPLATE.render(
        title=payload.title,
        kind_label=kind_label,
        generated_at=now,
        count=len(payload.items),
        items=payload.items,
        md_html=payload.md_html,
        source_path=payload.source_path,
    )
    _write_text(out_path, html)
    return out_path


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", required=True, choices=["cold", "duanzi"])
    parser.add_argument("--in", dest="in_path", required=True)
    parser.add_argument("--out", dest="out_path", required=True)
    parser.add_argument("--title", default="")
    args = parser.parse_args(list(argv) if argv is not None else None)

    out_path = render_html(kind=args.kind, in_path=args.in_path, out_path=args.out_path, title=args.title)
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
