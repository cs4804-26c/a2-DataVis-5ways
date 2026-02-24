library(ggplot2)
library(readr)

penguins <- read_csv("penglingsgg.csv")

ggplot(
  penguins,
  aes(
    x = flipper_length_mm,
    y = body_mass_g,
    color = species,
    size = bill_length_mm
  )
) +
  geom_point(alpha = 0.8) +
  scale_size_continuous(range = c(2, 8)) +
  scale_color_manual(
    values = c(
      "Adelie" = "red",
      "Chinstrap" = "orange",
      "Gentoo" = "yellow"
    )
  ) +
  labs(
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    title = "Penguins Body Mass vs Penguins Flipper Length"
  ) +
  theme(
    panel.background = element_rect(fill = "white"),
    plot.background  = element_rect(fill = "white"),
    panel.grid.major = element_line(color = "grey"),
    panel.grid.minor = element_line(color = "grey"),
    axis.text        = element_text(color = "black"),
    axis.title       = element_text(color = "black"),
    plot.title       = element_text(color = "black", hjust = 0.5)
  )

print(ggplot)
ggsave("penguins_ggplot.png", ggplot, width = 10, height = 8, dpi = 400)