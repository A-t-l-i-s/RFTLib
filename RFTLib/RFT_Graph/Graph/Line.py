from ..Require import *
from ..Utils.Color import *

from .BaseGeometry import *





__all__=["Line"]





class Line(BaseGeometry):
	def __new__(cls,
			x1:Number=0,
			y1:Number=0,
			x2:Number=0,
			y2:Number=0,
		):
		self=object.__new__(cls)

		self.x1=x1
		self.y1=y1

		self.x2=x2
		self.y2=y2

		return self



	def draw(self,canvas:np.ndarray,color:Color):
		cv2.line(
			canvas,
			(round(self.x1),round(self.y1)),
			(round(self.x2),round(self.y2)),
			color.get(),
			color.thickness
		)


