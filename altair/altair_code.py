import altair as alt
import pandas as pd
import openpyxl

# Loading data
file_name = "Penglings Data (CS 4804 A2).xlsx"
df = pd.read_excel(file_name)

# 2. Data Cleaning (Just in case, like we did in R)
# This converts columns to numbers and drops rows with missing values
df['Flipper_length_mm'] = pd.to_numeric(df['Flipper_Length_mm'], errors='coerce')
df['Body_Mass_g'] = pd.to_numeric(df['Body_Mass_g'], errors='coerce')
df['Bill_Length_mm'] = pd.to_numeric(df['Bill_Length_mm'], errors='coerce')
df = df.dropna()

# Creating the Chart
chart = alt.Chart(df).mark_circle(opacity=0.8).encode(
    # :Q means Quantitative (Numbers)
    # :N means Nominal (Categories/Names)
    x=alt.X('Flipper_Length_mm:Q', scale=alt.Scale(zero=False), title='Flipper Length (mm)'),
    y=alt.Y('Body_Mass_g:Q', scale=alt.Scale(zero=False), title='Body Mass (g)'),
    color=alt.Color('Species:N', scale=alt.Scale(
        domain=['Adelie', 'Chinstrap', 'Gentoo'],
        range=['#ff8c00', '#9932cc', '#008b8b']
    )),
    size='Bill_Length_mm:Q',
    tooltip=['Species', 'Flipper_Length_mm', 'Body_Mass_g', 'Bill_Length_mm']
).properties(
    width=600,
    height=400,
    title="Penguin Measurements (Altair)"
)

chart.save('altair_chart.html')
print("Chart saved as altair_chart.html. Open this file in your browser!")