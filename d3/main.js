document.body.insertAdjacentHTML("beforeend", "<p style='font-size:24px'>JS RAN </p>");
console.log("main.js loaded");

const svg = d3.select("svg");
const width = 800;
const height = 600;
const margin = { top: 40, right: 40, bottom: 60, left: 80 };

svg.attr("width", width).attr("height", height);

d3.csv("../penglings.csv")
  .then(raw => {
    console.log("CSV rows:", raw.length);
    console.log("Columns:", Object.keys(raw[0] || {}));
    console.log("First row:", raw[0]);

    const data = raw
      .map(d => ({
        ...d,
        flipper_length_mm: +d.flipper_length_mm,
        body_mass_g: +d.body_mass_g,
        bill_length_mm: +d.bill_length_mm,
      }))
      .filter(d =>
        Number.isFinite(d.flipper_length_mm) &&
        Number.isFinite(d.body_mass_g) &&
        Number.isFinite(d.bill_length_mm) &&
        d.species
      );

    console.log("Clean rows:", data.length);

    const x = d3.scaleLinear()
      .domain(d3.extent(data, d => d.flipper_length_mm))
      .range([margin.left, width - margin.right]);

    const y = d3.scaleLinear()
      .domain(d3.extent(data, d => d.body_mass_g))
      .range([height - margin.bottom, margin.top]);

    const size = d3.scaleLinear()
      .domain(d3.extent(data, d => d.bill_length_mm))
      .range([3, 12]);

    const color = d3.scaleOrdinal()
      .domain([...new Set(data.map(d => d.species))])
      .range(d3.schemeCategory10);

    svg.selectAll("circle")
      .data(data)
      .enter()
      .append("circle")
      .attr("cx", d => x(d.flipper_length_mm))
      .attr("cy", d => y(d.body_mass_g))
      .attr("r", d => size(d.bill_length_mm))
      .attr("fill", d => color(d.species))
      .attr("opacity", 0.8);

    svg.append("g")
      .attr("transform", `translate(0, ${height - margin.bottom})`)
      .call(d3.axisBottom(x));

    svg.append("g")
      .attr("transform", `translate(${margin.left}, 0)`)
      .call(d3.axisLeft(y));
  })
  .catch(err => {
    console.error("CSV load error:", err);
  });

svg.append("text")
  .attr("x", width / 2)
  .attr("y", height - 15)
  .attr("text-anchor", "middle")
  .attr("font-size", "14px")
  .text("Flipper Length (mm)");


svg.append("text")
  .attr("transform", "rotate(-90)")
  .attr("x", -height / 2)
  .attr("y", 20)
  .attr("text-anchor", "middle")
  .attr("font-size", "14px")
  .text("Body Mass (g)");

  svg.append("text")
  .attr("x", width / 2)
  .attr("y", 25)
  .attr("text-anchor", "middle")
  .attr("font-size", "18px")
  .attr("font-weight", "bold")
  .text("Penguin Body Mass vs Flipper Length");
