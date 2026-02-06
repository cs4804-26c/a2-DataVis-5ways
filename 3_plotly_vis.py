import plotly.express as px
from pathlib import Path
import pandas as pd

DATA, OUT = "penglings.csv", Path("img") / "plotly_scatter.html"
COLS = {"sp": "species", "bill": "bill_length_mm", "flip": "flipper_length_mm", "mass": "body_mass_g"}

def main():
    df = pd.read_csv(DATA)[COLS.values()].dropna()
    
    # Size scaling 
    bill_series = df[COLS["bill"]]
    bill_clipped = bill_series.clip(*bill_series.quantile([0.02, 0.98]))
    df["size_norm"] = 10 + (30 * (bill_clipped - bill_clipped.min()) / (bill_clipped.max() - bill_clipped.min() + 1e-12))
    
    # Plotly plot
    fig = px.scatter(df, x=COLS["flip"], y=COLS["mass"], color=COLS["sp"],
                     size="size_norm", opacity=0.85,
                     labels={COLS["flip"]: "Flipper Length (mm)", 
                             COLS["mass"]: "Body Mass (g)",
                             COLS["sp"]: "Species"},
                     color_discrete_map={"Adelie": "#5d8769", 
                                         "Chinstrap": "#3348b4", 
                                         "Gentoo": "#c25cb5"})
    
    # Layout
    fig.update_layout(
        xaxis=dict(
            range=[170, 235], 
            title="Flipper Length (mm)"
        ),
        yaxis=dict(
            range=[2500, 6500],  
            title="Body Mass (g)"
        ),
        plot_bgcolor='white',
        paper_bgcolor='#f8f9fa',
        showlegend=True,
        legend=dict(
            title="Species",
            bgcolor='white',
            bordercolor='lightgray',
            borderwidth=1
        ),
        width=1000,
        height=600
    )
    
    # Remove size from legend hover text and marker borders
    fig.update_traces(
        marker=dict(line=dict(width=1, color='white')),
        hovertemplate="<b>%{fullData.name}</b><br>Flipper: %{x} mm<br>Mass: %{y} g<br><extra></extra>"
    )
    
    # Hide size legend (to only show species)
    fig.update_layout(legend_traceorder="normal")
    
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.write_html(OUT)
    print(f"Saved: {OUT}")

if __name__ == "__main__":
    main()