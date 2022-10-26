from RFTLib.Require import *





__all__=["Color"]





class Color:


	r:int=0x00
	g:int=0x00
	b:int=0x00
	a:int=0x00


	def __init__(self,*values:Tuple[Number],fmt:str="RGBA",thickness:int=1):

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



			case "HLS":
				v=colorsys.hls_to_rgb(*values[:3])
				self.r=v[0]
				self.g=v[1]
				self.b=v[2]
				self.a=0xff



			case "HSV":
				v=colorsys.hsv_to_rgb(*values[:3])
				self.r=round(v[0] * 0xff)
				self.g=round(v[1] * 0xff)
				self.b=round(v[2] * 0xff)
				self.a=0xff



			case "YIQ":
				v=colorsys.yiq_to_rgb(*values[:3])
				self.r=round(v[0] * 0xff)
				self.g=round(v[1] * 0xff)
				self.b=round(v[2] * 0xff)
				self.a=0xff
				






	def get(self):
		return (self.r,self.g,self.b,self.a)




	def toQColor(self):
		return QColor(self.r,self.g,self.b,self.a)




	def random(alpha:int=255,thickness:int=1):
		return Color(random.randint(0x00,0xff),random.randint(0x00,0xff),random.randint(0x00,0xff),alpha,thickness=thickness)







