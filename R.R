library(ggplot2)
library(readr)

penguins <- read_csv("penglings.csv")

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
  scale_color_manual(
    values = c(
      "Adelie" = "#F28E2B",
      "Chinstrap" = "#8E63CE",
      "Gentoo" = "#1B9E9E"
    )
  ) +
  scale_size_continuous(range = c(4, 10)) +
  labs(
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    color = "species",
    size = "bill_length_mm"
  ) +
  theme_gray()
