function modifyChart() {
  let spreadsheet = SpreadsheetApp.openById('1OLkRzfr5S8nHUq84VbZ7uw3gTIUGplQE28-rcaVlAak');
  let sheet = spreadsheet.getSheetByName('penglings');

  // Define reusable styles
  let labelStyle = {
    fontName: 'Arial',
    fontSize: 18
  }
  let axisStyle = {
    titleTextStyle: {
      fontName: 'Arial',
      fontSize: 26
    },
    textStyle: labelStyle,
    gridlines: {
      color: 'white',
    },
    minorGridlines: {
      color: 'white',
      count: 1
    }
  }

  // Order data by Species column
  sheet.getRange('A2:I').sort(2);

  // Create new chart
  let chart = sheet.newChart()
    .setPosition(1, 1, 0, 0)
    .setChartType(Charts.ChartType.BUBBLE)
    .addRange(sheet.getRange('F1:F'))
    .addRange(sheet.getRange('G1:G'))
    .addRange(sheet.getRange('B1:B'))
    .addRange(sheet.getRange('D1:D'))
    .setNumHeaders(1)
    .setOption('backgroundColor', '#ebebeb')
    .setOption('colors', ['#fda246', '#ac5ad4', '#49a1a1'])
    .setOption('legend', {
      position: 'right',
      textStyle: labelStyle
    })
    .setOption('hAxis', {
      title: 'Flipper Length (mm)',
      minValue: 170,
      maxValue: 235
    })
    .setOption('hAxis', axisStyle)
    .setOption('vAxis', {
      title: 'Body Mass (g)',
      minValue: 2000,
      maxValue: 7000,
      gridlines: {
        count: 6
      }
    })
    .setOption('vAxis', axisStyle)
    .setOption('bubble.opacity', 0.8)
    .setOption('sizeAxis', {minSize: 5, maxSize: 20})
  .build();

  // Update Chart
  if(!spreadsheet.getSheetByName('temp')) {
    spreadsheet.insertSheet().setName('temp');
  }

  let tempSheet = spreadsheet.getSheetByName('temp');
  tempSheet.getCharts().forEach((chart) => tempSheet.removeChart(chart));
  tempSheet.insertChart(chart);

  // Move graph to its own page
  if(spreadsheet.getSheetByName('Chart')) {
    spreadsheet.deleteSheet(spreadsheet.getSheetByName('Chart'));
  }
  let objectSheet = spreadsheet.moveChartToObjectSheet(chart);
  objectSheet.setName('Chart');

  // Delete temporary spreadsheet
  spreadsheet.deleteSheet(tempSheet)
}
