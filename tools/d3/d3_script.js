// SVG Constants
var margin = {top: 30, right: 200, bottom: 80, left: 100},
		width = 1280 - margin.left - margin.right,
		height = 850 - margin.top - margin.bottom;

// Append the svg to the page
var svg = d3.select("#container")
	.append("svg")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
	.append("g")
		.attr("transform",
					"translate(" + margin.left + "," + margin.top + ")");

// Load data from the CSV
d3.csv('./penglings.csv', function(data) {

	// Add X axis
	var x = d3.scaleLinear()
		.domain([170, 235])
		.range([0, width]);
	svg.append("g")
		.attr("class", "axis x-axis text")
		.attr("transform", "translate(0," + height + ")")
		.call(d3.axisBottom(x)
			.tickPadding(8)
			.tickValues(ticks(x.domain()[0], 10, x.domain()[1]))
			.tickFormat((d,i) => tickLabels(x.domain()[0], 10, x.domain()[1])[i])
			.tickSize(-height)
		);

	// Add X axis label
	svg.append("text")
		.attr("class", "label text")
		.attr("text-anchor", "middle")
		.attr("x", width/2)
		.attr("y", height+60)
		.attr("font-size", 20)
		.text("Flipper Length (mm)");

	// Add Y axis
	var y = d3.scaleLinear()
		.domain([2500, 6500])
		.range([height, 0]);
	svg.append("g")
		.attr("class", "axis y-axis text")
		.call(d3.axisLeft(y)
			.tickPadding(5)
			.tickValues(ticks(y.domain()[0], 1000, y.domain()[1]))
			.tickFormat((d,i) => ['',...tickLabels(y.domain()[0]+500, 1000, y.domain()[1])][i])
			.tickSize(-width)
		);

	// Add Y axis label
	svg.append("text")
		.attr("class", "label text")
		.attr("text-anchor", "middle")
		.attr("y", -70)
		.attr("x", -height/2)
		.attr("transform", "rotate(-90)")
		.text("Body Mass (g)");

	// Add a scale for bubble size
	var z = d3.scaleLinear()
		.domain([30, 60])
		.range([5, 20]);

	// Add a scale for bubble color
	var myColor = d3.scaleOrdinal()
		.domain(['Adelie', 'Chinstrap', 'Gentoo'])
		.range(['#fda246', '#ac5ad4', '#49a1a1']);

	// Add bubbles
	svg.append('g')
		.selectAll("dot")
		.data(data)
		.enter()
		.append("circle")
			.attr("cx", function (d) { return x(d.flipper_length_mm); } )
			.attr("cy", function (d) { return y(d.body_mass_g); } )
			.attr("r", function (d) { return z(d.bill_length_mm); } )
			.style("fill", function (d) { return myColor(d.species); } )
			.style("opacity", "0.8")
			.style("stroke-width", "2px")

	// Bill Length Legend
	svg.selectAll("legend")
		.data([50, 40])
		.enter()
		.append("circle")
			.attr("cx", width+50)
			.attr("cy", function(d){ return 200 + (z(d) * 8) } )
			.attr("r", function(d){ return z(d) })
			.style("fill", "black")
			.style("opacity", "0.8")
			.attr("stroke", "black")

	// Bill Legend Labels
	svg.selectAll("legend")
		.data([50, 40])
		.enter()
		.append("text")
			.attr("class", "text")
			.attr('x', width+80)
			.attr('y', function(d){ return 200 + (z(d) * 8) } )
			.text( function(d){ return d + " mm" } )
			.style("font-size", 16)
			.attr('alignment-baseline', 'middle')

	// Bill Legend Title
	svg.append("text")
		.attr("class", "text")
		.attr('x', width+85)
		.attr("y", 250)
		.text("Bill Length")
		.style("font-weight", 700)
		.style("font-size", 20)
		.attr("text-anchor", "middle")

	// Species Legend
	svg.selectAll("legend")
		.data(myColor.domain())
		.enter()
		.append("circle")
			.attr("cx", width + 50)
			.attr("cy", function(d,i){ return 450 + i*30 })
			.attr("r", 8)
			.style("fill", function(d){ return myColor(d) })

	// Species Legend Labels
	svg.selectAll("legend")
		.data(myColor.domain())
		.enter()
		.append("text")
			.attr("class", "text")
			.attr("x", width + 65)
			.attr("y", function(d,i){ return 452 + i*30 })
			.text(function(d){ return d })
			.attr("text-anchor", "left")
			.style("alignment-baseline", "middle")

	// Bill Legend Title
	svg.append("text")
		.attr("class", "text")
		.attr('x', width+75)
		.attr("y", 425)
		.text("Species")
		.style("font-weight", 700)
		.style("font-size", 20)
		.attr("text-anchor", "middle")
})

// Generate array of tick locations
function ticks(start, step, end) {
	let ticks = [start];
	
	while (ticks[ticks.length-1] < end) {
		ticks.push(ticks[ticks.length-1] + (step/2))
	}

	return ticks;
}

// Generate array of tick labels
function tickLabels(start, step, end) {
	let ticks = [start];
	let currTick = start
	let labelled = false;
	
	while (currTick < end) {
		if (labelled) {
			currTick += step/2;
			ticks.push(currTick)
			labelled = false;
		}
		else {
			currTick += step/2;
			ticks.push('');
			labelled = true;
		}
	}

	return ticks;
}