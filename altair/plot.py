import altair as alt
import pandas as pd

df = pd.read_csv('penglings.csv')

colors = {
    "Adelie": "#F09539", 
    "Chinstrap": "#8E3BC6", 
    "Gentoo": "#3C898A"
}

# basically just took my r implementation and converted it to altair. started with https://altair-viz.github.io/gallery/scatter_tooltips.html
chart = alt.Chart(df).mark_circle(size=60, opacity=0.8, strokeWidth=2).encode(
    x=alt.X('flipper_length_mm:Q', title='Flipper Length (mm)', 
            scale=alt.Scale(domain=[169, 234]), axis=alt.Axis(tickCount=7, tickSize=5)),
    y=alt.Y('body_mass_g:Q', title='Body Mass (g)', 
            scale=alt.Scale(domain=[2500, 6500])),
    color=alt.Color('species:N', scale=alt.Scale(domain=['Adelie', 'Chinstrap', 'Gentoo'], range=[colors['Adelie'], colors['Chinstrap'], colors['Gentoo']])),
    size=alt.Size('bill_length_mm:Q', scale=alt.Scale(domain=[30, 60], range=[100, 625]), legend=alt.Legend(title='bill_length_mm', values=[40, 50])),
    fill=alt.Fill('species:N', scale=alt.Scale(domain=['Adelie', 'Chinstrap', 'Gentoo'], range=[colors['Adelie'], colors['Chinstrap'], colors['Gentoo']])),
    tooltip=['species', 'flipper_length_mm', 'body_mass_g', 'bill_length_mm']
).properties(
    width=600,
    height=400
).configure_view(
    strokeWidth=0
).configure_axis(
    gridColor='white',
    gridOpacity=1
).configure_legend(
    titleFontSize=12,
    labelFontSize=10,
    symbolSize=100
)

# Save as PNG (requires Kaleido installed)
chart.save('altair.png', scale=3)

# To display the chart (if running in Jupyter/Notebook)
chart.show()

chart.save("example.png", scale = 3)