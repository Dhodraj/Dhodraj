#!/usr/bin/env python3
"""Build the character card: me as a game class sheet.

Standard library only. Run:  python3 character-card.py
Writes character-card.svg (light) and character-card-dark.svg.
Bars count public work in each area. They are not a skill rating.
Edit the data below, then re-run.
"""
import os

NAME_1, NAME_2 = "DHODRAJ", "SUNDARAM"
CLASS = "ENGINEER / TECH LEAD"
METHOD = "first principles"

# domain, built, total  (built = areas with public work behind them)
LOADOUT = [
    ("Reasoning",     5, 5),
    ("Systems",       1, 5),
    ("Tools and AI",  3, 4),
    ("Product",       3, 3),
    ("Learning",      2, 3),
    ("Open source",   2, 2),
]
# honest, checked facts
VITALS = [
    ("public repos", "26"),
    ("packages",     "3  (pypi 1, npm 2)"),
    ("languages",    "Python / TypeScript / JS"),
    ("since",        "2021"),
]
ITEMS = ["colony", "seekly", "collectweak", "deep-freeze-utility",
         "pmos-companion", "hunt-mode", "medroute", "therionis"]

W, H = 860, 600
THEMES = {
    "light": dict(INK="#191B19", MUTED="#6B6D71", ACCENT="#087653", SAGE="#DDECE3",
                  RULE="#E4E2DC", BG="#FAF9F6", SLOT="#E4E2DC"),
    "dark":  dict(INK="#E6EDF3", MUTED="#9BA5AF", ACCENT="#46B57D", SAGE="#15281E",
                  RULE="#30363D", BG="#0D1117", SLOT="#30363D"),
}
SANS = '"Helvetica Neue", Helvetica, Arial, "Liberation Sans", sans-serif'
MONO = 'ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace'
SERIF = 'Georgia, "Times New Roman", "Liberation Serif", serif'


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def card(t):
    o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="ct cd">')
    o.append('<title id="ct">Dhodraj Sundaram as a game class card</title>')
    loadout = "; ".join(f"{d} {b} of {tot}" for d, b, tot in LOADOUT)
    o.append(f'<desc id="cd">A character card in a terminal style. Name {NAME_1} {NAME_2}, class {esc(CLASS)}, '
             f'method {METHOD}. Loadout bars count public work per area, not skill: {esc(loadout)}. '
             f'Vitals: {", ".join(f"{k} {v}" for k,v in VITALS)}. Inventory: {", ".join(ITEMS)}.</desc>')
    o.append('<style>')
    o.append('.blink{animation:bl 1.1s steps(1) infinite}@keyframes bl{50%{opacity:0}}')
    o.append('.fillin{animation:fi .5s ease-out both}@keyframes fi{from{opacity:0;transform:scale(.4)}to{opacity:1;transform:scale(1)}}')
    o.append('@media (prefers-reduced-motion:reduce){.blink,.fillin{animation:none}}')
    o.append('</style>')
    o.append(f'<rect width="{W}" height="{H}" fill="{t["BG"]}"/>')
    o.append(f'<rect x="14" y="14" width="{W-28}" height="{H-28}" fill="none" stroke="{t["RULE"]}"/>')
    for x, y in ((26, 26), (W-26, 26), (26, H-26), (W-26, H-26)):
        o.append(f'<path d="M{x-7} {y}H{x+7}M{x} {y-7}V{y+7}" stroke="{t["ACCENT"]}" stroke-width="1.2"/>')
    # masthead
    o.append(f'<rect x="40" y="42" width="8" height="8" fill="{t["ACCENT"]}"/>')
    o.append(f'<text class="m" x="56" y="50" font-family=\'{MONO}\' font-size="11" letter-spacing="2.4" fill="{t["ACCENT"]}">CHARACTER CARD</text>')
    o.append(f'<text x="38" y="100" font-family=\'{SERIF}\' font-size="42" fill="{t["INK"]}">{NAME_1}</text>')
    o.append(f'<text x="38" y="140" font-family=\'{SERIF}\' font-size="42" fill="{t["INK"]}">{NAME_2}</text>')
    o.append(f'<text x="42" y="168" font-family=\'{MONO}\' font-size="11.5" letter-spacing="1.4" fill="{t["MUTED"]}">CLASS   <tspan fill="{t["INK"]}">{esc(CLASS)}</tspan></text>')
    o.append(f'<text x="42" y="186" font-family=\'{MONO}\' font-size="11.5" letter-spacing="1.4" fill="{t["MUTED"]}">METHOD  <tspan fill="{t["INK"]}">{METHOD}</tspan><tspan class="blink" fill="{t["ACCENT"]}">_</tspan></text>')
    o.append(f'<line x1="38" y1="206" x2="{W-38}" y2="206" stroke="{t["INK"]}" stroke-width="1.3"/>')
    o.append(f'<line x1="38" y1="210" x2="{W-38}" y2="210" stroke="{t["RULE"]}"/>')
    # loadout (left)
    lx, ly = 40, 244
    o.append(f'<text x="{lx}" y="{ly}" font-family=\'{MONO}\' font-size="11" letter-spacing="2" fill="{t["ACCENT"]}">LOADOUT</text>')
    y = ly + 28
    for d, b, tot in LOADOUT:
        o.append(f'<text x="{lx}" y="{y}" font-family=\'{SANS}\' font-size="15" fill="{t["INK"]}">{esc(d)}</text>')
        bx = lx + 190
        for i in range(tot):
            fill = t["ACCENT"] if i < b else t["BG"]
            stroke = "" if i < b else f' stroke="{t["SLOT"]}" stroke-width="1.4"'
            cls = ' class="fillin"' if i < b else ''
            dly = f' style="transform-box:fill-box;transform-origin:center;animation-delay:{0.2 + (y-ly)*0.004 + i*0.08:.2f}s"' if i < b else ''
            o.append(f'<rect{cls}{dly} x="{bx + i*22}" y="{y-13}" width="15" height="15" fill="{fill}"{stroke}/>')
        o.append(f'<text x="{bx + tot*22 + 10}" y="{y}" font-family=\'{MONO}\' font-size="11" fill="{t["MUTED"]}">{b}/{tot}</text>')
        y += 30
    o.append(f'<text x="{lx}" y="{y+4}" font-family=\'{MONO}\' font-size="10" fill="{t["MUTED"]}">bars = public work in each area, not a skill rating</text>')
    # vitals (right)
    vx = 560
    o.append(f'<line x1="{vx-24}" y1="228" x2="{vx-24}" y2="452" stroke="{t["RULE"]}"/>')
    o.append(f'<text x="{vx}" y="{ly}" font-family=\'{MONO}\' font-size="11" letter-spacing="2" fill="{t["ACCENT"]}">VITALS</text>')
    vy = ly + 28
    for k, v in VITALS:
        o.append(f'<text x="{vx}" y="{vy}" font-family=\'{MONO}\' font-size="11.5" fill="{t["MUTED"]}">{k}</text>')
        o.append(f'<text x="{vx}" y="{vy+17}" font-family=\'{SANS}\' font-size="15" fill="{t["INK"]}">{esc(v)}</text>')
        vy += 46
    # inventory (bottom)
    iy = 498
    o.append(f'<line x1="38" y1="{iy-24}" x2="{W-38}" y2="{iy-24}" stroke="{t["RULE"]}"/>')
    o.append(f'<text x="40" y="{iy}" font-family=\'{MONO}\' font-size="11" letter-spacing="2" fill="{t["ACCENT"]}">INVENTORY</text>')
    cx = 40
    cyy = iy + 22
    for it in ITEMS:
        wch = 14 + len(it) * 7.4
        if cx + wch > W - 40:
            cx = 40; cyy += 32
        o.append(f'<rect x="{cx}" y="{cyy-15}" width="{wch:.0f}" height="22" fill="{t["BG"]}" stroke="{t["RULE"]}"/>')
        o.append(f'<rect x="{cx}" y="{cyy-15}" width="3" height="22" fill="{t["ACCENT"]}"/>')
        o.append(f'<text x="{cx+11}" y="{cyy}" font-family=\'{MONO}\' font-size="11.5" fill="{t["INK"]}">{esc(it)}</text>')
        cx += wch + 10
    o.append('</svg>')
    return "\n".join(o)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    for name, fn in (("light", "character-card.svg"), ("dark", "character-card-dark.svg")):
        with open(os.path.join(here, fn), "w") as f:
            f.write(card(THEMES[name]))
        print("wrote", fn)
