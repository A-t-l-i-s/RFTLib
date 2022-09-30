from RFTLib.Require import *
from RFTLib.Core.Graphics.Color import *
from RFTLib.Core.Base.BaseGeometry import *





__all__=["Velocity"]





class Velocity(BaseGeometry):
	def __init__(self,
			xVelocity:Number=0,
			yVelocity:Number=0,
		):

		self.xVelocity=xVelocity
		self.yVelocity=yVelocity



