library(ggplot2)
library(plotly)

penguins <- read.csv("/Users/mariana/projects/a2-DataVis-5ways/penglings.csv")
penguins$species <- as.factor(penguins$species)

species_colors <- c(
  "Adelie" = "orange",
  "Chinstrap" = "purple",
  "Gentoo" = "turquoise"
)

p <- ggplot(
  penguins,
  aes(
    x = flipper_length_mm,
    y = body_mass_g,
    color = species,
    size = bill_length_mm,
    text = paste0(
      "Species: ", species,
      "<br>Flipper: ", flipper_length_mm, " mm",
      "<br>Body mass: ", body_mass_g, " g",
      "<br>Bill length: ", bill_length_mm, " mm"
    )
  )
) +
  geom_point(alpha = 0.8) +
  scale_color_manual(values = species_colors) +
  scale_size_continuous(range = c(2, 8)) +
  labs(
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    color = "Species",
    size = "Bill Length (mm)"
  ) +
  theme_classic(base_size = 12)

ip <- ggplotly(p, tooltip = "text") %>%
  layout(legend = list(orientation = "v"))

htmlwidgets::saveWidget(ip, "ggplot_interactive.html", selfcontained = TRUE)

ggsave("ggplot.png", p, width = 8, height = 5, dpi = 150)

print("Saved ggplot_interactive.html and ggplot.png")