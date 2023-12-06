from ..Require import *

from .loader import *

from ..Core.Types import *
from ..Core.Structure import *





__all__ = ("RFT_Config_NIL",)





class RFT_Config_NIL(RFT_Config_Loader):
	exts = ("nil", "nil_s", "nil_i", "nil_f", "nil_a", "nil_b")



	def load(cls, path:RFT_Typing.Path):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()


		ext = path.suffix.lower()



		if (ext == ".nil"):
			return None

		elif (ext == ".nil_s"):
			return RFT_Structure({})

		elif (ext == ".nil_i"):
			return 0

		elif (ext == ".nil_f"):
			return 0.0

		elif (ext == ".nil_a"):
			return []

		elif (ext == ".nil_b"):
			return RFT_Buffer()

		else:
			return None


