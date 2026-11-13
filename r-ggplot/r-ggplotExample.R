library(ggplot2)
library(ggiraph)
library(htmlwidgets)

penguins <- read.csv("penglings.csv", na.strings = "NA")

required <- c("flipper_length_mm", "body_mass_g", "bill_length_mm")
penguins <- penguins[complete.cases(penguins[required]), ]

p <- ggplot(
  penguins,
  aes(
    x = flipper_length_mm,
    y = body_mass_g,
    color = species,
    group = species
  )
) +
  geom_point_interactive(
    aes(size = bill_length_mm, data_id = species),
    alpha = 0.8
  ) +
    geom_smooth_interactive(
    aes(data_id = species),
    method = lm, se = FALSE,
    color = "black", linewidth = 1.8,
    show.legend = FALSE
  ) +
  geom_smooth_interactive(
    aes(data_id = species),
    method = lm, se = FALSE,
    linewidth = 0.9,
    show.legend = FALSE
  ) +
  scale_color_manual_interactive(
    values = c(
      Adelie = "#FF8C00",
      Chinstrap = "#A032D2",
      Gentoo = "#008B8B"
    ),
    data_id = function(breaks) breaks
  ) +
  scale_x_continuous(limits = c(170, 235), expand = c(0, 0)) +
  scale_y_continuous(limits = c(2500, 6500), expand = c(0, 0)) +
  labs(
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    color = "Species",
    size = "Bill Length (mm)"
  )

ggsave(
  "r-ggplot/penguins.png",
  plot = p, width = 7, height = 5, dpi = 150
)

interactive_chart <- girafe(
  ggobj = p,
  width_svg = 7,
  height_svg = 5,
  options = list(
    opts_hover(css = "opacity:1;", linked = TRUE),
    opts_hover_key(css = "opacity:1;"),
    opts_hover_inv(css = "opacity:0.1;")
  )
)

saveWidget(
  interactive_chart,
  "r-ggplot/penguins.html",
  selfcontained = TRUE
)



