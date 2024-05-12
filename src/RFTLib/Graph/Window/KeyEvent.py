from RFTLib.Require import *

from RFTLib.Core.Object import *

from PyQt6.QtCore import Qt





__all__ = ("KeyEvent",)





class KeyEvent(RFT_Object):
	def press(self, event):
		key = event.key()

		match key:
			case Qt.Key.Key_Space:
				self.paused = not self.paused


			case Qt.Key.Key_Escape:
				self.exit()


			case Qt.Key.Key_Shift:
				self.shiftDown = True


			case Qt.Key.Key_Z:
				self.smoothing = not self.smoothing

			case Qt.Key.Key_X:
				self.displayText = not self.displayText

			case Qt.Key.Key_C:
				self.displayFPS = not self.displayFPS







	def release(self, event):
		key = event.key()

		match key:
			case Qt.Key.Key_Shift:
				self.shiftDown = False


