library(ggplot2)

df <- read.csv("penglings.csv")

ggplot(data = df, aes(x = flipper_length_mm, y = body_mass_g, color = species, size = bill_length_mm)) +
  geom_point(alpha = 0.8) + 
  scale_color_manual(values = c("Adelie"="#ff8f12", "Chinstrap"="#9b39cc", "Gentoo"="#008a8a")) +
  labs(x= "Flipper Length (mm)", y = "Body Mass (g)") + 
  scale_size(range=c(2, 8))

