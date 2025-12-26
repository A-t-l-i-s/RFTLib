from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Exception import *



__all__ = ("RFT_Math",)



class RFT_Math(RFT_Object):
	def pairing(a:int | float, b:int | float) -> int | float:
		if (isinstance(a, int | float)):
			if (isinstance(b, int | float)):
				if (a >= 0):
					a *= 2
				else:
					a *= -2
					a -= 1


				if (b >= 0):
					b *= 2
				else:
					b *= -2
					b -= 1


				c = (a + b) * (a + b + 1) / 2 + a

				return c

			else:
				raise RFT_Exception.TypeError(type(b))
		else:
			raise RFT_Exception.TypeError(type(a))


	def interpolate(num1:int | float, num2:int | float, factor:float) -> int | float:
		return num1 + factor * (num2 - num1)



