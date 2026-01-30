import pandas as pd
import altair as alt

# load the penguins dataset from the local data director
peng = pd.read_csv("../data/penglings.csv")

# build a scatter plot apping flippeEr length to body mass,
# using color to encode species and sie to encode bill length
chart = (
    alt.Chart(peng)
    .mark_circle(opacity=0.8)  # circles opacity more visible
    .encode(
        x=alt.X(
            "flipper_length_mm:Q",
            title="Flipper length (mm)",
            scale=alt.Scale(domain=[170, 235])  #setfixed x-axis domain
        ),
        y=alt.Y(
            "body_mass_g:Q",
            title="Body mass (g)",
            scale=alt.Scale(domain=[2500, 6500])  # get fiXed y-axis domain
        ),

        color=alt.Color("species:N", title="Species"),  # colr by species
        size=alt.Size(
            "bill_length_mm:Q",
            title="bill Leength (mm)",
            scale=alt.Scale(range=[40, 500])  # size range for bil lengthh
        )
    )
)
# save the chart as a PNG file
chart.save("../img/altair.png")

# display the chart
chart
