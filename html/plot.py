from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print __version__

import plotly
from plotly.graph_objs import Scatter, Layout

myChart = plotly.offline.plot({
    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": Layout(title="hello world", autosize=True)
    },output_type="div", show_link="False",include_plotlyjs="Flase",link_text="")

file = open('embed.html', 'w')
file.write(myChart)
