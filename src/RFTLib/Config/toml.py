from ..Require import *

import tomllib

from .loader import *

from ..Core.Types import *
from ..Core.Structure import *





__all__ = ("RFT_Config_TOML",)





class RFT_Config_TOML(RFT_Config_Loader):
	exts = ("toml",)



	def load(cls, path:RFT_Typing.Path):
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
		return RFT_Structure(data)



