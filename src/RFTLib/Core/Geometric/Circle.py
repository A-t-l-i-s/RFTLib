from RFTLib.Require import *

from . import *
from .Point import *





__all__ = ("RFT_Circle",)





class RFT_Circle(RFT_Geometric):
	# ~~~~~~~~~~~ Variables ~~~~~~~~~~
	center = None
	radius = None

	fields = ("center", "radius")
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def __init__(self, center = 0, radius = 0):
		self.center = RFT_Point(center)
		self.radius = radius



