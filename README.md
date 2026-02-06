# Assignment 2 - Data Visualization, 5 Ways  


## JavaScript + D3

I built the scatterplot in the browser using SVG with d3. Once the scales were set up, mapping color by species and size by bill length was pretty straightforward. The harder part was loading the CSV asynchronously and keeping the axis ticks consistent while adding hover. I could see d3 being useful in the future when you need very custom visuals or interactions on the web. The main workaround I used was manually setting the axis domains and tick values to match the reference chart.

<img src="img/d3-new.png" alt="d3" width="600">

## R + ggplot2

ggplot2 made the basic chart quick to build by mapping x, y, color, and size through aesthetics. The harder part was matching the non-zero axis scales and getting the tick breaks to look like the reference. I could see ggplot2 being useful for making clean plots quickly for reports or papers. To get closer to the reference, I limited bill length to a fixed range for consistent sizing and set explicit scale breaks.

<img src="img/r-ggplot2.png" alt="d3" width="600">

## Python + Altair

Altair’s style made it easy to set up the encodings without a lot of code. The hardest part was matching the axis domains and tick values to the reference. I could see Altair being useful for quick interactive prototypes, and the hover highlight and tooltip were easy to add. The main tweak I made was setting explicit domains and tick values so the chart matched more closely.

<img src="img/altair.png" alt="d3" width="600">

## JSON + Vega-Lite

Vega-Lite is compact and maps directly to the encodings, which made it pretty straightforward to build the scatterplot. Gridlines and legends were easy to include, but matching axis domains and tick values took more effort. I could see Vega-Lite being useful when you want a small, portable chart that can render in different places. The main tweak I made was setting explicit tick values for 1000-unit steps, and I added a simple hover selection for interaction.

<img src="img/vega.png" alt="d3" width="600">

## Python + Plotly

Plotly made it easy to produce a polished chart quickly. Setting ranges, gridlines, and colors was straightforward, but matching tick spacing and the legend layout took more work. I could see Plotly being useful for dashboards where you want something clean and presentable fast. The main adjustment I made was nudging the margins and the legend position to avoid clipping.

<img src="img/plotly.png" alt="d3" width="600">


## Technical Achievements
- **Hover interactions**: Built tooltips + hover highlights in d3, Altair, and Vega‑Lite so you can inspect values without changing the chart.
- **Explicit scales**: Set non-zero domains and specified tick values/breaks in each tool to match the reference as closely as possible.
- **Data cleaning**: Filtered out rows with missing values so only valid points were plotted.

### Design Achievements
- **Shared visual language**: Kept the same species colors and size range across all tools so the charts read the same.
- **Custom fonts**: Applied a custom font in the web‑based charts to keep labels and legends consistent.
- **Legend + grid consistency**: Kept legends and gridlines consistent across all visualizations.
