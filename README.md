
![penguins](https://github.com/cs4804-24c/a2-DataVis-5Ways/assets/412089/accc5680-3c77-4d29-9502-d3ff8cd922af)

# 02-DataVis-5ways

Assignment 2 - Data Visualization, 5 Ways  
===

## Dataset
All visualizations in this project use the penguins dataset. Each row represents a penguin observation and includes measurements such as flipper length, body mass, bill length, and species. Across all tools, the same visual encodings are used:
- X-axis: Flipper Length (mm)
- Y-axis: Body Mass (g)
- Color: Species
- Size: Bill Length (mm)
- Opacity: Applied to reduce overplotting

# R + ggplot2 + R Markdown

R is a language primarily focused on statistical computing, and ggplot2 is a powerful library for creating declarative visualizations. I used geom_point() to create a scatterplot and mapped color to species and size to bill length.

The static version was saved as a PNG, and I also created an interactive HTML version using plotly, which allows hovering over points to see exact values.

While it took some time to find the correct documentation for exporting interactive plots, ggplot2 made it relatively easy to build a clean and readable visualization once the mappings were set up.

<img width="831" height="519" alt="R" src="https://github.com/user-attachments/assets/485987d1-c46e-4c95-bd17-d8d370a514b4" />

# Python + Altair

Altair is a declarative visualization library for Python that makes it easy to build interactive charts. I used Altair to recreate the same scatterplot with tooltips showing species, flipper length, body mass, and bill length.

Altair handled interactivity automatically, which made hover interactions very straightforward to implement. I also explicitly disabled zero-based axes so the chart focused on the actual data range.

The final visualization was exported as an interactive HTML file.

<img width="813" height="497" alt="altair" src="https://github.com/user-attachments/assets/43aea990-8b5a-4e78-b597-b7c38891b526" />

# d3...

d3 is a low-level JavaScript library for building custom visualizations in the browser. For this version, I loaded the dataset using d3.csv, which required running a local web server due to asynchronous data loading.

This visualization includes:
- Scaled axes that do not start at zero
- Color encoding for species
- Size encoding for bill length
- Hover tooltips that display all relevant values

Compared to the other tools, d3 required the most code, but it also provided the most control over layout and interaction.

<img width="725" height="543" alt="d3" src="https://github.com/user-attachments/assets/b2b95a66-58c1-4ec1-89b4-ea2699fc7efd" />

# Datawrapper

Datawrapper was used as one of the visualization tools to recreate the same scatterplot. I mapped flipper length to the x-axis, body mass to the y-axis, color to species, and size to bill length.

While Datawrapper correctly applies the size encoding, the differences in bill length are relatively small, so the bubble size variation is very subtle. The size legend is included to explain the mapping, even though the visual differences are not highly pronounced.

<img width="536" height="403" alt="datawrapper" src="https://github.com/user-attachments/assets/3c065e02-373e-4033-8327-102894acb943" />

# Flourish

Flourish was used as the second visualization tool. Similar to Datawrapper, I mapped size to bill length, but Flourish automatically normalizes symbol sizes and does not provide direct control over minimum and maximum bubble size.

Because bill length values fall within a narrow range, the resulting size differences are there but difficult to distinguish visually. Despite this, the encoding is technically correct and consistent with the other visualizations.

<img width="1073" height="546" alt="flourish" src="https://github.com/user-attachments/assets/33058f76-2d5d-406c-81f7-5928ca03ea76" />

## Technical Achievements
- Created the same visualization using three libraries (ggplot2, Altair, d3) and two tools (Datawrapper, Flourish).
- Implemented interactive hover tooltips in Altair and d3.
- Loaded external data asynchronously in d3 using d3.csv.
- Made sure axes do not start at zero and are scaled to the data range.
- Exported both static and interactive visualizations.

### Design Achievements
- Used a consistent color scheme for species across all visualizations.
- Applied opacity to reduce overplotting.
- Included legends and axis labels to clearly communicate visual encodings.
- Prioritized accurate data representation over exaggerating visual differences.
