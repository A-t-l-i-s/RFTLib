from RFTLib.Require import *





__all__=["mousePressEvent"]





def mousePressEvent(self,event):
	buttons=event.buttons()
	
	if (buttons==Qt.LeftButton):
		self.mousePos=event.x(),event.y()


