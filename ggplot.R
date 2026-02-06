install.packages("ggplot2")
library(ggplot2)

data <- read.csv("penglings.csv")

p <- ggplot(data, aes(
    x = flipper_length_mm, 
    y = body_mass_g,
    color = species,
    size = bill_length_mm
    )) + 
    geom_point(alpha = 0.8) + 
    scale_color_manual(
        values = c(
            "Adelie" = "orange",
            "Chinstrap" = "purple",
            "Gentoo" = "#008080"
        )
    ) +
    labs(
        x = "Flipper Length (mm)",
        y = "Body Mass (g)"
    ) +
    scale_size(range = c(2,8), trans = "sqrt")

print(p)