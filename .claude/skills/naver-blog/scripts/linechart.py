#!/usr/bin/env python3
"""선 그래프 SVG를 만든다. card.html 의 그래프 블록에 그대로 넣는다.

    python3 linechart.py chart.json > chart.svg

chart.json:
{
  "x": ["1월", "2월", ...],          가로축 이름 (값 개수와 같아야 한다)
  "x_every": 2,                      가로축 이름을 몇 칸마다 적을지 (기본 1)
  "decimals": 2,                     값 라벨 소수 자리 (기본 2)
  "series": [                        선은 두 개까지
    {"name": "가 지표", "values": [...], "hero": true,  "label": [0, 5]},
    {"name": "나 지표", "values": [...], "step": true,  "label": [0, 5]}
  ]
}
hero  주인공 선(짙은 색, 점 표시). 하나만.
step  계단식으로 바뀌는 값(정책금리, 요금 등).
label 값 라벨을 달 지점의 순번(0부터). 선 위쪽에 단다.
values 안의 null 은 그 지점을 비운다.
"""
import json
import math
import sys

W, H = 840, 520
LEFT, RIGHT, TOP, BOTTOM = 76, 128, 36, 64
INK, GRAY, DIM, GRID = "#14171f", "#8a8f98", "#8a8f98", "rgba(23,23,23,0.09)"


def nice_step(span):
    raw = span / 3
    mag = 10 ** math.floor(math.log10(raw)) if raw > 0 else 1
    for m in (1, 2, 2.5, 5, 10):
        if raw <= m * mag:
            return m * mag
    return 10 * mag


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    xs, series = spec["x"], spec["series"]
    dec = spec.get("decimals", 2)
    every = max(1, int(spec.get("x_every", 1)))
    if len(series) > 2:
        sys.exit("선은 두 개까지만 그린다.")
    for s in series:
        if len(s["values"]) != len(xs):
            sys.exit(f"'{s['name']}' 의 값 개수({len(s['values'])})가 가로축 개수({len(xs)})와 다르다.")

    vals = [v for s in series for v in s["values"] if v is not None]
    lo, hi = min(vals), max(vals)
    step = nice_step((hi - lo) or abs(hi) or 1)
    y0 = math.floor(lo / step) * step
    y1 = math.ceil(hi / step) * step
    if y0 == y1:
        y1 = y0 + step
    n = len(xs)
    pw, ph = W - LEFT - RIGHT, H - TOP - BOTTOM

    def X(i):
        return LEFT + (pw * i / (n - 1) if n > 1 else pw / 2)

    def Y(v):
        return TOP + ph * (1 - (v - y0) / (y1 - y0))

    fmt = lambda v: f"{v:,.{dec}f}"
    num = 'style="font-variant-numeric:tabular-nums"'
    out = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" '
           f'style="display:block;font-family:inherit">']

    ticks = int(round((y1 - y0) / step))
    for k in range(ticks + 1):
        g = y0 + step * k
        out.append(f'<line x1="{LEFT}" x2="{W - RIGHT}" y1="{Y(g):.1f}" y2="{Y(g):.1f}" stroke="{GRID}"/>')
        out.append(f'<text x="{LEFT - 14}" y="{Y(g) + 8:.1f}" text-anchor="end" font-size="24" fill="{DIM}" {num}>{fmt(g)}</text>')
    for i, name in enumerate(xs):
        if i % every == 0:
            out.append(f'<text x="{X(i):.1f}" y="{H - BOTTOM + 40}" text-anchor="middle" font-size="24" fill="{DIM}">{name}</text>')

    for s in sorted(series, key=lambda s: bool(s.get("hero"))):  # 주인공 선을 위에 그린다
        hero = bool(s.get("hero"))
        color = INK if hero else GRAY
        pts = [(X(i), Y(v)) for i, v in enumerate(s["values"]) if v is not None]
        if s.get("step"):
            path = []
            for j, (x, y) in enumerate(pts):
                if j:
                    path.append((x, pts[j - 1][1]))
                path.append((x, y))
            pts_draw = path
        else:
            pts_draw = pts
        out.append(f'<polyline fill="none" stroke="{color}" stroke-width="4" stroke-linejoin="round" '
                   f'stroke-linecap="round" points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts_draw)}"/>')
        if hero:
            for x, y in pts:
                out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{INK}" stroke="#fff" stroke-width="2"/>')
        for i in s.get("label", []):
            v = s["values"][i]
            if v is None:
                continue
            dy = -18 if hero else -14
            anchor = "start" if i == 0 else ("end" if i == n - 1 else "middle")
            # 흰 테두리를 둘러 선이나 격자 위에서도 읽히게 한다
            out.append(f'<text x="{X(i):.1f}" y="{Y(v) + dy:.1f}" text-anchor="{anchor}" font-size="26" '
                       f'font-weight="700" fill="{INK if hero else "#6b7078"}" paint-order="stroke" '
                       f'stroke="#fff" stroke-width="7" stroke-linejoin="round" {num}>{fmt(v)}</text>')
        last = [(i, v) for i, v in enumerate(s["values"]) if v is not None][-1]
        out.append(f'<text x="{W - RIGHT + 14}" y="{Y(last[1]) + 8:.1f}" font-size="24" '
                   f'font-weight="{700 if hero else 500}" fill="{INK if hero else "#6b7078"}">{s["name"]}</text>')

    out.append("</svg>")
    print("\n".join(out))


if __name__ == "__main__":
    main()
