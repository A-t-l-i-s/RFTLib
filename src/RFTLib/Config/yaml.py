from ..Require import *

import yaml

from .loader import *

from ..Core.Types import *
from ..Core.Structure import *





__all__ = ("RFT_Config_YAML",)





class RFT_Config_YAML(RFT_Config_Loader):
	exts = ("yaml","yml")



	def load(cls, path:RFT_Typing.Path):
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



