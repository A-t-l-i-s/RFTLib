from pathlib import Path

from ..Core.Object import *
from ..Core.Types import *





__all__ = ("RFT_Config_Loader",)





class RFT_Config_Loader(RFT_Object):
	exts = ()



	def load(cls, path:RFT_Typing.Path):
		raise NotImplementedError

		



