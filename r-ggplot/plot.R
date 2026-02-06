
library(ggplot2)

df <- read.csv("../penglings.csv")

df <- na.omit(df)

p <- ggplot(df, aes(x = flipper_length_mm,
                    y = body_mass_g,
                    color = species,
                    size = bill_length_mm)) +


  geom_point(alpha = 0.8) +


  scale_x_continuous(n.breaks = 6) +
  scale_y_continuous(n.breaks = 6) +

  scale_size(range = c(3, 8)) +


  scale_color_manual(values = c("Adelie" = "#ff6c5f",
                                "Chinstrap" = "#9e6bed",
                                "Gentoo" = "#20b2aa")) +

  theme_gray() +

  labs(title = "Penguin Size vs Mass (R + ggplot2)",
       x = "Flipper Length (mm)",
       y = "Body Mass (g)",
       size = "Bill Length",
       color = "Species")

ggsave("plot.png", plot = p, width = 8, height = 6, dpi = 300)

print("Plot saved to plot.png")
