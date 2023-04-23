from RFTLib.Require import *

from RFTLib.Core.Types import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Object import *
from RFTLib.Core.Structure import *

from RFTLib.Core.Gui.Text import *
from RFTLib.Core.Gui.Color import *

from RFTLib.Config import *
from RFTLib.Config.qt import *
from RFTLib.Config.cv2 import *
from RFTLib.Config.json import *
from RFTLib.Config.text import *
from RFTLib.Config.toml import *
from RFTLib.Config.yaml import *
from RFTLib.Config.pillow import *
from RFTLib.Config.rypple import *

from RFTLib.Saves import *

from RFTLib.Graph import *
from RFTLib.Graph.nan import *
from RFTLib.Graph.line import *
from RFTLib.Graph.point import *
from RFTLib.Graph.circle import *
from RFTLib.Graph.ellipse import *
from RFTLib.Graph.velocity import *
from RFTLib.Graph.rectangle import *

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
				RFT_Graph_Rectangle(
					x, 0,
					x + spacing, y
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