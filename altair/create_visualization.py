import altair as alt
import pandas as pd

df = pd.read_csv("./data/penglings.csv").dropna(
    subset=["bill_length_mm", "body_mass_g", "flipper_length_mm", "species"]
)

chart = (
    alt.Chart(df)
    .mark_circle(opacity=0.7)
    .encode(
        x=alt.X(
            "flipper_length_mm:Q",
            title="Flipper Length (mm)",
            scale=alt.Scale(
                domain=[170, 235],
                nice=True
            ),
            axis=alt.Axis(
                tickCount=6,
                grid=True
            )
        ),
        y=alt.Y(
            "body_mass_g:Q",
            title="Body Mass (g)",
            scale=alt.Scale(
                domain=[2500, 6500],
                nice=True
            ),
            axis=alt.Axis(
                tickCount=6,
                grid=True
            )
        ),
        size=alt.Size(
            "bill_length_mm:Q",
            title="Bill Length (mm)",
            scale=alt.Scale(range=[30, 800]),
            legend=alt.Legend(
                orient="right",
                legendY=80,
                titleFontWeight="bold"
            )
        ),
        color=alt.Color(
            "species:N",
            title="Species",
            legend=alt.Legend(
                orient="right",
                legendY=225,
                titleFontWeight="bold"
            )
        ),
        tooltip=[
            alt.Tooltip("species:N", title="Species"),
            alt.Tooltip("flipper_length_mm:Q", title="Flipper (mm)"),
            alt.Tooltip("body_mass_g:Q", title="Body mass (g)"),
            alt.Tooltip("bill_length_mm:Q", title="Bill length (mm)"),
        ],
    )
    .properties(
        title="Penguin Measurements: Flipper Length vs Body Mass",
        width="container",
        height=400,
    )
    .configure_view(stroke=None)
    .configure_axis(
        labelFontSize=11,
        titleFontSize=12,
        gridColor="#e6e6e6",
        gridOpacity=1
    )
    .configure_title(
        fontSize=16,
        fontWeight="bold",
        anchor="middle"
    )
)

chart.save("altair/penguins_altair.html")
