# I used ChatGPT to help implement the Altair scatterplot, data loading,
# scale mappings, hover tooltips, and clickable species filtering.
# I chose the visual design myself.

from pathlib import Path

import altair as alt
import pandas as pd

folder = Path(__file__).resolve().parent
csv_path = folder.parent / "penglings.csv"
if not csv_path.exists():
    raise FileNotFoundError(
        "Place the altair folder next to penglings.csv in the assignment repository."
    )

data = pd.read_csv(csv_path, na_values=["NA"])
data = data.dropna(
    subset=["species", "flipper_length_mm", "body_mass_g", "bill_length_mm"]
)

colors = alt.Scale(
    domain=["Adelie", "Chinstrap", "Gentoo"],
    range=["#ff0000", "#0000ff", "#93e9be"],
)

species_selection = alt.selection_point(
    fields=["species"], bind="legend", on="click", toggle=True, empty=True
)

chart = (
    alt.Chart(data)
    .mark_circle(filled=True)
    .encode(
        x=alt.X(
            "flipper_length_mm:Q",
            title="Flipper Length (mm)",
            scale=alt.Scale(domain=[170, 235], zero=False),
            axis=alt.Axis(values=list(range(170, 236, 10)), grid=True),
        ),
        y=alt.Y(
            "body_mass_g:Q",
            title="Body Mass (g)",
            scale=alt.Scale(domain=[2500, 6500], zero=False),
            axis=alt.Axis(values=list(range(2500, 6501, 500)), grid=True),
        ),
        color=alt.Color("species:N", title="Species (click to filter)", scale=colors),
        size=alt.Size(
            "bill_length_mm:Q",
            title="Bill Length (mm)",
            scale=alt.Scale(domain=[30, 60], range=[30, 315], zero=False),
            legend=alt.Legend(values=[35, 45, 55]),
        ),
        opacity=alt.condition(species_selection, alt.value(0.8), alt.value(0.06)),
        tooltip=[
            alt.Tooltip("species:N", title="Species"),
            alt.Tooltip("flipper_length_mm:Q", title="Flipper length (mm)"),
            alt.Tooltip("body_mass_g:Q", title="Body mass (g)", format=",.0f"),
            alt.Tooltip("bill_length_mm:Q", title="Bill length (mm)"),
        ],
    )
    .add_params(species_selection)
    .properties(
        title="Penguin Body Mass vs. Flipper Length",
        width=820,
        height=470,
        background="#eeeeee",
    )
    .configure_view(stroke=None)
    .configure_axis(
        labelFont="Georgia",
        titleFont="Georgia",
        gridColor="#d8d8d8",
    )
    .configure_title(font="Georgia", fontSize=24)
    .configure_legend(labelFont="Georgia", titleFont="Georgia", orient="bottom")
)

output = folder / "altair_penguins.html"
chart.save(output)
print(f"Saved chart to: {output}")
