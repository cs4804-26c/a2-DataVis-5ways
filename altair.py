import altair as alt
import pandas as pd

data = pd.read_csv("penglings.csv")

chart = alt.Chart(data).mark_point(
    opacity = 0.8
).encode(
    x=alt.X("flipper_length_mm:Q", 
            scale=alt.Scale(domain=[170, 240]),
            title="Flipper Length (mm)"
           ),
    y=alt.Y("body_mass_g:Q", 
            scale=alt.Scale(domain=[2500, 6500]),
            title="Body Mass (g)"
           ),
    color=alt.Color(
        "species",
        scale=alt.Scale(
            range=["orange", "purple", "#008080"]
        ),
        legend=alt.Legend(title="Species"),
    ),
    size=alt.Size("bill_length_mm:Q",
                  scale=alt.Scale(domain=[30,60],range=[10,100]),
                  legend=alt.Legend(title="Bill Length (mm)")
                 )
).interactive()

chart