# d3

D3.js provided granular control but was code-intensive, requiring manual asynchronous data loading and DOM construction. 
I explicitly filtered "NA" values from `penglings.csv` to prevent scale errors.

**Achievements:**
- **Technical:** Implemented interactive tooltips and dynamic hover strokes to inspect overlapping points.
- **Design:** Used `d3.scaleSqrt` for perceptually accurate size mapping 

**Future:** Ideal for highly custom, interactive web visualizations where pixel-perfect control is necessary.


# Python Altair

Altair is a declarative statistical visualization library for Python. 
Unlike D3's imperative approach, Altair allows you to describe *what* you want the chart to look like rather than *how* to draw it.
The declarative syntax is incredibly concise. Mapping `flipper_length_mm` to the x-axis and `species` to color took only a few lines of readable code. 
Handling the "zero=False" requirement was as simple as adding `scale=alt.Scale(zero=False)`.

**Achievements :**
- **Technical:** I added a bound selection to the legend. You can **click on a species in the legend** to highlight those points and fade out the others. 
I also enabled Pan/Zoom and Tooltips.
- **Design:** Used the `category10` color scheme for clear categorical distinction and adjusted opacity to 0.8 to handle overplotting.


# R + ggplot2

R is a language primarily focused on statistical computing, and `ggplot2` is its most famous visualization package based on the "Grammar of Graphics" philosophy.

- **Design:** I manually tuned the `scale_size` range to ensure the differences in bill length were visually distinguishable but not overwhelming. 
- I also utilized `check.names = FALSE` during data loading to preserve the original column headers, simplifying the axis labeling process.


# DataWrapper
This was the fastest tool to use. I simply uploaded the penglings.csv file, selected "Scatter Plot," 
and assigned the columns to the axes. The interface automatically handled the data parsing

-**Technical:** Datawrapper automatically generates interactive tooltips. I didn't need to write any event listeners

