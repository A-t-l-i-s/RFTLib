from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Exception import *



__all__ = ("RFT_Production",)



class RFT_Production(RFT_Object):
	@classmethod
	def isProduction(self) -> bool:
		p = pathlib.Path("/production")

		return p.is_file()


