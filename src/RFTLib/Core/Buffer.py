from ..Require import *

from .Types import *
from .Object import *





__all__ = ("RFT_Buffer",)





class RFT_Buffer(RFT_Object):
	def __init__(self,data:int | str | RFT_Typing.Buffer | tuple | list = None) -> None:
		self.data = self.toBytes(data)





	def __add__(self,val:int | str | RFT_Typing.Buffer | tuple | list) -> None:
		self.data += self.toBytes(val)

		return self

	def __sub__(self,num:int) -> None:
		for i in range(num):
			self.pop(-1)

		return self

	def __mul__(self,num:int) -> None:
		self.data = self.data * num

		return self



	def __len__(self) -> int:
		return len(self.data)



	def __iter__(self) -> iter:
		return self.iter()



	def __getitem__(self,i:int) -> int:
		return self.data[i]

	def __setitem__(self,i:int,v:int | str) -> None:
		self.data[i] = v





	def toBytes(self,val:int | str | RFT_Typing.Buffer | tuple | list) -> bytearray:
		out = bytearray()



		if (isinstance(val,RFT_Buffer)):
			out = val.data



		elif (isinstance(val,int)):
			size = (val.bit_length() + 7) // 8
			
			out = bytearray(size)
			
			for i in range(size):
				out[size - i - 1] = (val >> (8 * i)) & 0xff



		elif (isinstance(val,RFT_Types.Buffer)):
			out = bytearray(val)



		elif (isinstance(val,str)):
			out = bytearray(val.encode("utf-8"))



		elif (isinstance(val,(tuple,list))):
			for v in val:
				out += self.toBytes(v)



		elif (val is None):
			...



		return out



	def iter(self) -> iter:
		return iter(self.data)

	def riter(self) -> iter:
		return reversed(self.data)
	


	def pop(self,i:int) -> int:
		self.data.pop(i)



	def hex(self) -> str:
		return self.data.hex()

	def int(self) -> int:
		out = 0

		for i,c in enumerate(self.riter()):
			out += c << (i * 8)

		return out

	def str(self) -> str:
		return self.data.decode("utf-8")




