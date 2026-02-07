library(ggplot2)

penguins <- read.csv("../../penglings.csv")

ggplot(data = penguins, aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point(aes(color = species, size = bill_length_mm), alpha = 0.8) +
  
  labs(
    x = "Flipper Length (mm)",
    y = "Body Mass (g)"
  ) +
  
  scale_color_manual(values = c(
    "Adelie" = "#fda246",
    "Chinstrap" = "#ac5ad4",
    "Gentoo" = "#49a1a1"
  )) +

  scale_size(range = c(2, 6)) +
  
  theme_minimal() +
  theme(

    plot.background = element_rect(fill = "white", color = NA),
    panel.background = element_rect(fill = "#ebebeb", color = NA),
    legend.background = element_rect(fill = "#ebebeb", color = NA),

    panel.grid.major = element_line(color = "white"),
    panel.grid.minor = element_line(color = "white"),

    legend.key = element_rect(fill = NA, color = NA)
  )
