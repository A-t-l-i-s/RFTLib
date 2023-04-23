from ..Require import *

import cv2
import numpy as np

from .geometry import *

from ..Core.Types import *
from ..Core.Object import *
from ..Core.Parser import *

from ..Core.Gui.Color import *





__all__ = ("RFT_Graph_Point",)





class RFT_Graph_Point(RFT_Graph_Geometry):
	def __init__(self,
			x:RFT_Typing.Number = 0,
			y:RFT_Typing.Number = 0,
		):
		
		self.x = x
		self.y = y



	def draw(self, canvas:np.ndarray, color:RFT_Color):
		x = round(self.x)
		y = round(self.y)

		if (x > -1 and x < canvas.shape[1] and y > -1 and y < canvas.shape[0]):
			canvas[y, x] = color.toRGBA()



