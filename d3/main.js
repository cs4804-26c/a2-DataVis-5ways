const margin = {top: 20, right: 20, bottom: 60, left: 90};
const width = 900;
const height = 500;

const svg = d3.select("#chart")
    .append("svg")
    .attr("width", width)
    .attr("height", height)

const chartWidth = width - margin.left - margin.right;
const chartHeight = height - margin.top - margin.bottom;

const g = svg.append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

const tooltip = d3.select("body")
    .append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

const color = d3.scaleOrdinal()
  .domain(["Adelie", "Chinstrap", "Gentoo"])
  .range(["#F28E2B", "#9C51B6", "#4E9E9A"]);

d3.csv("../data/penglings.csv", d3.autoType).then(raw => {

    // filter missing values
    const data = raw
  .map(d => ({
    species: (d.species ?? "").trim(),
    flipper_length_mm: +d.flipper_length_mm,
    body_mass_g: +d.body_mass_g,
    bill_length_mm: +d.bill_length_mm
  }))
  .filter(d =>
    d.species !== "" &&
    Number.isFinite(d.flipper_length_mm) &&
    Number.isFinite(d.body_mass_g) &&
    Number.isFinite(d.bill_length_mm)
  );

console.log("raw rows:", raw.length, "clean rows:", data.length);
console.log("example cleaned row:", data[0]);

    // scales
    const x = d3.scaleLinear()
        .domain(d3.extent(data, d => d.flipper_length_mm))
        .nice()
        .range([0, chartWidth]);
    
    const y = d3.scaleLinear()
        .domain(d3.extent(data, d => d.body_mass_g))
        .nice()
        .range([chartHeight, 0]);
    
    const r = d3.scaleLinear()
        .domain(d3.extent(data, d => d.bill_length_mm))
        .range([3, 12]);
    
    // gridlines
    // gridlines (optional design polish)
g.append("g")
  .call(
    d3.axisLeft(y)
      .ticks(8)
      .tickSize(-chartWidth)
      .tickFormat("")
  )
  .selectAll("line")
  .attr("stroke", "#eee");

g.append("g")
  .attr("transform", `translate(0,${chartHeight})`)
  .call(
    d3.axisBottom(x)
      .ticks(7)
      .tickSize(-chartHeight)
      .tickFormat("")
  )
  .selectAll("line")
  .attr("stroke", "#eee");

    // axes
    const xAxis = d3.axisBottom(x).ticks(7);
    const yAxis = d3.axisLeft(y).ticks(8);

    g.append("g")
        .attr("transform", `translate(0,${chartHeight})`)
        .call(xAxis)

    g.append("g")
        .call(yAxis)

    // axis labels
    g.append("text")
    .attr("class", "axis-label")
    .attr("x", chartWidth / 2)
    .attr("y", chartHeight + 45)
    .attr("text-anchor", "middle")
    .text("Flipper Length (mm)");

    g.append("text")
    .attr("class", "axis-label")
    .attr("transform", "rotate(-90)")
    .attr("x", -chartHeight / 2)
    .attr("y", -60)
    .attr("text-anchor", "middle")
    .text("Body Mass (g)");


    // points
    g.selectAll("circle")
        .data(data)
        .join("circle")
        .attr("cx", d => x(d.flipper_length_mm))
        .attr("cy", d => y(d.body_mass_g))
        .attr("r", d => r(d.bill_length_mm))
        .attr("fill", d => color(d.species))
        .attr("opacity", 0.8)
        .on("mousemove", (event, d) => {
            tooltip
                .style("opacity", 1)
                .style("left", (event.pageX + 12) + "px")
                .style("top", (event.pageY + 12) + "px")
                .html(`
                    <div><b>${d.species}</b></div>
                    <div>Flipper Length: ${d.flipper_length_mm} mm</div>
                    <div>Body Mass: ${d.body_mass_g} g</div>
                    <div>Bill Length: ${d.bill_length_mm} mm</div>
                `);
        })
        .on("mouseleave", () => { tooltip.style("opacity", 0); });
        });