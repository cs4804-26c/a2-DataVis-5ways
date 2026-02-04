library(ggplot2)
library(dplyr)

df <- read.csv("C:/Users/plumm/Documents/Classes/4th Year/C Term 2026/Data Visualization/A2/a2-DataVis-5ways/penglings.csv")
df <- df %>% 
  filter(!is.na(bill_length_mm), 
         !is.na(flipper_length_mm), 
         !is.na(body_mass_g))

p <- ggplot(df, aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point(aes(size = bill_length_mm, color = species), alpha = 0.8) +
  scale_color_manual(
    values = c("Adelie" = "#E28A37", "Chinstrap" = "#AF58BA", "Gentoo" = "#008080")
  ) +
  scale_size_continuous(
    range = c(3, 10), 
    breaks = c(40, 50),
    name = "bill_length_mm"
  ) +
  labs(
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    color = "species"
  ) +
  theme(
    aspect.ratio = 0.6, 
    
    panel.background = element_rect(fill = "#EBEBEB", color = NA),
    plot.background = element_rect(fill = "white", color = NA),
    panel.grid.major = element_line(color = "white", linewidth = 1.2),
    panel.grid.minor = element_line(color = "white", linewidth = 0.6),
    axis.line = element_blank(),
    axis.ticks = element_blank(),
    legend.key = element_rect(fill = "#EBEBEB", color = NA),
    legend.position = "right"
  )

print(p)