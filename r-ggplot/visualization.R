library(ggplot2)
setwd("/Users/esthermao/Documents/WPI/senior year/C26/CS 4804/a2-DataVis-5ways")
data <- read.csv("penglings.csv")

print(head(data))
print(names(data))
print(summary(data))

plot <- ggplot(data, aes(x = flipper_length_mm, y = body_mass_g,
                         color = species, size = bill_length_mm)) +
  geom_point(alpha = 0.8) +
  scale_color_manual(values = c("#ff52b8", "#bbe458", "#ff3d00")) +
  scale_x_continuous(breaks = seq(170, 240, by = 10)) +
  scale_y_continuous(breaks = seq(2500, 6500, by = 1000)) +
  labs(
    title = "Penguin Body Mass vs Flipper ad Bill Length",
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    color = "Species",
    size = "Bill Length (mm)"
  ) +
  theme_minimal()

print(plot)

ggsave("r-ggplot/output.png", plot, width = 10, height = 6, dpi = 300)