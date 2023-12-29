from ..Require import *

import cv2
import numpy as np

from .geometry import *

from ..Core.Object import *
from ..Core.Parser import *

from ..Core.Gui.Color import *





__all__ = ("RFT_Graph_Circle",)





class RFT_Graph_Circle(RFT_Graph_Geometry):
	def __init__(self,
			x:int | float = 0,
			y:int | float = 0,

			radius:int | float = 0
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



