from RFTLib.Require import *
from RFTLib.Core.Object import *





__all__=["RFT_Serialize"]





class RFT_Serialize(RFT_Object):
	def serialize(value):
		try:
			data=pickle.dumps(value)
		except:
			data=RFT_Serialize.NONE

		return data



	def deserialize(data):
		try:
			value=pickle.loads(data)
		except:
			value=None

		return value



	NONE:bytes=serialize(None)

