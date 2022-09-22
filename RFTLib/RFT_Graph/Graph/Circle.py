from ..Require import *
from ..Utils.Color import *

from .BaseGeometry import *




__all__=["Circle"]





class Circle(BaseGeometry):
	def __new__(cls,
			x:Number=0,
			y:Number=0,
			radius:Number=0,
		):
		self=object.__new__(cls)

		self.x=x
		self.y=y
		
		self.radius=radius

		return self



	def draw(self,canvas:np.array,color:Color):
		cv2.circle(
			canvas,
			(round(self.x),round(self.y)),
			round(self.radius),
			color.get(),
			color.thickness
		)

