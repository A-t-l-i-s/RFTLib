from ..Require import *

import cv2
import numpy as np

from .geometry import *

from ..Core.Types import *
from ..Core.Object import *
from ..Core.Parser import *

from ..Core.Gui.Color import *





__all__ = ("RFT_Graph_Circle",)





class RFT_Graph_Circle(RFT_Graph_Geometry):
	def __init__(self,
			x:RFT_Typing.Number = 0,
			y:RFT_Typing.Number = 0,

			radius:RFT_Typing.Number = 0
		):
		
		self.x = x
		self.y = y

		self.radius = radius



	def draw(self, canvas:np.ndarray, color:RFT_Color):
		cv2.circle(
			canvas,
			(
				round(self.x),
				round(self.y)
			),
			round(self.radius),
			color.toRGBA(),
			color.thickness
		)



