import altair as alt
import pandas as pd

# Load the dataset
df = pd.read_csv('penglings.csv')

# Clean the data by removing rows with missing values in the columns we're using
df_cleaned = df.dropna(subset=['flipper_length_mm', 'body_mass_g', 'bill_length_mm', 'species'])

# Create the scatter plot using Altair
chart = alt.Chart(df_cleaned).mark_circle(opacity=0.8).encode(
    x=alt.X('flipper_length_mm:Q', 
            scale=alt.Scale(zero=False), 
            axis=alt.Axis(values=list(range(170, 240, 5)),
                          labelExpr="datum.value % 10 == 0 ? datum.value : ''"),
            title='Flipper Length (mm)'),
    y=alt.Y('body_mass_g:Q', 
            scale=alt.Scale(zero=False), 
            axis=alt.Axis(values=list(range(2500, 7000, 500)),
                          labelExpr="datum.value % 1000 == 0 ? datum.value : ''"),
            title='Body Mass (g)'),
    color=alt.Color('species:N', 
                    scale=alt.Scale(domain=['Adelie', 'Chinstrap', 'Gentoo'],
                                    range=['#fe9013', '#9932cc', '#018b8b']),
                    title='Species'),
    size=alt.Size('bill_length_mm:Q', 
                  scale=alt.Scale(range=[50, 600], zero=False), 
                  title='Bill Length (mm)')
).properties(
    width=600,
    height=400,
    title='Penguin Flipper Length vs Body Mass'
).configure_axis(
    gridColor='white',
    gridWidth=1
).configure_view(
    fill='#ebebeb',
    strokeWidth=0
)

# Save the chart to an HTML file
chart.save('altair_method.html')