import pandas as pd
import altair as alt

FONT_FAMILY = "Source Sans 3"
FONT_LINKS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">"""

penguins = pd.read_csv("penglings.csv")
clean = penguins.dropna(subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"])

hover = alt.selection_point(on="mouseover", clear="mouseout")

chart = (
    alt.Chart(clean)
    .mark_circle(opacity=0.8)
    .encode(
        x=alt.X(
            "flipper_length_mm:Q",
            title="Flipper Length (mm)",
            scale=alt.Scale(domain=[170, 235]),
            axis=alt.Axis(grid=True, tickCount=7, offset=6),
        ),
        y=alt.Y(
            "body_mass_g:Q",
            title="Body Mass (g)",
            scale=alt.Scale(domain=[2600, 6400]),
            axis=alt.Axis(grid=True, values=[3000, 4000, 5000, 6000]),
        ),
        color=alt.Color(
            "species:N",
            title="Species",
            scale=alt.Scale(
                domain=["Adelie", "Chinstrap", "Gentoo"],
                range=["#4E79A7", "#E15759", "#59A14F"],
            ),
        ),
        size=alt.Size(
            "bill_length_mm:Q",
            title="Bill Length (mm)",
            scale=alt.Scale(domain=[40, 50], range=[80, 260], clamp=True),
            legend=alt.Legend(values=[40, 50]),
        ),
        opacity=alt.condition(hover, alt.value(0.9), alt.value(0.2)),
        stroke=alt.condition(hover, alt.value("#333"), alt.value(None)),
        strokeWidth=alt.condition(hover, alt.value(1.2), alt.value(0)),
        tooltip=["species", "bill_length_mm", "flipper_length_mm", "body_mass_g"],
    )
    .properties(width=500, height=350, background="#EBEBEB")
    .add_params(hover)
    .configure_view(stroke=None)
    .configure_axis(
        grid=True,
        gridColor="white",
        gridOpacity=1,
        ticks=True,
        tickSize=6,
        tickWidth=1,
        domainColor="#BDBDBD",
        tickColor="#BDBDBD",
        labelColor="#4D4D4D",
        titleColor="#4D4D4D",
        labelFont=FONT_FAMILY,
        titleFont=FONT_FAMILY,
    )
    .configure_legend(labelFont=FONT_FAMILY, titleFont=FONT_FAMILY)
)

chart.save("python-altair.html")

with open("python-altair.html", "r", encoding="utf-8") as handle:
    html = handle.read()

if "fonts.googleapis.com/css2?family=Source+Sans+3" not in html:
    html = html.replace("</head>", f"{FONT_LINKS}</head>")
    with open("python-altair.html", "w", encoding="utf-8") as handle:
        handle.write(html)
