# R + ggplot2 + plotly + HTML widgets

R is a language used for statistical computing and data visualization. ggplot2 is a data visualization library in R. plotly is a graphing library that allows for interactive graphs.
HTML widgets is a framework that can embed interactive visualizations without requiring Javascript coding.

I created a static visualization of the penglings dataset using ggplot2's geom_point(), aesthetic functions for the color and size of the data points, and labs() for the axis labels. The colors are hex codes that match the colors of the graph we were tasked with replicating. Creating a manual color scale and using hex codes let me keep consistent colors across all of my graphs.
I created an interactive visualization using plotly. When mousing over a point, a box appears showing the Flipper length, body mass, species, and bill length of the penguin that is represented by that data point. The box disappears when the mouse is removed.

Examples and documentation for ggplot2 and plotly were abundant and easy to find. ggplot2 allows for a diverse visualization with little code. The biggest barrier was familiarizing myself with the goem_point() and aes() functions since I had no previous experience with these.

![ggplot2](img/MVggplot2_plot.png)
## Link to interactive plot
https://morganvazy.github.io/a2-DataVis-5ways/R/penglings_R_interactive.html
## Technical Achievements
- Hover feature that shows the penguin's flipper length, body mass, species, and bill length using plotly.
## Design Achievements
- created a manual color scale with hex codes so colors were accurate to the original reference picture (hex codes: Adelie - #FA9702, Chinstrap - #B802FA, Gentoo - #018A75)
## Sources & References
- https://www.sthda.com/english/wiki/ggplot2-scatter-plots-quick-start-guide-r-software-and-data-visualization - reference for scatterplot
- https://ggplot2.tidyverse.org/reference/labs.html - used for axis labels
- https://stackoverflow.com/questions/37465285/interactive-scatter-plots-in-r-overlay-hover-summary-tooltip-as-user-supplied-p - used for hover feature

# Vega-Lite + JSON
Vega-Lite is a high level grammar used to create interactive visuals with JSON.
I created a scatterplot of the penglings data with a tooltip for hovering over data points. I explicitly coded in the values for tick marks to match the tick marks on the R graph. For the colors representing each pengin species, I used the same hex codes as for the R graph and created a scale that mapped the hex codes to each species. When hovering over a data point, the flipper length, body mass, species, and bill length appear in a box to the side of the point.

There are many strong resources on vega-lite and many examples of scatterplots. Adding the tooltip for interactivity was relatively straightforward and was easily scalable to display many fields when hovering. I felt like the sizes of each data point first generated based on bill length were appropriate and made for a legible graph. After replicating the graph, there was very little additional customization necessary in order to make the graph legible. I think Vega-Lite is a strong choice for someone looking for customizability without overwhlemingly complex syntax.

![Vega-Lite](img/Vega-Lite_plot.png)

## Link to interactive plot
https://morganvazy.github.io/a2-DataVis-5ways/Vega-Lite/penglings_Vega-Lite_interactive.html
## Technical Achievements
- Hover feature that shows the penguin's flipper length, body mass, species, and bill length using a tooltip.
## Design Achievements
- created a manual color scale with hex codes so colors were consistent across graphs (hex codes: Adelie - #FA9702, Chinstrap - #B802FA, Gentoo - #018A75)
- consistent tick marks values on x and y axis as all other graphs
## Sources & References
- https://vega.github.io/vega-lite/examples/point_2d.html
- https://vega.github.io/vega-lite/tutorials/explore.html
- https://vega.github.io/vega-lite/docs/scale.html
- https://vega.github.io/vega-lite/docs/axis.html

# d3 + Javascript
D3 is a open-source JavaScript library used to create interactive data visualizations with high levels of customizability. I replicated the Penglings scatterplot using the same colors and tick mark values as previously. The tickmarks were coded in by creating a d3.ticks() object and passing in the start value, end value, and number of intervals. The same was done for the y axis and these objcts were then passed into the variable for the x axis. When you hover over a point, the species, flipper length, body mass, and bill length of that point appear in a box to the side of the point.

D3 allows for highly customizable plots, however, I had to explicitly code many of the visual design components that were assumed in R and Vega-Lite. For example, the design for the box that holds the data for a point when hovering over it was already decided on in Vega-Lite and R and was legible. In D3, I had to explicitly code in the background color and border of the box in order to make it legible. I also had many issues trying to put margins for the graph and trying to figure out where the axis labels should lie. In the beginning, the labels were overlapping with the axis itself. Additionally, I had to set a range of pixel values for the size of the dots because without doing so, all of the points were extremely large and the graph became illegible. For more difficult or uncommon visualizations, D3 is a strong choice, but it felt slightly unnecessary for the scatterplot. While there are many resources for D3, I had to do a lot of searching and search term engineering to find a case that fit my needs.

![d3](img/d3_plot.png)

## Link to interactive plot
https://morganvazy.github.io/a2-DataVis-5ways/d3/penglings_D3.html
## Technical Achievements
- Hover feature that shows the penguin's flipper length, body mass, species, and bill length using a tooltip.
## Design Achievements
- created a manual color scale with hex codes so colors were consistent across graphs (hex codes: Adelie - #FA9702, Chinstrap - #B802FA, Gentoo - #018A75)
- consistent tick marks values on x and y axis as all other graphs
## Sources & References
- //https://d3-graph-gallery.com/graph/scatter_basic.html - reference for scatterplot code
- https://d3-graph-gallery.com/graph/interactivity_tooltip.html - tooltip for interactivity
- https://stackoverflow.com/questions/11189284/d3-axis-labeling - x-axis labeling
- https://d3-graph-gallery.com/graph/scatter_grouped.html - coloring based on species
- https://d3js.org/d3-scale/linear - adding size based on bill length
- https://observablehq.com/@d3/d3-extent
- https://medium.com/@kj_schmidt/hover-effects-for-your-scatter-plot-447df80ea116 - used for the logic on mouseover event
- https://chatgpt.com/ - used to help tailor the event logic to the correct D3 version

# Tableau
Tableau is a visual analytics platform. I created a scatterplot of the Penglings data in Tableau. I did not include the specific hex codes for the colors, but I chose a color palette and selected colors that were close to the colors that have been used in the other graphs. The x-axis ticks automatically used the same scale as the other graphs, but there were twice as many y-axis ticks so the spacing between each is half the size.

Tableau is relatively intuitive and I was able to figure out how to make and customize the scatterplot by playing around with Tableau. I did not have to add the hover feature in Tableau as it was done automatically. The Tableau graph also has a feature where selecting a species on the legend to the right highlights only that species on the graph and grays out the other species. You can also exclude different species. For a scatterplot with common colors, it was easy to replicate and to add interactivity. However, I could see it being difficult to customize this graph or other more complex graph types using Tableau as compared to Vega-Lite or R.
![d3](img/tableau_plot.png)

## Link to interactive plot
https://public.tableau.com/app/profile/morgan.vasiliou/viz/penglings-tableau/Sheet1?publish=yes
## Technical Achievements
- Hover feature that shows the penguin's flipper length, body mass, species, and bill length.
## Design Achievements
- color scheme was selected to remain consistent with the other graphs' coloring. 

# Vega Altair + Python
Vega-Altair is a visualization library for python built on Vega-Lite and Vega grammars. I replicated the Penglings scatterplot using the same hex codes for the colors and tick mark values as previously. The tick marks were explicitly coded in using alt.Axis (values = []). I added the same hover feature that shows flipper length, body mass, species, and bill length using a tooltip and .interactive().

There were sufficient resources for Vega altair and I felt like the examples were straightforward. However, I did have to synthesize a couple different resources to learn enough to replicate this plot. I preferred this Vega resource over Vega-Lite as Vega-altair felt much simpler and more concise than Vega-Lite. However, both libraries were concise and can add customization without much effort.
![d3](img/altair_plot.png)

## Link to interactive plot
https://morganvazy.github.io/a2-DataVis-5ways/altair/penglings_altair.html
## Technical Achievements
- Hover feature that shows the penguin's flipper length, body mass, species, and bill length using a tooltip and .interactive().
## Design Achievements
- created a manual color scale with hex codes so colors were consistent across graphs (hex codes: Adelie - #FA9702, Chinstrap - #B802FA, Gentoo - #018A75)
- consistent tick marks values on x and y axis as all other graphs
## Sources & References
- https://altair-viz.github.io/gallery/scatter_tooltips.html - scatterplot syntax and tooltip
- https://altair-viz.github.io/user_guide/customization.html - axis labels, color customization
- https://altair-viz.github.io/user_guide/generated/channels/altair.Size.html - size of the points
- https://altair-viz.github.io/user_guide/generated/core/altair.Axis.html - tick marks for the axis
