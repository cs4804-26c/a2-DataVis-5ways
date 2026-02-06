library(ggplot2)

penguins <- read.csv("penglings.csv")

p <- ggplot(penguins, aes(
  x = flipper_length_mm,
  y = body_mass_g,
  color = species,
  size = bill_length_mm
)) +
  geom_point(alpha = 0.8) +
  scale_x_continuous(limits = c(170, 240)) +
  scale_y_continuous(limits = c(2500, 6500)) +
  labs(
    x = "Flipper Length (mm)",
    y = "Body Mass (g)"
  ) +
  theme_minimal()

ggsave(
  filename = "ggplot.png",
  plot = p,
  width = 8,
  height = 5,
  dpi = 150
)
