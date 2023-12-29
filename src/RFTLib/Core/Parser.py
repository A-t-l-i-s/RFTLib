from ..Require import *

from .Object import *





__all__ = ("RFT_Parser",)





class RFT_Parser(RFT_Object):
	"""
		Converts an iterable/union/tuple/list into a correct tuple
	"""
	@classmethod
	def parseGroup(cls, value:tuple):
		if (isinstance(value, types.UnionType)):
			args = value.__args__

		elif (isinstance(value, (tuple | list | range | types.GeneratorType))):
			args = tuple(value)

		else:
			args = (value,)


		return args




	"""
		Verifies that the path is valid in a filesystem
	"""
	@classmethod
	def verifyPath(cls, path:str, chars:str = "\\/:*?<>|"):
		out = ""

		for c in str(path):
			if (c not in chars):
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
	def verifyColorInteger(cls, value:int | float, *, maxValue:int = 0xff):
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
	def verifyColorDecimal(cls, value:int | float, *, maxValue:float = 1.0):
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




