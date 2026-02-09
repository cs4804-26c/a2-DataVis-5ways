library(ggplot2)

script_dir <- tryCatch({
  normalizePath(dirname(rstudioapi::getActiveDocumentContext()$path))
}, error = function(e) {
  getwd()
})
setwd(script_dir)

cat("Working directory:", getwd(), "\n")

csv_path <- file.path("..", "penglings.csv")
if (!file.exists(csv_path)) {
  stop("Can't find penglings.csv at: ", normalizePath(csv_path, winslash = "/"))
}

penguins <- read.csv(csv_path, stringsAsFactors = FALSE)

penguins$bill_length_mm    <- suppressWarnings(as.numeric(penguins$bill_length_mm))
penguins$flipper_length_mm <- suppressWarnings(as.numeric(penguins$flipper_length_mm))
penguins$body_mass_g       <- suppressWarnings(as.numeric(penguins$body_mass_g))

penguins <- penguins[
  !is.na(penguins$species) &
  !is.na(penguins$bill_length_mm) &
  !is.na(penguins$flipper_length_mm) &
  !is.na(penguins$body_mass_g),
]

p <- ggplot(
  penguins,
  aes(
    x = flipper_length_mm,
    y = body_mass_g,
    color = species,
    size = bill_length_mm
  )
) +
  geom_point(alpha = 0.8) +
  labs(
    title = "Flipper Length vs Body Mass",
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    color = "Species",
    size = "Bill length (mm)"
  ) +
  theme_minimal()

out_dir <- file.path("..", "img")
if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)

out_file <- file.path(out_dir, "ggplot.png")
ggsave(out_file, plot = p, width = 10, height = 6, dpi = 150)

cat("Saved plot to:", normalizePath(out_file, winslash = "/"), "\n")
print(p)
