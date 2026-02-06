library(ggplot2)

penguins <- read.csv("penglings.csv")

penguins <- na.omit(penguins[, c("flipper_length_mm",
                                 "body_mass_g",
                                 "bill_length_mm",
                                 "species")])

p <- ggplot(penguins,
            aes(x = flipper_length_mm,
                y = body_mass_g,
                color = species,
                size = bill_length_mm)) +
  geom_point(alpha = 0.8) +
  scale_color_manual(values = c(
    "Adelie" = "#F28E2B",
    "Chinstrap" = "#8E44AD",
    "Gentoo" = "#1B9E9E"
  )) +                                 
  scale_x_continuous(limits = c(170, 235)) +
  scale_y_continuous(limits = c(2700, 6200)) +
  labs(x = "Flipper Length (mm)",
       y = "Body Mass (g)") +
  theme_classic()

ggsave("ggplot.png", plot = p, width = 8, height = 5, dpi = 200)
