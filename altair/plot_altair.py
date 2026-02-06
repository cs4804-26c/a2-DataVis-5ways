import pandas as pd
import altair as alt
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent
CSV_PATH = PROJECT_ROOT / "penglings.csv"

# load data
df = pd.read_csv(CSV_PATH)

needed = ["flipper_length_mm", "body_mass_g", "bill_length_mm", "species"]
df = df.dropna(subset=needed)

# chart
chart = (
    alt.Chart(df)
    .mark_circle(opacity=0.8)
    .encode(
        x=alt.X(
            "flipper_length_mm:Q",
            title="Flipper Length (mm)",
            scale=alt.Scale(zero=False),
        ),
        y=alt.Y(
            "body_mass_g:Q",
            title="Body Mass (g)",
            scale=alt.Scale(zero=False),
        ),
        color=alt.Color(
            "species:N",
            title="Species"
        ),
        size=alt.Size(
            "bill_length_mm:Q",
            title="Bill Length (mm)",
            scale=alt.Scale(range=[30, 500])
        ),
        tooltip=[
            alt.Tooltip("species:N", title="Species"),
            alt.Tooltip("flipper_length_mm:Q", title="Flipper Length (mm)"),
            alt.Tooltip("body_mass_g:Q", title="Body Mass (g)"),
            alt.Tooltip("bill_length_mm:Q", title="Bill Length (mm)"),
        ],
    )
    .properties(
        width=800,
        height=480,
        title="Penguins Flipper length vs Body mass Scatterplot "
    )
)

# some styling
chart = (
    chart
    .configure_view(strokeWidth=0)
    .configure_axis(
        grid=True,
        tickSize=6,
        labelFontSize=12,
        titleFontSize=13,
    )
    .configure_title(fontSize=16)
)

html_out = HERE / "altair_penguins.html"
chart.save(html_out)
print(f"✅ Saved interactive chart: {html_out}")

