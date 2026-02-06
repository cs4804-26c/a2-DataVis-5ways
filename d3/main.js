const width = 960;
const height = 560;
const margin = { top: 30, right: 190, bottom: 70, left: 90 };

const svg = d3
    .select("#chart")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

const tooltip = d3.select("#tooltip");
const filterEl = document.getElementById("speciesFilter");
const countEl = document.getElementById("count");
const downwardToggle = document.getElementById("downwardToggle");

const parseRow = (d) => {
    const toNum = (v) => (v === "NA" || v === "" || v == null ? null : +v);
    return {
        species: d.species,
        flipper_length_mm: toNum(d.flipper_length_mm),
        body_mass_g: toNum(d.body_mass_g),
        bill_length_mm: toNum(d.bill_length_mm),
    };
};

d3.csv("../penglings.csv", parseRow).then((raw) => {
    const dataAll = raw.filter(
        (d) =>
            d.species &&
            d.flipper_length_mm != null &&
            d.body_mass_g != null &&
            d.bill_length_mm != null
    );

    const domainOrder = ["Adelie", "Chinstrap", "Gentoo"];
    const speciesList = domainOrder.filter((s) => dataAll.some((d) => d.species === s));

    // Populate filter dropdown
    for (const s of speciesList) {
        const opt = document.createElement("option");
        opt.value = s;
        opt.textContent = s;
        filterEl.appendChild(opt);
    }

    // State for legend toggles
    const enabled = new Set(speciesList);

    // Scales (non-zero domains)
    const xExtent = d3.extent(dataAll, (d) => d.flipper_length_mm);
    const yExtent = d3.extent(dataAll, (d) => d.body_mass_g);
    const rExtent = d3.extent(dataAll, (d) => d.bill_length_mm);

    const xPad = 2;
    const yPad = 60;

    const x = d3
        .scaleLinear()
        .domain([xExtent[0] - xPad, xExtent[1] + xPad])
        .range([margin.left, width - margin.right])
        .nice();

    // IMPORTANT:
    // Default should match the reference (upward-trending):
    // Larger body_mass_g should appear higher => standard y axis (SVG goes down, so range is inverted).
    const yNormal = d3
        .scaleLinear()
        .domain([yExtent[0] - yPad, yExtent[1] + yPad])
        .range([height - margin.bottom, margin.top])
        .nice();

    // Optional "data downward" mode:
    // Larger values appear lower => range not inverted.
    const yDownward = d3
        .scaleLinear()
        .domain([yExtent[0] - yPad, yExtent[1] + yPad])
        .range([margin.top, height - margin.bottom])
        .nice();

    let y = yNormal;

    const r = d3.scaleSqrt().domain(rExtent).range([3, 12]);

    // Color palette (kept consistent across tools)
    const color = d3
        .scaleOrdinal()
        .domain(speciesList)
        .range(["#F28E2B", "#8F63B8", "#2CA7A0"]);

    // Gridlines (background) — not required, but allowed
    const xGrid = d3
        .axisBottom(x)
        .ticks(8)
        .tickSize(-(height - margin.top - margin.bottom))
        .tickFormat("");

    const yGrid = d3
        .axisLeft(y)
        .ticks(8)
        .tickSize(-(width - margin.left - margin.right))
        .tickFormat("");

    const xGridG = svg
        .append("g")
        .attr("class", "grid")
        .attr("transform", `translate(0,${height - margin.bottom})`)
        .call(xGrid)
        .call((g) => g.select(".domain").remove());

    const yGridG = svg
        .append("g")
        .attr("class", "grid")
        .attr("transform", `translate(${margin.left},0)`)
        .call(yGrid)
        .call((g) => g.select(".domain").remove());

    // Axes
    const xAxisG = svg
        .append("g")
        .attr("class", "axis")
        .attr("transform", `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(x).ticks(8));

    const yAxisG = svg
        .append("g")
        .attr("class", "axis")
        .attr("transform", `translate(${margin.left},0)`)
        .call(d3.axisLeft(y).ticks(8));

    // Axis labels
    const xLabel = svg
        .append("text")
        .attr("x", (margin.left + (width - margin.right)) / 2)
        .attr("y", height - 25)
        .attr("text-anchor", "middle")
        .attr("fill", "#111")
        .text("Flipper Length (mm)");

    const yLabel = svg
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("x", -(margin.top + (height - margin.bottom)) / 2)
        .attr("y", 28)
        .attr("text-anchor", "middle")
        .attr("fill", "#111")
        .text("Body Mass (g)");

    // Plot layer
    const plot = svg.append("g");

    function getFilteredData() {
        const dropdown = filterEl.value;
        return dataAll.filter((d) => {
            const okDropdown = dropdown === "ALL" ? true : d.species === dropdown;
            const okLegend = enabled.has(d.species);
            return okDropdown && okLegend;
        });
    }

    function updatePoints() {
        const data = getFilteredData();
        countEl.textContent = `${data.length} points shown`;

        const circles = plot
            .selectAll("circle")
            .data(
                data,
                (d, i) => `${d.species}-${d.flipper_length_mm}-${d.body_mass_g}-${i}`
            );

        circles.join(
            (enter) =>
                enter
                    .append("circle")
                    .attr("cx", (d) => x(d.flipper_length_mm))
                    .attr("cy", (d) => y(d.body_mass_g))
                    .attr("r", (d) => r(d.bill_length_mm))
                    .attr("fill", (d) => color(d.species))
                    .attr("fill-opacity", 0.8)
                    .attr("stroke", "#111")
                    .attr("stroke-opacity", 0.12)
                    .on("mousemove", (event, d) => {
                        tooltip
                            .style("opacity", 1)
                            .style("left", `${event.clientX}px`)
                            .style("top", `${event.clientY}px`)
                            .html(
                                `<b>${d.species}</b><br/>
                 flipper: ${d.flipper_length_mm} mm<br/>
                 body mass: ${d.body_mass_g} g<br/>
                 bill length: ${d.bill_length_mm} mm`
                            );
                    })
                    .on("mouseleave", () => tooltip.style("opacity", 0)),
            (update) =>
                update
                    .transition()
                    .duration(220)
                    .attr("cx", (d) => x(d.flipper_length_mm))
                    .attr("cy", (d) => y(d.body_mass_g))
                    .attr("r", (d) => r(d.bill_length_mm)),
            (exit) => exit.transition().duration(150).attr("r", 0).remove()
        );
    }

    function rerenderAxesAndGrid() {
        // Update axes
        yAxisG.transition().duration(250).call(d3.axisLeft(y).ticks(8));

        // Update gridlines to match new y scale
        yGridG
            .transition()
            .duration(250)
            .call(
                d3
                    .axisLeft(y)
                    .ticks(8)
                    .tickSize(-(width - margin.left - margin.right))
                    .tickFormat("")
            )
            .call((g) => g.select(".domain").remove());

        // Update y label text
        if (downwardToggle.checked) {
            yLabel.text("Body Mass (g) (increases downward)");
        } else {
            yLabel.text("Body Mass (g)");
        }
    }

    function updateAll() {
        updatePoints();
    }

    // Dropdown filter
    filterEl.addEventListener("change", updateAll);

    // Downward toggle
    downwardToggle.addEventListener("change", () => {
        y = downwardToggle.checked ? yDownward : yNormal;
        rerenderAxesAndGrid();
        updateAll();
    });

    // Legends (click to toggle species)
    const legend = svg
        .append("g")
        .attr("class", "legend")
        .attr(
            "transform",
            `translate(${width - margin.right + 20}, ${margin.top})`
        );

    legend
        .append("text")
        .attr("x", 0)
        .attr("y", 0)
        .attr("dy", "0.8em")
        .attr("font-weight", 700)
        .text("Species");

    const legendItems = legend
        .selectAll("g.item")
        .data(speciesList)
        .join("g")
        .attr("class", "item")
        .attr("transform", (d, i) => `translate(0, ${20 + i * 22})`)
        .style("cursor", "pointer")
        .on("click", (event, s) => {
            if (enabled.has(s)) enabled.delete(s);
            else enabled.add(s);
            legendItems.attr("opacity", (d) => (enabled.has(d) ? 1 : 0.35));
            updateAll();
        });

    legendItems
        .append("rect")
        .attr("x", 0)
        .attr("y", 4)
        .attr("width", 14)
        .attr("height", 14)
        .attr("rx", 3)
        .attr("fill", (d) => color(d));

    legendItems
        .append("text")
        .attr("x", 20)
        .attr("y", 16)
        .text((d) => d);

    // Size legend
    const sizeLegend = legend
        .append("g")
        .attr("transform", `translate(0, ${20 + speciesList.length * 22 + 22})`);

    sizeLegend
        .append("text")
        .attr("x", 0)
        .attr("y", 0)
        .attr("dy", "0.8em")
        .attr("font-weight", 700)
        .text("Bill length (mm)");

    const sizeValues = [
        Math.round(rExtent[0]),
        Math.round((rExtent[0] + rExtent[1]) / 2),
        Math.round(rExtent[1]),
    ];

    const sizeRow = sizeLegend
        .selectAll("g.s")
        .data(sizeValues)
        .join("g")
        .attr("transform", (d, i) => `translate(0, ${20 + i * 28})`);

    sizeRow
        .append("circle")
        .attr("cx", 9)
        .attr("cy", 9)
        .attr("r", (d) => r(d))
        .attr("fill", "#999")
        .attr("fill-opacity", 0.25)
        .attr("stroke", "#444")
        .attr("stroke-opacity", 0.35);

    sizeRow
        .append("text")
        .attr("x", 28)
        .attr("y", 13)
        .text((d) => d);

    // Initial render (default = reference-matching)
    rerenderAxesAndGrid();
    updateAll();
});