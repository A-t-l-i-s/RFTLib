from RFTLib.Require import *

from . import *
from .Point import *





__all__ = ("RFT_Rectangle",)





class RFT_Rectangle(RFT_Geometric):
	# ~~~~~~~~~~~ Variables ~~~~~~~~~~
	begin = None
	end = None

	fields = ("begin", "end")
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def __init__(self, begin = 0, end = 0):
		self.begin = RFT_Point(begin)
		self.end = RFT_Point(end)




