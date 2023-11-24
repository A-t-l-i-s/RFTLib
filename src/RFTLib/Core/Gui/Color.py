from ...Require import *

from ..Types import *
from ..Object import *
from ..Parser import *





__all__ = ("RFT_Color",)





class RFT_Color(RFT_Object):
	def __init__(self,
			r:RFT_Typing.Number,
			g:RFT_Typing.Number,
			b:RFT_Typing.Number,
			a:RFT_Typing.Number
		):
		
		# Convert all decimals to integers
		self.r:int = RFT_Parser.verifyColorInteger(r)
		self.g:int = RFT_Parser.verifyColorInteger(g)
		self.b:int = RFT_Parser.verifyColorInteger(b)
		self.a:int = RFT_Parser.verifyColorInteger(a)

		self.thickness:int = 1




	# ~~~~~~~~~~~~ Methods ~~~~~~~~~~~
	# Return as RGB Methods
	def toRGBA(self):
		return self.r, self.g, self.b, self.a

	def toRGB(self):
		return self.r, self.g, self.b





	def setThickness(self, value:int):
		self.thickness = value

		return self
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Class Methods ~~~~~~~~
	# RGB Methods
	@classmethod
	def RGBA(cls, r:RFT_Typing.Number, g:RFT_Typing.Number, b:RFT_Typing.Number, a:RFT_Typing.Number):
		return cls(r, g, b, a)

	@classmethod
	def RGB(cls, r:RFT_Typing.Number, g:RFT_Typing.Number, b:RFT_Typing.Number):
		return cls.RGBA(r, g, b, 0xff)



	# HSV Methods
	@classmethod
	def HSVA(cls, h:RFT_Typing.Number, s:RFT_Typing.Number, v:RFT_Typing.Number, a:RFT_Typing.Number):
		h = RFT_Parser.verifyColorDecimal(h, maxValue = 360)
		s = RFT_Parser.verifyColorDecimal(s, maxValue = 100)
		v = RFT_Parser.verifyColorDecimal(v, maxValue = 100)

		r, g, b = colorsys.hsv_to_rgb(h, s, v)

		return cls.RGBA(r, g, b, a)

	@classmethod
	def HSV(cls, h:RFT_Typing.Number, s:RFT_Typing.Number, v:RFT_Typing.Number):
		return cls.HSVA(h, s, v, 0xff)



	# HLS Methods
	@classmethod
	def HLSA(cls, h:RFT_Typing.Number, l:RFT_Typing.Number, s:RFT_Typing.Number, a:RFT_Typing.Number):
		h = RFT_Parser.verifyColorDecimal(h, maxValue = 360)
		l = RFT_Parser.verifyColorDecimal(l, maxValue = 100)
		s = RFT_Parser.verifyColorDecimal(s, maxValue = 100)

		r, g, b = colorsys.hls_to_rgb(h, l, s)

		return cls.RGBA(r, g, b, a)

	@classmethod
	def HLS(cls, h:RFT_Typing.Number, l:RFT_Typing.Number, s:RFT_Typing.Number):
		return cls.HLSA(h, s, v, 0xff)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~ Constant Colors ~~~~~~~
	@classmethod
	def Random(cls):
		return cls.RGB(
			random.randint(0, 0xff),
			random.randint(0, 0xff),
			random.randint(0, 0xff)
		)

	@classmethod
	def White(cls):
		return cls.RGB(0xff, 0xff, 0xff)

	@classmethod
	def Black(cls):
		return cls.RGB(0x00, 0x00, 0x00)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
















