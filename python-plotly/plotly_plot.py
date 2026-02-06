import pandas as pd
import plotly.express as px
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
csv_path = ROOT / "penglings.csv"

df = pd.read_csv(csv_path)
df = df.replace("NA", pd.NA)

for col in ["bill_length_mm", "flipper_length_mm", "body_mass_g"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["species", "bill_length_mm", "flipper_length_mm", "body_mass_g"])

# Match d3 ordering + colors exactly
domain_order = ["Adelie", "Chinstrap", "Gentoo"]
palette_map = {
    "Adelie": "#F28E2B",
    "Chinstrap": "#8F63B8",
    "Gentoo": "#2CA7A0",
}

# Plotly marker sizing controls (AREA-based)
desired_max_marker_px = 24  # tweak 20-28 if needed
max_bill = float(df["bill_length_mm"].max())
sizeref = (2.0 * max_bill) / (desired_max_marker_px**2)

fig = px.scatter(
    df,
    x="flipper_length_mm",
    y="body_mass_g",
    color="species",
    size="bill_length_mm",
    opacity=0.8,
    category_orders={"species": domain_order},
    color_discrete_map=palette_map,
    hover_data=["species", "flipper_length_mm", "body_mass_g", "bill_length_mm"],
    labels={
        "flipper_length_mm": "Flipper Length (mm)",
        "body_mass_g": "Body Mass (g)",
        "bill_length_mm": "Bill length (mm)",
    },
)

# Axes / ticks / grids
fig.update_xaxes(rangemode="normal", showgrid=True, ticks="outside", zeroline=False)
fig.update_yaxes(rangemode="normal", showgrid=True, ticks="outside", zeroline=False)

# Marker styling + sizing
fig.update_traces(
    marker=dict(
        sizemode="area",
        sizeref=sizeref,
        sizemin=3,
        line=dict(width=1, color="white"),
    )
)

# Size similar to d3 screenshot
fig.update_layout(
    autosize=False,
    width=960,
    height=560,
    margin=dict(l=90, r=190, t=30, b=70),
    plot_bgcolor="#ffffff",
    paper_bgcolor="#ffffff",
    legend_title_text="species",
)

# Precompute explicit y-axis ranges so toggling is reliable (no stuck autorange)
y_min = float(df["body_mass_g"].min())
y_max = float(df["body_mass_g"].max())
y_pad = 100  # mirrors d3-ish padding
y_range_normal = [y_min - y_pad, y_max + y_pad]
y_range_down = [y_max + y_pad, y_min - y_pad]

plot_div = fig.to_html(
    include_plotlyjs="cdn",
    full_html=False,
    config={"responsive": True, "displaylogo": False},
)

html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Plotly — Penguins bubble scatter</title>
  <style>
    body {{
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
      margin: 24px;
      color: #111;
    }}
    h1 {{
      margin: 0 0 12px 0;
      font-size: 44px;
      font-weight: 800;
      letter-spacing: -0.02em;
    }}
    .controls {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin: 8px 0 12px 0;
      font-size: 16px;
    }}
    .controls label {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      user-select: none;
    }}
    .note {{
      margin-top: 10px;
      color: #666;
      font-size: 14px;
    }}
  </style>
</head>
<body>
  <h1>Plotly — Penguins bubble scatter</h1>

  <div class="controls">
    <label>
      <input id="downwardToggle" type="checkbox" />
      Data downward (optional)
    </label>
  </div>

  {plot_div}

  <div class="note">
    Default view matches the reference plot (upward trend). Check “Data downward” to flip the y-axis screen direction.
  </div>

  <script>
    const plotDiv = document.querySelector('.plotly-graph-div');
    const toggle = document.getElementById('downwardToggle');

    const yNormal = {y_range_normal};
    const yDown = {y_range_down};

    function applyDownward(isDownward) {{
      if (!plotDiv) return;

      Plotly.relayout(plotDiv, {{
        'yaxis.autorange': false,
        'yaxis.range': isDownward ? yDown : yNormal,
        'yaxis.title.text': isDownward ? 'Body Mass (g) (increases downward)' : 'Body Mass (g)'
      }});
    }}

    toggle.addEventListener('change', (e) => {{
      applyDownward(e.target.checked);
    }});

    // Force default to reference-matching on load
    applyDownward(false);
  </script>
</body>
</html>
"""

out = Path(__file__).with_name("plotly.html")
out.write_text(html, encoding="utf-8")
print(f"Wrote {out}")