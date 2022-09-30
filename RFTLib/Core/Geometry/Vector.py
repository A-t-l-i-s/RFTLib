from RFTLib.Require import *
from RFTLib.Core.Graphics.Color import *
from RFTLib.Core.Base.BaseGeometry import *





__all__=["Vector"]





class Vector(BaseGeometry):
	def __init__(self,
			x:Number=0,
			y:Number=0,
			xVelocity:Number=0,
			yVelocity:Number=0,
		):

		self.x=x
		self.y=y

		self.xVelocity=xVelocity
		self.yVelocity=yVelocity



	def draw(self,canvas:np.ndarray,color:Color):

		to=[self.xVelocity,self.yVelocity]
		while (to[0]<canvas.shape[1] and to[1]<canvas.shape[0]):
			to[0]*=canvas.shape[1]
			to[1]*=canvas.shape[0]


		cv2.line(
			canvas,
			(round(self.x),round(self.y)),
			(round(to[0]),round(to[1])),
			color.get(),
			color.thickness
		)


