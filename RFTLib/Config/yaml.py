import io
import yaml
import traceback

from pathlib import Path

from .loader import *
from ..Core.Structure import *





__all__ = ("RFT_Config_YAML",)





class RFT_Config_YAML(RFT_Config_Loader):
	exts = ("yaml","yml")



	def load(cls,path):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()
		

		# Read file
		with path.open("r") as file:
			dataY = yaml.load(
				file,
				Loader=yaml.FullLoader
			)
			
			data = RFT_Structure(dataY)


		# Return data
		return data



