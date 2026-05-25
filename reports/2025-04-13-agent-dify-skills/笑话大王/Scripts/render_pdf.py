import argparse
import datetime as _dt
import sys
from typing import Iterable


def _read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


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


def render_pdf(*, kind: str, in_path: str, out_path: str, title: str) -> str:
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
        from reportlab.lib.units import mm
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.cidfonts import UnicodeCIDFont
        from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
    except ModuleNotFoundError as e:
        raise RuntimeError("缺少 reportlab，请先安装 requirements.txt") from e

    kind_norm = (kind or "").strip().lower()
    if kind_norm not in {"cold", "duanzi"}:
        raise ValueError("kind must be one of: cold, duanzi")

    raw_text = _read_text(in_path)
    prefix = "冷笑话：" if kind_norm == "cold" else "段子："
    items = _extract_items_by_prefix(raw_text, prefix=prefix) or _extract_items_fallback(raw_text)

    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "title_cn",
        parent=styles["Title"],
        fontName="STSong-Light",
        fontSize=18,
        leading=22,
        spaceAfter=8,
    )
    meta_style = ParagraphStyle(
        "meta_cn",
        parent=styles["Normal"],
        fontName="STSong-Light",
        fontSize=10,
        leading=14,
        textColor="#555555",
        spaceAfter=10,
    )
    item_style = ParagraphStyle(
        "item_cn",
        parent=styles["Normal"],
        fontName="STSong-Light",
        fontSize=12,
        leading=18,
        spaceAfter=6,
    )

    doc = SimpleDocTemplate(
        out_path,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title=title or ("冷笑话" if kind_norm == "cold" else "段子"),
    )

    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    kind_label = "冷笑话" if kind_norm == "cold" else "段子"
    title_text = title or kind_label
    meta_text = f"类型：{kind_label}　　生成时间：{now}　　共 {len(items)} 条"

    story: list[object] = []
    story.append(Paragraph(title_text, title_style))
    story.append(Paragraph(meta_text, meta_style))
    story.append(Spacer(1, 6))

    for i, it in enumerate(items, start=1):
        safe = (it or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        story.append(Paragraph(f"{i}. {safe}", item_style))

    doc.build(story)
    return out_path


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", required=True, choices=["cold", "duanzi"])
    parser.add_argument("--in", dest="in_path", required=True)
    parser.add_argument("--out", dest="out_path", required=True)
    parser.add_argument("--title", default="")
    args = parser.parse_args(list(argv) if argv is not None else None)

    try:
        out_path = render_pdf(kind=args.kind, in_path=args.in_path, out_path=args.out_path, title=args.title)
        print(out_path)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
