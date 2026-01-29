import "./style.css"
import * as d3 from "d3"
import { createHistogram } from "./histogram"

/* AI Usage Note: Can you mimic the ggplot2 theme_grey? It should have a white grid with a gray background. */

const CSV_PATH = "/penglings.csv"

const SPECIES_COLORS: Record<string, string> = {
	Adelie: "orange",
	Chinstrap: "purple",
	Gentoo: "darkcyan",
}

const DEFAULT_SPECIES_COLOR = "#888888"

/* AI Usage Note: Can you make the scales have a bit of padding (lower min, higher max) so that the points aren't on the axes? */
function padDomain(
	domain: [number, number],
	padFraction: number = 0.05,
): [number, number] {
	const [min, max] = domain
	const span = max - min
	const pad = span === 0 ? 1 : span * padFraction
	return [min - pad, max + pad]
}

document.querySelector<HTMLDivElement>("#app")!.innerHTML = `
  <div>
    <h1>d3-plot</h1>
    <div id="chart"></div>
    <div id="histogram-flipper"></div>
    <div id="histogram-mass"></div>
    <div id="histogram-bill"></div>
  </div>
`

d3.csv(CSV_PATH).then((data) => {
	const parsed = data
		.map((d) => {
			const species = (d.species ?? "").trim() || "Unknown"
			const bill_length_mm = Number(d.bill_length_mm)
			const flipper_length_mm = Number(d.flipper_length_mm)
			const body_mass_g = Number(d.body_mass_g)
			if (
				Number.isNaN(bill_length_mm) ||
				Number.isNaN(flipper_length_mm) ||
				Number.isNaN(body_mass_g)
			)
				return null
			return { species, bill_length_mm, flipper_length_mm, body_mass_g }
		})
		.filter(
			(
				d,
			): d is {
				species: string
				bill_length_mm: number
				flipper_length_mm: number
				body_mass_g: number
			} => d !== null,
		)

	const legendWidth = 200
	const width = 800 + legendWidth
	const height = 600
	const margin = { top: 20, right: 30, bottom: 55, left: 60 }
	const plotRight = width - margin.right - legendWidth
	const innerWidth = plotRight - margin.left
	const innerHeight = height - margin.top - margin.bottom

	const svg = d3
		.select("#chart")
		.append("svg")
		.attr("width", width)
		.attr("height", height)
		.style(
			"font-family",
			"system-ui, -apple-system, Segoe UI, Roboto, sans-serif",
		)
		.style("font-size", "12px")

	if (parsed.length === 0) {
		svg.append("text")
			.attr("x", width / 2)
			.attr("y", height / 2)
			.attr("text-anchor", "middle")
			.attr("fill", "currentColor")
			.text("No valid rows (NaN values skipped)")
		return
	}

	const xExtent = d3.extent(parsed, (d) => d.flipper_length_mm) as [
		number,
		number,
	]
	const yExtent = d3.extent(parsed, (d) => d.body_mass_g) as [number, number]

	const x = d3
		.scaleLinear()
		.domain(padDomain(xExtent, 0.03))
		.range([margin.left, plotRight])
		.nice()

	const y = d3
		.scaleLinear()
		.domain(padDomain(yExtent, 0.03))
		.range([height - margin.bottom, margin.top])
		.nice()

	const r = d3
		.scaleSqrt()
		.domain(d3.extent(parsed, (d) => d.bill_length_mm) as [number, number])
		.range([5, 13])
		.clamp(true)

	// ggplot2 theme_grey-like styling
	const panelBg = "#EBEBEB"
	const gridColor = "#FFFFFF"
	const axisText = "#4D4D4D"
	const titleText = "#333333"

	// Panel background
	svg.append("rect")
		.attr("x", margin.left)
		.attr("y", margin.top)
		.attr("width", innerWidth)
		.attr("height", innerHeight)
		.attr("fill", panelBg)

	// Major gridlines (white)
	const xGrid = d3
		.axisBottom(x)
		.tickSize(-innerHeight)
		.tickFormat(() => "")

	const yGrid = d3
		.axisLeft(y)
		.tickSize(-innerWidth)
		.tickFormat(() => "")

	svg.append("g")
		.attr("transform", `translate(0,${height - margin.bottom})`)
		.call(xGrid)
		.call((g) => g.select(".domain").remove())
		.call((g) =>
			g
				.selectAll<SVGLineElement, unknown>("line")
				.attr("stroke", gridColor)
				.attr("stroke-width", 1),
		)

	svg.append("g")
		.attr("transform", `translate(${margin.left},0)`)
		.call(yGrid)
		.call((g) => g.select(".domain").remove())
		.call((g) =>
			g
				.selectAll<SVGLineElement, unknown>("line")
				.attr("stroke", gridColor)
				.attr("stroke-width", 1),
		)

	const xAxis = d3.axisBottom(x).tickSizeOuter(0)
	const yAxis = d3.axisLeft(y).tickSizeOuter(0)

	svg.append("g")
		.attr("transform", `translate(0,${height - margin.bottom})`)
		.call(xAxis)
		.call((g) => g.select(".domain").remove())
		.call((g) => g.selectAll("line").remove())
		.call((g) => g.selectAll("text").attr("fill", axisText))

	svg.append("text")
		.attr("x", (margin.left + plotRight) / 2)
		.attr("y", height - 10)
		.attr("text-anchor", "middle")
		.attr("fill", titleText)
		.text("Flipper Length (mm)")

	svg.append("g")
		.attr("transform", `translate(${margin.left},0)`)
		.call(yAxis)
		.call((g) => g.select(".domain").remove())
		.call((g) => g.selectAll("line").remove())
		.call((g) => g.selectAll("text").attr("fill", axisText))

	svg.append("text")
		.attr("transform", "rotate(-90)")
		.attr("x", -(margin.top + (height - margin.bottom)) / 2)
		.attr("y", 18)
		.attr("text-anchor", "middle")
		.attr("fill", titleText)
		.text("Body Mass (g)")

	svg.append("g")
		.selectAll("circle")
		.data(parsed)
		.enter()
		.append("circle")
		.attr("cx", (d) => x(d.flipper_length_mm))
		.attr("cy", (d) => y(d.body_mass_g))
		.attr("r", (d) => r(d.bill_length_mm))
		.attr("fill", (d) => SPECIES_COLORS[d.species] ?? DEFAULT_SPECIES_COLOR)
		.attr("fill-opacity", 0.8)
		.attr(
			"stroke",
			(d) => SPECIES_COLORS[d.species] ?? DEFAULT_SPECIES_COLOR,
		)
		.attr("stroke-width", 0.5)
		.on("mouseover", function () {
			d3.select(this).attr("stroke-width", 2).attr("fill-opacity", 1.0)
		})
		.on("mouseout", function () {
			d3.select(this).attr("stroke-width", 0.5).attr("fill-opacity", 0.8)
		})
		.on("click", (_, d) => {
			const color = SPECIES_COLORS[d.species] ?? DEFAULT_SPECIES_COLOR
			createHistogram(
				"#histogram-flipper",
				parsed,
				d,
				"flipper_length_mm",
				"Flipper Length",
				color,
			)
			createHistogram(
				"#histogram-mass",
				parsed,
				d,
				"body_mass_g",
				"Body Mass",
				color,
			)
			createHistogram(
				"#histogram-bill",
				parsed,
				d,
				"bill_length_mm",
				"Bill Length",
				color,
			)
		})

	/* AI Usage Note:
    Can you add a legend off of the right side of the plot? It should be centered vertically. The first section should be for bill_length_mm, and it should have two circles representing the size of a point with data value 40 and with 50. The circles should be gray and slightly transparent, but with a solid border. 

    Below should be the species section, and it is similar but shows the colors.
  */
	// Legend (right side, centered vertically)
	const legendX = plotRight + 24
	const legendTitleSize = 12
	const legendTextSize = 12
	const legendLineHeight = 18

	const sizeLegendValues: [number, number] = [40, 50]
	const sizeLegendR = sizeLegendValues.map((v) => r(v))
	const sizeLegendMaxR = d3.max(sizeLegendR) ?? 0
	const sizeLegendTitleH = legendLineHeight
	const sizeLegendRowH = Math.max(legendLineHeight, sizeLegendMaxR * 2 + 6)
	const sizeLegendCirclesH = sizeLegendRowH * sizeLegendValues.length
	const sizeLegendH = sizeLegendTitleH + sizeLegendCirclesH + 6

	const species = Object.keys(SPECIES_COLORS)
	const speciesLegendTitleH = legendLineHeight
	const speciesLegendItemsH = species.length * legendLineHeight
	const speciesLegendH = speciesLegendTitleH + speciesLegendItemsH

	const legendGap = 18
	const legendH = sizeLegendH + legendGap + speciesLegendH
	const legendY = margin.top + innerHeight / 2 - legendH / 2

	const legend = svg
		.append("g")
		.attr("transform", `translate(${legendX},${legendY})`)

	// Size legend
	legend
		.append("text")
		.attr("x", 0)
		.attr("y", legendTitleSize)
		.attr("fill", titleText)
		.style("font-size", `${legendTitleSize}px`)
		.text("bill_length_mm")

	const sizeLegendTop = sizeLegendTitleH
	const sizeLegendCircleX = sizeLegendMaxR
	const sizeLegendLabelX = sizeLegendMaxR * 2 + 10

	sizeLegendValues.forEach((value, i) => {
		const radius = r(value)
		const cy = sizeLegendTop + i * sizeLegendRowH + sizeLegendRowH / 2
		legend
			.append("circle")
			.attr("cx", sizeLegendCircleX)
			.attr("cy", cy)
			.attr("r", radius)
			.attr("fill", "#7F7F7F")
			.attr("fill-opacity", 0.35)
			.attr("stroke", "#4D4D4D")
			.attr("stroke-width", 1)

		legend
			.append("text")
			.attr("x", sizeLegendLabelX)
			.attr("y", cy)
			.attr("dominant-baseline", "middle")
			.attr("fill", axisText)
			.style("font-size", `${legendTextSize}px`)
			.text(String(value))
	})

	// Species legend
	const speciesLegendY = sizeLegendH + legendGap
	legend
		.append("text")
		.attr("x", 0)
		.attr("y", speciesLegendY + legendTitleSize)
		.attr("fill", titleText)
		.style("font-size", `${legendTitleSize}px`)
		.text("species")

	const speciesItemStartY = speciesLegendY + speciesLegendTitleH
	const speciesDotR = 6
	const speciesDotX = speciesDotR
	const speciesLabelX = speciesDotR * 2 + 10

	species.forEach((sp, i) => {
		const yPos =
			speciesItemStartY + i * legendLineHeight + legendLineHeight / 2
		const c = SPECIES_COLORS[sp] ?? DEFAULT_SPECIES_COLOR

		legend
			.append("circle")
			.attr("cx", speciesDotX)
			.attr("cy", yPos)
			.attr("r", speciesDotR)
			.attr("fill", c)
			.attr("fill-opacity", 0.8)
			.attr("stroke", c)
			.attr("stroke-width", 1)

		legend
			.append("text")
			.attr("x", speciesLabelX)
			.attr("y", yPos)
			.attr("dominant-baseline", "middle")
			.attr("fill", axisText)
			.style("font-size", `${legendTextSize}px`)
			.text(sp)
	})
})

