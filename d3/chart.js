const margin = { top: 20, right: 140, bottom: 50, left: 65 };
const width = 760 - margin.left - margin.right;
const height = 480 - margin.top - margin.bottom;

const svg = d3.select("#chart").append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform", `translate(${margin.left},${margin.top})`);

d3.csv("../penglings.csv", d3.autoType).then(raw => {
  const data = raw.filter(d => d.flipper_length_mm != null && d.body_mass_g != null && d.bill_length_mm != null);
  const x = d3.scaleLinear().domain([170, 232]).range([0, width]);
  const y = d3.scaleLinear().domain([2500, 6500]).range([height, 0]);
  const r = d3.scaleLinear().domain(d3.extent(data, d => d.bill_length_mm)).range([2, 8]);
  const color = d3.scaleOrdinal()
  .domain(["Adelie", "Chinstrap", "Gentoo"])
  .range(["#ff8c00", "#a020f0", "#008b8b"]);
  svg.append("g").attr("transform", `translate(0,${height})`)
  .call(d3.axisBottom(x).tickValues(d3.range(170, 231, 10)));
  svg.append("g").call(d3.axisLeft(y).tickValues(d3.range(3000, 6001, 1000)));

  svg.append("text").attr("x", width / 2).attr("y", height + 42)
  .attr("text-anchor", "middle").text("Flipper Length (mm)");
  svg.append("text").attr("transform", "rotate(-90)")
  .attr("x", -height / 2).attr("y", -50)
  .attr("text-anchor", "middle").text("Body Mass (g)");

  const tip = d3.select("#tip");
  svg.selectAll("circle").data(data).join("circle")
  .attr("cx", d => x(d.flipper_length_mm))
  .attr("cy", d => y(d.body_mass_g))
  .attr("r", d => r(d.bill_length_mm))
  .attr("fill", d => color(d.species))
  .attr("opacity", 0.8)
  .on("mouseover", (e, d) => tip.style("opacity", 1)
  .html(`${d.species}<br>bill: ${d.bill_length_mm} mm<br>flipper: ${d.flipper_length_mm} mm<br>mass: ${d.body_mass_g} g`))
  .on("mousemove", e => tip.style("left", e.pageX + 12 + "px").style("top", e.pageY + 12 + "px"))
  .on("mouseout", () => tip.style("opacity", 0));

  // a legend
  const legend = svg.append("g").attr("transform", `translate(${width + 20},20)`);
  color.domain().forEach((s, i) => {
    legend.append("circle").attr("cy", i * 22).attr("r", 5).attr("fill", color(s));
    legend.append("text").attr("x", 14).attr("y", i * 22 + 4).text(s);
  });
});
