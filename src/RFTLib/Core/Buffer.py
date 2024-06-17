from RFTLib.Require import *

from .Object import *
from .Structure import *





__all__ = ("RFT_Buffer",)





class RFT_Buffer(RFT_Object):
	def __init__(self, data:int | str | bytes | bytearray | tuple | list | dict = None):
		self.data = self.toBytes(data)



	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	def __add__(self, val:int | str | bytes | bytearray | tuple | list | dict):
		self.data += self.toBytes(val)

		return self

	def __sub__(self, num:int):
		for i in range(num):
			self.pop(-1)

		return self

	def __mul__(self, num:int):
		self.data = self.data * num

		return self



	def __len__(self):
		return len(self.data)



	def __iter__(self):
		return self.iter()



	def __getitem__(self, i:int):
		return self.data[i]

	def __setitem__(self, i:int, v:int | str):
		self.data[i] = v
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~ Convert To Bytes ~~~~~~~
	@classmethod
	def toBytes(self, val:int | str | bytes | bytearray | tuple | list | dict):
		out = bytearray()



		# ~~~~~~~~ Buffer ~~~~~~~~
		if (isinstance(val, RFT_Buffer)):
			out = val.data



		# ~~~~~~~~ Integer ~~~~~~~
		elif (isinstance(val, int)):
			if (val == 0):
				out = bytearray([0])

			else:
				size = (val.bit_length() + 7) // 8
				
				out = bytearray(size)
				
				for i in range(size):
					out[size - i - 1] = (val >> (8 * i)) & 0xff



		# ~~~~~~~~~ Bytes ~~~~~~~~
		elif (isinstance(val, bytes | bytearray)):
			out = bytearray(val)



		# ~~~~~~~~ String ~~~~~~~~
		elif (isinstance(val, str)):
			out = bytearray(val, "utf-8")



		# ~~~~~~~~~ Array ~~~~~~~~
		elif (isinstance(val, (tuple, list, range, types.GeneratorType))):
			for v in val:
				out += self.toBytes(v)



		# ~~~~~~ Structure ~~~~~~~
		elif (isinstance(val, (dict, map, set, RFT_Structure))):
			if (isinstance(val, RFT_Structure)):
				val = val.toDict()

			elif (isinstance(val, (map, set))):
				val = dict(val)


			out_ = json.dumps(
				val,
				skipkeys = False,
				default = lambda o: None
			)
			out = bytes(out_, "utf-8")



		# ~~~~~~~~~ UUID ~~~~~~~~~
		elif (isinstance(val, uuid.UUID)):
			out = bytearray(
				val.bytes
			)



		# ~~~~~~~~~ None ~~~~~~~~~
		elif (val is None):
			...



		return out
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# ~~~~~~~~ Iterate ~~~~~~~
	def iter(self):
		return iter(self.data)


	# ~~~~ Reverse Iterate ~~~
	def riter(self):
		return reversed(self.data)	


	# ~~~~~~~~~~ Pop ~~~~~~~~~
	def pop(self, i:int):
		return self.data.pop(i)


	# ~~~~~~~~~ Clear ~~~~~~~~
	def clear(self):
		self.data = bytearray()


	# ~~~~~~~~~ Find ~~~~~~~~~
	def find(self, char: bytes):
		return self.data.find(char)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# ~~~~ To Hexidecimal ~~~~
	def toHex(self):
		return self.data.hex()


	# ~~~~~~ To Integer ~~~~~~
	def toInt(self):
		out = 0

		for i, c in enumerate(self.riter()):
			out += c << (i * 8)

		return out


	# ~~~~~~~ To String ~~~~~~
	def toStr(self):
		return self.data.decode("utf-8")


	# ~~~~~ To Structure ~~~~~
	def toStruct(self):
		out_ = json.loads(self.data)

		out = RFT_Structure(out_)

		return out


	# ~~~~~ To Dictionary ~~~~
	def toDict(self):
		return self.data
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# ~~~~~~~ Compress ~~~~~~~
	def compress(self):
		data = zlib.compress(
			self.data
		)

		return RFT_Buffer(data)


	# ~~~~~~ Decompress ~~~~~~
	def decompress(self):
		data = zlib.decompress(
			self.data
		)

		return RFT_Buffer(data)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





