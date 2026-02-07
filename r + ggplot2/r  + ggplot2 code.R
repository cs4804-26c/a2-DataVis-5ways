install.packages("ggplot2")
library(ggplot2)

# Convert the bill length column to numbers
# (It will turn "NA" or text into actual R missing values)
Penglings_Data_CS_4804_A2_$Bill_Length_mm <- as.numeric(Penglings_Data_CS_4804_A2_$Bill_Length_mm)
Penglings_Data_CS_4804_A2_$Flipper_Length_mm <- as.numeric(Penglings_Data_CS_4804_A2_$Flipper_Length_mm)
Penglings_Data_CS_4804_A2_$Body_Mass_g <- as.numeric(Penglings_Data_CS_4804_A2_$Body_Mass_g)

penguin_plot <- ggplot(Penglings_Data_CS_4804_A2_, aes(
  x = `Flipper_Length_mm`, 
  y = `Body_Mass_g`, 
  color = Species, 
  size = `Bill_Length_mm`
)) +
  geom_point(alpha = 0.8) +
  scale_color_manual(values = c(
    "Adelie" = "#ff8c00", 
    "Chinstrap" = "#9932cc", 
    "Gentoo" = "#008b8b"
  )) +
  scale_size_continuous(range = c(1, 10)) + 
  labs(x = "Flipper Length (mm)", 
       y = "Body Mass (g)",
       title = "Penguin Size Trends") +
  theme_minimal()

# Run this to see the result
print(penguin_plot)
