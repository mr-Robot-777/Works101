import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL, FB, GOOG

output_file("gfg.html")

graph = figure( x_axis_type = "datetime", title = "Stock Closing Prises")

graph.xaxis.axis.label = 'Date'
graph.yaxis.axis_label = 'Price (in USD)'


x_axis_coordinates = np.array(AAPL['date'], dtype = np.datetime64)
y_axis_coordinates = AAPL['adj_close']
color = "lightblue"
legend_label = 'AAPL'
graph.line(x_axis_coordinates, y_axis_coordinates, color=color, legend_label = legend_label)



x_axis_coordinates = np.array(FB['date'], dtype = np.datetime64)
y_axis_coordinates = FB['adj_close']
color = "black"
legend_label = 'FB'
graph.line(x_axis_coordinates, y_axis_coordinates, color=color, legend_label = legend_label)



x_axis_coordinates = np.array(GOOG['date'], dtype = np.datetime64)
y_axis_coordinates = GOOG['adj_close']
color = "orange"
legend_label = 'GOOG'
graph.line(x_axis_coordinates, y_axis_coordinates, color=color, legend_label = legend_label)


graph.legend.location = "top_left"
show(graph)


