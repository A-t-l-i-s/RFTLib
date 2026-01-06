from RFTLib.Require import *

from .Object import *
from .Enum import *
from .Structure import *
from .Exception import *



__all__ = ("RFT_Buffer",)



class RFT_Buffer(RFT_Object):
	def __init__(self, obj:bytes | bytearray | str | tuple | list | range | int | RFT_Object = None):
		# Define main data structure
		self.setattr("__rft_data__", bytearray())

		# Add data to buffer
		self.add(obj)


	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	# ~~~~~~ Arithmetic ~~~~~~
	def __add__(self, obj:bytes | bytearray | str | tuple | list | range | int | RFT_Object) -> RFT_Object:
		return self.add(obj)

	def __sub__(self, length:int) -> RFT_Object:
		return self.resize(len(self) - length)

	def __mul__(self, length:int) -> RFT_Object:
		length -= 1

		if (length >= 0):
			self.add(self.data * length, start = len(self))
		else:
			self.clear()
		
		return self

	def __eq__(self, obj:object) -> bool:
		if (isinstance(obj, RFT_Buffer)):
			return obj.data == self.data

		else:
			return RFT_Buffer(obj).data == self.data


	# ~~~~~~ Containers ~~~~~~
	def __len__(self) -> int:
		return len(self.data)

	def __getitem__(self, index:int) -> int:
		return self.data[index]

	def __setitem__(self, index:int, value:int | str):
		self.data[index] = value

	def __delitem__(self, index:int):
		self.pop(index)

	def __iter__(self) -> iter:
		return iter(self.data)

	def __reversed__(self) -> iter:
		return iter(reversed(self.data))

	def __contains__(self, buf:bytes | RFT_Object) -> bool:
		return self.find(buf) > -1


	# ~~~~ Type Conversion ~~~
	def __int__(self) -> int:
		return self.toInt()

	def __complex__(self) -> complex:
		return complex(self.toInt())

	def __bool__(self) -> bool:
		return len(self) > 0

	def __bytes__(self) -> bytes:
		return bytes(self.data)

	def __format__(self, fmt:str) -> str:
		return self.toStr()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~ Normalize ~~~~~~
	def normalize(self) -> bytearray:
		return self.data
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~ Raw Data ~~~~~~~
	@property
	def data(self) -> bytearray:
		return self.__dict__["__rft_data__"]


	# ~~~~~~~~~~ Add ~~~~~~~~~
	def add(self, obj:bytes | bytearray | str | tuple | list | range | int | RFT_Object) -> RFT_Object:
		buf = bytearray()

		# ~~~~~~~~~ None ~~~~~~~~~
		if (obj is None):
			...

		# ~~~~~~~~~ Bytes ~~~~~~~~
		elif (isinstance(obj, bytes | bytearray)):
			buf += obj


		# ~~~~~~~~ String ~~~~~~~~
		elif (isinstance(obj, str)):
			buf += bytearray(obj, "utf-8")


		# ~~~~~~~~~ Array ~~~~~~~~
		elif (isinstance(obj, tuple | list | range)):
			buf += bytearray(obj)


		# ~~~~~~~~ Integer ~~~~~~~
		elif (isinstance(obj, int)):
			if (obj == 0):
				buf += bytearray(1)

			else:
				size = (obj.bit_length() + 7) // 8
				
				buf += bytearray(size)
				
				for i in range(size):
					buf[size - i - 1] = (obj >> (8 * i)) & 0xff


		# ~~~~~~ RFT Buffer ~~~~~~
		elif (isinstance(obj, RFT_Buffer)):
			buf += obj.data


		else:
			raise RFT_Exception.TypeError(type(obj))

		# Add buffer to main buffer
		self.__dict__["__rft_data__"] += buf

		return self


	# ~~~~~~~~~~ Pop ~~~~~~~~~
	def pop(self, index:int) -> int:
		return self.__dict__["__rft_data__"].pop(index)


	# ~~~~~~~~ Resize ~~~~~~~~
	def resize(self, length:int) -> RFT_Object:
		l = len(self)

		if (l == length or length == 0):
			...

		if (length > l):
			self.__dict__["__rft_data__"] += bytearray(length - l)

		else:
			for i in range(min(l - length, l)):
				self.__dict__["__rft_data__"].pop(-1)

		return self


	# ~~~~~~~~~ Clear ~~~~~~~~
	def clear(self) -> RFT_Object:
		self.data.clear()
		return self


	# ~~~~~~~~~ Find ~~~~~~~~~
	def find(self, obj:bytes | bytearray | str | tuple | list | range | int | RFT_Object) -> int:
		with RFT_Buffer(obj) as buf:
			return self.__dict__["__rft_data__"].find(buf.data)


	# ~~~~ To Hexidecimal ~~~~
	def toHex(self) -> str:
		return self.data.hex()


	# ~~~~~~ To Integer ~~~~~~
	def toInt(self) -> int:
		out = 0

		for i, c in enumerate(reversed(self)):
			out += c << (i * 8)

		return out


	# ~~~~~~~ To String ~~~~~~
	def toStr(self) -> str:
		return str(self.data, "utf-8")


	# ~~~~~~~ Read File ~~~~~~
	def readFile(self, file:object, length:int = -1) -> RFT_Object:
		self += file.read(length)
		return self


	# ~~~~~~ Write File ~~~~~~
	def writeFile(self, file:object) -> RFT_Object:
		file.write(self.data)
		return self

