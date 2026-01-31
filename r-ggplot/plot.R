library(ggplot2)
library(readr)

# Load data
peng <- read_csv("penglings.csv")

# Remove rows with missing values
peng <- na.omit(peng)

# Plot
p <- ggplot(peng, aes(
  x = flipper_length_mm,
  y = body_mass_g,
  color = species,
  size = bill_length_mm
)) +
  geom_point(alpha = 0.7) +
  scale_color_manual(
    values = c(
      Adelie = "orange",
      Chinstrap = "purple",
      Gentoo = "#008080"
    )
  ) +
  scale_x_continuous(
    limits = c(170, 230),
    breaks = seq(170, 230, 10)
  ) +
  scale_y_continuous(
    limits = c(3000, 6000),
    breaks = seq(3000, 6000, 1000)
  ) +
  labs(
    title = "ggplot2",
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    size = "Bill Length (mm)",
    color = "species"
  ) +
  theme_minimal() +
	theme(plot.title = element_text(hjust=0.5))


# Save PNG
print(p)
ggsave("ggplot.png", p, width = 8, height = 6, dpi = 300)
