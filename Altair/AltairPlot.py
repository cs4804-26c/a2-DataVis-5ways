import pandas as pd
import altair as alt

df = pd.read_csv("penglings.csv")
df = df.dropna(subset=["flipper_length_mm", "body_mass_g", "bill_length_mm", "species"])

chart = (
    alt.Chart(df)
    .mark_circle(opacity=0.8)
    .encode(
        x=alt.X(
            "flipper_length_mm:Q",
            title="Flipper Length (mm)",
            scale=alt.Scale(zero=False),
            axis=alt.Axis(values=list(range(170, 236, 10)))
        ),
        y=alt.Y(
            "body_mass_g:Q",
            title="Body Mass (g)",
            scale=alt.Scale(zero=False),
            axis=alt.Axis(values=[3000, 4000, 5000, 6000])
        ),
        color=alt.Color(
            "species:N",
            legend=None,
            scale=alt.Scale(
                domain=["Adelie", "Chinstrap", "Gentoo"],
                range=["#F28E2B", "#8E44AD", "#1B9E9E"]
            )
        ),
        size=alt.Size("bill_length_mm:Q", legend=None, scale=alt.Scale(range=[30, 200]))
    )
    .properties(width=900, height=520)
    .configure_axis(grid=False)  # closer to the left image (no grid)
)

chart.save("altair.html")

