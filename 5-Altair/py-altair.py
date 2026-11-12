import altair as alt
import pandas as pd

source = pd.read_csv('penglings.csv')

species_domain = ['Adelie', 'Chinstrap', 'Gentoo']
species_range = ['orange', 'purple', 'darkcyan']

chart = alt.Chart(source).mark_point(filled=True, fillOpacity=0.8).encode(
    x=alt.X('flipper_length_mm', title='Flipper Length (mm)').scale(zero=False),
    y=alt.Y('body_mass_g', title='Body Mass (g)').scale(zero=False),
    size=alt.Size('bill_length_mm', title='Bill Length (mm)', legend=alt.Legend(tickCount=2)).scale(zero=False, domain=[source['bill_length_mm'].min(), source['bill_length_mm'].max()], range=[100, 300]),
    color=alt.Color('species', title='Species').scale(domain=species_domain, range=species_range),
    tooltip=[
        alt.Tooltip('species', title='Species'),
        alt.Tooltip('bill_length_mm', title='Bill Length (mm)'),
        alt.Tooltip('flipper_length_mm', title='Flipper Length (mm)'),
        alt.Tooltip('body_mass_g', title='Body Mass (g)')
    ]
)

alt.renderers.enable('browser')
chart.show()
chart.save("img/5-altair.png")