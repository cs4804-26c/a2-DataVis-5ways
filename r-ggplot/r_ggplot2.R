library(ggplot2)
library(readr)

# Load data
df <- read_csv("penglings.csv")

# Check data
head(df)

# Create plot
ggplot(df, aes(
  x = flipper_length_mm,
  y = body_mass_g,
  color = species,
  size = bill_length_mm
)) +
  geom_point(alpha = 0.8) +
  scale_x_continuous(
    name = "Flipper Length (mm)",
    limits = c(170, 235)
  ) +
  scale_y_continuous(
    name = "Body Mass (g)",
    limits = c(2700, 6500)
  ) +
  ggtitle("Penguin Body Mass vs Flipper Length") +
  theme_gray()
