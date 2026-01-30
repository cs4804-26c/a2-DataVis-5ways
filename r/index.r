library(tidyverse)

#load the csv
df <- read.csv("../penglings.csv")

#define colors for the species
species_colors <- c('Adelie' = 'orange', 'Chinstrap' = 'purple', 'Gentoo' = 'lightblue')

#create the scatter plot for each species
ggplot(df, aes(x = flipper_length_mm, y = body_mass_g, color = species, size = bill_length_mm)) +
  geom_point(alpha = 0.6) +
  scale_color_manual(values = species_colors) +
  theme_minimal() +
  labs(title = 'Penguin Size by Species',
       x = 'Flipper Length (mm)',
       y = 'Body Mass (g)') +
  theme(legend.title = element_blank()) +
  guides(size = FALSE) 

#show the plot!!
ggsave('penguin_size_by_species.png', width = 9, height = 4.5, dpi = 300)
