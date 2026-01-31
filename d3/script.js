// run using python -m http.server 8000
// then go to http://localhost:8000/index.html

const svg = d3.select("#chart");
const width = +svg.attr("width");
const height = +svg.attr("height");
const margin = { top: 40, right: 200, bottom: 60, left: 60 };

d3.csv("penglings.csv").then(data => {
  // Convert numeric fields
  data = data.filter(d =>
    d.flipper_length_mm !== "NA" &&
    d.body_mass_g !== "NA" &&
    d.bill_length_mm !== "NA"
  ).map(d => ({
    species: d.species,
    flipper: +d.flipper_length_mm,
    mass: +d.body_mass_g,
    bill: +d.bill_length_mm
  }));

    const x = d3.scaleLinear()
    .domain([165, 235])  // fixed domain from 170 to 230 (+- 5 to allow for overflow)
    .range([margin.left, width - margin.right]);


    const y = d3.scaleLinear()
    .domain([2500, 6500]) // fixed domain from 3000 to 6000 (+- 500 to allow for overflow)
    .range([height - margin.bottom, margin.top]);


  const color = d3.scaleOrdinal() // coloring for species
    .domain(["Adelie", "Chinstrap", "Gentoo"])
    .range(["orange", "purple", "teal"]);

  const size = d3.scaleLinear()
    .domain(d3.extent(data, d => d.bill))
    .range([3, 12]);

  // Axes
  svg.append("g") // x-axis
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x).ticks((d3.max(data,d=>d.flipper)-170)/10)); // have x start at 170 and increment by 10

    svg.append("g") // x-axis grid lines
    .attr("class", "grid")
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x)
        .tickSize(-(height - margin.top - margin.bottom))
        .tickFormat("")
    );

    svg.append("g") // y-axis
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y).ticks((d3.max(data, d => d.mass) - d3.min(data, d => d.mass)) / 1000)); // increment by 1000

    svg.append("g") // y-axis grid lines
    .attr("class", "grid")
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y)
        .tickSize(-(width - margin.left - margin.right))
        .tickFormat("")
    );

    // make gridlines grey
    svg.selectAll(".grid line")
    .attr("stroke", "#ccc")
    .attr("stroke-opacity", 0.7)
    .attr("shape-rendering", "crispEdges");
    svg.selectAll(".grid path") 
    .attr("stroke-width", 0);


  // Labels
  svg.append("text")
    .attr("x", width / 2)
    .attr("y", height - 15)
    .attr("text-anchor", "middle")
    .text("Flipper Length (mm)");

  svg.append("text")
    .attr("transform", "rotate(-90)")
    .attr("x", -height / 2)
    .attr("y", 20)
    .attr("text-anchor", "middle")
    .text("Body Mass (g)");

    // Title
    svg.append("text")
    .attr("x", width / 2)
    .attr("y", margin.top / 2)
    .attr("text-anchor", "middle")
    .attr("font-size", "20px")
    .attr("font-weight", "bold")
    .text("d3");

  // Points
  svg.selectAll("circle")
    .data(data)
    .enter()
    .append("circle")
    .attr("cx", d => x(d.flipper))
    .attr("cy", d => y(d.mass))
    .attr("r", d => size(d.bill))
    .attr("fill", d => color(d.species))
    .attr("opacity", 0.8);

  // Bill Legend
    const billLegend = svg.append("g")
    .attr("transform", `translate(${width - margin.right+80}, ${margin.top + 110})`);

    const billSizes = [40, 50];

    billLegend.selectAll("legend-circles")
    .data(billSizes)
    .enter()
    .append("circle")
        .attr("cx", 0)
        .attr("cy", (d, i) => i * 40)
        .attr("r", d => size(d))
        .attr("fill", "gray")
        .attr("opacity", 0.4);

    billLegend.selectAll("legend-text")
    .data(billSizes)
    .enter()
    .append("text")
        .attr("x", 30)
        .attr("y", (d, i) => i * 40 + 5)
        .text(d => `${d}`)
        .attr("font-size", "12px")
        .attr("alignment-baseline", "middle");

    billLegend.append("text")
    .attr("x", 0)
    .attr("y", -15)
    .text("Bill Length (mm)")
    .attr("font-size", "12px")
    .attr("font-weight", "bold");

    // Species legend
    const speciesLegend = svg.append("g")
    .attr("transform", `translate(${width - margin.right+80}, ${margin.top})`);

    const species = ["Adelie", "Chinstrap", "Gentoo"];

    speciesLegend.selectAll("legend-dots")
    .data(species)
    .enter()
    .append("circle")
        .attr("cx", 0)
        .attr("cy", (d, i) => i * 25)
        .attr("r", 7)
        .attr("fill", d => color(d))
        .attr("opacity", 0.8);

    speciesLegend.selectAll("legend-labels")
    .data(species)
    .enter()
    .append("text")
        .attr("x", 15)
        .attr("y", (d, i) => i * 25 + 5)
        .text(d => d)
        .attr("font-size", "12px")
        .attr("alignment-baseline", "middle");

    speciesLegend.append("text")
    .attr("x", 0)
    .attr("y", -15)
    .text("Species")
    .attr("font-size", "12px")
    .attr("font-weight", "bold");

    // easiest way for me to download chart into png, asked microsoft copilot for the following code
    document.getElementById("saveBtn").addEventListener("click", function () {
    const svg = document.getElementById("chart");
    const serializer = new XMLSerializer();
    const svgString = serializer.serializeToString(svg);

    const canvas = document.createElement("canvas");
    canvas.width = svg.width.baseVal.value;
    canvas.height = svg.height.baseVal.value;

    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "white"; ctx.fillRect(0, 0, canvas.width, canvas.height);    // add white background
    const img = new Image();

    img.onload = function () {
        ctx.drawImage(img, 0, 0);
        const png = canvas.toDataURL("image/png");

        const link = document.createElement("a");
        link.download = "d3.png";
        link.href = png;
        link.click();
    };

    img.src = "data:image/svg+xml;base64," + btoa(unescape(encodeURIComponent(svgString)));
    });

});
