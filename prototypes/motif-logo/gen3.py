import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen
from gen import AC, INK, GREY
OUT = sys.argv[1]
SW = 4.5
def mark(end):  # end: 51 = s'arrête dans la tuile ; 70 = sort par le bord (rogné)
    def m(fg, bg, ac):
        return (f'<rect width="64" height="64" rx="14" fill="{fg}"></rect>'
          f'<path d="M13 42 C22 42 26 22 35 22 L51 22" fill="none" stroke="{bg}" stroke-width="{SW}" stroke-linecap="round"></path>'
          f'<path d="M13 22 C22 22 26 42 35 42 L51 42" fill="none" stroke="{bg}" stroke-width="{SW}" stroke-linecap="round"></path>'
          f'<path d="M13 32 L{end} 32" fill="none" stroke="{ac}" stroke-width="{SW}" stroke-linecap="round"></path>')
    return m
def make_lockup(continuous, rule_em):
    def lk(m, size, fg, bg, ac, name_px, base_px, base_col, label=None):
        g = round(size*0.25); sw = SW/64*size
        rule_col = fg if ac == bg else ac
        text_x = size + g
        rule_x = size if continuous else text_x
        rule_w = text_x + rule_em*name_px - rule_x
        w = text_x + round(name_px*7.6)
        gv = max(3, round(size*0.09))
        a = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
        inner = m(fg, bg, ac)
        return f'''<div style="position: relative; width: {w}px; height: {size}px; flex-shrink: 0">
<svg width="{size}" height="{size}" viewBox="0 0 64 64" {a} style="position: absolute; left: 0; top: 0">{inner}</svg>
<span style="position: absolute; left: {rule_x}px; top: {size/2 - sw/2:.2f}px; width: {rule_w:.1f}px; height: {sw:.2f}px; border-radius: 0 {sw:.2f}px {sw:.2f}px 0; background: {rule_col}"></span>
<span style="position: absolute; left: {text_x}px; bottom: {size/2 + gv:.1f}px; font-family: 'Space Grotesk', sans-serif; font-weight: 600; font-size: {name_px}px; letter-spacing: -0.02em; color: {fg}; line-height: 1; white-space: nowrap">Henri Touchard</span>
<span style="position: absolute; left: {text_x}px; top: {size/2 + gv:.1f}px; font-size: {base_px}px; color: {base_col}; line-height: 1; white-space: nowrap">Optimisation opérationnelle</span>
</div>'''
    return lk
fav = lambda m: (lambda size: m(INK, "#FFFFFF", AC))
V = [
 ("BancFiletA.dc.html", "Filet détaché, moitié de Henri", mark(51), make_lockup(False, 1.3)),
 ("BancFiletB.dc.html", "Filet sorti de la tuile, moitié de Henri", mark(70), make_lockup(True, 1.3)),
 ("BancFiletC.dc.html", "Filet sorti de la tuile, tout Henri", mark(70), make_lockup(True, 2.55)),
]
for f, t, m, lk in V:
    favm = mark(51)
    open(os.path.join(OUT, f), "w").write(gen.bench(t, m, fav(favm), tile=True, lk=lk))
print("ok")
