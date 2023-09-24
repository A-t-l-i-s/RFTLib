from ..Require import *

from .Types import *
from .Object import *
from .Exception import *





__all__ = ("RFT_Math",)





class RFT_Math(RFT_Object):
	@classmethod
	def pairing(cls, a:RFT_Typing.Number, b:RFT_Typing.Number):
		if (isinstance(a, RFT_Types.Number)):
			if (isinstance(b, RFT_Types.Number)):
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



