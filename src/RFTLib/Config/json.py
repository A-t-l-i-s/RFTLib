from ..Require import *

from .loader import *

from ..Core.Types import *
from ..Core.Structure import *





__all__ = ("RFT_Config_JSON",)





class RFT_Config_JSON(RFT_Config_Loader):
	exts = ("json",)



	def load(cls, path:RFT_Typing.Path):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()


		# Read file
		with path.open("r") as file:
			# Read file data as a dictionary
			dataJ = json.load(file)


		data = RFT_Structure(dataJ)


		# Return data
		return data

		



