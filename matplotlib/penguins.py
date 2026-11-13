import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../penglings.csv").dropna(
    subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"])
colors = {"Adelie": "#ff8c00", "Chinstrap": "#a020f0", "Gentoo": "#008b8b"}
fig, ax = plt.subplots(figsize=(8.5, 5.3))

# matplotlib has no "color by column", so draw one scatter per species
for species, g in df.groupby("species"):
    ax.scatter(g["flipper_length_mm"], g["body_mass_g"],
               s=(g["bill_length_mm"] - 25) * 4,  # marker area scales with bill length
               c=colors[species], alpha=0.8, label=species, linewidths=0)

ax.set_xlabel("Flipper Length (mm)")
ax.set_ylabel("Body Mass (g)")
ax.set_xticks(range(170, 231, 10))
ax.set_yticks(range(3000, 6001, 1000))
ax.grid(color="#dddddd")
ax.set_axisbelow(True)
ax.legend(title="species", loc="upper left", markerscale=0.6)
fig.tight_layout()
fig.savefig("../img/matplotlib.png", dpi=200)
