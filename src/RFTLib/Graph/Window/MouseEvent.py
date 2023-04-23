from ...Require import *

from PyQt6.QtCore import Qt

from ...Core.Object import *





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
				gPos = event.globalPosition()

				self.widget.move(
					round(gPos.x() - self.mousePos[0]),
					round(gPos.y() - self.mousePos[1])
				)



