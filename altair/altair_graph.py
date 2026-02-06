import altair as alt
import pandas as pd

df = pd.read_csv('../penglings.csv')

selection = alt.selection_point(fields=['species'], bind='legend')

chart = alt.Chart(df).mark_circle().encode(
    x=alt.X('flipper_length_mm', 
            scale=alt.Scale(zero=False),
            title='Flipper Length (mm)'),
    y=alt.Y('body_mass_g', 
            scale=alt.Scale(zero=False),
            title='Body Mass (g)'),
    size=alt.Size('bill_length_mm', 
            scale=alt.Scale(range=[20, 100]),
            legend=alt.Legend(values=[40, 50])),
    color=alt.Color('species', 
            scale=alt.Scale(range=['#FDA247', '#AC5AD4', '#4AA1A1'])),
    opacity=alt.condition(selection, alt.value(0.8), alt.value(0.1)),
    tooltip=['species', 'bill_length_mm', 'body_mass_g', 'flipper_length_mm']
).add_params(selection).interactive()

chart.save('altair_graph.html')