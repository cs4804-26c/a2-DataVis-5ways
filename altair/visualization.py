import altair as alt
import pandas as pd

data = pd.read_csv("/Users/esthermao/Documents/WPI/senior year/C26/CS 4804/a2-DataVis-5ways/penglings.csv")

chart = alt.Chart(data).mark_circle(opacity=0.8).encode(
    x=alt.X('flipper_length_mm:Q',
            title = 'Flipper Length (mm)',
            scale = alt.Scale(zero=False)),
    y=alt.Y('body_mass_g:Q',
            title = 'Body Mass (g)',
            scale=alt.Scale(zero=False)),
    color=alt.Color('species:N',
                    title='Species',
                    scale=alt.Scale(range=["#ff52b8", "#bbe458", "#ff3d00"])),
    size=alt.Size('bill_length_mm:Q',
                  title = 'Bill Length (mm)',
                  scale = alt.Scale(range=[50, 300])),
    tooltip = ['species', 'flipper_length_mm', 'body_mass_g', 'bill_length_mm', 'bill_depth_mm', 'island', 'sex' ]
).properties(
    width = 600, 
    height = 400,
    title = 'Penguin Flipper Length vs Body Mass & Bill Length'
).configure_mark(
    opacity = 0.8
)

chart.save('output.html')