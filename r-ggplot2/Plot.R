penglings <- read.csv("../penglings.csv")

head(penglings)

library(ggplot2)

ggplot(penglings, aes(x=flipper_length_mm, y=body_mass_g, size=bill_length_mm, color=species)) + 
  geom_point(alpha=0.8) +
  theme_grey() +
  scale_color_manual(values = c(
    Adelie = "orange",
    Chinstrap = "purple",
    Gentoo = "darkcyan"
  )) +
  labs(x = "Flipper Length (mm)", y = "Body Mass (g)") +
  guides(
    size = guide_legend(order = 1),
    color = guide_legend(order = 2)
  )
