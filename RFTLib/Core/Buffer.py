from RFTLib.Require import *
from RFTLib.Core.Object import *





__all__=["RFT_Buffer"]





class RFT_Buffer(RFT_Object):
	def intToList(value,size,littleEndian=False):
		arr=[]

		for i in range(size):
			arr.append(value >> (((size - 1) - i) * 8) & 0xff)


		if (littleEndian):
			arr.reverse();


		return arr



	def intToBytes(value,size,littleEndian=False):
		return bytes(
			RFT_Buffer.intToList(
				value,
				size,
				littleEndian
			)
		)



	def intToHex(value,size,littleEndian=False):
		return binascii.hexlify(
			RFT_Buffer.intToBytes(
				value,
				size,
				littleEndian
			)
		)





	def intFromList(data,littleEndian=False):
		value=0

		size=len(data)
		for i,b in enumerate(data):
			if (littleEndian):
				idx=i
			else:
				idx=(size - 1) - i


			value+=(int(b) << (idx*8))


		return value



	def intFromBytes(data,littleEndian=False):
		return RFT_Buffer.intFromList(
			data,
			littleEndian
		)



	def intFromHex(data,littleEndian=False):
		return RFT_Buffer.intFromList(
			binascii.unhexlify(
				data
			),
			littleEndian
		)




	def listToStr(data,strict=False):
		out=[]
		v=string.printable.encode("utf-8")

		for c in data:
			if (c in v):
				out.append(c)

			elif (strict):
				return None


		out=bytes(out).decode("utf-8")
		return out




