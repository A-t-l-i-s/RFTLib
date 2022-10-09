from RFTLib.Require import *





__all__=["mouseMoveEvent"]





def mouseMoveEvent(self,event):
	buttons=event.buttons()
	pos=event.position()
	gPos=event.globalPosition()

	
	if (buttons==Qt.MouseButton.LeftButton):
		self.widget.move(
			round(gPos.x()-self.mousePos[0]),
			round(gPos.y()-self.mousePos[1])
		)


