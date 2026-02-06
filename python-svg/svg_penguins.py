import pandas as pd

df = pd.read_csv('../penglings.csv').dropna(subset=['flipper_length_mm','body_mass_g','bill_length_mm','species'])

W, H = 700, 500
m = {'t': 20, 'r': 140, 'b': 50, 'l': 70}
pw, ph = W - m['l'] - m['r'], H - m['t'] - m['b']
xd, yd = (170, 235), (2500, 6500)
colors = {'Adelie': '#E8862A', 'Chinstrap': '#9B59B6', 'Gentoo': '#2E9E8F'}

sx = lambda v: m['l'] + (v - xd[0]) / (xd[1] - xd[0]) * pw
sy = lambda v: m['t'] + ph - (v - yd[0]) / (yd[1] - yd[0]) * ph
sr = lambda v: 3 + (v - 30) / 30 * 12

parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" font-family="sans-serif">']
parts.append(f'<rect x="{m["l"]}" y="{m["t"]}" width="{pw}" height="{ph}" fill="#f5f5f5"/>')

# Grid
for y in range(3000, 6501, 500):
    parts.append(f'<line x1="{m["l"]}" y1="{sy(y):.0f}" x2="{m["l"]+pw}" y2="{sy(y):.0f}" stroke="#ddd"/>')
for x in range(170, 236, 10):
    parts.append(f'<line x1="{sx(x):.0f}" y1="{m["t"]}" x2="{sx(x):.0f}" y2="{m["t"]+ph}" stroke="#ddd"/>')

# Axes + ticks
for x in range(170, 231, 10):
    parts.append(f'<text x="{sx(x):.0f}" y="{m["t"]+ph+20}" text-anchor="middle" font-size="11">{x}</text>')
for y in range(3000, 6501, 500):
    parts.append(f'<text x="{m["l"]-8}" y="{sy(y)+4:.0f}" text-anchor="end" font-size="11">{y:,}</text>')

parts.append(f'<text x="{m["l"]+pw/2}" y="{H-5}" text-anchor="middle" font-size="13">Flipper Length (mm)</text>')
parts.append(f'<text transform="translate(15,{m["t"]+ph/2}) rotate(-90)" text-anchor="middle" font-size="13">Body Mass (g)</text>')

# Circles
for _, r in df.iterrows():
    parts.append(f'<circle cx="{sx(r.flipper_length_mm):.1f}" cy="{sy(r.body_mass_g):.1f}" r="{sr(r.bill_length_mm):.1f}" fill="{colors[r.species]}" opacity="0.8"/>')

# Legend for graph
ly = m['t'] + 20
for sp, c in colors.items():
    parts.append(f'<circle cx="{m["l"]+pw+25}" cy="{ly}" r="7" fill="{c}" opacity="0.8"/>')
    parts.append(f'<text x="{m["l"]+pw+38}" y="{ly+4}" font-size="12">{sp}</text>')
    ly += 25

parts.append('</svg>')
with open('penguins.svg', 'w') as f:
    f.write('\n'.join(parts))
print("Done")
