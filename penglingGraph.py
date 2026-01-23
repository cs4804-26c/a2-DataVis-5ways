import altair as alt
import pandas as pd
import numpy as np

penglings = pd.read_csv("penglings.csv")

x_nice_min = np.floor(penglings['flipper_length_mm'].min() / 10) * 10
x_nice_max = np.ceil(penglings['flipper_length_mm'].max() / 10) * 10

y_nice_min = np.floor(penglings['body_mass_g'].min() / 500) * 500
y_nice_max = np.ceil(penglings['body_mass_g'].max() / 500) * 500

chart = alt.Chart(penglings).mark_circle(opacity=0.7).encode(
    x=alt.X('flipper_length_mm:Q',
            scale=alt.Scale(domain=[x_nice_min, x_nice_max],
                           nice=True)),
    
    y=alt.Y('body_mass_g:Q',
            scale=alt.Scale(domain=[y_nice_min, y_nice_max],
                           nice=True)),
    
    color='species:N',
    size='bill_length_mm:Q'
)

chart.save('penguins_chart.html')
print("Chart saved as penguins_chart.html")