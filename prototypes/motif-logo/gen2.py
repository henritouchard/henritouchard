import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen
from gen import AC, INK
OUT = sys.argv[1]
def tile(fg, bg, inner): return f'<rect width="64" height="64" rx="14" fill="{fg}"></rect>' + inner
def a(fg, bg, ac):
    return tile(fg, bg, f'<g transform="translate(8 8) scale(0.75)">{gen.m_faisceau(bg, fg, ac)}</g>')
def b(fg, bg, ac):
    return tile(fg, bg,
      f'<path d="M13 42 C22 42 26 22 35 22 L51 22" fill="none" stroke="{bg}" stroke-width="4.5" stroke-linecap="round"></path>'
      f'<path d="M13 22 C22 22 26 42 35 42 L51 42" fill="none" stroke="{bg}" stroke-width="4.5" stroke-linecap="round"></path>'
      f'<path d="M13 32 L44 32" fill="none" stroke="{ac}" stroke-width="4.5" stroke-linecap="round"></path>'
      f'<circle cx="51" cy="32" r="3.4" fill="{ac}"></circle>')
def c(fg, bg, ac):
    return tile(fg, bg,
      f'<path d="M13 14 C24 14 26 23 37 23 L51 23" fill="none" stroke="{bg}" stroke-width="4.5" stroke-linecap="round"></path>'
      f'<path d="M13 50 C24 50 26 41 37 41 L51 41" fill="none" stroke="{bg}" stroke-width="4.5" stroke-linecap="round"></path>'
      f'<path d="M13 32 L44 32" fill="none" stroke="{ac}" stroke-width="4.5" stroke-linecap="round"></path>'
      f'<circle cx="51" cy="32" r="3.4" fill="{ac}"></circle>')
fav = lambda m: (lambda size: m(INK, "#FFFFFF", AC))
files = {
 "BancFaisceauTuileA.dc.html": gen.bench("Faisceau en tuile · ondulé", a, fav(a), tile=True),
 "BancFaisceauTuileB.dc.html": gen.bench("Faisceau en tuile · croisement", b, fav(b), tile=True),
 "BancFaisceauTuileC.dc.html": gen.bench("Faisceau en tuile · convergence", c, fav(c), tile=True),
}
for k, v in files.items(): open(os.path.join(OUT, k), "w").write(v)
print("ok")
