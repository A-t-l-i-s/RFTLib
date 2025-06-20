from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Structure import *

from .C import *
from .CPP import *
from .Python import *

from .Process import *
from .Filesystem import *





__all__ = (
	"RFT_Rypple",
	"RFT_Rypple_Process",
	"RFT_Rypple_Filesystem",

	"RFT_Rypple_C",
	"RFT_Rypple_CPP",
	"RFT_Rypple_Python"
)





class RFT_Rypple(RFT_Object):
	default = RFT_Structure({
	})



	@classmethod
	def begin(self, *plugins: tuple | list) -> RFT_Structure:
		scope = self.default.copy()

		for pl in plugins:
			pl.scope = scope

			s = RFT_Structure(pl)
			for k, v in s.items():
				if (callable(v)):
					scope[k] = v

		return scope


	@classmethod
	def end(self, scope):
		scope.clear()




