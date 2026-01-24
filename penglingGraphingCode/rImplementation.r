install.packages("ggplot2")
library(ggplot2)

penglings <- read.csv("..penglings.csv")

ggplot(penglings, aes(flipper_length_mm, body_mass_g, color = species, size = bill_length_mm)) +
    geom_point(alpha = 0.7) +
    labs(x = "Flipper Length (mm)", y = "Body Mass (g)")

