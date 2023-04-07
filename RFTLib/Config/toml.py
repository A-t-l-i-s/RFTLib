import toml
import traceback

from pathlib import Path

from .loader import *
from ..Core.Structure import *





__all__ = ("RFT_Config_TOML",)





class RFT_Config_TOML(RFT_Config_Loader):
	exts = ("toml",)



	def load(cls,path):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()
		

		# Read file
		with path.open("r") as file:
			dataT = toml.load(file)
			
			data = RFT_Structure(dataT)


		# Return data
		return data



