if(!require(ggplot2)) install.packages("ggplot2")
library(ggplot2)

data <- read.csv('../penglings.csv')

ggplot(data, aes(x=flipper_length_mm, y=body_mass_g, size=bill_length_mm, fill=species)) +

    geom_point(alpha=0.8, shape=21, color="black") +
    scale_fill_manual(values=c('Adelie'='#017339', 'Gentoo'='#e8ac0e', 'Chinstrap'='#e25501')) +
    scale_size(range = c(3, 8)) +

    labs(title='Penguin Size vs Mass (R + ggplot2)',
    x='Flipper Length (mm)',
    y='Body Mass (g)') +

    theme_minimal()

    ggsave('a2-r-ggplot-graph.png', width=6, height=4)
