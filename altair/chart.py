import altair as alt
import pandas as pd


df = pd.read_csv('../penglings.csv')

chart = alt.Chart(df).mark_circle(opacity=0.8, stroke='black', strokeWidth=1).encode(

x=alt.X('flipper_length_mm', scale = alt.Scale(zero=False), title = 'Flipper Length (mm)'),
y=alt.Y('body_mass_g', scale=alt.Scale(zero=False), title='Body Mass (g)'),

color=alt.Color('species', scale=alt.Scale(
domain=['Adelie', 'Gentoo', 'Chinstrap'],
range=['#017339', '#e8ac0e', '#e25501']
)),

size = alt.Size('bill_length_mm', title='Bill Length (mm)'),

tooltip = ['species', 'flipper_length_mm', 'body_mass_g', 'bill_length_mm']).properties(
title='Penguin Size vs Mass (Altair)',
width = 600,
height = 480
).interactive()

chart.save('a2-altair-graph.html')
print('Chart saved as a2-altair-graph.html')
