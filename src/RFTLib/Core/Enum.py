from RFTLib.Require import *

from .Object import *
from .Exception import *





__all__ = ("RFT_Enum",)





class RFT_Enum(RFT_Object):
	def __init__(self, items:object, *, start = 0):
		data = {}

		if (isinstance(items, tuple | list)):
			for i, k in enumerate(items):
				data[k] = start + i

		elif (isinstance(items, RFT_Enum)):
			for i, k in enumerate(items.keys()):
				data[k] = start + i

		else:
			raise RFT_Exception.TypeError(type(items))


		# Set new object data
		object.__setattr__(self, "__data__", data)




	# ~~~~~~~~ Attr Assignment ~~~~~~~
	def __getattr__(self, attr:str):
		# Get dict data
		v = self.data()

		# Return value
		return v[attr]



	def __setattr__(self, attr:str, value):
		raise RFT_Exception("Enum is readonly", RFT_Exception.ERROR)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~ Item Assignment ~~~~~~~
	def __getitem__(self, attr:str):
		return self.__getattr__(attr)



	def __setitem__(self, path:tuple | list | str, value):
		raise RFT_Exception("Enum is readonly", RFT_Exception.ERROR)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	def __len__(self):
		return len(
			self.keys()
		)


	def __str__(self, showMagic:bool = False, indent:int = 0, found:list = [], ignore:list = []):
		o = RFT_Object()
		o.__dict__ = self.data()

		return o.__str__(
			showMagic = showMagic,
			indent = indent,
			found = found,
			ignore = dir(RFT_Object) + ignore
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Retrieve Data ~~~~~~~~
	# ~~~~~ Get Raw Data ~~~~~
	def data(self):
		return self.__dict__["__data__"]


	# ~~~~~ Copy Raw Data ~~~~
	def copy(self):
		return RFT_Enum(self)


	# ~~~~~~~~ Get Key ~~~~~~~
	def get(self, key, default = None):
		if (self.contains(key)):
			return self[key]

		else:
			return default


	# ~~~~~ Get All Keys ~~~~~
	def keys(self):
		d = self.data()

		return d.keys()


	# ~~~~~ Get All Items ~~~~
	def items(self):
		d = self.data()

		return d.items()


	# ~~~~ Get All Values ~~~~
	def values(self):
		d = self.data()

		return d.values()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Contains Data ~~~~~~~~
	# ~~~~~~~ Contains ~~~~~~~
	def contains(self, attr:str | tuple | list):
		d = self.data()
		k = d.keys()

		if (isinstance(attr, list | tuple)):
			return all(
				[a in k for a in attr]
			)

		else:
			return attr in k
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~ First/Last ~~~~~~
	def first(self):
		for k, v in self.items():
			return k


	def last(self):
		keys = tuple(self.keys())

		if (keys):
			return keys[-1]
	# ~~~~~~~~~~~~~~~~~~~~~~~~




