import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

df = pd.read_csv("penglings.csv")

print(df)

# data cleaning
df = df.dropna(subset=[
    "flipper_length_mm",
    "body_mass_g",
    "bill_length_mm",
    "species"
])

colors = {
    "Adelie": "#fda147",     # orange
    "Chinstrap": "#ab5ad3",  # purple
    "Gentoo": "#48a1a0"      # teal
}

plt.figure(figsize=(12, 8))

for species, color in colors.items():
    subset = df[df["species"] == species]
    plt.scatter(
        subset["flipper_length_mm"],
        subset["body_mass_g"],
        s=subset["bill_length_mm"] * 8,
        alpha=0.8,
        color=color,
        label=species,
        edgecolors="none"
    )

size_legend = [40, 50]
size_scale = 8

size_handles = [
    plt.scatter(
        [], [], 
        s=s * size_scale,
        color="gray",
        alpha=0.8
    )
    for s in size_legend
]

species_handles = [
    Line2D(
        [0], [0],
        marker='o',
        color='w',
        label=species,
        markerfacecolor=color,
        markersize=10,
        alpha=1.0
    )
    for species, color in colors.items()
]

first_legend = plt.legend(
    handles=size_handles,
    labels=[f"{s} mm" for s in size_legend],
    title="Bill length",
    loc="center left",
    bbox_to_anchor=(1.02, 0.4),
    frameon=True
)

plt.gca().add_artist(first_legend)
plt.legend(
    handles=species_handles,
    title="species",
    loc="center left",
    bbox_to_anchor=(1.02, 0.6),
    frameon=True
)

plt.xlabel("Flipper Length (mm)", fontsize=14)
plt.ylabel("Body Mass (g)", fontsize=14)
plt.yticks(range(2500, 6500, 1000))
plt.grid(True, alpha=0.3)
plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.show()