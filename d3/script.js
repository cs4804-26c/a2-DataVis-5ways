const svg = d3.select("#chart");
const width = +svg.attr("width");
const height = +svg.attr("height");

const margin = { top: 30, right: 30, bottom: 60, left: 70 };
const innerWidth = width - margin.left - margin.right;
const innerHeight = height - margin.top - margin.bottom;

const g = svg.append("g")
  .attr("transform", `translate(${margin.left},${margin.top})`);

d3.csv("../penglings.csv").then(raw => {
  const data = raw
    .map(d => ({
      species: d.species,
      flipper_length_mm: +d.flipper_length_mm,
      body_mass_g: +d.body_mass_g,
      bill_length_mm: +d.bill_length_mm
    }))
    .filter(d =>
      d.species &&
      Number.isFinite(d.flipper_length_mm) &&
      Number.isFinite(d.body_mass_g) &&
      Number.isFinite(d.bill_length_mm)
    );

  // ---- REQUIRED: scales should not start at 0 ----
  // Use fixed domains similar to the example image (not 0-based).
  const xScale = d3.scaleLinear()
    .domain([170, 235])
    .range([0, innerWidth]);

  const yScale = d3.scaleLinear()
    .domain([2700, 6200])
    .range([innerHeight, 0]);

  // ---- REQUIRED: color mapping to species ----
  // Match the example’s palette/order as closely as possible.
  const colorScale = d3.scaleOrdinal()
    .domain(["Adelie", "Chinstrap", "Gentoo"])
    .range(["orange", "purple", "#1B9E9E"]); 


  const rScale = d3.scaleSqrt()
    .domain(d3.extent(data, d => d.bill_length_mm))
    .range([3, 10]);


  const xTicks = d3.range(170, 236, 10);     
  const yTicks = [3000, 4000, 5000, 6000];    

  g.append("g")
    .attr("transform", `translate(0,${innerHeight})`)
    .call(d3.axisBottom(xScale).tickValues(xTicks));

  g.append("g")
    .call(d3.axisLeft(yScale).tickValues(yTicks));

  g.append("text")
    .attr("x", innerWidth / 2)
    .attr("y", innerHeight + 45)
    .attr("text-anchor", "middle")
    .text("Flipper Length (mm)");

  g.append("text")
    .attr("transform", "rotate(-90)")
    .attr("x", -innerHeight / 2)
    .attr("y", -50)
    .attr("text-anchor", "middle")
    .text("Body Mass (g)");

  g.selectAll("circle")
    .data(data)
    .enter()
    .append("circle")
    .attr("cx", d => xScale(d.flipper_length_mm))
    .attr("cy", d => yScale(d.body_mass_g))
    .attr("r", d => rScale(d.bill_length_mm))
    .attr("fill", d => colorScale(d.species))
    .attr("opacity", 0.8);
});
