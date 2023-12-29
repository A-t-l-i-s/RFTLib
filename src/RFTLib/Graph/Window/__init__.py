from ...Require import *

import numpy as np

from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication, QWidget

from .. import *

from .KeyEvent import *
from .MouseEvent import *
from .closeEvent import *
from .paintEvent import *

from ...Core.Buffer import *
from ...Core.Object import *
from ...Core.Structure import *

from ...Core.Gui.Text import *
from ...Core.Gui.Color import *


# Initialize qt app 
QtApp = QApplication([])





__all__ = ("RFT_Graph_Window",)





class RFT_Graph_Window(RFT_Object):



	# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
	closeEvent = closeEvent
	paintEvent = paintEvent

	keyPressEvent = KeyEvent.press
	keyReleaseEvent = KeyEvent.release
	
	mousePressEvent = MouseEvent.press
	mouseReleaseEvent = MouseEvent.release
	mouseMoveEvent = MouseEvent.move
	wheelEvent = MouseEvent.wheel
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def __init__(self, width:int, height:int):
		self.running = True
		self.paused = False

		self.smoothing = False

		self.displayText = True
		self.displayFPS = False

		self.x = 0
		self.y = 0
		self.width = width
		self.height = height

		self.shiftDown = False
		self.mousePos = (0, 0)

		self.fps = 0
		self.fpsFrames = collections.deque(maxlen = 50)
		self.fpsFrames.append(time.time())

		self.backgroundColor = RFT_Color.RGBA(0, 0, 0, 255)

		self.graphs = []
		self.texts = []





		# Create window
		self.widget = QWidget()


		# Register events
		self.widget.closeEvent = self.closeEvent
		self.widget.paintEvent = self.paintEvent
		
		self.widget.keyPressEvent = self.keyPressEvent
		self.widget.keyReleaseEvent = self.keyReleaseEvent

		self.widget.mousePressEvent = self.mousePressEvent
		self.widget.mouseReleaseEvent = self.mouseReleaseEvent
		self.widget.mouseMoveEvent = self.mouseMoveEvent
		self.widget.wheelEvent = self.wheelEvent


		# Configuration
		self.widget.setWindowTitle("RFT Graph") # Set title
		self.widget.setCursor(Qt.CursorShape.CrossCursor) # Set cursor

		self.widget.setWindowFlags(Qt.WindowType.FramelessWindowHint) # Set frameless window
		self.widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True) # Set transparent background

		self.widget.resize(self.width, self.height) # Set window size





	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	def __add__(self, obj):
		if (isinstance(obj, RFT_Graph)):
			self.graphs.append(
				obj
			)

		elif (isinstance(obj, RFT_Text)):
			self.texts.append(
				obj
			)


		return self



	def __sub__(self, obj):
		if (isinstance(obj, RFT_Graph)):
			self.graphs.remove(
				obj
			)

		elif (isinstance(obj, RFT_Text)):
			self.texts.remove(
				obj
			)


		return self
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Methods ~~~~~~~~~~~
	def show(self):
		self.widget.show()

	def hide(self):
		self.widget.hide()



	def resize(self, width:int, height:int):
		self.width = width
		self.height = height

		self.widget.resize(self.width,self.height)



	def exit(self):
		self.running = False
		self.paused = False

		self.hide()



	def pause(self):
		self.paused = True

	def resume(self):
		self.paused = False



	def clearText(self):
		self.texts.clear()



	def update(self, *, skipEvents:bool = False, skipRepaint:bool = False, skipPause:bool = False):
		# Get current FPS
		current = time.time() # Get current time

		self.fpsFrames.append(current) # Append current time

		last = self.fpsFrames[-1] # Get last frame
		first = self.fpsFrames[0] # Get first frame
		dif = last - first # Get difference between frames
		
		if (dif):
			self.fps = len(self.fpsFrames) / dif # Get difference between first and final frame




		if (not skipEvents):
			# Process user events
			QtApp.processEvents()


		if (not skipRepaint):
			# Send repaint event
			self.widget.repaint()


		if (not skipPause):
			while self.paused:
				self.update(skipPause = True)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~









