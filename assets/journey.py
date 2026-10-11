#!/usr/bin/env python3
"""Build the journey run: a figure that runs across my timeline, self-playing.

Standard library only. Run:  python3 journey.py
Writes journey.svg (light) and journey-dark.svg. CSS animation only, no input.
Milestones are real, from the public repositories. Edit and re-run.
"""
import os

# year, label  (checked against the public history)
STOPS = [
    ("2021", "coursework, IoT, first web apps"),
    ("2022", "browser video call"),
    ("2024", "first npm packages"),
    ("2025", "seekly on PyPI, ML"),
    ("2026", "agents, product work"),
]
W, H = 900, 210
LOOP = 12  # seconds
THEMES = {
    "light": dict(INK="#191B19", MUTED="#6B6D71", ACCENT="#087653", RULE="#E4E2DC", BG="#FAF9F6", GROUND="#C7D3CB"),
    "dark":  dict(INK="#E6EDF3", MUTED="#9BA5AF", ACCENT="#46B57D", RULE="#30363D", BG="#0D1117", GROUND="#2A3A31"),
}
MONO = 'ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace'
SANS = '"Helvetica Neue", Helvetica, Arial, "Liberation Sans", sans-serif'
SERIF = 'Georgia, "Times New Roman", "Liberation Serif", serif'


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def run(t):
    gy = 150                      # ground line
    x0, x1 = 60, W - 70
    n = len(STOPS)
    xs = [x0 + (x1 - x0) * i / (n - 1) for i in range(n)]
    o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="jt jd">')
    o.append('<title id="jt">A figure running across Dhodraj Sundaram\'s timeline</title>')
    o.append(f'<desc id="jd">A self-playing side-scroller. A small figure runs left to right along a ground line '
             f'past dated milestones from the public history: {"; ".join(f"{y} {esc(l)}" for y,l in STOPS)}.</desc>')
    o.append('<style>')
    # runner crosses from first to last stop and loops; legs alternate; milestones light up as it passes
    o.append(f'.runner{{animation:runx {LOOP}s linear infinite}}')
    o.append(f'@keyframes runx{{from{{transform:translateX({xs[0]-30:.0f}px)}}to{{transform:translateX({xs[-1]-30:.0f}px)}}}}')
    o.append('.legA{animation:legA .28s steps(1) infinite}.legB{animation:legB .28s steps(1) infinite}')
    o.append('@keyframes legA{50%{opacity:0}}@keyframes legB{0%,50%{opacity:0}50.01%{opacity:1}}')
    o.append('.bob{animation:bob .28s ease-in-out infinite}@keyframes bob{50%{transform:translateY(-3px)}}')
    for i in range(n):
        frac = (xs[i] - xs[0]) / (xs[-1] - xs[0]) if xs[-1] != xs[0] else 0
        pct = max(0.1, frac * 100)
        o.append(f'.lit{i}{{animation:lit{i} {LOOP}s linear infinite}}'
                 f'@keyframes lit{i}{{0%,{pct-0.1:.1f}%{{opacity:.35}}{pct:.1f}%,100%{{opacity:1}}}}')
    o.append('@media (prefers-reduced-motion:reduce){.runner,.legA,.legB,.bob,'
             + ",".join(f".lit{i}" for i in range(n)) + '{animation:none}}')
    o.append('</style>')
    o.append(f'<rect width="{W}" height="{H}" fill="{t["BG"]}"/>')
    o.append(f'<rect x="12" y="12" width="{W-24}" height="{H-24}" fill="none" stroke="{t["RULE"]}"/>')
    o.append(f'<text x="34" y="44" font-family=\'{MONO}\' font-size="11" letter-spacing="2.2" fill="{t["ACCENT"]}">THE RUN SO FAR</text>')
    o.append(f'<text x="34" y="70" font-family=\'{SERIF}\' font-size="20" fill="{t["INK"]}">From coursework to agents.</text>')
    # ground
    o.append(f'<line x1="{x0-16}" y1="{gy}" x2="{x1}" y2="{gy}" stroke="{t["GROUND"]}" stroke-width="2"/>')
    # milestones
    for i, (yr, lab) in enumerate(STOPS):
        x = xs[i]
        o.append(f'<g class="lit{i}">')
        o.append(f'<line x1="{x:.0f}" y1="{gy}" x2="{x:.0f}" y2="{gy-26}" stroke="{t["ACCENT"]}" stroke-width="1.4"/>')
        o.append(f'<rect x="{x:.0f}" y="{gy-32}" width="13" height="10" fill="{t["ACCENT"]}"/>')
        anc = ' text-anchor="end"' if i == n - 1 else ''
        tx = x + 13 if i == n - 1 else x
        o.append(f'<text x="{tx:.0f}" y="{gy+20}"{anc} font-family=\'{MONO}\' font-size="12" font-weight="600" fill="{t["INK"]}">{yr}</text>')
        o.append(f'<text x="{tx:.0f}" y="{gy+36}"{anc} font-family=\'{SANS}\' font-size="10.5" fill="{t["MUTED"]}">{esc(lab)}</text>')
        o.append('</g>')
    # runner (two leg frames, a little bob)
    o.append('<g class="runner">')
    o.append('<g class="bob">')
    c = t["INK"]
    o.append(f'<rect x="{-4}" y="{gy-30}" width="9" height="9" fill="{c}"/>')          # head
    o.append(f'<rect x="{-3}" y="{gy-20}" width="7" height="13" fill="{c}"/>')          # body
    o.append(f'<line class="legA" x1="0" y1="{gy-8}" x2="-5" y2="{gy}" stroke="{c}" stroke-width="2.4"/>')
    o.append(f'<line class="legA" x1="1" y1="{gy-8}" x2="7" y2="{gy}" stroke="{c}" stroke-width="2.4"/>')
    o.append(f'<line class="legB" x1="0" y1="{gy-8}" x2="1" y2="{gy}" stroke="{c}" stroke-width="2.4"/>')
    o.append(f'<line class="legB" x1="1" y1="{gy-8}" x2="2" y2="{gy}" stroke="{c}" stroke-width="2.4"/>')
    o.append(f'<line x1="2" y1="{gy-18}" x2="9" y2="{gy-14}" stroke="{c}" stroke-width="2.2"/>')  # arm
    o.append('</g></g>')
    o.append('</svg>')
    return "\n".join(o)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    for name, fn in (("light", "journey.svg"), ("dark", "journey-dark.svg")):
        with open(os.path.join(here, fn), "w") as f:
            f.write(run(THEMES[name]))
        print("wrote", fn)
