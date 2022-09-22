from ..Require import *





__all__=["mouseReleaseEvent"]





def mouseReleaseEvent(self,event):
	buttons=event.buttons()
	
	if (buttons==Qt.NoButton):
		self.mousePos=event.x(),event.y()


