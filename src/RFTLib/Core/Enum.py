from RFTLib.Require import *

from .Object import *
from .Structure import *
from .Exception import *



__all__ = ("RFT_Enum",)



class RFT_Enum(RFT_Object):
	def __init__(self, obj:tuple | list, *, start:int = 0):
		self.setattr("__rft_data__", dict())

		if (isinstance(obj, tuple | list | RFT_Enum)):
			for k in obj:
				self.add(k)

		else:
			raise RFT_Exception.TypeError(type(obj))


	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	# ~~~~~~~ Operators ~~~~~~
	def __add__(self, key:str) -> RFT_Object:
		return self.add(key)

	def __eq__(self, obj:object) -> bool:
		if (isinstance(obj, RFT_Enum)):
			return obj.data == self.data

		else:
			return obj == self.data


	# ~~~~~~ Containers ~~~~~~
	def __len__(self) -> int:
		return len(
			self.keys()
		)

	def __getattr__(self, key:str) -> int:
		if (isinstance(key, str)):
			# Return value
			return self.__dict__["__rft_data__"][key]

		else:
			raise RFT_Exception.TypeError(type(key))

	def __setattr__(self, key:str, value:object):
		raise RFT_Exception(f"{type(self).__name__} is readonly.")

	def __getitem__(self, key:str) -> int:
		return self.__getattr__(key)

	def __setitem__(self, key:str, value:object):
		raise RFT_Exception(f"{type(self).__name__} is readonly.")

	def __iter__(self) -> iter:
		return iter(self.keys())

	def __reversed__(self) -> iter:
		return iter(reversed(self.keys()))

	def __contains__(self, key:str) -> bool:
		return self.contains(key)


	# ~~~~~~ Converters ~~~~~~
	def __bool__(self) -> bool:
		return len(self) > 0

	def __str__(self, **kwargs:dict) -> str:
		o = RFT_Object()
		o.__dict__ = self.__dict__["__rft_data__"]

		return o.__str__(
			**kwargs
		)

	def __format__(self, fmt:str) -> str:
		return RFT_Object.__str__(self)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~ Get Raw Data ~~~~~
	@property
	def data(self) -> dict:
		return self.__dict__["__rft_data__"]


	# ~~~~~~~~~~ Add ~~~~~~~~~
	def add(self, key:str) -> RFT_Object:
		self.__dict__["__rft_data__"][str(key)] = len(self)
		return self


	# ~~~~~~~~ Get Key ~~~~~~~
	def get(self, key:str, default:object = None) -> object:
		if (self.contains(key)):
			return self[key]

		else:
			return default


	# ~~~~~ Get All Keys ~~~~~
	def keys(self) -> tuple[str]:
		return tuple(self.__dict__["__rft_data__"].keys())


	# ~~~~~ Get All Items ~~~~
	def items(self) -> tuple[str, object]:
		return tuple(self.__dict__["__rft_data__"].items())


	# ~~~~ Get All Values ~~~~
	def values(self) -> tuple[object]:
		return tuple(self.__dict__["__rft_data__"].values())


	# ~~~~~~~ Contains ~~~~~~~
	def contains(self, key:str) -> bool:
		return key in self.keys()


	# ~~~~~ To Dictionary ~~~~
	def toDict(self) -> dict:
		out = {}

		for k, v in self.items():
			if (isinstance(v, RFT_Structure | RFT_Enum)):
				out[k] = v.toDict()

			else:
				out[k] = v

		return out

