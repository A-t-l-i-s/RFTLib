from ..Require import *
from ..Utils.Color import *

from .BaseGeometry import *





__all__=["Ellipse"]





class Ellipse(BaseGeometry):
	def __new__(cls,
			x:Number=0,
			y:Number=0,
			xAxis:Number=0,
			yAxis:Number=0,
			angle:Number=0,
			startAngle:Number=0,
			endAngle:Number=0,
		):
		self=object.__new__(cls)

		self.x=x
		self.y=y

		self.xAxis=xAxis
		self.yAxis=yAxis

		self.angle=angles
		self.startAngle=startAngle
		self.endAngle=endAngle

		return self



	def draw(self,canvas:np.ndarray,color:Color):
		cv2.ellipse(
			canvas,
			(round(self.x),round(self.y)),
			(round(self.xAxis),round(self.yAxis)),
			round(self.angle),
			round(self.startAngle),
			round(self.endAngle),
			color.get(),
			color.thickness
		)


