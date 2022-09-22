from ..Require import *
from ..Utils.Color import *

from .BaseGeometry import *

from .Velocity import *





__all__=["Point"]





class Point(BaseGeometry):
	def __new__(cls,
			x:Number=0,
			y:Number=0,
		):
		self=object.__new__(cls)

		self.x=x
		self.y=y

		return self



	def draw(self,canvas:np.ndarray,color:Color):
		x=round(self.x)
		y=round(self.y)
		
		if (x>-1 and x<canvas.shape[1] and y>-1 and y<canvas.shape[0]):
			canvas[y,x]=color.get()



	def update(self,obj:Any):
		if (isinstance(obj,Velocity)):
			self.x+=obj.xVelocity
			self.y+=obj.yVelocity


