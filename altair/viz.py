import pandas as pd
import altair as alt

df = pd.read_csv("../penglings.csv")

for c in ["bill_length_mm", "flipper_length_mm", "body_mass_g"]:
    df[c] = pd.to_numeric(df[c], errors="coerce")

df["species"] = df["species"].astype(str).str.replace('"', "", regex=False).str.strip()

df = df.dropna(subset=["species", "bill_length_mm", "flipper_length_mm", "body_mass_g"])

x_min, x_max = df["flipper_length_mm"].min(), df["flipper_length_mm"].max()
y_min, y_max = df["body_mass_g"].min(), df["body_mass_g"].max()

x_pad = 2
y_pad = 150

x_domain = [x_min - x_pad, x_max + x_pad]
y_domain = [y_min - y_pad, y_max + y_pad]

chart = (
    alt.Chart(df)
    .mark_circle(opacity=0.7)
    .encode(
        x=alt.X(
            "flipper_length_mm:Q",
            title="Flipper Length (mm)",
            scale=alt.Scale(domain=x_domain)
        ),
        y=alt.Y(
            "body_mass_g:Q",
            title="Body Mass (g)",
            scale=alt.Scale(domain=y_domain)
        ),
        color=alt.Color("species:N", title="Species"),
        size=alt.Size(
            "bill_length_mm:Q",
            title="Bill length (mm)",
            legend=alt.Legend(values=[35, 40, 45, 50, 55])
        ),
        tooltip=["species", "flipper_length_mm", "body_mass_g", "bill_length_mm"],
    )
    .properties(
        width=650,
        height=420,
        title="Flipper Length vs Body Mass"
    )
)

chart.save("index.html")
print("Wrote altair/index.html")
