from ..Require import *





__all__=["Color"]





class Color:


	r:int=0x00
	g:int=0x00
	b:int=0x00
	a:int=0x00


	def __new__(cls,*values,fmt:str="RGBA",thickness:int=1):
		self=object.__new__(cls)

		self.thickness=thickness

		values+=(255,255,255,255)

		match fmt:
			case "RGBA":
				self.r=values[0]
				self.g=values[1]
				self.b=values[2]
				self.a=values[3]



			case "RGB":
				self.r=values[0]
				self.g=values[1]
				self.b=values[2]
				self.a=0xFF



			case "ABGR":
				self.r=values[3]
				self.g=values[2]
				self.b=values[1]
				self.a=values[0]



			case "BGR":
				self.r=values[2]
				self.g=values[1]
				self.b=values[0]
				self.a=0xFF


		return self






	def get(self):
		return (self.r,self.g,self.b,self.a)




	def toQColor(self):
		return QColor(self.r,self.g,self.b,self.a)




	def random(alpha:int=255,thickness:int=1):
		return Color(random.randint(0x00,0xff),random.randint(0x00,0xff),random.randint(0x00,0xff),alpha,thickness=thickness)






