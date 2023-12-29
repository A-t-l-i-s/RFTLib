from ..Require import *

from .loader import *

from ..Core.Structure import *





__all__ = ("RFT_Config_JSON",)





class RFT_Config_JSON(RFT_Config_Loader):
	exts = ("json",)



	def import_(cls, path:str):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()


		# Read file
		with path.open("r") as file:
			try:
				data = json.load(file)
			except:
				data = {}


		# Return data
		if (isinstance(data, dict)):
			return RFT_Structure(data)

		else:
			return data


		



