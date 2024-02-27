from RFTLib.Require import *

from . import *





__all__ = ("RFT_Point",)





class RFT_Point(RFT_Geometric):
	# ~~~~~~~~~~~ Variables ~~~~~~~~~~
	x = None
	y = None

	fields = ("x", "y")
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def __init__(self, pos:tuple = (0, 0)):
		if (isinstance(pos, (int, float))):
			self.x = pos
			self.y = pos

		elif (isinstance(pos, (tuple, list, RFT_Point))):
			self.x, self.y = pos



