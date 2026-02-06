// D3 Penguins Scatterplot (ggplot-like theme)
// Robust to different CSV header names.
// Encodings: x = flipper length, y = body mass, color = species, size = bill length, opacity ~ 0.8

const WIDTH = 900;
const HEIGHT = 520;

const margin = { top: 20, right: 30, bottom: 60, left: 70 };
const innerW = WIDTH - margin.left - margin.right;
const innerH = HEIGHT - margin.top - margin.bottom;

// Create SVG
const svg = d3
  .select("#chart")
  .append("svg")
  .attr("width", WIDTH)
  .attr("height", HEIGHT);

const g = svg
  .append("g")
  .attr("transform", `translate(${margin.left},${margin.top})`);

// Background rectangle for the plot area (ggplot-like)
g.append("rect")
  .attr("class", "plot-bg")
  .attr("x", 0)
  .attr("y", 0)
  .attr("width", innerW)
  .attr("height", innerH);

// Tooltip
const tooltip = d3
  .select("body")
  .append("div")
  .attr("class", "tooltip");

// Load CSV (async)
d3.csv("./penglings.csv", d3.autoType)
  .then((raw) => {
    if (!raw || raw.length === 0) {
      throw new Error("CSV loaded but contains no rows.");
    }

    // ---- Detect column names (handles common penguin dataset variants) ----
    const cols = raw.columns || Object.keys(raw[0] || {});
    const pick = (candidates) => candidates.find((k) => cols.includes(k));

    const X_COL = pick([
      "flipper_length",
      "flipper_length_mm",
      "Flipper Length",
      "Flipper Length (mm)",
      "flipper_length (mm)"
    ]);

    const Y_COL = pick([
      "body_mass",
      "body_mass_g",
      "Body Mass",
      "Body Mass (g)",
      "body_mass (g)"
    ]);

    const SIZE_COL = pick([
      "bill_length",
      "bill_length_mm",
      "Bill Length",
      "Bill Length (mm)",
      "bill_length (mm)"
    ]);

    const COLOR_COL = pick(["species", "Species"]);

    console.log("CSV columns:", cols);
    console.log("Using columns:", { X_COL, Y_COL, SIZE_COL, COLOR_COL });

    if (!X_COL || !Y_COL || !SIZE_COL || !COLOR_COL) {
      throw new Error(
        `Missing required columns. Found columns: ${cols.join(", ")}`
      );
    }

    // ---- Normalize rows into consistent fields ----
    const data = raw
      .map((d) => ({
        x: d[X_COL],
        y: d[Y_COL],
        r: d[SIZE_COL],
        species: d[COLOR_COL],
      }))
      .filter(
        (d) =>
          d.x != null &&
          d.y != null &&
          d.r != null &&
          d.species != null &&
          !Number.isNaN(d.x) &&
          !Number.isNaN(d.y) &&
          !Number.isNaN(d.r)
      );

    if (data.length === 0) {
      throw new Error(
        "After filtering missing values, there are 0 rows left to plot. Check your CSV for blanks."
      );
    }

    const xExtent = d3.extent(data, (d) => d.x);
    const yExtent = d3.extent(data, (d) => d.y);
    const sizeExtent = d3.extent(data, (d) => d.r);

    // padding so points aren't at the border
    const xPad = (xExtent[1] - xExtent[0]) * 0.05;
    const yPad = (yExtent[1] - yExtent[0]) * 0.05;

    const xScale = d3
      .scaleLinear()
      .domain([xExtent[0] - xPad, xExtent[1] + xPad])
      .range([0, innerW]);

    const yScale = d3
      .scaleLinear()
      .domain([yExtent[0] - yPad, yExtent[1] + yPad])
      .range([innerH, 0]);

    // Size mapping: bill length -> radius
    const rScale = d3
      .scaleSqrt()
      .domain(sizeExtent)
      .range([3, 13]);

    // Color mapping: species -> categorical colors
    const colorScale = d3
      .scaleOrdinal()
      .domain(["Adelie", "Chinstrap", "Gentoo"])
      .range([
        "#4E79A7", // Blue  → Adelie
        "#F28E2B", // Orange → Chinstrap
        "#E15759"  // Red → Gentoo
      ]);
    const xGrid = d3
      .axisBottom(xScale)
      .ticks(10)
      .tickSize(-innerH)
      .tickFormat("");

    const yGrid = d3
      .axisLeft(yScale)
      .ticks(10)
      .tickSize(-innerW)
      .tickFormat("");

    // Draw gridlines first so points go on top
    g.append("g")
      .attr("class", "grid")
      .attr("transform", `translate(0,${innerH})`)
      .call(xGrid);

    g.append("g")
      .attr("class", "grid")
      .call(yGrid);

    // ---- Axes ----
    const xAxis = d3.axisBottom(xScale).ticks(10);
    const yAxis = d3.axisLeft(yScale).ticks(10);

    g.append("g")
      .attr("class", "axis")
      .attr("transform", `translate(0,${innerH})`)
      .call(xAxis);

    g.append("g")
      .attr("class", "axis")
      .call(yAxis);

    // Axis labels
    g.append("text")
      .attr("class", "axis-label")
      .attr("x", innerW / 2)
      .attr("y", innerH + 45)
      .attr("text-anchor", "middle")
      .text("Flipper Length");

    g.append("text")
      .attr("class", "axis-label")
      .attr("x", -innerH / 2)
      .attr("y", -50)
      .attr("transform", "rotate(-90)")
      .attr("text-anchor", "middle")
      .text("Body Mass");

    // ---- Points ----
    g.append("g")
      .selectAll("circle")
      .data(data)
      .join("circle")
      .attr("cx", (d) => xScale(d.x))
      .attr("cy", (d) => yScale(d.y))
      .attr("r", (d) => rScale(d.r))
      .attr("fill", (d) => colorScale(d.species))
      .attr("fill-opacity", 0.8)
      .attr("stroke", "none")
      .on("mouseenter", (event, d) => {
        tooltip
          .style("opacity", 1)
          .html(
            `<strong>${d.species}</strong><br/>
             Flipper: ${d.x}<br/>
             Body Mass: ${d.y}<br/>
             Bill: ${d.r}`
          );
      })
      .on("mousemove", (event) => {
        tooltip.style("left", `${event.pageX}px`).style("top", `${event.pageY}px`);
      })
      .on("mouseleave", () => {
        tooltip.style("opacity", 0);
      });
  })
  .catch((err) => {
    console.error("Error:", err);
    d3.select("#chart")
      .append("p")
      .style("color", "crimson")
      .style("font-weight", "600")
      .text(`Error: ${err.message}`);
  });
