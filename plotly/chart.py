import pandas as pd
import plotly.express as px

data = pd.read_csv("penglings.csv")
data = data.dropna(subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"])

chart = px.scatter(data,
    x="flipper_length_mm", y="body_mass_g",
    color="species", size="bill_length_mm", opacity=0.8,
    range_x=[170, 235], range_y=[2500, 6500]
)

chart.update_xaxes(title="Flipper Length (mm)")
chart.update_yaxes(title="Body Mass (g)")
chart.write_html("penguins.html")
