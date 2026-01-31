# Altair is concise and decorative, but size scaling is less intuitive than ggplot2

import altair as alt
import pandas as pd

# load data
df = pd.read_csv("penglings.csv")

# some rows have NA values, this code will ignore them
df = df.dropna(subset=[
    "flipper_length_mm",
    "body_mass_g",
    "bill_length_mm",
    "species"
])

chart = alt.Chart(df).mark_circle(opacity=0.8).encode( # opacity 0f 0.8 matches given image
    x=alt.X("flipper_length_mm:Q", title="Flipper Length (mm)",
            scale=alt.Scale(domain=[170,235])),
    y=alt.Y("body_mass_g:Q", title="Body Mass (g)",
            scale=alt.Scale(domain=[2500, 6500])), # this changes the scale in accordance to given image
    color=alt.Color("species:N", title="Species",
                    scale=alt.Scale(
                        range=["orange", "purple", "teal"])), # this gives specific colors to each species
    size=alt.Size(
        "bill_length_mm:Q",
        title="Bill Length (mm)",
        legend=alt.Legend(values=[40,50]) # this specifies the values shown in the legend
    ),
    tooltip=["species", "bill_length_mm", "body_mass_g"]
).properties(
    width=600,
    height=400,
    title="Altair"
)

print("Saving image now...")
chart.save("altair.html") # was not able to figure out how to save to png without downloading extra things

print("done!")
