from ..Require import *

import cv2
import numpy as np

from .geometry import *

from ..Core.Types import *
from ..Core.Object import *
from ..Core.Parser import *

from ..Core.Gui.Color import *





__all__ = ("RFT_Graph_Rectangle",)





class RFT_Graph_Rectangle(RFT_Graph_Geometry):
	def __init__(self,
			x1:RFT_Typing.Number = 0,
			y1:RFT_Typing.Number = 0,
			
			x2:RFT_Typing.Number = 0,
			y2:RFT_Typing.Number = 0
		):
		
		self.x1 = x1
		self.y1 = y1

		self.x2 = x2
		self.y2 = y2



	def draw(self, canvas:np.ndarray, color:RFT_Color):
		cv2.rectangle(
			canvas,
			(
				round(self.x1),
				round(self.y1)
			),
			(
				round(self.x2),
				round(self.y2)
			),
			color.toRGBA(),
			color.thickness
		)



