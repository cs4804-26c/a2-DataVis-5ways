import altair as alt
import pandas as pd
import os


csv_path = '../penglings.csv'

if not os.path.exists(csv_path):
    csv_path = 'penglings.csv'

df = pd.read_csv(csv_path)


df = df.dropna(subset=['flipper_length_mm', 'body_mass_g', 'bill_length_mm', 'species'])


selection = alt.selection_point(fields=['species'], bind='legend')


chart = alt.Chart(df).mark_circle(
    size=60,
    opacity=0.8
).encode(
    # X
    x=alt.X('flipper_length_mm',
            scale=alt.Scale(zero=False),
            title='Flipper Length (mm)'),

    # Y
    y=alt.Y('body_mass_g',
            scale=alt.Scale(zero=False),
            title='Body Mass (g)'),


    color=alt.condition(
        selection,
        alt.Color('species:N', scale=alt.Scale(scheme='category10')),
        alt.value('lightgray')
    ),


    size=alt.Size('bill_length_mm', title='Bill Length (mm)'),

    # Tooltip
    tooltip=['species', 'flipper_length_mm', 'body_mass_g', 'bill_length_mm']
).properties(
    title='Penguin Size vs. Mass (Altair)',
    width=600,
    height=400
).add_params(
    selection
).interactive()


chart.save('altair_chart.html')

print("Chart saved to altair_chart.html")
