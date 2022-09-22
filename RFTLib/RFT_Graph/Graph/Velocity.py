from ..Require import *
from ..Utils.Color import *

from .BaseGeometry import *





__all__=["Velocity"]





class Velocity(BaseGeometry):
	def __new__(cls,
			xVelocity:Number=0,
			yVelocity:Number=0,
		):
		self=object.__new__(cls)

		self.xVelocity=xVelocity
		self.yVelocity=yVelocity

		return self



