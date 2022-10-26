from RFTLib.Require import *
from RFTLib.Core.Object import *





__all__=["RFT_Serialize"]





class RFT_Serialize(RFT_Object):
	


	chunkSize:int=512



	# Serialize Function
	def serialize(value,*,compress=True):
		try:
			data=pickle.dumps(value)
		except:
			data=RFT_Serialize.NONE


		if (compress):
			# Compress data
			data=zlib.compress(data)

		
		return data



	# Deserialize Function
	def deserialize(data,*,decompress=True):
		if (decompress):
			try:
				# Decompress data
				data=zlib.decompress(data)
			except:
				...


		try:
			value=pickle.loads(data)
		except:
			value=None

		return value





	NONE:bytes=serialize(None)

	PY_OBJECT:bytes=serialize(object)
	RFT_OBJECT:bytes=serialize(RFT_Object)
	
	TRUE:bytes=serialize(True)
	FALSE:bytes=serialize(False)






