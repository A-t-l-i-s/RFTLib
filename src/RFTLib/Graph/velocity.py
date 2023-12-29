from ..Require import *

import cv2
import numpy as np

from .geometry import *

from ..Core.Object import *
from ..Core.Parser import *

from ..Core.Gui.Color import *





__all__ = ("RFT_Graph_Velocity",)





class RFT_Graph_Velocity(RFT_Graph_Geometry):
	def __init__(self,
			xVelocity:int | float = 0,
			yVelocity:int | float = 0
		):

		self.xVelocity = xVelocity
		self.yVelocity = yVelocity



