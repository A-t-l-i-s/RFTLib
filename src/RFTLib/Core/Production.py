from RFTLib.Require import *

from .Object import *
from .Exception import *





__all__ = ("RFT_Production",)





class RFT_Production(RFT_Object):
	@classmethod
	def isProduction(self):
		p = Path("/production")

		return p.is_file()


