from RFTLib.Require import *





__all__=["mouseMoveEvent"]





def mouseMoveEvent(self,event):
	buttons=event.buttons()
	
	if (buttons==Qt.LeftButton):
		self.widget.move(event.globalX()-self.mousePos[0],event.globalY()-self.mousePos[1])


