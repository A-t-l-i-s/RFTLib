from ...Require import *

from ..Object import *
from ..Parser import *

from .Color import *





__all__ = ("RFT_Text",)





class RFT_Text(RFT_Object):
	def __init__(self, text:str = ""):
		self.text = text

		self.x = -1
		self.y = -1

		self.color = RFT_Color.Black()

		self.font = None
		self.fontSize = 12

		self.isBold = False
		self.isItalic = False
		self.isStrikeOut = False
		self.isOverline = False
		self.isUnderline = False





	# ~~~~~~~~~~~~ Methods ~~~~~~~~~~~
	# Set text
	def setText(self, text:str):
		self.text = text

		return self



	# Text position
	def setPos(self, x:int, y:int):
		self.x = x
		self.y = y

		return self



	# Text color
	def setColor(self, color:RFT_Color):
		self.color = color

		return self



	# Font family
	def setFont(self, font:str):
		self.font = font

		return self



	# Font size
	def setFontSize(self, fontSize:int):
		self.fontSize = fontSize

		return self



	def setIsBold(self, isBold:str):
		self.isBold = isBold

		return self


	def setIsItalic(self, isItalic:str):
		self.isItalic = isItalic

		return self


	def setIsStrikeOut(self, isStrikeOut:str):
		self.isStrikeOut = isStrikeOut

		return self


	def setIsOverline(self, isOverline:str):
		self.isOverline = isOverline

		return self


	def setIsUnderline(self, isUnderline:str):
		self.isUnderline = isUnderline

		return self
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




