from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *

from .C import *





__all__ = ("RFT_Rypple_CPP",)





class RFT_Rypple_CPP(RFT_Object):
	exe_:str = "g++"



	@classmethod
	def exe(self, file:str):
		self.exe_ = file
		return self


	@classmethod
	def done(self):
		exe_ = RFT_Rypple_C.exe_
		RFT_Rypple_C.exe_ = self.exe_
		
		ret = RFT_Rypple_C.done()
		RFT_Rypple_C.exe_ = exe_

		return ret


