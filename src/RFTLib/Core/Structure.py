from RFTLib.Require import *

from .Object import *
from .Exception import *



__all__ = ("RFT_Structure",)



class RFT_Structure(RFT_Object):
	def __init__(self, obj:dict | RFT_Object = None, *, getEvent:object = None, setEvent:object = None):
		# Define main data structure
		self.setattr("__rft_data__", dict())


		# ~~~~~~~~~ None ~~~~~~~~~
		if (obj is None):
			...

		# ~~~~~~ Dictionary ~~~~~~
		elif (isinstance(obj, dict | RFT_Structure)):
			self.default(
				obj,
				forced = True
			)

		else:
			raise RFT_Exception.TypeError(type(obj))


		# ~~~~~~~ Get Event ~~~~~~
		if (getEvent is not None):
			self.setattr("__rft_get_event__", getEvent)
		# ~~~~~~~~~~~~~~~~~~~~~~~~
		
		# ~~~~~~~ Set Event ~~~~~~
		if (setEvent is not None):
			self.setattr("__rft_set_event__", setEvent)
		# ~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	# ~~~~~~~ Operators ~~~~~~
	def __add__(self, obj:dict | RFT_Object) -> RFT_Object:
		self.default(obj)
		return self

	def __sub__(self, attr:str) -> RFT_Object:
		self.pop(attr)
		return self

	def __mul__(self, obj:dict | RFT_Object) -> RFT_Object:
		self.default(obj, forced = True)
		return self

	def __eq__(self, obj:object) -> bool:
		if (isinstance(obj, RFT_Structure)):
			return obj.data == self.data

		else:
			return obj == self.data


	# ~~~~~~ Containers ~~~~~~
	def __len__(self) -> int:
		return len(
			self.keys()
		)

	def __getattr__(self, key:str) -> object:
		if (self.__rft_get_event__(key)):
			try:
				# Return value
				return self.__dict__["__rft_data__"][key]

			except:
				raise RFT_Exception.AttributeError(type(self), key)

	def __setattr__(self, key:str, value:object):
		if (self.__rft_set_event__(key)):
			# Convert value to structure
			if (isinstance(value, dict)):
				# Convert to structure
				self.__dict__["__rft_data__"][key] = RFT_Structure(value)

			else:
				# Set value
				self.__dict__["__rft_data__"][key] = value

	def __getitem__(self, key:str) -> object:
		# Get value
		return self.__getattr__(
			key
		)

	def __setitem__(self, key:str, value:object):
		# Set value
		return self.__setattr__(
			key,
			value
		)

	def __delitem__(self, key:str) -> object:
		self.pop(key)

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

	def __repr__(self) -> str:
		return self.__str__()

	def __format__(self, fmt:str) -> str:
		return self.__str__()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~ RFT Methods ~~~~~~~~~
	def __rft_get_event__(self, key:str) -> bool:
		return True

	def __rft_set_event__(self, key:str) -> bool:
		return True
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~ Raw Data ~~~~~~~
	@property
	def data(self) -> dict:
		return self.__dict__["__rft_data__"]


	# ~~~~~~~ Allocate ~~~~~~~
	def allocate(self, attr:str | tuple | list) -> RFT_Object:
		parent = self

		if (isinstance(attr, str)):
			attr = attr.split(".")

		for key in attr:
			if (key):
				if (parent.containsInst(RFT_Structure, key)):
					parent = parent[key]

				else:
					s = RFT_Structure()
					parent[key] = s
					parent = s

		return parent


	# ~~~~~~~~ Get Key ~~~~~~~
	def get(self, key:str, default:object = None, type_:type = None) -> object:
		v = self.__dict__["__rft_data__"].get(key, default)

		if (type_ is not None):
			if (not isinstance(v, value)):
				return default

		return v


	# ~~~~~ Get All Keys ~~~~~
	def keys(self) -> tuple[str]:
		return tuple(self.__dict__["__rft_data__"].keys())


	# ~~~~~ Get All Items ~~~~
	def items(self) -> tuple[str, object]:
		return tuple(self.__dict__["__rft_data__"].items())


	# ~~~~ Get All Values ~~~~
	def values(self) -> tuple[object]:
		return tuple(self.__dict__["__rft_data__"].values())


	# ~~~~~~~~~ Index ~~~~~~~~
	def index(self, index:int) -> str:
		keys = self.keys()

		if (len(keys) - 1 >= index >= 0):
			return keys[index]

		else:
			raise RFT_Exception.IndexError(index)


	# ~~~~~~~ Contains ~~~~~~~
	def contains(self, *keys:str) -> bool:
		l = []
		for key in keys:
			l.append(
				key in self.keys()
			)

		return all(l)


	# ~~~ Contains Instance ~~
	def containsInst(self, type_:type, *keys:str) -> bool:
		if (keys):
			# Check if those keys exists and match types
			l = []
			for key in keys:
				l.append(
					isinstance(self.get(key), type_)
				)

			return all(l)


		else:
			# Check if that type exists in structure
			for v in self.values():
				if (isinstance(v, type_)):
					return True

			return False


	# ~~~~~~~ All True ~~~~~~~
	def all(self) -> bool:
		return all([bool(v) for v in self.values()])


	# ~~~~~~~ Any True ~~~~~~~
	def any(self) -> bool:
		return any([bool(v) for v in self.values()])


	# ~~~~~~~~~~ Pop ~~~~~~~~~
	def pop(self, key:str) -> object:
		return self.__dict__["__rft_data__"].pop(key)


	# ~~~~~~~~~ Clear ~~~~~~~~
	def clear(self) -> RFT_Object:
		self.__dict__["__rft_data__"].clear()
		return self


	# ~~~~~~~~ Default ~~~~~~~
	def default(self, obj:dict | RFT_Object, *, forced:bool = False) -> RFT_Object:
		for k, v in obj.items():
			if (not self.contains(k) or forced):
				self[k] = v

		return self


	# ~~~~~ Default Inst ~~~~~
	def defaultInst(self, type_:type, obj:dict | RFT_Object, *, forced:bool = False) -> RFT_Object:
		for k, v in obj.items():
			k = str(k)

			if (not self.containsInst(type_, k) or forced):
				self[k] = v

		return self


	# ~~~~~ To Dictionary ~~~~
	def toDict(self) -> dict:
		out = {}

		for k, v in self.items():
			if (isinstance(v, RFT_Structure | RFT_Enum)):
				out[k] = v.toDict()

			else:
				out[k] = v

		return out


