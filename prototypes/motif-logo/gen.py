import math, random, sys, os
OUT = sys.argv[1] if len(sys.argv)>1 else '.'
INK, GREY, AC = "#101418", "#5B616E", "{{accent}}"
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&amp;family=Space+Grotesk:wght@500;600&amp;family=IBM+Plex+Mono:wght@400&amp;display=swap">'

def page(title, w, h, body):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>
body{{margin:0}}
</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"accent":{{"editor":"color","default":"#F0503C","options":["#F0503C","#C7362A","#101418"]}},"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{ accent: this.props.accent ?? '#F0503C' }};
}}
}}
</script>
</body>
</html>
'''

def catmull(pts):
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(len(pts)-1):
        p0 = pts[i-1] if i else pts[i]; p1, p2 = pts[i], pts[i+1]
        p3 = pts[i+2] if i+2 < len(pts) else p2
        c1 = (p1[0]+(p2[0]-p0[0])/6, p1[1]+(p2[1]-p0[1])/6)
        c2 = (p2[0]-(p3[0]-p1[0])/6, p2[1]-(p3[1]-p1[1])/6)
        d += f" C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}"
    return d

W, H = 880, 360
def motif_faisceau():
    random.seed(7)
    n = 11; tg = [72 + i*22 for i in range(n)]
    st = tg[:]; random.shuffle(st)
    paths = []
    for i in range(n):
        pts = []
        for x in range(-20, 560, 60):
            d = max(0.0, 1 - x/520) ** 1.6
            y = tg[i] + (st[i]-tg[i])*d + random.uniform(-26, 26)*d
            pts.append((x, y))
        pts.append((900, tg[i]))
        col, sw = (AC, 3.5) if i == 5 else (INK, 2)
        paths.append(f'<path d="{catmull(pts)}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"></path>')
    return "\n".join(paths)

def motif_points():
    random.seed(3)
    out = []
    for r in range(9):
        y0 = 60 + r*30
        for c in range(42):
            x0 = 30 + c*20
            d = max(0.0, 1 - x0/560) ** 1.4
            x = x0 + random.uniform(-14, 14)*d
            y = y0 + random.uniform(-70, 70)*d
            col = AC if r == 4 else INK
            rad = 3.4 if r == 4 else 2.6
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rad}" fill="{col}"></circle>')
    return "\n".join(out)

def motif_fil():
    pts = []
    s = 30.0
    while s <= 900:
        A = 34 * max(0.0, 1 - s/580) ** 1.2
        w = 0.085
        x = s - A*math.sin(w*s)*1.0
        y = 180 - A*math.cos(w*s)
        pts.append((x, y)); s += 1.5
    split = next(i for i, p in enumerate(pts) if p[0] > 600)
    a = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts[:split+1])
    b = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts[split:])
    return (f'<path d="{a}" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path>\n'
            f'<path d="{b}" fill="none" stroke="{AC}" stroke-width="3.5" stroke-linecap="round"></path>')

def motif_board(title, label, svg):
    body = f'''<div style="width: {W}px; height: {H}px; background: #FFFFFF; overflow: hidden">
<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">
{svg}
</svg>
</div>'''
    return page(title, W, H, body)

# ---------- marks (viewBox 0 0 64 64): fg = trait principal, bg = fond sous la marque, ac = accent
def m_tuile(fg, bg, ac):
    return (f'<rect width="64" height="64" rx="14" fill="{fg}"></rect>'
            f'<text x="31" y="43" text-anchor="middle" font-family="Space Grotesk, sans-serif" font-weight="600" font-size="32" letter-spacing="-1.3" fill="{bg}">ht</text>'
            f'<rect x="46" y="46" width="8" height="8" rx="2" fill="{ac}"></rect>')
def m_fil(fg, bg, ac):
    return (f'<path d="M6 42 C16 42 26 34 26 24 C26 16 16 16 16 24 C16 32 24 34 34 34" fill="none" stroke="{fg}" stroke-width="5" stroke-linecap="round"></path>'
            f'<path d="M34 34 L50 34" fill="none" stroke="{ac}" stroke-width="5" stroke-linecap="round"></path>'
            f'<circle cx="56" cy="34" r="4.5" fill="{ac}"></circle>')
def m_faisceau(fg, bg, ac):
    return (f'<path d="M6 46 C18 46 22 20 34 20 L58 20" fill="none" stroke="{fg}" stroke-width="5" stroke-linecap="round"></path>'
            f'<path d="M6 18 C18 18 22 44 34 44 L58 44" fill="none" stroke="{fg}" stroke-width="5" stroke-linecap="round"></path>'
            f'<path d="M6 32 C11 24 16 40 22 32 C26 27 29 32 34 32 L50 32" fill="none" stroke="{ac}" stroke-width="5" stroke-linecap="round"></path>'
            f'<circle cx="56.5" cy="32" r="4" fill="{ac}"></circle>')
def m_tuile_trait(fg, bg, ac):
    return (f'<rect width="64" height="64" rx="14" fill="{fg}"></rect>'
            f'<text x="32" y="36" text-anchor="middle" font-family="Space Grotesk, sans-serif" font-weight="600" font-size="28" letter-spacing="-1.1" fill="{bg}">ht</text>'
            f'<path d="M11 48 C14 43 17 53 20 48 C23 43 26 50 28 48" fill="none" stroke="{bg}" stroke-width="3" stroke-linecap="round" opacity="0.7"></path>'
            f'<path d="M28 48 L53 48" fill="none" stroke="{ac}" stroke-width="3.5" stroke-linecap="round"></path>')

def fav_tile_h(size):
    fs = 34 if size <= 16 else 30
    txt = "h" if size <= 16 else "ht"
    return (f'<rect width="64" height="64" rx="14" fill="{AC}"></rect>'
            f'<text x="32" y="{44 if size<=16 else 42}" text-anchor="middle" font-family="Space Grotesk, sans-serif" font-weight="600" font-size="{44 if size<=16 else fs}" letter-spacing="-1.2" fill="#FFFFFF">{txt}</text>')
def fav_line(mark):
    def f(size):
        return f'<rect width="64" height="64" rx="14" fill="#FFFFFF"></rect><g transform="translate(4 4) scale(0.875)">{mark(INK, "#FFFFFF", AC)}</g>'
    return f

def svg(size, inner, label=None):
    a = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" {a}>{inner}</svg>'

def lockup(mark, size, fg, bg, ac, name_px, base_px, base_col, label=None):
    return f'''<div style="display: flex; align-items: center; gap: {round(size*0.25)}px">
{svg(size, mark(fg, bg, ac), label)}
<div style="display: flex; flex-direction: column; gap: {max(2, round(base_px*0.3))}px">
<span style="font-family: 'Space Grotesk', sans-serif; font-weight: 600; font-size: {name_px}px; letter-spacing: -0.02em; color: {fg}; line-height: 1.1">Henri Touchard</span>
<span style="font-size: {base_px}px; color: {base_col}; line-height: 1.2">Optimisation opérationnelle</span>
</div>
</div>'''

def cap(t, col=GREY):
    return f'<span style="font-family: \'IBM Plex Mono\', monospace; font-size: 11px; letter-spacing: 0.04em; text-transform: uppercase; color: {col}">{t}</span>'

def bench(title, mark, fav, tile=False):
    BW, BH = 880, 560
    body = f'''<div style="width: {BW}px; height: {BH}px; display: flex; flex-direction: column; background: #FFFFFF; color: {INK}; font-family: 'IBM Plex Sans', sans-serif">
