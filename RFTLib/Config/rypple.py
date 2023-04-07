import traceback

import Rypple
from Rypple.namespace import *

from pathlib import Path

from .loader import *
from ..Core.Structure import *





__all__ = ("RFT_Config_RYPPLE",)





class RFT_Config_RYPPLE(RFT_Config_Loader):
	exts = ("ryp", "rypl", "ryc", "rycl")



	def load(cls,path):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()

		# Read file as Rypple_Namespace
		dataRyp = Rypple.load(path)

		# Convert to dictionary
		dataRyp_ = dataRyp.toJSON()

		# COnvert dictionary to RFT_Structure
		data = RFT_Structure(dataRyp_)


		# Return data
		return data




