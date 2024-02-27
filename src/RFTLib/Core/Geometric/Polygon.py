from RFTLib.Require import *

from . import *
from .Point import *





__all__ = ("RFT_Polygon",)





class RFT_Polygon(RFT_Geometric):
	# ~~~~~~~~~~~ Variables ~~~~~~~~~~
	fields = []
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def __init__(self, **points):
		for k, v in points.items():
			self.fields.append(k)
			self[k] = RFT_Point(v)




