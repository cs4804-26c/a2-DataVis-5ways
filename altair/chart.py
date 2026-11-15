import altair as alt
import pandas as pd

data = pd.read_csv("penglings.csv")
data = data.dropna(subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"])

chart = alt.Chart(data).mark_circle(opacity=0.8).encode(
    x=alt.X("flipper_length_mm:Q", title="Flipper Length (mm)", scale=alt.Scale(domain=[170, 235])),
    y=alt.Y("body_mass_g:Q", title="Body Mass (g)", scale=alt.Scale(domain=[2500, 6500])),
    color="species:N",
    size="bill_length_mm:Q",
    tooltip=["species", "flipper_length_mm", "body_mass_g", "bill_length_mm"]
).properties(width=700, height=470)

chart.save("penguins.html")
