import seaborn as sns
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA, OUT = "penglings.csv", Path("img") / "seaborn_scatter.png"
COLS = {"sp": "species", "bill": "bill_length_mm", "flip": "flipper_length_mm", "mass": "body_mass_g"}

def main():
    df = pd.read_csv(DATA)[COLS.values()].dropna()
    
    # Size scaling
    bill_series = df[COLS["bill"]]
    bill_clipped = bill_series.clip(*bill_series.quantile([0.02, 0.98]))
    df["size_norm"] = 30 + (230 * (bill_clipped - bill_clipped.min()) / (bill_clipped.max() - bill_clipped.min() + 1e-12))
    
    # Seaborn plot
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid", {'grid.linestyle': '--', 'grid.alpha': 0.3})
    
    # Plot each species separately to control size
    ax = plt.gca()
    palette = {"Adelie": "#5d8769", "Chinstrap": "#3348b4", "Gentoo": "#c25cb5"}
    
    for species in df[COLS["sp"]].unique():
        species_data = df[df[COLS["sp"]] == species]
        ax.scatter(x=species_data[COLS["flip"]], y=species_data[COLS["mass"]],
                   s=species_data["size_norm"], alpha=0.85,
                   color=palette[species], edgecolor='white', linewidth=0.8,
                   label=species)
    
    # Set specific axis limits
    plt.xlim(167, 250)
    plt.ylim(2500, 6500)
    
    # Labels & Legend
    ax.set(xlabel="Flipper Length (mm)", ylabel="Body Mass (g)")
    ax.legend(title="Species", framealpha=0.9, edgecolor='#dee2e6', facecolor='white')
    
    OUT.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUT, dpi=160, bbox_inches='tight', facecolor='#f8f9fa')
    plt.close()
    print(f"Saved: {OUT}")

if __name__ == "__main__":
    main()