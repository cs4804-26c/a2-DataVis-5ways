#Using Statistical tools for high-throughput
#data analysis ggplot2 scatter plots quick guide
#as reference
#https://ggplot2.tidyverse.org/reference/labs.html for labels

library(ggplot2)
library(plotly)
library(htmlwidgets)

#create a static scatterplot with Penglings data
#create a color scale with hex values
static <- ggplot(penglings, aes(x=flipper_length_mm, y=body_mass_g
  )) + geom_point(aes(color=species, size=bill_length_mm), alpha=0.8) +
  scale_color_manual(values = c("Adelie" = "#FA9702", "Chinstrap"="#B802FA", "Gentoo"="#018A75")) +
  labs(
    x = "Flipper length (mm)",
    y = "Body mass (g)"
  )

#make the graph interactive & add a feature where hovering over a point shows its values
#https://stackoverflow.com/questions/37465285/interactive-scatter-plots-in-r-overlay-hover-summary-tooltip-as-user-supplied-p
interactive <- ggplotly(static)

#turning it into html file to retain interactivity
#https://stackoverflow.com/questions/37465285/interactive-scatter-plots-in-r-overlay-hover-summary-tooltip-as-user-supplied-p
htmlwidgets::saveWidget(
  interactive, "penglings_R_interactive.html",selfcontained=TRUE
)

#save an image of the plot
ggsave(filename = "img/MVggplot2_plot.png",width=7,height=5,dpi=300)
