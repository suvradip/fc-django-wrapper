from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..lib.fusioncharts import FusionCharts

from ..models import *

# The `fc_dict` function is defined to load data from a Python Dictionary. This data will be converted to
# JSON and the chart will be rendered.

def fc_db(request):
	# Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
	dataSource = {}
	dataSource['chart'] = { 
		"caption" : "Top 10 Most Populous Countries",
	    "paletteColors" : "#0075c2",
	    "bgColor" : "#ffffff",
	    "borderAlpha": "20",
	    "canvasBorderAlpha": "0",
	    "usePlotGradientColor": "0",
	    "plotBorderAlpha": "10",
	    "showXAxisLine": "1",
	    "xAxisLineColor" : "#999999",
	    "showValues" : "0",
	    "divlineColor" : "#999999",
	    "divLineIsDashed" : "1",
	    "showAlternateHGridColor" : "0"
		}
   
    # Convert the data in the `actualData` array into a format that can be consumed by FusionCharts. 
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

	dataSource['data'] = []
    # Iterate through the data in `Country` model and insert in to the `dataSource['data']` list.
	for key in Country.objects.all():
	  data = {}
	  data['label'] = key.Name
	  data['value'] = key.Population
	  dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor        	  		
	column2D = FusionCharts("column2D", "ex1" , "600", "400", "chart-1", "json", dataSource)
	return render(request, 'fusioncharts-html-template.html', {'output': column2D.render()}) 
