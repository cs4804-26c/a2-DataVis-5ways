install.packages("ggplot2")
library(ggplot2)

penglings <- read.csv("../penglings.csv", na.strings = "NA")

r_plot <- ggplot(penglings, aes(x = flipper_length_mm,
                                y = body_mass_g,
                                color = species,
                                size = bill_length_mm)) +
  geom_point(alpha = 0.8) +
  labs(title = "Penguin Size by Species",
       x = "Flipper Length (mm)",
       y = "Body Mass (g)",
       size = "Bill Length (mm)",
       color = "Species") +
  scale_color_manual(values = c("Adelie" = "orange",
                                "Chinstrap" = "purple",
                                "Gentoo" = "blue"))

r_plot
