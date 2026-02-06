from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA, OUT = "penglings.csv", Path("img") / "pandas_scatter.png"
COLS = {"sp": "species", "bill": "bill_length_mm", "flip": "flipper_length_mm", "mass": "body_mass_g"}
COLORS = {"Adelie": "#5d8769", "Chinstrap": "#3348b4", "Gentoo": "#c25cb5"}

def main():
    df = pd.read_csv(DATA)[COLS.values()].dropna()
    
    # Axis ranges
    x, y = df[COLS["flip"]], df[COLS["mass"]]
    x0, x1, y0, y1 = *x.quantile([0.02, 0.98]), *y.quantile([0.02, 0.98])
    xpad, ypad = (x1 - x0) * 0.08, (y1 - y0) * 0.08
    
    # Size scaling
    bill_series = df[COLS["bill"]]
    bill_clipped = bill_series.clip(*bill_series.quantile([0.02, 0.98]))
    df["_size"] = 30 + (230 * (bill_clipped - bill_clipped.min()) / (bill_clipped.max() - bill_clipped.min() + 1e-12))
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f8f9fa')
    ax.set_facecolor('#ffffff')
    
    for sp, g in df.groupby(COLS["sp"]):
        ax.scatter(x=g[COLS["flip"]], y=g[COLS["mass"]], s=g["_size"], alpha=0.85,
                  color=COLORS[sp], edgecolor='white', linewidth=0.8, label=sp)
    
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.7)
    ax.set(xlabel="Flipper Length (mm)", ylabel="Body Mass (g)",
           xlim=(x0 - xpad, x1 + xpad), ylim=(y0 - ypad, y1 + ypad))
    
    # Stylish legend
    ax.legend(title="Species", framealpha=0.9, edgecolor='#dee2e6', facecolor='white',
              title_fontsize=11, fontsize=10, loc='upper left')
    
    # Add subtle border
    for spine in ax.spines.values():
        spine.set_edgecolor('#dee2e6')
        spine.set_linewidth(1.2)
    
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=160, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved: {OUT}")

if __name__ == "__main__":
    main()