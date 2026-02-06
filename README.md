
![penguins](https://github.com/cs4804-24c/a2-DataVis-5Ways/assets/412089/accc5680-3c77-4d29-9502-d3ff8cd922af)

# 02-DataVis-5ways

Assignment 2 - Data Visualization, 5 Ways
Ayush Kulkarni
Link to Github Pages: https://ayushk2023.github.io/a2-DataVis-5ways/index.html
===

# Original Chart

![ggplot2](/docs/img/ggplot2.png)

# d3 Chart
![D3 Visualization](/docs/img/D3Viz.JPG)

For the d3 chart, I used the following resourcs:
chart: https://d3js.org/getting-started
tooltip: https://d3-graph-gallery.com/graph/interactivity_tooltip.html
legends: https://d3-graph-gallery.com/graph/custom_legend.html

I was able to recreate the graph close to the original. I attempted, but had difficulty with implementing grid lines and a legend for the size in d3. Adding enhancements such as a legend and tooltip were also relatively easy.

## Technical Achievements
- A tooltip functionality that shows the details of the data point on hover
- A legend for the species
- Tooltip for viewing data for each point

### Design Achievements
- Used built-in color scheme

# ggplot Chart
![ggplot Visualization](/docs/img/ggplotViz.JPG)

For the ggplot chart, I used the following resources:
chart: https://www.geeksforgeeks.org/r-language comprehensive-guide-to-scatter-plot-using-ggplot2-in-r/
save: https://ggplot2.tidyverse.org/reference/ggsave.html

This graph was also easy to create. The hardest part was getting r files to run properly on my system and display properly on my website. My workaround was to save the graph as a png and upload that onto the website. The legend was automatic, and formatting was completed accurately to the original. It was also easy to change the opacity.

## Technical Achievements
- Exported as png image to upload to website
- Legend for both size and species

### Design Achievements
- Grid layout
- similar layout as reference for axis labels and legend

# altair chart
![altair Visualization](/docs/img/AltairViz.JPG)

For the altair chart, I used the following resourcs:
sample: https://altair-viz.github.io/user_guide/data.html
I used chatGPT to assist in providing the method in which the chart could be integrated onto the website (saving as json file)

This was also relatively easy, although more complex than the previous charts to implement. Although it ended up being easy, references for filling in the data points and changing opacity were difficult to find. Despite having the title as a readable format in the code, the chart still appears with axis labels equivalent to the csv header names. Integrating this graph onto my website was more complex than I had anticipated, as it required cleaning up the "NaN" data values in the csv.

## Technical Achievements
- A tooltip functionality that shows the details of the data point on hover
- A legend for the species and bill-length

### Design Achievements
- Grid lines
- Adjust scale of data points

# gnuplot chart
![gnuPlot Visualization](/docs/img/GNUPlotViz.JPG)

For the gnuplot chart, I used the following resourcs:
docs: http://www.gnuplot.info/docs_6.0/Gnuplot_6.pdf
particularly the sections for plot, points & variable point properties, if and using commands, set styles, and csv files

This was the hardest to implement. This is because the documentation for this is complex, difficult-to-read, and lacks real examples. There were also no real examples available on the internet that I found. Therefore, I made a very simple design that met minimum requirements. However, setting up the environment for writing code, syntax, and outputting to png were easier than the other charts. 

## Technical Achievements
- A legend for the species
- PNG output

### Design Achievements
- tick marks at consistent increments

# datawrapper chart
![datawrapper Visualization](/docs/img/datawrapper.png)

This was the easiest method to implement, because it required no setup, the website had easy to navigate UI, and generated both png and website versions of the chart at the end. I could not figure out, however, how to change the location of the legends where they did not interfere with other elements of the chart or increase their size. The version on the website is dynamic to fit display size.

## Technical Achievements
- A tooltip functionality that shows the details of the data point on hover
- A legend for the species and bill-length

### Design Achievements
- Grid lines
- Adjust scale of data points
- Tooltip formatting
- Matching color scheme to reference chart