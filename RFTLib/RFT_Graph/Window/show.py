from ..Require import *





__all__=["show"]





def show(self,show=True):
	if (show):
		self.widget.show() # hide window
	else:
		self.widget.hide() # show window


