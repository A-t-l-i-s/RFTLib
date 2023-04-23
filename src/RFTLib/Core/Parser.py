from ..Require import *

from .Types import *
from .Object import *





__all__ = ("RFT_Parser",)





class RFT_Parser(RFT_Object):
	"""
		Converts an iterable/union/tuple/list into a correct tuple
	"""
	@classmethod
	def parseGroup(cls, val:RFT_Typing.Group):
		if (isinstance(val, RFT_Types.Union)):
			args = val.__args__

		elif (isinstance(val, RFT_Types.Iterable)):
			args = tuple(val)

		else:
			args = (val,)


		return args




	"""
		Verifies that the path is valid in a filesystem
	"""
	@classmethod
	def verifyPath(cls, path:RFT_Typing.Path):
		out = ""

		for c in str(path):
			if (c not in "\\/:*?<>|"):
				out += c
			else:
				out += "_"

		return out





	"""
		Takes an float/int and outputs a int value.
		If it takes in a float the output will be the percent of the maxValue variable as a whole integer value.
		If it takes in an int the function willl just send it through while keeping it below the maxValue
	"""
	@classmethod
	def verifyColorInteger(cls, value:RFT_Typing.Number, *, maxValue:int = 0xff):
		if (isinstance(value, float)):
			return max(
				min(
					round(value * maxValue),
					maxValue
				),
				0
			)

		elif (isinstance(value, (int, complex))):
			return max(
				min(
					value,
					maxValue
				),
				0
			)

		else:
			raise TypeError



	"""
		Sames function as above but reversed. It outputs a float.
	"""
	@classmethod
	def verifyColorDecimal(cls, value:RFT_Typing.Number, *, maxValue:int = 0xff):
		if (isinstance(value, float)):
			return max(
				min(
					value,
					1.0
				),
				0
			)

		elif (isinstance(value, (int, complex))):
			return max(
				min(
					value / maxValue,
					1.0
				),
				0
			)

		else:
			raise TypeError




