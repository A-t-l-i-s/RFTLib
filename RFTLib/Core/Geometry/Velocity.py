from RFTLib.Require import *
from RFTLib.Core.BaseGeometry import *
from RFTLib.Core.Graphics.Color import *





__all__=["Velocity"]





class Velocity(RFT_BaseGeometry):
	def __init__(self,
			xVelocity:Number=0,
			yVelocity:Number=0,
		):

		self.xVelocity=xVelocity
		self.yVelocity=yVelocity



