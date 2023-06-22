from ..Require import *

import cv2
import numpy as np

from .geometry import *

from ..Core.Types import *
from ..Core.Object import *
from ..Core.Parser import *

from ..Core.Gui.Color import *





__all__ = ("RFT_Graph_NAN",)





class RFT_Graph_NAN(RFT_Graph_Geometry):
	def __init__(self,
			*args,
			**kwargs
		):
		...



	def __getattr__(self, attr:str):
		return 0



