import pandas as pd
import plotly.express as px

FONT_FAMILY = "Source Sans 3"
FONT_LINKS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">"""
penguins = pd.read_csv("penglings.csv")
clean = penguins.dropna(subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"]).copy()
clean["bill_length_mm_clamped"] = clean["bill_length_mm"].clip(40, 50)
size_max = 26
sizeref = 2.0 * clean["bill_length_mm_clamped"].max() / size_max

fig = px.scatter(
    clean,
    x="flipper_length_mm",
    y="body_mass_g",
    color="species",
    size="bill_length_mm_clamped",
    opacity=0.8,
    size_max=size_max,
    custom_data=["species", "bill_length_mm_clamped"],
    color_discrete_map={
        "Adelie": "#4E79A7",
        "Chinstrap": "#E15759",
        "Gentoo": "#59A14F",
    },
    labels={
        "flipper_length_mm": "Flipper Length (mm)",
        "body_mass_g": "Body Mass (g)",
        "species": "Species",
        "bill_length_mm_clamped": "Bill Length",
    },
)

fig.update_xaxes(
    range=[170, 235],
    showgrid=True,
    dtick=10,
    gridcolor="white",
    showline=True,
    linecolor="#BDBDBD",
    tickcolor="#BDBDBD",
)
fig.update_yaxes(
    range=[2500, 6600],
    showgrid=True,
    dtick=1000,
    tick0=3000,
    gridcolor="white",
    showline=True,
    linecolor="#BDBDBD",
    tickcolor="#BDBDBD",
)
fig.update_layout(
    width=760,
    height=500,
    plot_bgcolor="#EBEBEB",
    paper_bgcolor="white",
    legend={"itemsizing": "trace", "x": 1.02, "xanchor": "left"},
    font={"family": FONT_FAMILY},
    margin=dict(l=80, r=200, t=40, b=60),
)
fig.update_traces(
    marker=dict(sizemode="diameter", sizeref=sizeref, sizemin=2),
)

fig.add_scatter(
    x=[None],
    y=[None],
    mode="markers",
    marker=dict(size=10, color="#4D4D4D", opacity=0.8, sizemode="diameter", sizeref=1),
    legendgroup="size",
    legendgrouptitle_text="Bill Length (mm)    ",
    name="40",
    hoverinfo="skip",
    showlegend=True,
)
fig.add_scatter(
    x=[None],
    y=[None],
    mode="markers",
    marker=dict(size=16, color="#4D4D4D", opacity=0.8, sizemode="diameter", sizeref=1),
    legendgroup="size",
    name="50",
    hoverinfo="skip",
    showlegend=True,
)

fig.write_html(
    "python-plotly.html",
    include_plotlyjs="cdn",
    config={"staticPlot": True},
)

with open("python-plotly.html", "r", encoding="utf-8") as handle:
    html = handle.read()

if "fonts.googleapis.com/css2?family=Source+Sans+3" not in html:
    html = html.replace("</head>", f"{FONT_LINKS}</head>")
    with open("python-plotly.html", "w", encoding="utf-8") as handle:
        handle.write(html)
