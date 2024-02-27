from RFTLib.Require import *

from . import *
from .Point import *





__all__ = ("RFT_Ellipse",)





class RFT_Ellipse(RFT_Geometric):
	# ~~~~~~~~~~~ Variables ~~~~~~~~~~
	center = None
	axis = None
	angle = None
	startAngle = None
	endAngle = None

	fields = ("center", "axis", "angle", "startAngle", "endAngle")
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def __init__(self, center = 0, axis = 0, angle = 0, startAngle = 0, endAngle = 0):
		self.center = RFT_Point(center)
		self.axis = RFT_Point(axis)
		self.angle = angle
		self.startAngle = startAngle
		self.endAngle = endAngle




