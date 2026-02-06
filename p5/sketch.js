let table;
let penguins = [];

let margin = { left: 110, right: 220, top: 90, bottom: 90 };

function preload() {
  table = loadTable(
    'penglings.csv',
    'csv',
    'header',
    () => console.log('CSV loaded successfully!'),
    (err) => console.error('Failed to load CSV:', err)
  );
}

function setup() {
  createCanvas(windowWidth, windowHeight);
  textAlign(CENTER, CENTER);
  background(255);

  if (!table || table.getRowCount() === 0) {
    textSize(24);
    text('CSV not loaded or empty!', width / 2, height / 2);
    return;
  }

  penguins = [];

  for (let r = 0; r < table.getRowCount(); r++) {
    const row = table.getRow(r);

    let flipper = parseFloat(row.get('flipper_length_mm'));
    let body = parseFloat(row.get('body_mass_g'));
    let bill = parseFloat(row.get('bill_length_mm'));
    let species = row.get('species');

    if (isNaN(flipper) || isNaN(body) || isNaN(bill)) continue;

    penguins.push({ flipper, body, bill, species });
  }

  if (penguins.length === 0) {
    textSize(24);
    text('No valid data in CSV!', width / 2, height / 2);
    return;
  }

  let flipperMin = 170;
  let flipperMax = 235;
  let bodyMin = 2700;
  let bodyMax = 6300;
  let billMin = Math.min(...penguins.map(p => p.bill));
  let billMax = Math.max(...penguins.map(p => p.bill));

  drawTitle();
  drawAxes(flipperMin, flipperMax, bodyMin, bodyMax);
  drawPenguins(flipperMin, flipperMax, bodyMin, bodyMax, billMin, billMax);
  drawLegends(billMin, billMax);
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
  background(255);
  setup();
}

function drawTitle() {
  textSize(28);
  fill(0);
  text(
    'Penguin Flipper Length vs Body Mass',
    width / 2 - margin.right / 2,
    margin.top / 2
  );
}

function drawAxes(flipperMin, flipperMax, bodyMin, bodyMax) {
  stroke(0);
  strokeWeight(1);

  let x0 = margin.left;
  let x1 = width - margin.right;
  let y0 = height - margin.bottom;
  let y1 = margin.top;

  // Axes
  line(x0, y0, x1, y0);
  line(x0, y0, x0, y1);

  // axis labels
  noStroke();
  fill(0);
  textSize(16);
  text('Flipper Length (mm)', (x0 + x1) / 2, height - 35);

  push();
  translate(35, (y0 + y1) / 2);
  rotate(-PI / 2);
  text('Body Mass (g)', 0, 0);
  pop();

  stroke(0);

  // X axis tics 
  for (let x = 170; x <= 235; x += 10) {
    let xpos = map(x, flipperMin, flipperMax, x0, x1);
    line(xpos, y0, xpos, y0 + 5);
    noStroke();
    fill(0);
    textSize(12);
    text(x, xpos, y0 + 18);
    stroke(0);
  }

  // Y axis tic
  for (let y = 2700; y <= 6300; y += 600) {
    let ypos = map(y, bodyMin, bodyMax, y0, y1);
    line(x0 - 5, ypos, x0, ypos);
    noStroke();
    fill(0);
    textSize(12);
    text(y, x0 - 45, ypos);
    stroke(0);
  }
}

function drawPenguins(flipperMin, flipperMax, bodyMin, bodyMax, billMin, billMax) {
  for (let p of penguins) {
    let x = map(
      p.flipper,
      flipperMin,
      flipperMax,
      margin.left,
      width - margin.right
    );
    let y = map(
      p.body,
      bodyMin,
      bodyMax,
      height - margin.bottom,
      margin.top
    );
    let s = map(p.bill, billMin, billMax, 6, 20);

    let c;
    switch (p.species.toLowerCase()) {
      case 'adelie': c = color(228, 26, 28, 200); break;
      case 'chinstrap': c = color(77, 175, 74, 200); break;
      case 'gentoo': c = color(55, 126, 184, 200); break;
      default: c = color(150, 150, 150, 200);
    }

    noStroke();
    fill(c);
    ellipse(x, y, s, s);
  }
}

function drawLegends(billMin, billMax) {
  let lx = width - margin.right + 30;
  let ly = margin.top + 10;

  textAlign(LEFT, CENTER);
  textSize(14);
  fill(0);
  noStroke();

  // species legend
  text('Species', lx, ly);

  let species = ['Adelie', 'Chinstrap', 'Gentoo'];
  let colors = [
    color(228, 26, 28),
    color(77, 175, 74),
    color(55, 126, 184)
  ];

  for (let i = 0; i < species.length; i++) {
    fill(colors[i]);
    ellipse(lx + 10, ly + 25 + i * 22, 10, 10);
    fill(0);
    text(species[i], lx + 25, ly + 25 + i * 22);
  }

  // Size legend
  let sy = ly + 110;
  text('Bill Length (mm)', lx, sy);

  let sizes = [billMin, (billMin + billMax) / 2, billMax];
  for (let i = 0; i < sizes.length; i++) {
    let s = map(sizes[i], billMin, billMax, 6, 20);
    noFill();
    stroke(0);
    ellipse(lx + 10, sy + 30 + i * 28, s, s);
    noStroke();
    fill(0);
    text(sizes[i].toFixed(1), lx + 35, sy + 30 + i * 28);
  }
}
