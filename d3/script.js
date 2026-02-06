const svg = d3.select("svg");
const tooltip = d3.select(".tooltip");

const margin = { top: 60, right: 200, bottom: 80, left: 80 };
const width = 900 - margin.left - margin.right;
const height = 600 - margin.top - margin.bottom;

const g = svg.append("g")
  .attr("transform", `translate(${margin.left},${margin.top})`);

// title
svg.append("text")
  .attr("x", 450)
  .attr("y", 30)
  .attr("text-anchor", "middle")
  .style("font-size", "20px")
  .style("font-weight", "bold")
  .text("Penguin Body Mass vs Flipper Length");

// loading data
d3.csv("penglings.csv").then(data => {

  data.forEach(d => {
    d.flipper_length_mm = +d.flipper_length_mm;
    d.body_mass_g = +d.body_mass_g;
    d.bill_length_mm = +d.bill_length_mm;
  });

  const x = d3.scaleLinear()
    .domain([170, 235])
    .range([0, width]);

  const y = d3.scaleLinear()
    .domain([2700, 6300])
    .range([height, 0]);

  const color = d3.scaleOrdinal(d3.schemeCategory10);

  // x-axis
  g.append("g")
    .attr("transform", `translate(0,${height})`)
    .call(d3.axisBottom(x));

  g.append("text")
    .attr("x", width / 2)
    .attr("y", height + 50)
    .attr("text-anchor", "middle")
    .style("font-size", "14px")
    .text("Flipper Length (mm)");

  // y-axis
  g.append("g")
    .call(d3.axisLeft(y));

  g.append("text")
    .attr("transform", "rotate(-90)")
    .attr("x", -height / 2)
    .attr("y", -55)
    .attr("text-anchor", "middle")
    .style("font-size", "14px")
    .text("Body Mass (g)");

  // circles
  g.selectAll("circle")
    .data(data)
    .enter()
    .append("circle")
    .attr("cx", d => x(d.flipper_length_mm))
    .attr("cy", d => y(d.body_mass_g))
    .attr("r", d => d.bill_length_mm / 5)
    .attr("fill", d => color(d.species))
    .attr("opacity", 0.8)
    .on("mouseover", (event, d) => {
      tooltip
        .style("opacity", 1)
        .html(
          `<strong>Species:</strong> ${d.species}<br>
           <strong>Flipper:</strong> ${d.flipper_length_mm} mm<br>
           <strong>Body Mass:</strong> ${d.body_mass_g} g<br>
           <strong>Bill Length:</strong> ${d.bill_length_mm} mm`
        );
    })
    .on("mousemove", event => {
      tooltip
        .style("left", (event.pageX + 10) + "px")
        .style("top", (event.pageY - 28) + "px");
    })
    .on("mouseout", () => {
      tooltip.style("opacity", 0);
    });

  // species legend
  const species = Array.from(new Set(data.map(d => d.species)));

  const legendColor = svg.append("g")
    .attr("transform", `translate(${width + margin.left + 20}, ${margin.top})`);

  legendColor.append("text")
    .attr("y", -10)
    .style("font-weight", "bold")
    .text("Species");

  species.forEach((s, i) => {
    const row = legendColor.append("g")
      .attr("transform", `translate(0, ${i * 20})`);

    row.append("rect")
      .attr("width", 12)
      .attr("height", 12)
      .attr("fill", color(s));

    row.append("text")
      .attr("x", 18)
      .attr("y", 10)
      .style("font-size", "12px")
      .text(s);
  });

  // size legend - dynamically based on actual data
  const sizeLegend = svg.append("g")
    .attr("transform", `translate(${width + margin.left + 20}, ${margin.top + 120})`);

  sizeLegend.append("text")
    .attr("y", -10)
    .style("font-weight", "bold")
    .text("Bill Length (mm)");

  // compute min, median, max bill lengths from data
  const billLengths = data.map(d => d.bill_length_mm);
  const minBill = d3.min(billLengths);
  const maxBill = d3.max(billLengths);
  const medianBill = d3.median(billLengths);

  const sizeValues = [minBill, medianBill, maxBill];

  sizeValues.forEach((v, i) => {
    // draw a circle with radius proportional to the bill length
    sizeLegend.append("circle")
      .attr("cx", 10)
      .attr("cy", i * 30)
      .attr("r", v / 5) // scale down actual value to fit 
      .attr("fill", "gray")
      .attr("opacity", 0.8);

    // add text next to the circle to show the value
    sizeLegend.append("text")
      .attr("x", 30)
      .attr("y", i * 30 + 5)
      .style("font-size", "12px")
      .text(Math.round(v));
  });


});
