library(ggplot2)

penguins <- read.csv("penglings.csv")

clean <- subset(penguins,
  !is.na(flipper_length_mm) & !is.na(body_mass_g) & !is.na(bill_length_mm)
)
clean$bill_length_mm_clamped <- pmin(pmax(clean$bill_length_mm, 40), 50)

plot <- ggplot(clean, aes(
  x = flipper_length_mm,
  y = body_mass_g,
  color = species,
  size = bill_length_mm_clamped
)) +
  geom_point(alpha = 0.8) +
  labs(
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    color = "Species",
    size = "Bill Length (mm)"
  ) +
  scale_color_manual(values = c(
    "Adelie" = "#4E79A7",
    "Chinstrap" = "#E15759",
    "Gentoo" = "#59A14F"
  )) +
  scale_size_continuous(
    limits = c(40, 50),
    breaks = c(40, 50),
    range = c(3, 5)
  ) +
  scale_x_continuous(limits = c(170, 235), breaks = seq(170, 235, 10), expand = c(0, 0)) +
  scale_y_continuous(limits = c(2700, 6400), breaks = seq(3000, 6400, 1000)) +
  guides(color = guide_legend(order = 1), size = guide_legend(order = 2)) +
  theme_grey(base_family = "Helvetica")

print(plot)

ggsave("r-ggplot2.png", plot, width = 7, height = 4.5, dpi = 144)
