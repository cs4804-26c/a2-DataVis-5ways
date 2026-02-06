import pandas as pd
import altair as alt

df = pd.read_csv("/Users/mariana/projects/a2-DataVis-5ways/penglings.csv")

species_colors = {
    "Adelie": "#F8766D",
    "Chinstrap": "#C77CFF",
    "Gentoo": "#00BFC4",
}

df = df.dropna(subset=["species", "flipper_length_mm", "body_mass_g", "bill_length_mm"])
df["species"] = df["species"].astype(str)

chart = (
    alt.Chart(df)
    .mark_circle(opacity=0.8)
    .encode(
        x=alt.X("flipper_length_mm:Q", scale=alt.Scale(zero=False), title="Flipper Length (mm)"),
        y=alt.Y("body_mass_g:Q", scale=alt.Scale(zero=False), title="Body Mass (g)"),
        color=alt.Color(
            "species:N",
            scale=alt.Scale(domain=list(species_colors.keys()), range=list(species_colors.values())),
            title="Species",
            legend=alt.Legend(orient="right"),
        ),
        size=alt.Size(
            "bill_length_mm:Q",
            title="Bill Length (mm)",
            legend=alt.Legend(values=[40, 50]),  # avoids showing 0
            scale=alt.Scale(range=[30, 400]),
        ),
        tooltip=[
            alt.Tooltip("species:N", title="Species"),
            alt.Tooltip("flipper_length_mm:Q", title="Flipper (mm)"),
            alt.Tooltip("body_mass_g:Q", title="Body mass (g)"),
            alt.Tooltip("bill_length_mm:Q", title="Bill (mm)"),
        ],
    )
    .properties(
        title="",            # no title
        width=650,
        height=450,
        padding=5            # <- THIS replaces configure_padding
    )
    .configure_title(fontSize=1)   # minimizes leftover title space
    .configure_view(stroke=None)
)

chart.save("output.html")
print("Wrote output.html")
