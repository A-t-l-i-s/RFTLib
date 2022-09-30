from RFTLib.Require import *
from RFTLib.Core.Graphics.Color import *
from RFTLib.Core.Base.BaseGeometry import *
from RFTLib.Core.Geometry.Velocity import *





__all__=["Point"]





class Point(BaseGeometry):
	def __init__(self,
			x:Number=0,
			y:Number=0,
		):

		self.x=x
		self.y=y



	def draw(self,canvas:np.ndarray,color:Color):
		x=round(self.x)
		y=round(self.y)
		
		if (x>-1 and x<canvas.shape[1] and y>-1 and y<canvas.shape[0]):
			canvas[y,x]=color.get()



	def update(self,obj:Any):
		if (isinstance(obj,Velocity)):
			self.x+=obj.xVelocity
			self.y+=obj.yVelocity


