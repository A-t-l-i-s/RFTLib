from ...Require import *

from PyQt6.QtCore import Qt

from ...Core.Object import *





__all__ = ("KeyEvent",)





class KeyEvent(RFT_Object):
	def press(self, event):
		key = event.key()

		match key:
			case Qt.Key.Key_Space:
				self.paused = not self.paused

			case Qt.Key.Key_Escape:
				self.exit()





	def release(self, event):
		...



