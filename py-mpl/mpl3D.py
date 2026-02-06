import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D

df = pd.read_csv("penglings.csv")

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

# 3D figure
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(
    df['flipper_length_mm'],
    df['body_mass_g'],
    df['bill_depth_mm'],
    s=df['bill_length_mm'] * 8,  # size scaled by bill length
    c=df['species'].map(colors),
    alpha=0.8
)

ax.set_xlabel('Flipper Length (mm)')
ax.set_ylabel('Body Mass (g)')
ax.set_zlabel('Bill Depth (mm)')

ymin, ymax = df['body_mass_g'].min(), df['body_mass_g'].max()
ax.set_yticks(range(int(ymin // 1000 * 1000), int(ymax // 1000 * 1000) + 1000, 1000))

legend_species = [
    Line2D([0], [0], marker='o', color='w', label=species,
           markerfacecolor=color, markersize=10, alpha=1.0)
    for species, color in colors.items()
]
ax.legend(handles=legend_species, title="Species", loc='upper left', bbox_to_anchor=(1.05, 1))

plt.tight_layout()
plt.show()
