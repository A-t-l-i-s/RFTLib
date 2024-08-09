from RFTLib.Require import *

from ..Object import *
from ..Geometric.Point import *

from .Color import *





__all__ = ("RFT_Text",)





class RFT_Text(RFT_Object):
	# ~~~~~~~~~~~ Variables ~~~~~~~~~~
	text:str = 				None

	pos = 					RFT_Point()

	color = 				RFT_Color.Black()

	font:str = 				None
	fontSize:int = 			12

	isBold:bool = 			False
	isItalic:bool = 		False
	isStrikeOut:bool = 		False
	isOverline:bool = 		False
	isUnderline:bool = 		False
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	def __init__(self, text:str = ""):
		if (isinstance(text, RFT_Text)):
			self.text = text.text
			
			self.pos = text.pos
			
			self.color = text.color

			self.font = text.font
			self.fontSize = text.fontSize

			self.isBold = text.isBold
			self.isItalic = text.isItalic
			self.isStrikeOut = text.isStrikeOut
			self.isOverline = text.isOverline
			self.isUnderline = text.isUnderline

		else:
			self.text = text


	# ~~~~~~~~~~~~ Methods ~~~~~~~~~~~
	# Set text
	def setText(self, text:str):
		self.text = text

		return self



	# Text position
	def setPos(self, pos):
		self.pos = RFT_Point(pos)

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



	def setIsBold(self, isBold:bool = True):
		self.isBold = isBold

		return self


	def setIsItalic(self, isItalic:bool = True):
		self.isItalic = isItalic

		return self


	def setIsStrikeOut(self, isStrikeOut:bool = True):
		self.isStrikeOut = isStrikeOut

		return self


	def setIsOverline(self, isOverline:bool = True):
		self.isOverline = isOverline

		return self


	def setIsUnderline(self, isUnderline:bool = True):
		self.isUnderline = isUnderline

		return self
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




