from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Structure import *
from RFTLib.Core.Exception import *



__all__ = ("RFT_Enum",)



class RFT_Enum(RFT_Object):
	def __init__(self, obj:tuple | list | RFT_Object, *, start:int = 0):
		object.__setattr__(self, "__rft_data__", dict())

		if (isinstance(obj, tuple | list)):
			for k in obj:
				self.add(k)

		elif (isinstance(obj, RFT_Object)):
			obj.__rft_enum__(self)

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

	def __str__(self, *, showMagic:bool = False, indent:int = 0, found:list = [], ignore:list = []) -> str:
		o = RFT_Object()
		o.__dict__ = self.__dict__["__rft_data__"]

		return o.__str__(
			showMagic = showMagic,
			indent = indent,
			found = found,
			ignore = dir(RFT_Object) + ignore
		)

	def __repr__(self) -> str:
		return RFT_Object.__str__(self)

	def __format__(self, fmt:str) -> str:
		return RFT_Object.__str__(self)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~ RFT Methods ~~~~~~~~~
	def __rft_buffer__(self, obj:RFT_Object):
		obj += self.data

	def __rft_structure__(self, obj:RFT_Object):
		obj += self.data

	def __rft_enum__(self, obj:RFT_Object):
		for k in self.keys():
			obj += k

	def __rft_clear__(self):
		self.__dict__["__rft_data__"].clear()
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


	# ~~~~~~~ Normalize ~~~~~~
	def normalize(self):
		out = {}

		for k, v in self.items():
			out[k] = v

		return out

