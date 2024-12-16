from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Structure import *

from .scope import *
from .regex import *





__all__ = (
	"RFT_Rypple",
	"RFT_Rypple_Scope",
	"RFT_Rypple_Regex"
)





class RFT_Rypple(RFT_Object):
	@classmethod
	def read(self, file):
		quotes = []


		for l in file.readlines():
			s = RFT_Rypple_Regex.readStatement(l)

			if (s):
				print(s.toDict())




