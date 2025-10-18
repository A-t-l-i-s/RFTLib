from RFTLib.Require import *

from .Object import *
from .Structure import *
from .Exception import *



__all__ = ("RFT_Buffer",)



class RFT_Buffer(RFT_Object):
	def __init__(self, obj:bytes | bytearray | str | tuple | list | range | int | dict | map | set | RFT_Object = None):
		# Define main data structure
		self.setattr("__rft_data__", bytearray())

		if (isinstance(obj, RFT_Object)):
			obj.__rft_buffer__(self)

		else:
			self.add(obj)


	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	# ~~~~~~ Arithmetic ~~~~~~
	def __add__(self, obj:bytes | bytearray | str | tuple | list | range | int | dict | map | set | RFT_Object) -> RFT_Object:
		self.add(obj)
		return self

	def __sub__(self, length:int) -> RFT_Object:
		self.deflate(length)
		return self

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

	def __index__(self) -> int:
		raise RFT_Exception.NotImplemented()

	def __bool__(self) -> bool:
		return len(self) > 0

	def __str__(self) -> str:
		return RFT_Object.__str__(self)

	def __repr__(self) -> str:
		return RFT_Object.__str__(self)

	def __bytes__(self) -> bytes:
		return bytes(self.data)

	def __format__(self, fmt:str) -> str:
		return self.toStr()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~ RFT Methods ~~~~~~~~~
	def __rft_exception__(self, obj:RFT_Object):
		obj.text = self.toStr()

	def __rft_buffer__(self, obj:RFT_Object):
		obj += self.data

	def __rft_structure__(self, obj:RFT_Object):
		try:
			obj += json.loads(self.data)

		except:
			raise RFT_Exception("Failed to parse content.")

	def __rft_clear__(self):
		self.clear()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~ Raw Data ~~~~~~~
	@property
	def data(self) -> bytearray:
		return self.__dict__["__rft_data__"]


	# ~~~~~~~~~~ Add ~~~~~~~~~
	def add(self, obj:bytes | bytearray | str | tuple | list | range | int | dict | map | set | RFT_Object, *, start:int = -1) -> RFT_Object:
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


		# ~~~~~~ Structure ~~~~~~~
		elif (isinstance(obj, dict | map | set)):
			try:
				objStr = json.dumps(
					dict(obj),
					skipkeys = False,
					default = lambda o: None
				)

			except:
				raise RFT_Exception("Failed to dump dictionary.")

			else:
				buf += bytearray(objStr, "utf-8")


		# ~~~~~~ RFT Object ~~~~~~
		elif (isinstance(obj, RFT_Object)):
			tempBuf = RFT_Buffer(obj)
			buf += tempBuf.data


		else:
			raise RFT_Exception.TypeError(type(obj))


		curLen = len(self)
		bufLen = len(buf)
		
		if (start >= 0):
			maxLen = start + bufLen

			# Check if buffer need to extend
			if (maxLen > curLen):
				self.inflate(maxLen - curLen)

		else:
			start = curLen
			self.inflate(curLen + bufLen)


		# Place new characters in buffer
		for i, c in enumerate(buf):
			self[start + i] = c

		return self


	# ~~~~~~~~~~ Pop ~~~~~~~~~
	def pop(self, index:int) -> int:
		return self.data.pop(index)


	# ~~~~~~~~ Resize ~~~~~~~~
	def resize(self, length:int) -> RFT_Object:
		l = len(self)

		if (l == length):
			...

		elif (length > l):
			self.inflate(length - l)

		else:
			self.deflate(l - length)

		return self


	# ~~~~~~~~ Inflate ~~~~~~~
	def inflate(self, length:int) -> RFT_Object:
		self.__dict__["__rft_data__"] += bytearray(max(length, 0))
		return self


	# ~~~~~~~~ Deflate ~~~~~~~
	def deflate(self, length:int) -> RFT_Object:
		for i in range(max(length, 0)):
			self.pop(-1)
		return self


	# ~~~~~~~~~ Clear ~~~~~~~~
	def clear(self) -> RFT_Object:
		self.data.clear()
		return self


	# ~~~~~~~~~ Find ~~~~~~~~~
	def find(self, obj:bytes | bytearray | str | tuple | list | range | int | dict | map | set | RFT_Object) -> int:
		with RFT_Buffer(obj) as buf:
			return self.data.find(buf.data)


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


	# ~~~~~~~ File Read ~~~~~~
	def read(self, file:object, size:int = -1) -> RFT_Object:
		self += file.read(
			size
		)
		return self


	# ~~~~~~ File Write ~~~~~~
	def write(self, file:object) -> RFT_Object:
		file.write(
			self.data
		)
		return self


	# ~~~~~~~ Normalize ~~~~~~
	def normalize(self):
		return self.data





