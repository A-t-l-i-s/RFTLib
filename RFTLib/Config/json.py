import json
import traceback

from pathlib import Path

from .loader import *
from ..Core.Structure import *





__all__ = ("RFT_Config_JSON",)





class RFT_Config_JSON(RFT_Config_Loader):
	exts = ("json",)



	def load(cls,path):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()


		# Read file
		with path.open("r") as file:
			# Read file data as a dictionary
			dataJson = json.load(file)
			
			# Convert dictionary data to RFT_Structure
			data = RFT_Structure(dataJson)


		# Return data
		return data

		



