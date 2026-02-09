import pandas as pd
import altair as alt
from altair.datasets import data
import vl_convert as vlc

alt.renderers.enable("browser")

species_names = ['Adelie', 'Chinstrap', 'Gentoo']
colors = ['#fda246', '#ac5ad4', '#49a1a1']

chart = alt.Chart(
	pd.read_csv('../../penglings.csv'),
	width=1000,
	height=800
).mark_point(
	opacity=0.8,
	filled=True
).encode(
	alt.X('flipper_length_mm').scale(domain=(170, 235)).title("Flipper Length (mm)"),
	alt.Y('body_mass_g').scale(domain=(2500, 6500)).title("Body Mass (g)"),
	color=alt.Color('species').legend().title("Species").scale(domain=species_names, range=colors),
	size=alt.Size('bill_length_mm').legend(values=[40,50]).title("Bill Length (mm)").scale(domain=(30, 60), range=(100,1000))
).configure_axis(
	gridColor='white',
	titleFontSize=26,
	labelFontSize=18,
	format='d'
).configure_axisX(
	titlePadding=10,
 	tickCount=((235-170) / 5) + 1,
  labelExpr="datum.value % 10 ? null : datum.label"
).configure_axisY(
	titlePadding=20,
 	tickCount=((6500-2500) / 500) + 1,
  labelExpr="datum.value % 1000 ? null : datum.label"
).configure_view(
	fill='#ebebeb',
	stroke='white'
).configure_legend(
	titleFontSize=22,
	labelFontSize=18,
 	padding=10
).show()
