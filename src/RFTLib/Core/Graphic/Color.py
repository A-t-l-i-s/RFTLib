from RFTLib.Require import *

from ..Object import *





__all__ = ("RFT_Color",)





class RFT_Color(RFT_Object):
	def __init__(self, r:int | float, g:int | float, b:int | float, a:int | float):
		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.r:int = self.verifyInteger(r)
		self.g:int = self.verifyInteger(g)
		self.b:int = self.verifyInteger(b)
		self.a:int = self.verifyInteger(a)

		self.thickness:int = 1
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
	def RGBA(cls, r:int | float, g:int | float, b:int | float, a:int | float):
		return cls(r, g, b, a)

	@classmethod
	def RGB(cls, r:int | float, g:int | float, b:int | float):
		return cls.RGBA(r, g, b, 0xff)



	# HSV Methods
	@classmethod
	def HSVA(cls, h:int | float, s:int | float, v:int | float, a:int | float):
		h = cls.verifyDecimal(h, maxValue = 360)
		s = cls.verifyDecimal(s, maxValue = 100)
		v = cls.verifyDecimal(v, maxValue = 100)

		r, g, b = colorsys.hsv_to_rgb(h, s, v)

		return cls.RGBA(r, g, b, a)

	@classmethod
	def HSV(cls, h:int | float, s:int | float, v:int | float):
		return cls.HSVA(h, s, v, 0xff)



	# HLS Methods
	@classmethod
	def HLSA(cls, h:int | float, l:int | float, s:int | float, a:int | float):
		h = cls.verifyDecimal(h, maxValue = 360)
		l = cls.verifyDecimal(l, maxValue = 100)
		s = cls.verifyDecimal(s, maxValue = 100)

		r, g, b = colorsys.hls_to_rgb(h, l, s)

		return cls.RGBA(r, g, b, a)

	@classmethod
	def HLS(cls, h:int | float, l:int | float, s:int | float):
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

	@classmethod
	def Transparent(cls):
		return cls.RGBA(0x00, 0x00, 0x00, 0x00)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Verify Values ~~~~~~~~
	@classmethod
	def verifyInteger(cls, value:int | float, *, maxValue:int = 0xff):
		if (isinstance(value, float)):
			return max(min(round(value * maxValue), maxValue), 0)

		elif (isinstance(value, int)):
			return max(min(value, maxValue), 0)

		else:
			return 0


	@classmethod
	def verifyDecimal(cls, value:int | float, *, maxValue:float = 1.0):
		if (isinstance(value, float)):
			return max(min(value, 1.0), 0)

		elif (isinstance(value, int)):
			return max(min(value / maxValue, 1.0), 0)

		else:
			return 0.0
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






