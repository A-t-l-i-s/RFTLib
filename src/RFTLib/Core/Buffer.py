from ..Require import *

from .Types import *
from .Object import *
from .Structure import *





__all__ = ("RFT_Buffer",)





class RFT_Buffer(RFT_Object):
	def __init__(self, data:int | str | RFT_Typing.Buffer | tuple | list = None) -> RFT_Typing.Self:
		self.data = self.toBytes(data)




	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	def __add__(self, val:int | str | RFT_Typing.Buffer | tuple | list) -> None:
		self.data += self.toBytes(val)

		return self

	def __sub__(self, num:int) -> None:
		for i in range(num):
			self.pop(-1)

		return self

	def __mul__(self, num:int) -> None:
		self.data = self.data * num

		return self



	def __len__(self) -> int:
		return len(self.data)



	def __iter__(self) -> iter:
		return self.iter()



	def __getitem__(self, i:int) -> int:
		return self.data[i]

	def __setitem__(self, i:int, v:int | str) -> None:
		self.data[i] = v
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Methods ~~~~~~~~~~~
	@classmethod
	def toBytes(self, val:int | str | RFT_Typing.Buffer | RFT_Typing.Array | RFT_Typing.Dictionary) -> bytearray:
		out = bytearray()



		if (isinstance(val, RFT_Buffer)):
			out = val.data



		elif (isinstance(val, int)):
			if (val == 0):
				out = bytearray([0])

			else:
				size = (val.bit_length() + 7) // 8
				
				out = bytearray(size)
				
				for i in range(size):
					out[size - i - 1] = (val >> (8 * i)) & 0xff




		elif (isinstance(val, RFT_Types.Buffer)):
			out = bytearray(val)



		elif (isinstance(val, str)):
			out = bytearray(val.encode("utf-8"))



		elif (isinstance(val, (tuple, list, range, RFT_Types.Generator))):
			for v in val:
				out += self.toBytes(v)



		elif (isinstance(val, (dict, map, set, RFT_Structure))):
			if (isinstance(val, RFT_Structure)):
				val = val.toDict()

			elif (isinstance(val, (map, set))):
				val = dict(val)


			out = json.dumps(val)



		elif (isinstance(val, uuid.UUID)):
			out = bytearray(
				val.bytes
			)



		elif (val is None):
			...



		return out





	# Manipulation methods
	def iter(self) -> iter:
		return iter(self.data)


	def riter(self) -> iter:
		return reversed(self.data)	


	def pop(self, i:int) -> int:
		return self.data.pop(i)


	def clear(self):
		self.data = bytearray()


	def find(self, char: bytes):
		return self.data.find(char)






	# Output methods
	def toHex(self) -> str:
		return self.data.hex()


	def toInt(self) -> int:
		out = 0

		for i,c in enumerate(self.riter()):
			out += c << (i * 8)

		return out


	def toStr(self) -> str:
		return self.data.decode("utf-8")


	def toStruct(self):
		out_ = json.loads(self.data)

		out = RFT_Structure(out_)

		return out





	# Compression methods
	def compress(self) -> RFT_Typing.Self:
		data = zlib.compress(self.data)

		return RFT_Buffer(data)


	def decompress(self) -> RFT_Typing.Self:
		data = zlib.decompress(self.data)

		return RFT_Buffer(data)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





