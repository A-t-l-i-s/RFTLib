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
		elif (isinstance(obj, dict)):
			for k, v in obj.items():
				self[str(k)] = v

		# ~~~~~~~~ Object ~~~~~~~~
		elif (isinstance(obj, RFT_Object)):
			obj.__rft_structure__(self)

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

	def __sub__(self, attr:str | list | tuple | int) -> RFT_Object:
		self.pop(attr)
		return self

	def __mul__(self, obj:dict | RFT_Object) -> RFT_Object:
		self.default(obj, force = True)
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

	def __getattr__(self, attr:str) -> object:
		if (self.__rft_get_event__(attr)):
			try:
				# Return value
				return self.__dict__["__rft_data__"][attr]

			except:
				raise RFT_Exception.AttributeError(type(self), attr)

	def __setattr__(self, attr:str, value:object):
		if (self.__rft_set_event__(attr)):
			# Convert value to structure
			if (isinstance(value, dict)):
				# Convert to structure
				self.__dict__["__rft_data__"][attr] = RFT_Structure(value)

			else:
				# Set value
				self.__dict__["__rft_data__"][attr] = value

	def __getitem__(self, attr:str | list | tuple | int) -> object:
		# Get parent
		parent, key = self.parent(attr)

		# Get value
		return parent.__getattr__(
			key
		)

	def __setitem__(self, attr:str | list | tuple | int, value:object):
		# Get parent
		parent, key = self.parent(attr)

		# Set value
		return parent.__setattr__(
			key,
			value
		)

	def __delitem__(self, attr:str | list | tuple | int) -> object:
		self.pop(attr)

	def __iter__(self) -> iter:
		return iter(self.keys())

	def __reversed__(self) -> iter:
		return iter(reversed(self.keys()))

	def __contains__(self, attr:str | tuple | list | int) -> bool:
		return self.contains(attr)


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
	def __rft_exception__(self, obj:RFT_Object):
		obj.text = str(self)

	def __rft_buffer__(self, obj:RFT_Object):
		obj += self.toDict()

	def __rft_structure__(self, obj:RFT_Object):
		for k, v in self.items():
			if (isinstance(v, RFT_Object)):
				obj[k] = RFT_Structure(v)

			else:
				obj[k] = v

	def __rft_enum__(self, obj:RFT_Object):
		for k in self.keys():
			obj += k

	def __rft_clear__(self):
		self.clear()

	def __rft_get_event__(self, attr:str) -> bool:
		return True

	def __rft_set_event__(self, attr:str) -> bool:
		return True
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~ Raw Data ~~~~~~~
	@property
	def data(self) -> dict:
		return self.__dict__["__rft_data__"]


	# ~~~~~~~~ Parent ~~~~~~~~
	def parent(self, attr:str | tuple | list | int, *, allocate:bool = False, child:bool = False) -> RFT_Object:
		"""
		Gets parent structure of given attr path.
		"""
		attr = self.formatAttr(attr)
		attrEnd = attr.pop(-1)

		# Default parent
		parent = self

		for k in attr:
			# If integer then get key by index
			if (isinstance(k, int)):
				k = parent.index(k)

			if (k in parent.keys()):
				# Get value in namespace
				v = parent[k]

				if (isinstance(v, RFT_Structure)):
					# Set new parent
					parent = v

				else:
					# Doesn't exist or invalid value
					raise RFT_Exception.TypeError(type(v))

			else:
				if (allocate):
					# If allocate then create new structure and assign it as new parent
					parent[k] = RFT_Structure()
					parent = parent[k]

				else:
					# Key doesn't exist
					raise RFT_Exception.AttributeError(k)


		# Get attribute end key
		if (isinstance(attrEnd, int)):
			attrEnd = parent.index(attrEnd)

		# Add structure for attrEnd
		if (child):
			parent += {attrEnd: RFT_Structure()}

		return parent, attrEnd


	# ~~~~~~~~ Get Key ~~~~~~~
	def get(self, attr:str | list | tuple | int, default:object = None) -> object:
		parent, key = self.parent(attr)

		if (parent.contains(key)):
			return parent[key]

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


	# ~~~~~~~~~ Index ~~~~~~~~
	def index(self, index:int) -> str:
		keys = self.keys()

		if (len(keys) - 1 >= index >= 0):
			return keys[index]

		else:
			raise RFT_Exception.IndexError(index)


	# ~~~~~~~ Contains ~~~~~~~
	def contains(self, attr:str | tuple | list | int) -> bool:
		try:
			parent, key = self.parent(attr)
		
		except:
			return False

		else:
			return key in parent.keys()


	# ~~~ Contains Instance ~~
	def containsInst(self, attr:str | list | tuple | int, type_:type) -> bool:
		return isinstance(self.get(attr), type_)


	# ~~~~~~~ All True ~~~~~~~
	def all(self) -> bool:
		return all([bool(v) for v in self.values()])


	# ~~~~~~~ Any True ~~~~~~~
	def any(self) -> bool:
		return any([bool(v) for v in self.values()])


	# ~~~~~~~~~~ Pop ~~~~~~~~~
	def pop(self, attr:str | tuple | list | int) -> object:
		parent, key = self.parent(attr)
		return parent.__dict__["__rft_data__"].pop(key)


	# ~~~~~~~~~ Clear ~~~~~~~~
	def clear(self) -> RFT_Object:
		self.__dict__["__rft_data__"].clear()
		return self


	# ~~~~~~~~ Default ~~~~~~~
	def default(self, struct:dict | RFT_Object, *, force:bool = False) -> RFT_Object:
		for k, v in struct.items():
			k = str(k)

			if (not self.contains(k) or force):
				self[k] = v

		return self


	# ~~~~~ Default Inst ~~~~~
	def defaultInst(self, attr:str, value:object, type_:type, *, force:bool = False) -> RFT_Object:
		parent, key = self.parent(attr)

		if (not parent.containsInst(key, type_) or force):
			parent[key] = value

		return self


	# ~~~ Format Attribute ~~~
	def formatAttr(self, attr:str | tuple | list | int) -> tuple[str | int]:
		"""
		Format any input and return a proper attr as a tuple
		"""
		outAttr = []

		if (not isinstance(attr, tuple | list)):
			if (attr is not None):
				if (isinstance(attr, int)):
					outAttr.append(attr)

				else:
					for s in str(attr).split("."):
						s = s.strip()

						if (s):
							outAttr.append(s)

		else:
			for v in attr:
				outAttr += self.formatAttr(v)


		if (len(outAttr) > 0):
			return outAttr

		else:
			raise RFT_Exception("Attribute is empty.")


	# ~~~~~~~ Normalize ~~~~~~
	def normalize(self):
		out = {}

		for k, v in self.items():
			if (isinstance(v, RFT_Object)):
				out[k] = v.normalize()

			else:
				out[k] = v

		return out




