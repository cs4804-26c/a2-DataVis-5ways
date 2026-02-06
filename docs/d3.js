const app = {
    init() {
        d3.csv("penglings.csv", d => ({
            flipper: +d.flipper_length_mm,
            mass: +d.body_mass_g,
            bill: +d.bill_length_mm,
            species: d.species
        })).then((data) => {
            console.log(data);
            this.createGraph(data);
        })
    },

    createGraph(data) {

        const width = 600;
        const height = 400;
        const margin = 60;

        this.svg = d3.select("#viz").attr("width", width).attr("height", height);

        const x = d3.scaleLinear().domain([170, 240]).range([margin, width - margin]);
        const y = d3.scaleLinear().domain([2500, 6500]).range([height - margin, margin]);
        const r = d3.scaleLinear().domain(d3.extent(data, d => d.bill)).range([3, 8]);
        const color = d3.scaleOrdinal().domain([...new Set(data.map(d => d.species))]).range(d3.schemeTableau10);

        const legend = this.svg.append("g").attr("transform", `translate(${width - margin - 20}, ${margin})`);
        legend.append("circle").attr("cx",0).attr("cy",0).attr("r", 6).style("fill", color("Adelie"));
        legend.append("circle").attr("cx",0).attr("cy",30).attr("r", 6).style("fill", color("Chinstrap"));
        legend.append("circle").attr("cx",0).attr("cy",60).attr("r", 6).style("fill", color("Gentoo"));
        legend.append("text").attr("x", 12).attr("y", 0).text("Adelie").style("font-size", "15px").attr("alignment-baseline","middle");
        legend.append("text").attr("x", 12).attr("y", 30).text("Chinstrap").style("font-size", "15px").attr("alignment-baseline","middle");
        legend.append("text").attr("x", 12).attr("y", 60).text("Gentoo").style("font-size", "15px").attr("alignment-baseline","middle");

        this.svg.append("g").attr("transform", `translate(0, ${height - margin})`).call(d3.axisBottom(x));
        this.svg.append("g").attr("transform", `translate(${margin}, 0)`).call(d3.axisLeft(y));
        this.svg.append("text").attr("x", width / 2).attr("y", height - 15).attr("text-anchor", "middle").text("Flipper Length (mm)");
        this.svg.append("text").attr("transform", "rotate(-90)").attr("x", -height/2).attr("y", 20).attr("text-anchor", "middle").text("Body Mass (g)");

        const tooltip = d3.select("body").append("div").style("position", "absolute").style("background", "gray").style("border", "1px solid black").style("padding", "6px").style("pointer-events", "none").style("opacity", 0);
        this.svg.selectAll("circle").data(data).enter().append("circle")
            .attr("cx", d => x(d.flipper)).attr("cy", d => y(d.mass)).attr("r", d => r(d.bill)).attr("fill", d => color(d.species)).attr("opacity", 0.8)
            .on("mouseover", (event, d) => {tooltip.style("opacity", 1).html(`Species: ${d.species}<br>Bill Length (mm): ${d.bill}<br>Flipper Length (mm): ${d.flipper}<br>Body Mass (g): ${d.mass}`);})
            .on("mousemove", (event) => {tooltip.style("left", (event.pageX + 10) + "px").style("top", (event.pageY - 20) + "px");})
            .on("mouseout", () => {tooltip.style("opacity", 0);});
    }
}

window.addEventListener("DOMContentLoaded", () => app.init())