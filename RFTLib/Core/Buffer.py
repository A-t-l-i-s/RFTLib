from RFTLib.Require import *
from RFTLib.Core.Object import *





__all__=["RFT_Buffer"]





class RFT_Buffer(RFT_Object):
	def intToBytes(value,size,littleEndian=False):
		arr=[]

		for i in range(size):
			arr.append(value >> (((size - 1) - i) * 8) & 0xff)


		if (littleEndian):
			arr.reverse();


		return arr



	def intToHex(value,size,littleEndian=False):
		return binascii.hexlify(
			bytes(
				RFT_Buffer.intToBytes(
					value,
					size,
					littleEndian
				)
			)
		)





	def intFromBytes(data,littleEndian=False):
		value=0

		size=len(data)
		for i,b in enumerate(data):
			if (littleEndian):
				idx=i
			else:
				idx=(size - 1) - i


			value+=(int(b) << (idx*8))


		return value




	def intFromHex(data,littleEndian=False):
		return RFT_Buffer.intFromHex(
			binascii.unhexlify(
				data
			),
			littleEndian
		)