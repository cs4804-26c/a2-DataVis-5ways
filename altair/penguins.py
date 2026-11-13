import altair as alt
import pandas as pd

df = pd.read_csv("../penglings.csv")

chart = (
    alt.Chart(df)
    .mark_circle(opacity=0.8)
    .encode(
        x=alt.X("flipper_length_mm:Q", title="Flipper Length (mm)",
                scale=alt.Scale(zero=False), axis=alt.Axis(tickMinStep=10)),
        y=alt.Y("body_mass_g:Q", title="Body Mass (g)",
                scale=alt.Scale(zero=False)),
        color=alt.Color("species:N", scale=alt.Scale(
            domain=["Adelie", "Chinstrap", "Gentoo"],
            range=["#ff8c00", "#a020f0", "#008b8b"])),
        size=alt.Size("bill_length_mm:Q", title="bill_length_mm",
                      scale=alt.Scale(zero=False, range=[20, 250])),
        tooltip=["species", "island", "bill_length_mm",
                 "flipper_length_mm", "body_mass_g"],
    )
    .properties(width=600, height=400)
    .interactive()
)

chart.save("penguins.html")
chart.save("../img/altair.png", scale_factor=2)
