from RFTLib.Require import *

from RFTLib.Core.Math import *
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
	graph = RFT_Graph(256 * 3, 256 * 3)

	win = RFT_Graph_Window(800,800)
	win += graph

	win.smoothing = True
	win.displayFPS = True

	win.show()

	texts = {}
	for t in range(0xff + 1):
		texts[t] = RFT_Text("").setColor(RFT_Color.White()).setFont("Consolas").setFontSize(8)
		win += texts[t]




	while win.running:
		origData = list(range(0xff + 1))
		size = len(origData)


		seed = RFT_Math.pairing(
			random.randint(-180, 180),
			random.randint(-180, 180)
		)


		w1 = graph.width // size
		h1 = graph.height // size


		for i, v in enumerate(origData):
			shift = math.floor(math.sin(( i + 1 + size) * seed) * 256)

			v += shift
			v %= 0xff

			x = i * w1
			y = v * h1

			text = texts[i]
			text.setText(f"{i}:{v}").setPos((x, win.height - y))

			graph[
				RFT_Line(
					graph.first.end,
					(x, y)
				)
			] = RFT_Color.RGB(256 - v, v % 256, i % 256)



		win.update()
		win.pause()

		graph.reset()



