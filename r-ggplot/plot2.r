library(readr)
library(dplyr)
library(ggplot2)

dir.create("../output", showWarnings = FALSE)

df <- read_csv("../penglings.csv", show_col_types = FALSE) %>%
  filter(
    !is.na(flipper_length_mm),
    !is.na(body_mass_g),
    !is.na(bill_length_mm),
    !is.na(species)
  )

# Force species order to match legend order (Adelie, Chinstrap, Gentoo)
df$species <- factor(df$species, levels = c("Adelie", "Chinstrap", "Gentoo"))

# Chat helped me match the colors
species_colors <- c(
  "Adelie" = "#F28E2B",
  "Chinstrap" = "#8E44AD",
  "Gentoo" = "#1F9E89"
)

p <- ggplot(df, aes(
  x = flipper_length_mm,
  y = body_mass_g,
  color = species,
  size = bill_length_mm
)) +
  geom_point(alpha = 0.8) +
  labs(x = "Flipper Length (mm)", y = "Body Mass (g)") +

  # Axis ranges + ticks (not starting at 0)
  scale_x_continuous(limits = c(170, 232), breaks = seq(170, 230, 10)) +
  scale_y_continuous(limits = c(2600, 6400), breaks = seq(3000, 6000, 1000)) +

  scale_color_manual(values = species_colors) +

  # Size legend like the reference (show 40 and 50)
  scale_size_continuous(breaks = c(40, 50)) +

  # gray ggplot background
  theme_gray() + guides(size  = guide_legend(order = 1), color = guide_legend(order = 2))

ggsave("../output/ggplot2.png", p, width = 10, height = 6, dpi = 150)
print(p)
