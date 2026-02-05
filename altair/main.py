import altair as alt
import pandas as pd

##get data
data = pd.read_csv("data/penglings.csv")

##create chart
chart = alt.Chart(data).mark_circle(opacity=0.7).encode(
    ##axes and scales
    x=alt.X("flipper_length_mm", title="Flipper Length (mm)", 
            scale=alt.Scale(domain=[170, 240])),
    y=alt.Y("body_mass_g", title="Body Mass (g)", 
            scale=alt.Scale(domain=[3000, 6500])),
    color=alt.Color("species", title="Species", 
                    scale=alt.Scale(scheme="category10")),
    size=alt.Size("bill_length_mm", title="Bill Length (mm)", 
                  scale=alt.Scale(range=[50, 100]))
)

##save as an html file
chart.save("altair.html")

chart 


