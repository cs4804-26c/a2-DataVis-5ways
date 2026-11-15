library(ggplot2)

data <- read.csv("penglings.csv")

chart <- ggplot(data, aes(x=flipper_length_mm, y=body_mass_g,
                          color=species, size=bill_length_mm)) +
  geom_point(alpha=0.8, na.rm=TRUE) +
  coord_cartesian(xlim=c(170, 235), ylim=c(2500, 6500)) +
  labs(x="Flipper Length (mm)", y="Body Mass (g)") +
  theme_minimal()

ggsave("../img/ggplot2.png", chart, width=9, height=6)
