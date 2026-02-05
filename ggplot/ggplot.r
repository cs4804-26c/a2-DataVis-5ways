install.packages("ggplot2")
library(ggplot2)

penguins <- read.csv("data/penglings.csv")

ggplot(data = penguins, aes(x= flipper_length_mm, y= body_mass_g, color= species, size= bill_length_mm)) +
  geom_point(alpha=0.7) +
  labs(title= "Penguin Flipper Length vs Body Mass",
       x= "Flipper Length (mm)",
       y= "Body Mass (g)") +
  xlim(170,230) + 
  ylim(3000,6000)
  theme_minimal()


ggsave("img/ggplotimg.png", width=8, height=6, dpi=300)

