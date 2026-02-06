import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

const width = 800;
const height = 500;
const margin = { top: 40, right: 40, bottom: 60, left: 70 };

const innerWidth = width - margin.left - margin.right;
const innerHeight = height - margin.top - margin.bottom;

const svg = d3.create("svg")
  .attr("width", width)
  .attr("height", height);

const g = svg.append("g")
  .attr("transform", `translate(${margin.left},${margin.top})`);

d3.csv("penglings.csv").then(data => {
  data.forEach(d => {
    d.flipper_length_mm = +d.flipper_length_mm;
    d.body_mass_g = +d.body_mass_g;
    d.bill_length_mm = +d.bill_length_mm;
  });
  const x = d3.scaleLinear()
    .domain(d3.extent(data, d => d.flipper_length_mm))
    .range([0, innerWidth])
    .nice();

  const y = d3.scaleLinear()
    .domain(d3.extent(data, d => d.body_mass_g))
    .range([innerHeight, 0])

    .nice();

  const color = d3.scaleOrdinal()
    .domain([...new Set(data.map(d => d.species))])
    .range(["#E69F00", "#56B4E9", "#009E73"]);
  const size = d3.scaleLinear()
    .domain(d3.extent(data, d => d.bill_length_mm))
    .range([4, 12]);
  g.append("g")
    .attr("transform", `translate(0,${innerHeight})`)
    .call(d3.axisBottom(x));

  g.append("g")
    .call(d3.axisLeft(y));


  g.append("text")
    .attr("x", innerWidth / 2)
    .attr("y", innerHeight + 45)
    .attr("text-anchor", "middle")
    .text("Flipper Length (mm)");

  g.append("text")
    .attr("x", -innerHeight / 2)
    .attr("y", -50)
    .attr("transform", "rotate(-90)")
    .attr("text-anchor", "middle")
    .text("Body Mass (g)");

  g.selectAll("circle")
    .data(data)
    .enter()
    .append("circle")
    .attr("cx", d => x(d.flipper_length_mm))
    .attr("cy", d => y(d.body_mass_g))
    .attr("r", d => size(d.bill_length_mm))
    .attr("fill", d => color(d.species))
    .attr("opacity", 0.8);
});

document.getElementById("container").appendChild(svg.node());