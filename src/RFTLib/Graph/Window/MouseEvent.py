from RFTLib.Require import *

from RFTLib.Core.Object import *

from PyQt6.QtCore import Qt





__all__ = ("MouseEvent",)





class MouseEvent(RFT_Object):
	def press(self, event):
		buttons = event.buttons()

		match buttons:
			case Qt.MouseButton.LeftButton:
				self.mousePos = event.pos().x(), event.pos().y()





	def release(self, event):
		buttons = event.buttons()

		match buttons:
			case Qt.MouseButton.NoButton:
				self.mousePos = event.pos().x(), event.pos().y()





	def move(self, event):
		buttons = event.buttons()

		match buttons:
			case Qt.MouseButton.LeftButton:
				if (not self.shiftDown):
					gPos = event.globalPosition()

					self.widget.move(
						round(gPos.x() - self.mousePos[0]),
						round(gPos.y() - self.mousePos[1])
					)




	def wheel(self, event):
		...



