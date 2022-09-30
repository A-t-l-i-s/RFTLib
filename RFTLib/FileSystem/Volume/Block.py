from RFTLib.Require import *
from RFTLib.Core.Object import *
from RFTLib.Core.Converters.intToBytes import *
from RFTLib.Core.Converters.intFromBytes import *





__all__=["RFT_Block"]





class RFT_Block(RFT_Object):
	def __init__(self,data):
		self.data=np.fromstring(
			data,
			dtype=np.uint8
		)





	@property
	def attributes(self):
		return {}



	@attributes.setter
	def attributes(self,value):
		...





	@property
	def pointer(self):
		return intFromBytes(
			self.data[1:5]
		)



	@pointer.setter
	def pointer(self,value):
		self.data[1:5]=intToBytes(
			value,
			4
		)






