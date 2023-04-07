from .Types import *
from .Object import *





__all__ = ("RFT_Parser",)





class RFT_Parser(RFT_Object):
	@classmethod
	def parseGroup(cls, val:RFT_Typing.Group):
		if (isinstance(val, RFT_Types.Union)):
			args = val.__args__

		elif (isinstance(val, RFT_Types.Iterable)):
			args = tuple(val)

		else:
			args = (val,)


		return args




