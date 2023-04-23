from ..Require import *

import cv2
import numpy as np

from .geometry import *

from ..Core.Types import *
from ..Core.Object import *
from ..Core.Parser import *

from ..Core.Gui.Color import *





__all__ = ("RFT_Graph_Ellipse",)





class RFT_Graph_Ellipse(RFT_Graph_Geometry):
	def __init__(self,
			x:RFT_Typing.Number = 0,
			y:RFT_Typing.Number = 0,

			xAxis:RFT_Typing.Number = 0,
			yAxis:RFT_Typing.Number = 0,

			angle:RFT_Typing.Number = 0,
			startAngle:RFT_Typing.Number = 0,
			endAngle:RFT_Typing.Number = 0
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