<div style="height: 250px; box-sizing: border-box; padding: 0 48px; display: flex; align-items: center; justify-content: space-between; gap: 32px">
<div style="display: flex; flex-direction: column; gap: 16px">
{cap("Complète")}
{lockup(mark, 88, INK, "#FFFFFF", AC, 34, 15, GREY, "Logo " + title)}
</div>
<div style="display: flex; flex-direction: column; gap: 14px">
{cap("Monochrome")}
{lockup(mark, 44, INK, "#FFFFFF", "#FFFFFF" if tile else INK, 18, 10, INK)}
<div style="padding: 10px 12px; background: {INK}; border-radius: 6px">
{lockup(mark, 44, "#FFFFFF", INK, INK if tile else "#FFFFFF", 18, 10, "#FFFFFF")}
</div>
</div>
</div>
<div style="flex-grow: 1; box-sizing: border-box; padding: 0 48px; background: {INK}; display: flex; align-items: center; justify-content: space-between">
<div style="display: flex; flex-direction: column; gap: 12px; align-items: center">
{svg(72, mark("#FFFFFF", INK, AC), "Marque seule sur fond encre")}
{cap("Marque seule", "#9AA0AA")}
</div>
<div style="display: flex; flex-direction: column; gap: 12px; align-items: center">
<div style="width: 104px; height: 104px; border-radius: 50%; background: #F4F4F2; display: flex; align-items: center; justify-content: center">{svg(60, mark(INK, "#FFFFFF", AC), "Avatar LinkedIn")}</div>
{cap("Avatar", "#9AA0AA")}
</div>
<div style="display: flex; flex-direction: column; gap: 12px; align-items: center">
<div style="display: flex; gap: 14px; align-items: center; padding: 10px 14px; border-radius: 8px; background: #F4F4F2">{svg(32, fav(32), "Favicon 32 px")}{svg(16, fav(16), "Favicon 16 px")}</div>
{cap("Favicon 32 · 16", "#9AA0AA")}
</div>
<div style="display: flex; flex-direction: column; gap: 12px; align-items: center">
<div style="width: 255px; height: 165px; box-sizing: border-box; padding: 20px; border-radius: 6px; background: #FFFFFF; display: flex; flex-direction: column; justify-content: space-between">
{lockup(mark, 36, INK, "#FFFFFF", AC, 15, 8, GREY)}
<span style="font-size: 9px; color: {GREY}">henritouchard.fr</span>
</div>
{cap("Carte · 85 × 55 mm", "#9AA0AA")}
</div>
</div>
</div>'''
    return page(title, BW, BH, body)

if __name__ == '__main__':
 files = {
 "MotifFaisceau.dc.html": motif_board("Motif faisceau", "Des lignes emmêlées qui se rangent en faisceau parallèle", motif_faisceau()),
 "MotifPoints.dc.html": motif_board("Motif points", "Des points épars qui se rangent en grille", motif_points()),
 "MotifFil.dc.html": motif_board("Motif fil", "Un fil qui boucle puis file droit", motif_fil()),
 "BancTuile.dc.html": bench("Tuile monogramme", m_tuile, fav_tile_h),
 "BancFil.dc.html": bench("Fil démêlé", m_fil, fav_line(m_fil)),
 "BancFaisceau.dc.html": bench("Faisceau", m_faisceau, fav_line(m_faisceau)),
 "BancTuileTrait.dc.html": bench("Tuile à trait", m_tuile_trait, fav_tile_h),
}
 os.makedirs(OUT, exist_ok=True)
 for k, v in files.items():
    open(os.path.join(OUT, k), "w").write(v)
 print("ok", list(files))
