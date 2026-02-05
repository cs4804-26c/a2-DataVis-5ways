import pandas as pd
import altair as alt

df = pd.read_csv("penglings.csv")

df = df.dropna(subset=[
    "species",
    "bill_length_mm",
    "flipper_length_mm",
    "body_mass_g"
])

chart = alt.Chart(df).mark_circle(opacity=0.85).encode(
    x=alt.X(
        "flipper_length_mm:Q",
        title="Flipper Length (mm)",
        scale=alt.Scale(zero=False)
    ),
    y=alt.Y(
        "body_mass_g:Q",
        title="Body Mass (g)",
        scale=alt.Scale(zero=False)
    ),
    size=alt.Size(
        "bill_length_mm:Q",
        title="bill_length_mm",
        scale=alt.Scale(
            range=[50, 500],
            zero=False
        ),
        legend=alt.Legend(values=[40, 50])
    ),
    color=alt.Color(
        "species:N",
        title="species",
        scale=alt.Scale(
            domain=["Adelie", "Chinstrap", "Gentoo"],
            range=["#E28A37", "#7B2CBF", "#00A5A8"]
        )
    ),
    tooltip=[
        alt.Tooltip("bill_length_mm:Q", title="Bill Length (mm)"),
        alt.Tooltip("species:N"),
        alt.Tooltip("flipper_length_mm:Q", title="Flipper Length (mm)"),
        alt.Tooltip("body_mass_g:Q", title="Body Mass (g)")
    ]
).properties(
    width=800,
    height=500
).configure_view(
    fill="#EBEBEB",
    strokeWidth=0
).configure_axis(
    grid=True,
    gridColor="white",
    gridWidth=1.2,
    domain=False,
    tickColor="white",
    labelFontSize=14,
    titleFontSize=16
).configure_legend(
    labelFontSize=14,
    titleFontSize=16
)

chart