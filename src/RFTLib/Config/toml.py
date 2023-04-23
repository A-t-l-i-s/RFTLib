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
			dataT = tomllib.load(file)
			
			data = RFT_Structure(dataT)


		# Return data
		return data



