from RFTLib.Require import *





__all__=["mouseReleaseEvent"]





def mouseReleaseEvent(self,event):
	buttons=event.buttons()
	pos=event.position()
	gPos=event.globalPosition()
	
	if (buttons==Qt.MouseButton.NoButton):
		self.mousePos=pos.x(),pos.y()


