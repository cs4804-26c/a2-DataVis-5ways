import * as d3 from "d3"

export interface Pengling {
	species: string
	bill_length_mm: number
	flipper_length_mm: number
	body_mass_g: number
}

/* AI Usage Note: Create a histogram create a plot below the current plot that highlights where the selected point is in the distribution of flipper length for its own species (probably in a histogram) */
/* Then, I refactored it to support multiple histograms */

export function createHistogram(
	containerId: string,
	data: Pengling[],
	selectedDatum: Pengling,
	metric: keyof Pengling,
	metricLabel: string,
	color: string,
) {
	d3.select(containerId).html("")

	const speciesData = data.filter((d) => d.species === selectedDatum.species)

	const width = 800
	const height = 300
	const margin = { top: 20, right: 30, bottom: 50, left: 60 }

	const svg = d3
		.select(containerId)
		.append("svg")
		.attr("width", width)
		.attr("height", height)
		.style(
			"font-family",
			"system-ui, -apple-system, Segoe UI, Roboto, sans-serif",
		)
		.style("font-size", "12px")

	const getMetricValue = (d: Pengling) => {
		const val = d[metric]
		return typeof val === "number" ? val : 0
	}

	const x = d3
		.scaleLinear()
		.domain(d3.extent(speciesData, getMetricValue) as [number, number])
		.range([margin.left, width - margin.right])
		.nice()

	const histogram = d3
		.bin<Pengling, number>()
		.value(getMetricValue)
		.domain(x.domain() as [number, number])
		.thresholds(x.ticks(20))

	const bins = histogram(speciesData)

	const y = d3
		.scaleLinear()
		.domain([0, d3.max(bins, (d) => d.length) as number])
		.range([height - margin.bottom, margin.top])
		.nice()

	const panelBg = "#EBEBEB"
	const gridColor = "#FFFFFF"
	const axisText = "#4D4D4D"
	const titleText = "#333333"

	svg.append("rect")
		.attr("x", margin.left)
		.attr("y", margin.top)
		.attr("width", width - margin.left - margin.right)
		.attr("height", height - margin.top - margin.bottom)
		.attr("fill", panelBg)

	const xGrid = d3
		.axisBottom(x)
		.tickSize(-(height - margin.top - margin.bottom))
		.tickFormat(() => "")
	const yGrid = d3
		.axisLeft(y)
		.tickSize(-(width - margin.left - margin.right))
		.tickFormat(() => "")

	svg.append("g")
		.attr("transform", `translate(0,${height - margin.bottom})`)
		.call(xGrid)
		.call((g) => g.select(".domain").remove())
		.call((g) => g.selectAll("line").attr("stroke", gridColor))

	svg.append("g")
		.attr("transform", `translate(${margin.left},0)`)
		.call(yGrid)
		.call((g) => g.select(".domain").remove())
		.call((g) => g.selectAll("line").attr("stroke", gridColor))

	svg.append("g")
		.selectAll("rect")
		.data(bins)
		.join("rect")
		.attr("x", (d) => x(d.x0!))
		.attr("width", (d) => Math.max(0, x(d.x1!) - x(d.x0!) - 1))
		.attr("y", (d) => y(d.length))
		.attr("height", (d) => y(0) - y(d.length))
		.attr("fill", color)
		.attr("fill-opacity", (d) => (d.includes(selectedDatum) ? 1 : 0.4))

	const xAxis = d3.axisBottom(x)
	const yAxis = d3.axisLeft(y)

	svg.append("g")
		.attr("transform", `translate(0,${height - margin.bottom})`)
		.call(xAxis)
		.call((g) => g.select(".domain").remove())
		.call((g) => g.selectAll("text").attr("fill", axisText))

	svg.append("g")
		.attr("transform", `translate(${margin.left},0)`)
		.call(yAxis)
		.call((g) => g.select(".domain").remove())
		.call((g) => g.selectAll("text").attr("fill", axisText))

	svg.append("text")
		.attr("x", (width + margin.left - margin.right) / 2)
		.attr("y", height - 10)
		.attr("text-anchor", "middle")
		.attr("fill", titleText)
		.text(
			`${metricLabel} distribution for ${selectedDatum.species} (selected: ${getMetricValue(selectedDatum)}${metricLabel === "Body Mass" ? "g" : "mm"})`,
		)
}

