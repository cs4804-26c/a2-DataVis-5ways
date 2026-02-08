library(ggplot2)

# r is silly. I had to put the file in the same folder
penguins <- read.csv("penglings.csv")

colors <- c("Adelie" = "#F09539", "Chinstrap" = "#8E3BC6", "Gentoo" = "#3C898A")
# this article helped me see what i could do with this library https://songbiaozhu.github.io/ggplot2-legend-adjustment-methods/
ggplot(penguins, aes(x = flipper_length_mm, 
                     y = body_mass_g,
                     color = species,
                     size = bill_length_mm)) +
  geom_point(alpha = 0.8, stroke = 2, aes(fill = species), shape = 21) +
  scale_color_manual(values = colors) +
  scale_fill_manual(values = colors) +
  scale_size_continuous(range = c(2, 6), breaks = c(40, 50)) +
  scale_x_continuous(limits = c(169, 234),
                     breaks = seq(170, 231, 10)) + # need manual for some reason - the other is perf
  scale_y_continuous(limits = c(2500, 6500)) +
  labs(
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    size = "bill_length_mm",
    color = "species",
    fill  = "species"
  ) +
  guides(
    size  = guide_legend(order = 1,
                         override.aes = list(
                           fill = "black",
                           color = "black",
                           alpha = 1
                         )),
    fill  = guide_legend(order = 2),
    color = guide_legend(order = 2)
  ) +
  theme_grey(base_size = 14) 
  theme(
    panel.background = element_rect(fill = "#e8e8e8"),
    legend.position = "right"
  )

ggsave("ggplot2.png", width = 10, height = 7, dpi = 300)
