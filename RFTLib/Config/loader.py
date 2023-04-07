from pathlib import Path

from ..Core.Object import *





__all__ = ("RFT_Config_Loader",)





class RFT_Config_Loader(RFT_Object):
	exts = ()



	def load(cls,path):
		raise NotImplementedError

		



