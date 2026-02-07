import pandas as pd
import altair as alt

# Load data
df = pd.read_csv("data/penglings.csv")

# Clean rows
df = df.dropna(subset=[
    "flipper_length_mm",
    "body_mass_g",
    "bill_length_mm",
    "species"
])

# Custom colors to match d3/Tableau look
species_colors = {
    "Adelie": "#F28E2B",
    "Chinstrap": "#9C51B6",
    "Gentoo": "#4E9E9A"
}

chart = (
    alt.Chart(df, title="Penguins Scatter (Altair)")
    .mark_circle(opacity=0.8)
    .encode(
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
        color=alt.Color(
            "species:N",
            scale=alt.Scale(
                domain=list(species_colors.keys()),
                range=list(species_colors.values())
            ),
            legend=alt.Legend(title="Species")
        ),
        size=alt.Size(
            "bill_length_mm:Q",
            legend=alt.Legend(title="Bill Length (mm)"),
            scale=alt.Scale(range=[30, 600])   # important for smooth size variation
        ),
        tooltip=[
            "species",
            "flipper_length_mm",
            "body_mass_g",
            "bill_length_mm"
        ]
    )
    .properties(
        width=600,
        height=400
    )
)

chart.save("altair/altair_penguins.html")

print("Saved altair/altair_penguins.html")

