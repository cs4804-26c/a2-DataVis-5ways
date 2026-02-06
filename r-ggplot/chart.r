library(ggplot2)
library(plotly)
library(htmlwidgets)

penglings <- read.csv("../penglings.csv")

chart <- ggplot(penglings, aes(
  x = flipper_length_mm,
  y = body_mass_g,
  size = bill_length_mm,
  color = species,
  text = paste0(
    "Species: ", species,
    "<br>Flipper: ", flipper_length_mm, " mm",
    "<br>Body Mass: ", body_mass_g, " g",
    "<br>Bill: ", bill_length_mm, " mm"
  )
)) +
  geom_point(alpha = 0.8) +
  labs(
    x = "Flipper Length (mm)",
    y = "Body Mass (g)"
  ) +
  scale_size(
    range = c(2, 8),
    breaks = c(40, 50),
    name = "bill_length_mm",
    guide = guide_legend(order = 2)
  ) +
  scale_color_manual(values = c(
    Adelie = "#F28E2B",
    Chinstrap = "#7B3C9B",
    Gentoo = "#1B9E77"
  )) +
  guides(color = guide_legend(order = 1)) +
  theme_minimal(base_family = "Comic Sans MS") +
  theme(text = element_text(family = "Comic Sans MS"))

interactive <- ggplotly(chart, tooltip = "text") |>
  layout(font = list(family = "Comic Sans MS"))
saveWidget(interactive, "chart.html")
