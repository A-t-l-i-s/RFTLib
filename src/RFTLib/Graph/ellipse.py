from ..Require import *

import cv2
import numpy as np

from .geometry import *

from ..Core.Object import *
from ..Core.Parser import *

from ..Core.Gui.Color import *





__all__ = ("RFT_Graph_Ellipse",)





class RFT_Graph_Ellipse(RFT_Graph_Geometry):
	def __init__(self,
			x:int | float = 0,
			y:int | float = 0,

			xAxis:int | float = 0,
			yAxis:int | float = 0,

			angle:int | float = 0,
			startAngle:int | float = 0,
			endAngle:int | float = 0
		):
		
		self.x = x
		self.y = y

		self.xAxis = xAxis
		self.yAxis = yAxis

		self.angle = angle
		self.startAngle = startAngle
		self.endAngle = endAngle



	def draw(self, canvas:np.ndarray, color:RFT_Color):
		cv2.ellipse(
			canvas,
			(
				round(self.x),
				round(self.y)
			),
			(
				round(self.xAxis),
				round(self.yAxis)
			),
			round(self.angle),
			round(self.startAngle),
			round(self.endAngle),
			color.toRGBA(),
			color.thickness
		)



