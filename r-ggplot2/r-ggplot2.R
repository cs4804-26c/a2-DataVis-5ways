library(ggplot2)

getwd()
penguins_data <- read.csv("../penglings.csv", stringsAsFactors = FALSE)
head(penguins_data)

ggplot(data = penguins_data, 
       aes(x = flipper_length_mm, y = body_mass_g, 
           color = species, size = bill_length_mm)) +
  geom_point(alpha = 0.8) + 
  scale_color_manual(values = c("Adelie" = "#fda147", 
                                "Chinstrap" = "#ab5ad3", 
                                "Gentoo" = "#48a1a0")) +
  scale_size(range = c(3, 6)) +  
  theme_minimal() +
  labs(
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    size = "bill_length_mm",
    color = "species"
  ) +
  guides(
    size = guide_legend(order = 1),   # size legend first
    color = guide_legend(order = 2)   # color legend second
  )
