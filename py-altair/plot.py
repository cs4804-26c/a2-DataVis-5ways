from pathlib import Path
import csv
import altair as alt

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTDIR = REPO_ROOT / "output"
OUTDIR.mkdir(exist_ok=True)
CSV_PATH = REPO_ROOT / "penglings.csv"

rows = []
with CSV_PATH.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        if r.get("species") in (None, "", "NA"):
            continue
        if r.get("flipper_length_mm") in (None, "", "NA"):
            continue
        if r.get("body_mass_g") in (None, "", "NA"):
            continue
        if r.get("bill_length_mm") in (None, "", "NA"):
            continue

        try:
            rows.append({
                "species": r["species"],
                "flipper_length_mm": float(r["flipper_length_mm"]),
                "body_mass_g": float(r["body_mass_g"]),
                "bill_length_mm": float(r["bill_length_mm"]),
            })
        except ValueError:
            continue

print("Loaded rows:", len(rows))

species_order = ["Adelie", "Chinstrap", "Gentoo"]
palette = ["#F28E2B", "#8E44AD", "#1F9E89"]

chart = (
    alt.Chart(alt.Data(values=rows))
    .mark_circle(opacity=0.8)
    .encode(
        x=alt.X(
            "flipper_length_mm:Q",
            title="Flipper Length (mm)",
            scale=alt.Scale(domain=[170, 232]),
            axis=alt.Axis(values=list(range(170, 231, 10))),
        ),
        y=alt.Y(
            "body_mass_g:Q",
            title="Body Mass (g)",
            scale=alt.Scale(domain=[2600, 6400]),
            axis=alt.Axis(values=[3000, 4000, 5000, 6000]),
        ),
        color=alt.Color(
            "species:N",
            scale=alt.Scale(domain=species_order, range=palette),
            legend=alt.Legend(title="species"),
        ),
        size=alt.Size(
            "bill_length_mm:Q",
            scale=alt.Scale(domain=[35, 55]),
            legend=alt.Legend(title="bill_length_mm", values=[40, 50]),
        ),
        tooltip=["species:N", "flipper_length_mm:Q", "body_mass_g:Q", "bill_length_mm:Q"],
    )
)

out_html = OUTDIR / "altair.html"
chart.save(str(out_html))
print("Wrote:", out_html)
