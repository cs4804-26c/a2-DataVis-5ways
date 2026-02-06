import pandas as pd
import altair as alt

df = pd.read_csv("penglings.csv")

chart = alt.Chart(df).mark_circle(opacity=0.8).encode(
    x=alt.X('flipper_length_mm:Q', scale=alt.Scale(domain=[170, 235]), title='Flipper Length (mm)'),
    y=alt.Y('body_mass_g:Q', scale=alt.Scale(domain=[2700, 6300]), title='Body Mass (g)'),
    color=alt.Color('species:N'),
    size=alt.Size('bill_length_mm:Q', title='Bill Length (mm)')
).properties(
    title='Penguin Measurements Scatterplot',
    width=800,   
    height=600, 
    autosize=alt.AutoSizeParams(
        type='fit-x', 
        contains='padding'
    )
).configure_title(
    fontSize=20,
    anchor='start',
    color='black'
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
).configure_legend(
    titleFontSize=14,
    labelFontSize=12
)

# Save chart as HTML
chart.save('penguins_chart.html')
print("Chart saved! Open penguins_chart.html in your browser to view it.")
