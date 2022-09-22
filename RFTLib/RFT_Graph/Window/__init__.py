from ..Require import *

from ..Graph import *
from ..Utils import *

from .exit import *
from .show import *
from .update import *

from .closeEvent import *
from .paintEvent import *

from .mousePressEvent import *
from .mouseReleaseEvent import *
from .mouseMoveEvent import *

from .keyPressEvent import *
from .keyReleaseEvent import *





__all__=["Window"]





class Window:


	exit=exit
	show=show
	update=update

	closeEvent=closeEvent
	paintEvent=paintEvent

	mousePressEvent=mousePressEvent
	mouseReleaseEvent=mouseReleaseEvent
	mouseMoveEvent=mouseMoveEvent

	keyPressEvent=keyPressEvent
	keyReleaseEvent=keyReleaseEvent


	def __init__(self,*,width:int=256,height:int=256,x:int=0,y:int=0,graph:Graph=None):
		# ~~~~~~~ configure window ~~~~~~~
		self.widget=QWidget() # create widget


		# set default geometry
		self.x=x
		self.y=y

		self.width=width
		self.height=height

		
		# set widget events
		self.widget.paintEvent=self.paintEvent
		self.widget.keyPressEvent=self.keyPressEvent
		self.widget.keyReleaseEvent=self.keyReleaseEvent

		self.widget.mouseMoveEvent=self.mouseMoveEvent
		self.widget.mousePressEvent=self.mousePressEvent
		self.widget.mouseReleaseEvent=self.mouseReleaseEvent

		self.widget.closeEvent=self.closeEvent



		self.widget.setCursor(Qt.CrossCursor) # set cursor
		self.widget.setWindowTitle("Raphter") # set window title

		self.widget.setWindowFlags(Qt.FramelessWindowHint) # make window frameless
		self.widget.setAttribute(Qt.WA_TranslucentBackground,True) # make background translucent

		self.widget.setGeometry(self.x,self.y,self.width,self.height) # set window geometry
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 



		# ~~~~~~~~~ set variables ~~~~~~~~
		self.running=True

		self.pause=False

		self.smooth=False


		self.mousePos=(0,0)

		self.fps=0
		self.displayFPS=True
		self.fpsFrames=collections.deque(maxlen=50)
		self.fpsFrames.append(time.time())

		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 



		# ~~~~~~ set paint variables ~~~~~
		self.backgroundColor:Color=Color(0x00,0x00,0x00,0xFF) # set default background color

		self.graph=graph
			
		self.texts:Dict[str,Text]={}
		self.graphs:Dict[str,Graph]={}
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





	def clearTexts(self):
		self.texts.clear()




	def clearGraphs(self):
		self.graphs.clear()



