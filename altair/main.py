import altair as alt
import pandas as pd

penguinData = pd.read_csv("penglings.csv")

# make the chart
chart = alt.Chart(penguinData).mark_point(filled=True).encode(
    alt.X("flipper_length_mm")
        .axis(ticks=False)
        .scale(domain=(170, 240))
        .title("Flipper Length (mm)"),
    alt.Y("body_mass_g")
        .axis(ticks=False)
        .scale(domain=(2000, 7000))
        .title("Body Mass (g)"),
    alt.Color("species")
        .scale(
            domain=["Adelie", "Chinstrap", "Gentoo"],
            range=["darkorange", "magenta", "teal"]
        ),
    alt.Size("bill_length_mm")
        .scale(
            domain=(30,60),
            range=(100, 400)
        )
).properties(
    width=600,
    height=600
)

chart.save("chart.html")