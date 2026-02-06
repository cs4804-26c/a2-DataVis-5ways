const width = 700;
const height = 470;
const margin = { top: 20, right: 140, bottom: 50, left: 70 };

const svg = d3
  .select("#chart")
  .append("svg")
  .attr("width", width)
  .attr("height", height);

const plotWidth = width - margin.left - margin.right;
const plotHeight = height - margin.top - margin.bottom;

const plot = svg
  .append("g")
  .attr("transform", `translate(${margin.left},${margin.top})`);

const tooltip = d3.select("#tooltip");

d3.csv("../penglings.csv", d3.autoType).then((data) => {
  const clean = data.filter(
    (d) => d.flipper_length_mm != null && d.body_mass_g != null && d.bill_length_mm != null
  );

  const x = d3.scaleLinear().domain([170, 235]).range([0, plotWidth]);
  const y = d3.scaleLinear().domain([2600, 6400]).range([plotHeight, 0]);
  const size = d3.scaleSqrt().domain([40, 50]).range([5, 7]).clamp(true);
  const color = d3
    .scaleOrdinal()
    .domain(["Adelie", "Chinstrap", "Gentoo"])
    .range(["#4E79A7", "#E15759", "#59A14F"]);

  const xAxis = d3.axisBottom(x).tickValues(d3.range(170, 236, 10));
  const yAxis = d3.axisLeft(y).tickValues(d3.range(3000, 6401, 1000));

  const axisOffset = 6;

  plot
    .append("rect")
    .attr("class", "panel")
    .attr("width", plotWidth)
    .attr("height", plotHeight + axisOffset);
  plot
    .append("g")
    .attr("class", "axis")
    .attr("transform", `translate(0,${plotHeight + axisOffset})`)
    .call(xAxis);

  plot.append("g").attr("class", "axis").call(yAxis);

  const xGrid = d3.axisBottom(x).tickValues(d3.range(170, 236, 10)).tickSize(-plotHeight).tickFormat("");
  const yGrid = d3.axisLeft(y).tickValues(d3.range(3000, 6401, 1000)).tickSize(-plotWidth).tickFormat("");

  plot
    .append("g")
    .attr("class", "grid")
    .attr("transform", `translate(0,${plotHeight + axisOffset})`)
    .call(xGrid);

  plot.append("g").attr("class", "grid").call(yGrid);

  plot
    .append("text")
    .attr("x", plotWidth / 2)
    .attr("y", plotHeight + 40)
    .attr("text-anchor", "middle")
    .text("Flipper Length (mm)");

  plot
    .append("text")
    .attr("x", -plotHeight / 2)
    .attr("y", -50)
    .attr("transform", "rotate(-90)")
    .attr("text-anchor", "middle")
    .text("Body Mass (g)");

  plot
    .selectAll("circle")
    .data(clean)
    .join("circle")
    .attr("cx", (d) => x(d.flipper_length_mm))
    .attr("cy", (d) => y(d.body_mass_g))
    .attr("r", (d) => size(d.bill_length_mm))
    .attr("fill", (d) => color(d.species))
    .attr("opacity", 0.8)
    .on("mouseenter", function (event, d) {
      plot.selectAll("circle").attr("opacity", 0.2);
      d3.select(this).attr("opacity", 0.9).attr("stroke", "#333").attr("stroke-width", 1.5);
      tooltip
        .style("opacity", 1)
        .html(
          `<strong>${d.species}</strong><br/>` +
            `Bill Length: ${d.bill_length_mm} mm<br/>` +
            `Flipper Length: ${d.flipper_length_mm} mm<br/>` +
            `Body Mass: ${d.body_mass_g} g`
        );
    })
    .on("mousemove", function (event) {
      tooltip.style("left", `${event.pageX + 12}px`).style("top", `${event.pageY - 28}px`);
    })
    .on("mouseleave", function () {
      plot.selectAll("circle").attr("opacity", 0.8).attr("stroke", null);
      tooltip.style("opacity", 0);
    });

  const species = Array.from(new Set(clean.map((d) => d.species)));
  const legendX = margin.left + plotWidth + 10;
  const legend = svg.append("g").attr("transform", `translate(${legendX}, ${margin.top + 24})`);

  const speciesGroup = legend.append("g");
  const speciesHeaderY = 0;
  const speciesRowStart = 18;
  const speciesRowGap = 18;
  speciesGroup
    .append("text")
    .attr("class", "legend-title")
    .attr("x", 0)
    .attr("y", speciesHeaderY)
    .attr("font-size", 12)
    .attr("font-weight", 600)
    .text("Species");

  speciesGroup
    .selectAll("circle")
    .data(species)
    .join("circle")
    .attr("cx", 6)
    .attr("cy", (d, i) => speciesRowStart + i * speciesRowGap)
    .attr("r", 5)
    .attr("fill", (d) => color(d));

  speciesGroup
    .selectAll("text.species-label")
    .data(species)
    .join("text")
    .attr("class", "species-label")
    .attr("x", 18)
    .attr("y", (d, i) => speciesRowStart + i * speciesRowGap + 4)
    .attr("font-size", 12)
    .text((d) => d);

  const sizeLegendValues = [40, 50];
  const sizeLegendY = species.length * speciesRowGap + speciesRowStart + 20;

  legend
    .append("text")
    .attr("x", 0)
    .attr("y", sizeLegendY)
    .attr("font-size", 12)
    .attr("font-weight", 600)
    .text("Bill Length (mm)");

  legend
    .selectAll(".size-circle")
    .data(sizeLegendValues)
    .join("circle")
    .attr("class", "size-circle")
    .attr("cx", 5)
    .attr("cy", (d, i) => sizeLegendY + 16 + i * 20)
    .attr("r", (d) => size(d))
    .attr("fill", "#4d4d4d")
    .attr("opacity", 0.8);

  legend
    .selectAll(".size-label")
    .data(sizeLegendValues)
    .join("text")
    .attr("class", "size-label")
    .attr("x", 20)
    .attr("y", (d, i) => sizeLegendY + 20 + i * 20)
    .attr("font-size", 12)
    .text((d) => d);
});
