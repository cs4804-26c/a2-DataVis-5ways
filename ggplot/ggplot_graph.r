install.packages("ggplot2")

library(ggplot2)

penguins <- read.csv("penglings.csv")

p <- ggplot(penguins, aes(x = flipper_length_mm, 
                    y = body_mass_g, 
                    color = species, 
                    size = bill_length_mm)) +
     # add regression line
     geom_smooth(method = "lm", se = FALSE, size = 0.5, alpha = 0.4) +
     geom_point(alpha = 0.8) +
     scale_x_continuous(limits = c(170, 235)) +
     scale_y_continuous(limits = c(2500, 6500)) +
     scale_size_continuous(breaks = c(40, 50), range = c(1, 6)) +

     scale_color_manual(values = c("Adelie" = "#FDA247", 
                                "Chinstrap" = "#AC5AD4", 
                                "Gentoo" = "#4AA1A1")) +
  
     labs(title = "Penguin Size: Flipper vs Body Mass",
       x = "Flipper Length (mm)",
       y = "Body Mass (g)",
       size = "Bill Length (mm)",
       color = "Species") +
     theme_grey()

print(p)