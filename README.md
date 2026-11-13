Randy Gomez

# a2-DataVis-5ways
Assignment 2 - Data Visualization, 5 Ways. Each tool recreates the same exact scatterplot: flipper length (x) vs. body mass (y), colored by species, sized by bill length, 0.8 opacity, non-zero axes.

Libraries and tools: 
# ggplot2, Altair, d3, Vega-Lite, Matplotlib.

# R/ggplot2
ggplot2 was the easiest tool. `geom_point(alpha = 0.8)` and `aes(color = species, size = bill_length_mm)` reproduced the OG graph. The only change was `scale_color_manual()` with `darkorange`, `purple`, `cyan4` to match the color scheme.
![ggplot2](img/ggplot2.png)

# Altair
Altair shows the chart using `mark_circle(opacity=0.8)` and `x`, `y`, `color`, `size`. Two things needed to change specifically, `scale=alt.Scale(zero=False)` so the axes don't start at 0 and an explicit size `range` so bill length is visible. `tooltip` and `.interactive()`, the zoom and zoom out were short implementations. Great overall for a lot. Code: `altair/penguins.py` or open `altair/penguins.html` for the interactive version.
![Altair](img/altair.png)

# d3
d3 is the most busy work stuff: scales, axes, axis labels, legend, and tooltips are all manual. The key thing to note that I had to was that `d3.csv` is asynchronous, so everything is drawn inside `.then()`. I also filter out rows with `NA` values. I set tick values and used a radius scale instead of an area scale, so size is a little less perceptually accurate than ggplot2's. 
You gotta run a local server from the repo root (`python3 -m http.server`) and open `/d3/`. Code: `d3/index.html`, `d3/chart.js`.

![d3](img/d3.png)

# Vega-Lite
Vega-Lite is nearly the same as Altair but written as a JSON, which makes it easy to embed in any web page with `vega-embed`. Same two fixes as Altair: `zero: false` and a size range. Code: `vega-lite/spec.json`, `vega-lite/index.html`.
![Vega-Lite](img/vega-lite.png)

# Matplotlib
Matplotlib is the most standard Python plotting library and Ahrens agreed it was an easy pick, and it runs fully offline and writes the PNG directly. It was a bit more manual than the declarative tools, there is no "color by column" option, so I loop over species and call `ax.scatter()` once per group, and the marker area is computed by hand like this: (`s=(bill_length - 25) * 4`). Opacity (`alpha=0.8`), non-zero axes, and tick marks every 10 mm / 1000 g were each a line. Code: `matplotlib/penguins.py`.
![Matplotlib](img/matplotlib.png)

# Technical Achievements
- Tooltips on hover: in d3, Altair, and Vega-Lite showing species, bill length, flipper length, and body mass.
- Pan/zoom in the Altair version.

# Design Achievements
- Consistent colors across all five charts: orange `#ff8c00`, purple `#a020f0`, teal `#008b8b`.
- Tuned size ranges so bill length differences are visible without hiding the points behind each other.