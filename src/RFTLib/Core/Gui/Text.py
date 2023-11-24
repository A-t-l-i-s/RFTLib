from ...Require import *

from ..Types import *
from ..Object import *
from ..Parser import *

from .Color import *





__all__ = ("RFT_Text",)





class RFT_Text(RFT_Object):
	def __init__(self, text:str = "") -> RFT_Typing.Self:
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
	def setText(self, text:str) -> RFT_Typing.Self:
		self.text = text

		return self



	# Text position
	def setPos(self, x:int, y:int) -> RFT_Typing.Self:
		self.x = x
		self.y = y

		return self



	# Text color
	def setColor(self, color:RFT_Color) -> RFT_Typing.Self:
		self.color = color

		return self



	# Font family
	def setFont(self, font:str) -> RFT_Typing.Self:
		self.font = font

		return self



	# Font size
	def setFontSize(self, fontSize:int) -> RFT_Typing.Self:
		self.fontSize = fontSize

		return self



	def setIsBold(self, isBold:str) -> RFT_Typing.Self:
		self.isBold = isBold

		return self


	def setIsItalic(self, isItalic:str) -> RFT_Typing.Self:
		self.isItalic = isItalic

		return self


	def setIsStrikeOut(self, isStrikeOut:str) -> RFT_Typing.Self:
		self.isStrikeOut = isStrikeOut

		return self


	def setIsOverline(self, isOverline:str) -> RFT_Typing.Self:
		self.isOverline = isOverline

		return self


	def setIsUnderline(self, isUnderline:str) -> RFT_Typing.Self:
		self.isUnderline = isUnderline

		return self
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




