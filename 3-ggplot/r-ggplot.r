library(ggplot2)

# Extract data from csv
data <- read.csv("penglings.csv")

custom_colors = c("Adelie" = "orange", "Chinstrap" = "purple", "Gentoo" = "darkcyan")

# Bubble plot
plot <- ggplot(data, aes(x = flipper_length_mm, y = body_mass_g, size = bill_length_mm, color = species)) +
  geom_point(alpha = 0.8) +
  scale_color_manual(values = custom_colors) +
  scale_size_continuous(range = c(1.5, 7)) +
  labs(x = "Flipper Length (mm)", y = "Body Mass (g)", size = "Bill Length (mm)", color = "Species")

ggsave("img/3-ggplot.png", plot = plot, width = 8, height = 6, dpi = 300)