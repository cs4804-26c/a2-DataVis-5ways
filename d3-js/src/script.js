const CONFIG = {
    colors: {
        adelie: "#E57C58",
        chinstrap: "#353A4C",
        gentoo: "#9C74B5"
    },
    dims: {
        w: 800,
        h: 550,
        margin: { top: 50, right: 30, bottom: 60, left: 70 }
    }
};

const width = CONFIG.dims.w - CONFIG.dims.margin.left - CONFIG.dims.margin.right;
const height = CONFIG.dims.h - CONFIG.dims.margin.top - CONFIG.dims.margin.bottom;

const svg = d3.select("#vis")
    .append("svg")
    .attr("width", CONFIG.dims.w)
    .attr("height", CONFIG.dims.h)
    .append("g")
    .attr("transform", `translate(${CONFIG.dims.margin.left},${CONFIG.dims.margin.top})`);

const tooltip = d3.select("#tooltip");

d3.csv("../../penglings.csv").then(raw_data => {
    const data = raw_data
        .filter(d => d.flipper_length_mm !== "NA" && d.body_mass_g !== "NA")
        .map(d => {
            return {
                species: d.species,
                flipper: +d.flipper_length_mm,
                mass: +d.body_mass_g,
                bill: +d.bill_length_mm
            };
        });

    const xScale = d3.scaleLinear()
        .domain([170, 240])
        .range([0, width]);

    const yScale = d3.scaleLinear()
        .domain([2500, 6500])
        .range([height, 0]);

    const radiusScale = d3.scaleSqrt()
        .domain([30, 60])
        .range([4, 10]);

    const colorScale = d3.scaleOrdinal()
        .domain(["Adelie", "Chinstrap", "Gentoo"])
        .range([CONFIG.colors.adelie, CONFIG.colors.chinstrap, CONFIG.colors.gentoo]);

    const makeXGrid = () => d3.axisBottom(xScale).ticks(8);
    const makeYGrid = () => d3.axisLeft(yScale).ticks(8);

    svg.append("g")
        .attr("class", "grid")
        .attr("transform", `translate(0,${height})`)
        .call(makeXGrid().tickSize(-height).tickFormat(""));

    svg.append("g")
        .attr("class", "grid")
        .call(makeYGrid().tickSize(-width).tickFormat(""));

    svg.append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(xScale).ticks(8))
        .append("text")
        .attr("y", 40)
        .attr("x", width / 2)
        .attr("fill", "#333")
        .attr("font-weight", "bold")
        .text("Flipper Length (mm)");

    svg.append("g")
        .call(d3.axisLeft(yScale).ticks(8))
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", -50)
        .attr("x", -height / 2)
        .attr("text-anchor", "middle")
        .attr("fill", "#333")
        .attr("font-weight", "bold")
        .text("Body Mass (g)");

    svg.selectAll(".penguin-dot")
        .data(data)
        .join("circle")
        .attr("class", "penguin-dot")
        .attr("cx", d => xScale(d.flipper))
        .attr("cy", d => yScale(d.mass))
        .attr("r", d => radiusScale(d.bill))
        .style("fill", d => colorScale(d.species))
        .style("opacity", 0.8)
        .style("stroke", "white")
        .style("stroke-width", 0.5)

        .on("mouseover", function(event, d) {
            d3.select(this)
                .transition().duration(100)
                .style("opacity", 1)
                .style("stroke", "#333")
                .style("stroke-width", 2)
                .attr("r", radiusScale(d.bill) + 3);


            tooltip.style("opacity", 1)
                .html(`
                    <div style="font-family: sans-serif; font-size: 14px;">
                        <strong style="color:${colorScale(d.species)}">${d.species}</strong><br/>
                        <span>Flipper: ${d.flipper} mm</span><br/>
                        <span>Mass: ${d.mass} g</span>
                    </div>
                `);
        })
        .on("mousemove", (event) => {
            tooltip
                .style("left", (event.pageX + 15) + "px")
                .style("top", (event.pageY - 28) + "px");
        })
        .on("mouseout", function() {
            d3.select(this)
                .transition().duration(200)
                .style("opacity", 0.8)
                .style("stroke", "white")
                .style("stroke-width", 0.5)
                .attr("r", d => radiusScale(d.bill));

            tooltip.style("opacity", 0);
        });

    svg.append("text")
        .attr("x", width / 2)
        .attr("y", -20)
        .attr("text-anchor", "middle")
        .style("font-size", "18px")
        .style("font-weight", "bold")
        .style("font-family", "sans-serif")
        .text("Penguin Size: Flipper vs. Mass");

}).catch(error => {
    console.error("Error loading CSV:", error);
    d3.select("#vis").append("p")
        .style("color", "red")
        .text("Could not load data. Is the CSV file in the right folder?");
});
