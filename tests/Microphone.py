from RFTLib.Require import *

from RFTLib.Core.Buffer import *
from RFTLib.Core.Object import *
from RFTLib.Core.Structure import *

from RFTLib.Core.Geometric.Circle import *
from RFTLib.Core.Geometric.Ellipse import *
from RFTLib.Core.Geometric.Line import *
from RFTLib.Core.Geometric.Nan import *
from RFTLib.Core.Geometric.Point import *
from RFTLib.Core.Geometric.Polygon import *
from RFTLib.Core.Geometric.Rectangle import *

from RFTLib.Core.Graphic.Text import *
from RFTLib.Core.Graphic.Color import *

from RFTLib.Graph import *
from RFTLib.Graph.Window import *





if (__name__ == "__main__"):
	import pyaudio
	import numpy as np



	audio = pyaudio.PyAudio()
	stream = audio.open(
		format = pyaudio.paInt16,
		channels = 1,
		rate = 44100,
		input = True,
		frames_per_buffer = 1024,
	)



	graph = RFT_Graph(256 * 4 , 256 * 2)

	window = RFT_Graph_Window(graph.width, graph.height)
	window.show()

	window.smoothing = True
	window.displayFPS = True

	window += graph



	spacing = graph.width / 256
	i = 0



	while window.running:

		data_ = stream.read(1024)
		data = np.frombuffer(data_, np.uint16)
		data = np.resize(data, 256)


		for i, c in enumerate(data):
			x = spacing * i
			y = c / 32


			if (c >= (2 ** 16) / 2):
				y = 0


			graph[
				RFT_Rectangle(
					(x, 0),
					(x + spacing, y)
				)
			] = RFT_Color.RGB(
				round(c / 2),
				round(i * 2),
				255
			)


		graph.first.x2 = 0
		graph.first.y2 = 0

		window.update()
		graph.clear()