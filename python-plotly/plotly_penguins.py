import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("penglings.csv")

# Remove rows with missing bill_length_mm
df = df.dropna(subset=['bill_length_mm'])


# Create Plotly scatterplot
fig = px.scatter(
    df,
    x="flipper_length_mm",
    y="body_mass_g",
    color="species",
    size="bill_length_mm",
    opacity=0.8,
    hover_data=['species','flipper_length_mm','body_mass_g','bill_length_mm'],
    labels={
        "flipper_length_mm": "Flipper Length (mm)",
        "body_mass_g": "Body Mass (g)",
        "bill_length_mm": "Bill Length (mm)"
    },
    title="Penguins Scatterplot"
)


fig.update_xaxes(range=[170, 235])
fig.update_yaxes(range=[2700, 6300])


fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    legend_title_text="Species"
)

# Save chart
fig.write_html("penguins_plotly.html")
fig.show()

print("Plotly chart saved! Open penguins_plotly.html in your browser to view it.")
