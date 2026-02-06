import pandas as pd
import altair as alt

# Load CSV
penguins = pd.read_csv("penglings.csv")

# Create scatter plot
chart = (
    alt.Chart(penguins)
    .mark_circle(opacity=0.8)
    .encode(
        x=alt.X(
            "flipper_length_mm:Q",
            title="Flipper Length (mm)",
            scale=alt.Scale(domain=[170, 235])
        ),
        y=alt.Y(
            "body_mass_g:Q",
            title="Body Mass (g)",
            scale=alt.Scale(domain=[2550, 6400])
        ),
        color=alt.Color(
            "species:N",
            title="species",
            scale=alt.Scale(
                domain=["Adelie", "Chinstrap", "Gentoo"],
                range=["#F28E2B", "#8E63CE", "#1B9E9E"]
            )
        ),
        size=alt.Size(
            "bill_length_mm:Q",
            title="bill_length_mm",
            scale=alt.Scale(range=[40, 400]),  # circle size
            legend=alt.Legend(
                values=[40, 50],
                title="Bill length (mm)"
            )
        )
    )
    .properties(
        width=650,
        height=400
    )
)

chart
chart.save("altair_scatterplot.html")

