import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/penglings.csv")

# Drop missing values
df = df.dropna(subset=[
    "flipper_length_mm",
    "body_mass_g",
    "bill_length_mm",
    "species"
])

# Color map (match d3 / Altair)
colors = {
    "Adelie": "#F28E2B",
    "Chinstrap": "#9C51B6",
    "Gentoo": "#4E9E9A"
}

# ---- STYLE SETTINGS ----
plt.style.use("default")

fig, ax = plt.subplots(figsize=(9, 5))

# Grey background
ax.set_facecolor("#f0f0f0")
fig.patch.set_facecolor("white")

# White gridlines
ax.grid(
    True,
    color="white",
    linewidth=1
)

# Ensure grid is behind points
ax.set_axisbelow(True)

# plot
for species, group in df.groupby("species"):
    ax.scatter(
        group["flipper_length_mm"],
        group["body_mass_g"],
        s=group["bill_length_mm"] * 6,  # size scaling
        alpha=0.8,
        label=species,
        color=colors.get(species, "gray"),
        edgecolors="none"
    )

# Labels and title
ax.set_xlabel("Flipper Length (mm)")
ax.set_ylabel("Body Mass (g)")
ax.set_title("Penguins Scatter (Matplotlib)")

# Legend
ax.legend(title="Species")

# Tight layout and save
plt.tight_layout()
plt.savefig("img/matplotlib.png", dpi=150)
plt.show()
