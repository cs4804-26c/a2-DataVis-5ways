
// Margin convention is standard in D3 to ensure axes have space
const margin = {top: 50, right: 150, bottom: 60, left: 70};
const width = 800 - margin.left - margin.right;
const height = 600 - margin.top - margin.bottom;

const svg = d3.select("#chart")
  .append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform", `translate(${margin.left},${margin.top})`);

// Tooltip
const tooltip = d3.select("#tooltip");

d3.csv("../penglings.csv").then(function(data) {
  const cleanData = data.filter(d =>
    d.flipper_length_mm !== "NA" &&
    d.body_mass_g !== "NA" &&
    d.bill_length_mm !== "NA"
  ).map(d => {
    return {
      species: d.species,
      flipper_length_mm: +d.flipper_length_mm,
      body_mass_g: +d.body_mass_g,
      bill_length_mm: +d.bill_length_mm
    };
  });


  const xScale = d3.scaleLinear()
    .domain([
      d3.min(cleanData, d => d.flipper_length_mm) - 5,
      d3.max(cleanData, d => d.flipper_length_mm) + 5
    ])
    .range([0, width]);

  // Y: Body Mass
  const yScale = d3.scaleLinear()
    .domain([
      d3.min(cleanData, d => d.body_mass_g) - 200,
      d3.max(cleanData, d => d.body_mass_g) + 200
    ])
    .range([height, 0]);


  const colorScale = d3.scaleOrdinal()
    .domain(["Adelie", "Chinstrap", "Gentoo"])
    .range(["#ff6f61", "#9370db", "#20b2aa"]); // Orangeish, Purple, Teal


  const sizeScale = d3.scaleSqrt()
    .domain(d3.extent(cleanData, d => d.bill_length_mm))
    .range([4, 12]); // 圆的半径范围


  // X Axis
  svg.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(d3.axisBottom(xScale).tickSize(-height).ticks(10)) // tickSize(-height) 模拟网格线
    .call(g => g.select(".domain").remove()) // 去掉轴线，更像 ggplot 风格
    .call(g => g.selectAll(".tick line").attr("stroke-opacity", 0.1)); // 浅色网格

  // X Axis Label
  svg.append("text")
    .attr("text-anchor", "middle")
    .attr("x", width / 2)
    .attr("y", height + 40)
    .style("font-family", "sans-serif")
    .text("Flipper Length (mm)");

  // Y Axis
  svg.append("g")
    .call(d3.axisLeft(yScale).tickSize(-width).ticks(10))
    .call(g => g.select(".domain").remove())
    .call(g => g.selectAll(".tick line").attr("stroke-opacity", 0.1));

  // Y Axis Label
  svg.append("text")
    .attr("text-anchor", "middle")
    .attr("transform", "rotate(-90)")
    .attr("y", -50)
    .attr("x", -height / 2)
    .style("font-family", "sans-serif")
    .text("Body Mass (g)");

  // --- 绘制散点 (Circles) ---

  svg.selectAll("circle")
    .data(cleanData)
    .enter()
    .append("circle")
    .attr("cx", d => xScale(d.flipper_length_mm))
    .attr("cy", d => yScale(d.body_mass_g))
    .attr("r", d => sizeScale(d.bill_length_mm))
    .attr("fill", d => colorScale(d.species))
    .attr("opacity", 0.8)
    .attr("stroke", "white")
    .attr("stroke-width", 0.5)

    // Interaction
    .on("mouseover", function(event, d) {
      d3.select(this).attr("stroke", "black").attr("stroke-width", 2);
      tooltip.classed("hidden", false)
        .style("left", (event.pageX + 10) + "px")
        .style("top", (event.pageY - 28) + "px")
        .html(`
                    <strong>${d.species}</strong><br>
                    Mass: ${d.body_mass_g}g<br>
                    Flipper: ${d.flipper_length_mm}mm<br>
                    Bill: ${d.bill_length_mm}mm
                `);
    })
    .on("mouseout", function() {
      d3.select(this).attr("stroke", "white").attr("stroke-width", 0.5);
      tooltip.classed("hidden", true);
    });

  const legend = svg.selectAll(".legend")
    .data(colorScale.domain())
    .enter().append("g")
    .attr("transform", (d, i) => `translate(${width + 20}, ${i * 25 + 20})`);

  legend.append("circle")
    .attr("cx", 0)
    .attr("cy", 0)
    .attr("r", 6)
    .style("fill", colorScale);

  legend.append("text")
    .attr("x", 15)
    .attr("y", 5)
    .style("font-family", "sans-serif")
    .style("font-size", "12px")
    .text(d => d);

}).catch(function(error){
  console.log(error);
});
