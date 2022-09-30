from RFTLib.Require import *
from RFTLib.Core.Graphics.Color import *
from RFTLib.Core.Base.BaseGeometry import *





__all__=["Line"]





class Line(BaseGeometry):
	def __init__(self,
			x1:Number=0,
			y1:Number=0,
			x2:Number=0,
			y2:Number=0,
		):

		self.x1=x1
		self.y1=y1

		self.x2=x2
		self.y2=y2



	def draw(self,canvas:np.ndarray,color:Color):
		cv2.line(
			canvas,
			(round(self.x1),round(self.y1)),
			(round(self.x2),round(self.y2)),
			color.get(),
			color.thickness
		)


