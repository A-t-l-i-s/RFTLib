from ..Require import *

import Rypple

from .loader import *

from ..Core.Structure import *





__all__ = ("RFT_Config_RYPPLE",)





class RFT_Config_RYPPLE(RFT_Config_Loader):
	exts = ("ryp", "rypl", "ryc", "rycl")



	def import_(cls, path:str):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()

		# Read file as Rypple_Namespace
		data = Rypple.load(path)

		# Return data
		return data




