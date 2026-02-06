const width = 800;
const height = 500;
const margin = { top: 40, right: 180, bottom: 60, left: 70 };

const svg = d3.select("svg")
  .attr("width", width)
  .attr("height", height)
  .style("font-family", '"Comic Sans MS", "Comic Sans", cursive');

const tooltip = d3.select("body")
  .append("div")
  .style("position", "absolute")
  .style("pointer-events", "none")
  .style("background", "white")
  .style("border", "1px solid #ccc")
  .style("border-radius", "6px")
  .style("padding", "6px 8px")
  .style("font-family", '"Comic Sans MS", "Comic Sans", cursive')

d3.csv("../penglings.csv", d => ({
  flipper: +d.flipper_length_mm,
  mass: +d.body_mass_g,
  bill: +d.bill_length_mm,
  species: d.species
})).then(data => {

  const x = d3.scaleLinear()
    .domain(d3.extent(data, d => d.flipper))
    .range([margin.left, width - margin.right]);

  const y = d3.scaleLinear()
    .domain(d3.extent(data, d => d.mass))
    .range([height - margin.bottom, margin.top]);

  const size = d3.scaleLinear()
    .domain(d3.extent(data, d => d.bill))
    .range([4, 12]);

  const speciesDomain = ["Adelie", "Chinstrap", "Gentoo"];
  const color = d3.scaleOrdinal()
    .domain(speciesDomain)
    .range(["#F28E2B", "#7B3C9B", "#1B9E77"]);
  
  svg.append("g")
    .attr("class", "grid x-grid")
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x)
      .tickSize(-(height - margin.top - margin.bottom))
      .tickFormat('')
    );

  svg.append("g")
    .attr("class", "grid y-grid")
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y)
      .tickSize(-(width - margin.left - margin.right))
      .tickFormat('')
    );

  svg.selectAll('.grid line')
    .attr('stroke', 'lightgray')
  svg.selectAll('.grid path')
    .attr('stroke', 'none');

  svg.append("g")
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x));

  svg.append("g")
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y));

  svg.selectAll("circle")
    .data(data)
    .enter()
    .append("circle")
    .attr("cx", d => x(d.flipper))
    .attr("cy", d => y(d.mass))
    .attr("r", d => size(d.bill))
    .attr("fill", d => color(d.species))
    .attr("opacity", 0.8)
    .on("mouseover", function (event, d) {
      d3.select(this).attr("stroke", "#222").attr("stroke-width", 1);

      tooltip
        .style("opacity", 1)
        .html(`
          <div style="font-weight:600">${d.species}</div>
          <div>Flipper: ${d.flipper} mm</div>
          <div>Body Mass: ${d.mass} g</div>
          <div>Bill: ${d.bill} mm</div>
        `);
    })
    .on("mousemove", function (event) {
      tooltip
        .style("left", (event.pageX + 12) + "px")
        .style("top", (event.pageY - 20) + "px");
    })
    .on("mouseout", function () {
      d3.select(this).attr("stroke", "none");
      tooltip.style("opacity", 0);
    });

  const legendX = width - margin.right + 50;

  const speciesLegend = svg.append("g")
    .attr("transform", `translate(${legendX},${margin.top})`);

  speciesLegend.append("text")
    .text("species")
    .style("font-weight", 600);

  const speciesRows = speciesLegend.selectAll("g.row")
    .data(speciesDomain)
    .enter()
    .append("g")
    .attr("class", "row")
    .attr("transform", (d, i) => `translate(0,${18 + i * 20})`);

  speciesRows.append("circle")
    .attr("cx", 6)
    .attr("cy", 0)
    .attr("r", 6)
    .attr("fill", d => color(d))
    .attr("opacity", 0.8);

  speciesRows.append("text")
    .attr("x", 18)
    .attr("y", 4)
    .text(d => d);

  const billLegend = svg.append("g")
    .attr("transform", `translate(${legendX},${margin.top + 90})`);

  billLegend.append("text")
    .text("bill_length_mm")
    .style("font-weight", 600);

  const sizeValues = [30, 40, 50];
  const sizeRows = billLegend.selectAll("g.sizerow")
    .data(sizeValues)
    .enter()
    .append("g")
    .attr("class", "sizerow")
    .attr("transform", (d, i) => `translate(0,${22 + i * 26})`);

  sizeRows.append("circle")
    .attr("cx", 10)
    .attr("cy", 0)
    .attr("r", d => size(d))
    .attr("fill", "#111")
    .attr("opacity", 0.25);

  sizeRows.append("text")
    .attr("x", 30)
    .attr("y", 4)
    .text(d => d);
});
