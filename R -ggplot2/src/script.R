library(ggplot2)

penguins <- read.csv("penglings.csv", stringsAsFactors = TRUE)
penguins <- na.omit(penguins)

plot <- ggplot(penguins, aes(x = flipper_length_mm,
                             y = body_mass_g,
                             color = species,
                             size = bill_length_mm)) +
  geom_point(alpha = 0.8) +
  labs(title = "Penguin Size: Flipper Length vs Body Mass",
       x = "Flipper Length (mm)",
       y = "Body Mass (g)",
       size = "Bill Length (mm)",
       color = "Species") +
  scale_color_manual(values = c("Adelie" = "#E57C58",
                                "Chinstrap" = "#353A4C",
                                "Gentoo" = "#9C74B5"))

ggsave("img/r-ggplot2.png", plot = plot, width = 8, height = 5)