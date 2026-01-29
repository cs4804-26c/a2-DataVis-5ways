import pandas as pd
import altair as alt

data = pd.read_csv('../penglings.csv')

color_domain = ['Adelie', 'Chinstrap', 'Gentoo']
color_range = ['orange', '#A550EF', 'darkcyan']

alt.Chart(data).mark_circle(size=60).encode(
    x=alt.X('flipper_length_mm', title='Flipper Length (mm)', scale=alt.Scale(zero=False)),
    y=alt.Y('body_mass_g', title='Body Mass (g)', scale=alt.Scale(zero=False)),
    color=alt.Color('species', scale=alt.Scale(domain=color_domain, range=color_range)),
    size='bill_length_mm',
).configure_view( # AI Usage Note: Can you mimic the darkgrid style of seaborn/matplotlib?
    fill="#EBEBEB",
    stroke=None
).configure_axis(
    grid=True,
    gridColor="white",
    domain=False,
    ticks=False
).configure_mark(opacity=0.8).properties(width=600, height=400).save('../img/altair-scatterplot.png', scale_factor=3)