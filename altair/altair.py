import altair as alt
import pandas as pd

data = pd.read_csv("penglings.csv")
minBillLength = data['bill_length_mm'].min()
maxBillLength = data['bill_length_mm'].max()

alt.Chart(data).mark_circle(opacity=0.8).encode(
    alt.X('flipper_length_mm').scale(domain=(170, 235)).axis(tickMinStep=10).title("Flipper Length (mm)"),
    alt.Y('body_mass_g').scale(domain=(2500, 6500)).axis(tickMinStep=1000).title("Body Mass (g)"),
    alt.Size('bill_length_mm').scale(domain=[minBillLength, maxBillLength],range=[25,300]),
    alt.Color('species').scale(domain=["Adelie", "Chinstrap", "Gentoo"],range=["orange", "purple", "teal"]),
).properties(width=400)