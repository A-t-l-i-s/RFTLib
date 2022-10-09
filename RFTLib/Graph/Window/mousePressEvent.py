from RFTLib.Require import *





__all__=["mousePressEvent"]





def mousePressEvent(self,event):
	buttons=event.buttons()
	pos=event.position()
	gPos=event.globalPosition()
	
	if (buttons==Qt.MouseButton.LeftButton):
		self.mousePos=pos.x(),pos.y()


