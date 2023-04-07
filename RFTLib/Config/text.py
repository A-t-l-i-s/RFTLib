import json
import traceback

from pathlib import Path

from .loader import *
from ..Core.Types import *





__all__ = ("RFT_Config_TEXT",)





class RFT_Config_TEXT(RFT_Config_Loader):
	exts = ("txt", "log")



	def load(cls,path):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()
		

		# Read file
		with path.open("r") as file:
			data = file.read()


		# Return data
		return data

		



