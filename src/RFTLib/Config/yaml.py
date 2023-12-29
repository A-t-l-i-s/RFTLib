from ..Require import *

import yaml

from .loader import *

from ..Core.Structure import *





__all__ = ("RFT_Config_YAML",)





class RFT_Config_YAML(RFT_Config_Loader):
	exts = ("yaml", "yml")



	def import_(cls, path:str):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()
		

		# Read file
		with path.open("r") as file:
			try:
				data = yaml.load(
					file,
					Loader = yaml.FullLoader
				)

				if (data == None):
					data = {}
			except:
				data = {}


		# Return data
		if (isinstance(data, dict)):
			return RFT_Structure(data)

		else:
			return data



