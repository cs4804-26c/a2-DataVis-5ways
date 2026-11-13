library(ggplot2)

penguins <- read.csv("../penglings.csv")

p <- ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g,
                          color = species, size = bill_length_mm)) +
  geom_point(alpha = 0.8, na.rm = TRUE) +
  scale_color_manual(values = c(Adelie = "darkorange",
                                Chinstrap = "purple",
                                Gentoo = "cyan4")) +
  labs(x = "Flipper Length (mm)", y = "Body Mass (g)")

ggsave("../img/ggplot2.png", p, width = 8.5, height = 5.3, dpi = 200)
