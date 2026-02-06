import altair as alt
import numpy as np
import pandas as pd
import json

df = pd.read_csv("penglings.csv")

chart = alt.Chart(df).mark_point(filled=True,opacity=0.8).encode(
    x=alt.X("flipper_length_mm:Q", title="Flipper Length (mm)", scale=alt.Scale(domain=[170, 240])),
    y=alt.Y("body_mass_g:Q", title="Body Mass (g)", scale=alt.Scale(domain=[2500, 6500])),
    color="species:N",
    size=alt.Size("bill_length_mm:Q",scale=alt.Scale(type="sqrt", domain=[40, 50], range=[20, 80]), legend=alt.Legend(values=[40, 45, 50], format=".0f")),
    tooltip=["flipper_length_mm:Q", "body_mass_g:Q", "species:N", "bill_length_mm:Q"]
)


chart_dict = chart.to_dict()
def replace_nan(d):
    if isinstance(d, dict):
        return {k: replace_nan(v) for k, v in d.items()}
    elif isinstance(d, list):
        return [replace_nan(v) for v in d]
    elif isinstance(d, float) and (np.isnan(d)):
        return None
    else:
        return d
chart_dict = replace_nan(chart_dict)
with open("altair.json", "w") as f:
    json.dump(chart_dict, f)