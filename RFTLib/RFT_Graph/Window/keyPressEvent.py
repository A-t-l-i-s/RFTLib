from ..Require import *





__all__=["keyPressEvent"]





def keyPressEvent(self,event):
	key=event.key()

	if (key==Qt.Key_Space):
		self.pause=not self.pause


	elif (key==Qt.Key_Escape):
		self.exit()


