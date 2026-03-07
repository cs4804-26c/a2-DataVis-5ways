import base64
import pandas as pd
import plotly.express as px

# loading data
df = pd.read_csv("../penglings.csv").dropna(subset=[
    "flipper_length_mm", "body_mass_g", "bill_length_mm", "species"
]).copy()

# og scatter plot
fig = px.scatter(
    df,
    x="flipper_length_mm",
    y="body_mass_g",
    color="species",
    size="bill_length_mm",
    opacity=0.8,
    title="Penguin Flipper Length vs Body Mass",
    labels={
        "flipper_length_mm": "Flipper Length (mm)",
        "body_mass_g": "Body Mass (g)",
        "bill_length_mm": "Bill Length (mm)",
        "species": "Species"
    }
)

fig.update_layout(
    plot_bgcolor="white",     
    paper_bgcolor="white",     
    font=dict(color="black")   
)


# update axes
fig.update_xaxes(range=[df.flipper_length_mm.min(), df.flipper_length_mm.max()])
fig.update_yaxes(range=[df.body_mass_g.min(), df.body_mass_g.max()])


# use penguin image
with open("penguin.jpeg", "rb") as f:
    encoded = base64.b64encode(f.read()).decode("ascii")
penguin_uri = "data:image/png;base64," + encoded

icon_sizex = (df.flipper_length_mm.max() - df.flipper_length_mm.min()) * 0.07
icon_sizey = (df.body_mass_g.max() - df.body_mass_g.min()) * 0.07

penguin_images = []
for x, y in zip(df["flipper_length_mm"], df["body_mass_g"]):
    penguin_images.append(
        dict(
            source=penguin_uri,
            xref="x",
            yref="y",
            x=float(x),
            y=float(y),
            xanchor="center",
            yanchor="middle",
            sizex=float(icon_sizex),
            sizey=float(icon_sizey),
            sizing="contain",
            opacity=1.0,
            layer="above"
        )
    )

# toggle between normal points and peguin points
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="down",
            x=1.02, y=0.95,
            xanchor="left", yanchor="top",
            buttons=[
                dict(
                    label="📈 Normal points",
                    method="update",
                    args=[
                        {"visible": [True]},           
                        {"images": []}                 
                    ],
                ),
                dict(
                    label="🐧 Penguin points",
                    method="update",
                    args=[
                        {"visible": [False]},          
                        {"images": penguin_images}     
                    ],
                ),
            ],
        )
    ],
    margin=dict(r=220)  
)

fig.show()
