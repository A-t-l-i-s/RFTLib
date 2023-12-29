from ..Require import *

import tomllib

from .loader import *

from ..Core.Structure import *





__all__ = ("RFT_Config_TOML",)





class RFT_Config_TOML(RFT_Config_Loader):
	exts = ("toml",)



	def import_(cls, path:str):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()
		

		# Read file
		with path.open("r") as file:
			try:
				data = tomllib.load(file)
			except:
				data = {}
	

		# Return data
		if (isinstance(data, dict)):
			return RFT_Structure(data)

		else:
			return data



