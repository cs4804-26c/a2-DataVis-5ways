import pandas as pd
import altair as alt

penguins_data = pd.read_csv("penglings.csv")
penguins_data = penguins_data.dropna(subset=["flipper_length_mm", "body_mass_g", "bill_length_mm", "species"])

chart = alt.Chart(penguins_data).mark_circle(opacity=0.8).encode(
    x=alt.X('flipper_length_mm', 
            title='Flipper Length (mm)',
            scale=alt.Scale(domain=[170, 235]),
            axis=alt.Axis(values=list(range(170, 236, 10)))
           ),
    y=alt.Y('body_mass_g', 
            title='Body Mass (g)',
            scale=alt.Scale(domain=[2500, 6500]),
            axis=alt.Axis(values=list(range(2500, 6501, 1000)))
           ),
    color=alt.Color('species:N', 
                    scale=alt.Scale(domain=['Adelie', 'Chinstrap', 'Gentoo'],
                                    range=["#fda147", "#ab5ad3", "#48a1a0" ]),
                    title='Species'),
    size=alt.Size('bill_length_mm', 
                  scale=alt.Scale(range=[30, 100]), 
                  legend=alt.Legend(values=[40,50]),
                  title='Bill Length (mm)')
).properties(
    width=600,
    height=400
).configure_legend(
    symbolSize=100
)

chart.save("altair.html")

