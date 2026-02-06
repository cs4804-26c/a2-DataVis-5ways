import json
import pandas as pd
import altair as alt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
csv_path = ROOT / "penglings.csv"

df = pd.read_csv(csv_path)
df = df.replace("NA", pd.NA)

for col in ["bill_length_mm", "flipper_length_mm", "body_mass_g"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["species", "bill_length_mm", "flipper_length_mm", "body_mass_g"])

# Keep ordering & colors consistent across tools
domain_order = ["Adelie", "Chinstrap", "Gentoo"]
palette = ["#F28E2B", "#8F63B8", "#2CA7A0"]

# Bill length domain (used for size scale)
bill_min = float(df["bill_length_mm"].min())
bill_max = float(df["bill_length_mm"].max())

# IMPORTANT:
# Vega-Lite/Altair "size" is AREA (px^2), while your d3 uses radius ~ [3..12].
# To match d3 (and visually match ggplot-style point sizing), set area range ~ [3^2 .. 12^2] = [9..144].
size_range = [20, 500]

base = (
    alt.Chart(df)
    .mark_circle(opacity=0.8)
    .encode(
        x=alt.X(
            "flipper_length_mm:Q",
            title="Flipper Length (mm)",
            scale=alt.Scale(zero=False),
            axis=alt.Axis(tickCount=8),
        ),
        y=alt.Y(
            "body_mass_g:Q",
            title="Body Mass (g)",
            scale=alt.Scale(zero=False),
            axis=alt.Axis(tickCount=8),
        ),
        color=alt.Color(
            "species:N",
            title="species",
            scale=alt.Scale(domain=domain_order, range=palette),
            legend=alt.Legend(title="species"),
        ),
        size=alt.Size(
            "bill_length_mm:Q",
            title="bill_length_mm",
            scale=alt.Scale(domain=[bill_min, bill_max], range=size_range, zero=False),
            # Match the ggplot reference legend vibe (40/50 shown)
            legend=alt.Legend(title="bill_length_mm", values=[40, 50]),
        ),
        tooltip=["species:N", "flipper_length_mm:Q", "body_mass_g:Q", "bill_length_mm:Q"],
    )
    .properties(width=850, height=450)
)

# Default: match reference (upward-trending)
chart_normal = base

# Optional: "data downward" mode (flip the screen mapping for y)
chart_downward = base.encode(
    y=alt.Y(
        "body_mass_g:Q",
        title="Body Mass (g) (increases downward)",
        scale=alt.Scale(zero=False, reverse=True),
        axis=alt.Axis(tickCount=8),
    )
)

spec_normal = chart_normal.to_dict()
spec_down = chart_downward.to_dict()

html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Altair — Penguins bubble scatter</title>

  <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>

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
  <h1>Altair — Penguins bubble scatter</h1>

  <div class="controls">
    <label>
      <input id="downwardToggle" type="checkbox" />
      Data downward (optional)
    </label>
  </div>

  <div id="vis"></div>

  <div class="note">
    Default view matches the reference plot (upward trend). Check “Data downward” to flip the y-axis screen direction.
  </div>

  <script>
    const specNormal = {json.dumps(spec_normal)};
    const specDown = {json.dumps(spec_down)};

    const toggle = document.getElementById('downwardToggle');
    const target = document.getElementById('vis');

    async function render(isDownward) {{
      const spec = isDownward ? specDown : specNormal;
      target.innerHTML = "";
      await vegaEmbed('#vis', spec, {{ actions: true }});
    }}

    toggle.addEventListener('change', (e) => {{
      render(e.target.checked);
    }});

    render(false);
  </script>
</body>
</html>
"""

out = Path(__file__).with_name("altair.html")
out.write_text(html, encoding="utf-8")
print(f"Wrote {out}")