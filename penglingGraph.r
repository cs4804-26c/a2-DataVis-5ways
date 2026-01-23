library(ggplot2)

penglings <- read.csv("C:/Users/Ben/Data Vis. Assignment Folder/a2/penglings.csv")

ggplot(penglings, aes(flipper_length_mm, body_mass_g, color = species, size = bill_length_mm)) +
    geom_point(alpha = 0.7) +
    labs(x = "Flipper Length (mm)", y = "Body Mass (g)")