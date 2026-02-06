import altair as alt
import pandas as pd

alt.data_transformers.enable('csv')

url = "C:/Users/maxwe/OneDrive/Documents/Data Vis/a2-DataVis-5ways/data/penglings.csv"

df = pd.read_csv(url)

print(df)

domain = ['Adelie', "Gentoo", "Chinstrap"]
range_ = ['#f09600', '#00a08d', '#8c00b4']

alt.renderers.enable('mimetype')

chart = alt.Chart(df).mark_point(filled=True,fillOpacity=0.6,strokeOpacity=1,strokeWidth=1).encode(
    alt.X('flipper_length_mm').scale(zero=False),
    alt.Y('body_mass_g').scale(zero=False),
    alt.Size('bill_length_mm').scale(domain=(30, 50)),
    color=alt.Color('species').scale(domain=domain,range=range_),
    stroke=alt.Color('species').scale(domain=domain,range=range_)
)

chart.save('chart.html')
