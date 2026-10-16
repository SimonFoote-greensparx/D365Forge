"""A small Markdown to HTML renderer for the hosted website. Standard library only.

It covers what this repository's Markdown uses: frontmatter, headings, paragraphs, nested bullet and numbered lists,
fenced code (also inside list items), tables, block quotes, rules, inline code, bold, italic, links and bare URLs.
Raw HTML in the source is escaped, never passed through. `link` is a callback that rewrites each link target; it
returns the new href, or None to drop the link and keep its text.
"""
from __future__ import annotations

import html
import re
from typing import Callable, Optional

LinkFn = Callable[[str], Optional[str]]

_LIST = re.compile(r"^( {0,3})([-*+]|\d{1,9}[.)])( +)(.*)$")
_HEADING = re.compile(r"^ {0,3}(#{1,6})\s+(.*?)\s*#*\s*$")
_FENCE = re.compile(r"^ {0,3}(```|~~~)")
_RULE = re.compile(r"^ {0,3}([-*_])( *\1){2,}\s*$")
_TABLE_SEP = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")


def strip_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter, body)."""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[4:end], text[end + 5:]
    return "", text


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_]+", "-", text).strip("-")


def inline(text: str, link: LinkFn, _store: list[str] | None = None) -> str:
    """Render inline Markdown. Code spans and links are swapped for placeholders before escaping."""
    top = _store is None
    store: list[str] = [] if _store is None else _store

    def keep(s: str) -> str:
        store.append(s)
        return f"\x00{len(store) - 1}\x00"

    text = re.sub(r"(`+)(.+?)\1", lambda m: keep(f"<code>{html.escape(m.group(2).strip())}</code>"), text)

    def md_link(m: re.Match) -> str:
        label, target = m.group(1), m.group(2)
        href = link(target)
        rendered = inline(label, link, store)
        return keep(rendered if href is None else f'<a href="{html.escape(href)}">{rendered}</a>')

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", md_link, text)

    def bare(m: re.Match) -> str:
        url = m.group(0)
        tail = ""
        while url and url[-1] in ".,;:!?":
            tail, url = url[-1] + tail, url[:-1]
        href = link(url)
        shown = html.escape(url)
        return keep(shown if href is None else f'<a href="{html.escape(href)}">{shown}</a>') + tail

    text = re.sub(r"https?://[^\s<>()\[\]\"']+", bare, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?=\S)(.+?)(?<=\S)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"(?<![\w])_(?=\S)(.+?)(?<=\S)_(?![\w])", r"<em>\1</em>", text)
    while top and "\x00" in text:
        text = re.sub(r"\x00(\d+)\x00", lambda m: store[int(m.group(1))], text)
    return text


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _dedent(line: str, n: int) -> str:
    return line[min(n, _indent(line)):]


def _starts_block(line: str) -> bool:
    return bool(_HEADING.match(line) or _FENCE.match(line) or _RULE.match(line) or _LIST.match(line)
                or line.lstrip().startswith(">") or line.lstrip().startswith("|"))


def _table(rows: list[str], link: LinkFn) -> str:
    def cells(row: str) -> list[str]:
        row = row.strip()
        if row.startswith("|"):
            row = row[1:]
        if row.endswith("|") and not row.endswith("\\|"):
            row = row[:-1]
        parts = re.split(r"(?<!\\)\|", row)
        return [p.strip().replace("\\|", "|") for p in parts]

    head, body = cells(rows[0]), [cells(r) for r in rows[2:]]
    out = ['<div class="table-wrap"><table class="grid">']
    if any(head):
        out += ["<thead><tr>"] + [f"<th>{inline(c, link)}</th>" for c in head] + ["</tr></thead>"]
    out.append("<tbody>")
    for r in body:
        r = (r + [""] * len(head))[:len(head)]
        out.append("<tr>" + "".join(f"<td>{inline(c, link)}</td>" for c in r) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def blocks(lines: list[str], link: LinkFn, tight: bool = False) -> str:
    out: list[str] = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        fence = _FENCE.match(line)
        if fence:
            ind, mark = _indent(line), fence.group(1)
            i += 1
            code = []
            while i < n and not lines[i].strip().startswith(mark):
                code.append(_dedent(lines[i], ind))
                i += 1
            i += 1
            out.append(f"<pre><code>{html.escape(chr(10).join(code))}</code></pre>")
            continue
        h = _HEADING.match(line)
        if h:
            level, text = len(h.group(1)), h.group(2)
            out.append(f'<h{level} id="{slugify(text)}">{inline(text, link)}</h{level}>')
            i += 1
            continue
        if _RULE.match(line):
            out.append("<hr>")
            i += 1
            continue
        if line.lstrip().startswith("|") and i + 1 < n and _TABLE_SEP.match(lines[i + 1]):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(lines[i])
                i += 1
            out.append(_table(rows, link))
            continue
        if line.lstrip().startswith(">"):
            quote = []
            while i < n and lines[i].strip() and (lines[i].lstrip().startswith(">") or not _starts_block(lines[i])):
                quote.append(re.sub(r"^\s*> ?", "", lines[i]))
                i += 1
            out.append(f"<blockquote>{blocks(quote, link)}</blockquote>")
            continue
        m = _LIST.match(line)
        if m:
            i = _list(lines, i, link, out)
            continue
        para = [line.strip()]
        i += 1
        while i < n and lines[i].strip() and not _starts_block(lines[i]):
            para.append(lines[i].strip())
            i += 1
        text = inline(" ".join(para), link)
        out.append(text if tight else f"<p>{text}</p>")
    return "\n".join(out)


def _list(lines: list[str], i: int, link: LinkFn, out: list[str]) -> int:
    first = _LIST.match(lines[i])
    base = len(first.group(1))
    ordered = first.group(2)[0].isdigit()
    start = int(first.group(2)[:-1]) if ordered else 1
    items: list[list[str]] = []
    loose = False
    n = len(lines)
    while i < n:
        m = _LIST.match(lines[i])
        if not m or len(m.group(1)) != base or m.group(2)[0].isdigit() != ordered:
            break
        content_indent = base + len(m.group(2)) + len(m.group(3))
        item = [m.group(4)]
        i += 1
        while i < n:
            line = lines[i]
            if not line.strip():
                j = i + 1
                while j < n and not lines[j].strip():
                    j += 1
                if j < n and _indent(lines[j]) >= content_indent:
                    item.extend([""] * (j - i))
                    loose = loose or not _LIST.match(lines[j])
                    i = j
                    continue
                if j < n and (nxt := _LIST.match(lines[j])) and len(nxt.group(1)) == base:
                    loose = True
                break
            if _indent(line) >= content_indent:
                item.append(_dedent(line, content_indent))
            elif _LIST.match(line) and _indent(line) <= base:
                break
            elif _LIST.match(line):
                item.append(_dedent(line, content_indent))
            elif not _starts_block(line) and item[-1].strip():
                item.append(line.strip())
            else:
                break
            i += 1
        items.append(item)
        if i < n and not lines[i].strip():
            j = i
            while j < n and not lines[j].strip():
                j += 1
            nxt = _LIST.match(lines[j]) if j < n else None
            if nxt and len(nxt.group(1)) == base and nxt.group(2)[0].isdigit() == ordered:
                loose = True
                i = j
    tag = "ol" if ordered else "ul"
    attr = f' start="{start}"' if ordered and start != 1 else ""
    rendered = "".join(f"<li>{blocks(item, link, tight=not loose)}</li>" for item in items)
    out.append(f"<{tag}{attr}>{rendered}</{tag}>")
    return i


def render(text: str, link: LinkFn) -> str:
    """Render Markdown (frontmatter already removed) to HTML."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return blocks(text.replace("\t", "    ").split("\n"), link)
