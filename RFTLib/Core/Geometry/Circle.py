from RFTLib.Require import *
from RFTLib.Core.Graphics.Color import *
from RFTLib.Core.Base.BaseGeometry import *





__all__=["Circle"]





class Circle(BaseGeometry):
	def __init__(self,
			x:Number=0,
			y:Number=0,
			radius:Number=0,
		):

		self.x=x
		self.y=y
		
		self.radius=radius



	def draw(self,canvas:np.array,color:Color):
		cv2.circle(
			canvas,
			(round(self.x),round(self.y)),
			round(self.radius),
			color.get(),
			color.thickness
		)

