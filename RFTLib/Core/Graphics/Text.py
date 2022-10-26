from RFTLib.Require import *
from RFTLib.Core.Graphics.Color import *





__all__=["Text"]





class Text:


	Arial:str="Arial"
	Helvetica:str="Helvetica"


	def __init__(self,
			x:int=0,
			y:int=0,
			text:str="",
			color:Color=Color(),
			font:str="Consolas",
			size:int=12,
			*,
			isBold:bool=False,
			isItalic:bool=False,
			isStrikeOut:bool=False,
			isOverline:bool=False,
			isUnderline:bool=False,
			isKerning:bool=False,
			isFixedPitch:bool=True,
			letterSpacing:int=0,
			wordSpacing:int=0,
		):

		self.x=x
		self.y=y

		self.text=text

		self.color=color

		self.font=font
		self.size=size

		self.isBold=isBold
		self.isItalic=isItalic
		self.isStrikeOut=isStrikeOut
		self.isOverline=isOverline
		self.isUnderline=isUnderline
		self.isKerning=isKerning
		self.isFixedPitch=isFixedPitch

		self.letterSpacing=letterSpacing
		self.wordSpacing=wordSpacing



