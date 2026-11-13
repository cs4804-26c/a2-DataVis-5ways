// I used ChatGPT to help implement the D3 scatterplot, CSV loading, scales,
// axes, tooltips, and click-to-filter legend. I chose the visual design myself.

const speciesColors = {
  Adelie: "red",
  Chinstrap: "blue",
  Gentoo: "#93e9be" // seafoam green
};

const width = 1000;
const height = 560;
const margin = { top: 20, right: 30, bottom: 70, left: 85 };
const innerWidth = width - margin.left - margin.right;
const innerHeight = height - margin.top - margin.bottom;
const species = Object.keys(speciesColors);

const svg = d3.select("#chart").append("svg")
  .attr("viewBox", `0 0 ${width} ${height}`)
  .attr("preserveAspectRatio", "xMidYMid meet");
const plot = svg.append("g")
  .attr("transform", `translate(${margin.left},${margin.top})`);

const x = d3.scaleLinear().domain([170, 235]).range([0, innerWidth]);
const y = d3.scaleLinear().domain([2500, 6500]).range([innerHeight, 0]);
// Keep the earlier point-size range until I choose a different size.
const pointRadius = d3.scaleSqrt().domain([30, 60]).range([3, 10]);

plot.append("g").attr("class", "grid")
  .call(d3.axisLeft(y).tickValues(d3.range(2500, 6501, 500))
    .tickSize(-innerWidth).tickFormat(""));
plot.append("g").attr("class", "axis")
  .attr("transform", `translate(0,${innerHeight})`)
  .call(d3.axisBottom(x).tickValues(d3.range(170, 236, 10)));
plot.append("g").attr("class", "axis")
  .call(d3.axisLeft(y).tickValues(d3.range(2500, 6501, 500)).tickFormat(d3.format(",")));

svg.append("text").attr("class", "axis-label")
  .attr("x", margin.left + innerWidth / 2).attr("y", height - 15)
  .attr("text-anchor", "middle").text("Flipper Length (mm)");
svg.append("text").attr("class", "axis-label")
  .attr("transform", `translate(24,${margin.top + innerHeight / 2}) rotate(-90)`)
  .attr("text-anchor", "middle").text("Body Mass (g)");

const tooltip = d3.select("#tooltip");
let selectedSpecies = null;

// The CSV lives one folder above d3/ in the assignment repository.
d3.csv("../penglings.csv", d3.autoType).then(rows => {
  const data = rows.filter(d =>
    Number.isFinite(d.flipper_length_mm) &&
    Number.isFinite(d.body_mass_g) &&
    Number.isFinite(d.bill_length_mm) &&
    species.includes(d.species)
  );

  const circles = plot.selectAll(".point").data(data)
    .join("circle")
    .attr("class", "point")
    .attr("cx", d => x(d.flipper_length_mm))
    .attr("cy", d => y(d.body_mass_g))
    .attr("r", d => pointRadius(d.bill_length_mm))
    .attr("fill", d => speciesColors[d.species])
    .attr("opacity", 0.8)
    .on("mousemove", (event, d) => {
      tooltip.style("opacity", 1)
        .style("left", `${Math.min(event.clientX + 14, window.innerWidth - 200)}px`)
        .style("top", `${Math.max(8, event.clientY - 80)}px`)
        .html(`<strong>${d.species}</strong><div>Flipper length: ${d.flipper_length_mm} mm</div><div>Body mass: ${d.body_mass_g.toLocaleString()} g</div><div>Bill length: ${d.bill_length_mm} mm</div>`);
    })
    .on("mouseleave", () => tooltip.style("opacity", 0));

  // Click a species to isolate it; click the same species again to show all.
  const buttons = d3.select("#species-legend").selectAll("button")
    .data(species).join("button")
    .attr("type", "button").attr("class", "species-button")
    .attr("aria-pressed", "false")
    .each(function(name) {
      const button = d3.select(this);
      button.append("span").attr("class", "swatch")
        .style("background", speciesColors[name]);
      button.append("span").text(name);
    })
    .on("click", (event, name) => {
      selectedSpecies = selectedSpecies === name ? null : name;
      buttons.classed("selected", d => d === selectedSpecies)
        .attr("aria-pressed", d => String(d === selectedSpecies));
      circles.interrupt().transition().duration(200)
        .attr("opacity", d => !selectedSpecies || d.species === selectedSpecies ? 0.8 : 0.06);
    });

  const sizeSvg = d3.select("#size-legend").append("svg")
    .attr("viewBox", "0 0 205 65").attr("width", 205).attr("height", 65);
  [35, 45, 55].forEach((value, index) => {
    const cx = 30 + index * 69;
    sizeSvg.append("circle").attr("cx", cx).attr("cy", 22)
      .attr("r", pointRadius(value))
      .attr("fill", "#777").attr("opacity", 0.8);
    sizeSvg.append("text").attr("x", cx).attr("y", 52)
      .attr("text-anchor", "middle").attr("font-size", 13).text(value);
  });
}).catch(error => {
  d3.select("#error").text("Could not load penglings.csv. Run a local server from the repository root (python3 -m http.server 8000). ");
  console.error(error);
});
