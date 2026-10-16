#!/usr/bin/env python3
"""Draw progress.svg (the panel at the top of the README) from progress.json.

progress.json holds, for each skill and level, a percentage toward that
level's exam (0-100), plus the level exams passed so far. See CURRICULUM.md,
section "Progress", for how the percentages are set.

Usage: python3 tools/progress.py [--today YYYY-MM-DD]
"""
import datetime as dt
import html
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
LEVELS = ["A1", "A2", "B1"]
SKILLS = [
    # name in progress.json, English label, light colour, dark colour
    ("Lesen", "Reading", "#2a78d6", "#3987e5"),
    ("Hören", "Listening", "#eb6834", "#d95926"),
    ("Schreiben", "Writing", "#1baf7a", "#199e70"),
    ("Sprechen", "Speaking", "#eda100", "#c98500"),
]


def tint(hex_color, amount, base="#fcfcfb"):
    a = [int(hex_color[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(base[i:i + 2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(y + (x - y) * amount) for x, y in zip(a, b))


def esc(s):
    return html.escape(str(s), quote=True)


def plural(n, word):
    return word if n == 1 else word + "s"


def build_svg(data, today):
    W, pad = 880, 24
    start = dt.date.fromisoformat(data["start"])
    goal = dt.date.fromisoformat(data["goal"])
    passed = [lv for lv in LEVELS if data["exams"].get(lv)]
    current = next((lv for lv in LEVELS if lv not in passed), None)
    days_left = max((goal - today).days, 0)

    tiles = [
        ("Working toward", current or "B1 ✓", "" if current else "done"),
        ("Level exams passed", str(len(passed)), f"of {len(LEVELS)}"),
        ("Words in Anki", str(data.get("anki_words", 0)), plural(data.get("anki_words", 0), "word")),
        ("Days to goal", str(days_left), goal.strftime("%-d %b %Y")),
    ]
    if today < start:
        when = f"Starts {start.strftime('%a %-d %b %Y')} · updated {today.strftime('%a %-d %b %Y')}"
    else:
        week = (today - start).days // 7 + 1
        when = f"Week {week} · updated {today.strftime('%a %-d %b %Y')}"

    span_y, top_rows, row_h = 158, 174, 52
    H = top_rows + row_h * len(SKILLS) + 8

    light = "".join(f"--c{i}:{c};--c{i}b:{tint(c, .45)};--c{i}t:{tint(c, .14)};"
                    for i, (_, _, c, _) in enumerate(SKILLS))
    dark = "".join(f"--c{i}:{c};--c{i}b:{tint(c, .62, '#1a1a19')};--c{i}t:{tint(c, .17, '#1a1a19')};"
                   for i, (_, _, _, c) in enumerate(SKILLS))
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
         f'aria-label="German progress: working toward {esc(current or "done")}, {len(passed)} of 3 level exams passed">',
         "<style>",
         f"svg{{--bg:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--mut:#898781;--line:#e1e0d9;--tile:#f4f3f0;{light}}}",
         f"@media (prefers-color-scheme: dark){{svg{{--bg:#1a1a19;--ink:#f0efec;--ink2:#c3c2b7;--mut:#898781;"
         f"--line:#2c2c2a;--tile:#232322;{dark}}}}}",
         "text{font-family:system-ui,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif;fill:var(--ink)}",
         ".h{font-size:17px;font-weight:650}.m{font-size:12px;fill:var(--mut)}.lv{font-size:12px;font-weight:600;fill:var(--ink2)}",
         ".tl{font-size:12px;fill:var(--ink2)}.tv{font-size:26px;font-weight:650}.tu{font-size:12.5px;fill:var(--ink2)}",
         ".tr{font-size:14px;font-weight:600}.cnt{font-size:13px;fill:var(--ink2)}",
         "</style>",
         f'<rect width="{W}" height="{H}" rx="12" fill="var(--bg)" stroke="var(--line)"/>',
         f'<text x="{pad}" y="36" class="h">Progress</text>',
         f'<text x="{W - pad}" y="36" class="m" text-anchor="end">{esc(when)}</text>']

    gap = 12
    tw = (W - 2 * pad - gap * (len(tiles) - 1)) / len(tiles)
    for i, (label, value, unit) in enumerate(tiles):
        x = pad + i * (tw + gap)
        p.append(f'<rect x="{x:.1f}" y="54" width="{tw:.1f}" height="76" rx="8" fill="var(--tile)"/>')
        p.append(f'<text x="{x + 14:.1f}" y="76" class="tl">{esc(label)}</text>')
        p.append(f'<text x="{x + 14:.1f}" y="113" class="tv">{esc(value)}'
                 f'<tspan class="tu" dx="6">{esc(unit)}</tspan></text>')

    # one full-width bar per skill, covering only the current level
    # (A0 -> A1 until the A1 exam is passed, then A1 -> A2, then A2 -> B1)
    prev = LEVELS[LEVELS.index(current) - 1] if current and current != LEVELS[0] else "A0"
    span = f"{prev} → {current}" if current else "B1 reached"
    p.append(f'<text x="{pad}" y="{span_y}" class="lv">{esc(span)}</text>')
    p.append(f'<text x="{W - pad}" y="{span_y}" class="m" text-anchor="end">'
             f'{"100% in all four = ready for the " + current + " exam" if current else "all level exams passed"}</text>')

    bw = W - 2 * pad
    for i, (key, label, _, _) in enumerate(SKILLS):
        y = top_rows + i * row_h
        vals = data["skills"][key]
        pct = max(0, min(100, vals.get(current, 0))) if current else 100
        p.append(f'<text x="{pad}" y="{y + 14}" class="tr">{esc(key)}'
                 f'<tspan class="m" dx="8">{esc(label)}</tspan></text>')
        p.append(f'<text x="{W - pad}" y="{y + 14}" class="cnt" text-anchor="end">{round(pct)}%</text>')
        by = y + 24
        p.append(f'<rect x="{pad}" y="{by}" width="{bw}" height="10" rx="4" fill="var(--c{i}t)"/>')
        if pct:
            p.append(f'<rect x="{pad}" y="{by}" width="{max(bw * pct / 100, 6):.1f}" height="10" '
                     f'rx="4" fill="var(--c{i})"/>')
    p.append("</svg>")
    return "\n".join(p)


def main():
    today = dt.date.today()
    if "--today" in sys.argv:
        today = dt.date.fromisoformat(sys.argv[sys.argv.index("--today") + 1])
    data = json.loads((REPO / "progress.json").read_text(encoding="utf-8"))
    (REPO / "progress.svg").write_text(build_svg(data, today), encoding="utf-8")
    print("progress.svg updated")


if __name__ == "__main__":
    main()
