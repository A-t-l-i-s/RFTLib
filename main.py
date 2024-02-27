from RFTLib.Require import *

from RFTLib.Core.Math import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Object import *
from RFTLib.Core.Exception import *
from RFTLib.Core.Structure import *

from RFTLib.Core.Graphic.Text import *
from RFTLib.Core.Graphic.Color import *

from RFTLib.Core.Geometric.Nan import *
from RFTLib.Core.Geometric.Line import *
from RFTLib.Core.Geometric.Point import *
from RFTLib.Core.Geometric.Circle import *
from RFTLib.Core.Geometric.Ellipse import *
from RFTLib.Core.Geometric.Polygon import *
from RFTLib.Core.Geometric.Rectangle import *

from RFTLib.Core.Decorators.Label import *
from RFTLib.Core.Decorators.Structure import *
from RFTLib.Core.Decorators.Threading import *

from RFTLib.Config import *
from RFTLib.Config.qt import *
from RFTLib.Config.cv2 import *
from RFTLib.Config.nil import *
from RFTLib.Config.json import *
from RFTLib.Config.text import *
from RFTLib.Config.toml import *
from RFTLib.Config.yaml import *
from RFTLib.Config.pillow import *
from RFTLib.Config.python import *

from RFTLib.Tables import *

from RFTLib.Graph import *
from RFTLib.Graph.Window import *





if (__name__ == "__main__"):
	graph = RFT_Graph(1000, 1000)

	win = RFT_Graph_Window(800, 800)
	win += graph

	# win.fps = 240
	win.smoothing = True
	win.displayFPS = True

	win.show()



	while win.running:
		for i in range(300):
			r = RFT_Rectangle(graph.randomPos(), graph.randomPos())
			graph[r] = RFT_Color.RGB((r.begin.x - r.end.x) % 255, ((r.begin.y - r.end.y) % 255), 200)
			win.update()
			win.wait()


		graph[RFT_Rectangle(graph.randomPos(), graph.randomPos())] = RFT_Color.Transparent().setThickness(-1)





