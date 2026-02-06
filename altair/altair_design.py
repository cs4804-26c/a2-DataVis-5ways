import altair as alt
import pandas as pd

data = pd.read_csv("penglings.csv")
minBillLength = data['bill_length_mm'].min()
maxBillLength = data['bill_length_mm'].max()

charts = alt.Chart(data).encode(
    alt.X('flipper_length_mm').scale(domain=(170, 235)).axis(tickMinStep=10).title("Flipper Length (mm)"),
    alt.Y('body_mass_g').scale(domain=(2500, 6500)).axis(tickMinStep=1000).title("Body Mass (g)")

)

points = charts.mark_circle(opacity=0.8).encode(
    alt.Size('bill_length_mm', legend=None).scale(domain=[minBillLength, maxBillLength],range=[25,300]),
    alt.Color('species', legend=None).scale(domain=["Adelie", "Chinstrap", "Gentoo"],range=["orange", "purple", "teal"])
)

lines = charts.transform_regression(
    'flipper_length_mm',
    'body_mass_g',
    groupby=['species'],
    extent=[170, 235]
).mark_line(color="black", opacity=0.5)


all = (points + lines).properties(width=300).facet(
    alt.Column('species', title=None, header=alt.Header(labelFontSize=16, labelFontWeight='bold'))
)

all