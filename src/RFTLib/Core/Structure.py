from RFTLib.Require import *

from .Object import *
from .Exception import *





__all__ = ("RFT_Structure",)





class RFT_Structure(RFT_Object):
	def __init__(self, struct:object = None, *, defaults:dict = {}, readonly:bool = False, showMagic:bool = False):
		# If no struct then create one
		if (struct == None):
			struct = dict()


		# Set new variables
		newStruct = struct
		newDefaults = defaults

		object.__setattr__(self, "__readonly__", readonly)


		# ~~~~ Convert To Dict ~~~
		if (isinstance(struct, RFT_Structure)):
			newStruct = struct.data()


		if (isinstance(defaults, RFT_Structure)):
			newDefaults = defaults.data()
		# ~~~~~~~~~~~~~~~~~~~~~~~~



		if (isinstance(newStruct, dict)):
			# ~~~~~~ Dictionary ~~~~~~
			# Copy dictionary
			data = copy.deepcopy(newDefaults)
			data.update(newStruct)


			# Iterate keys
			for k in data.keys():
				v = data[k]

				if (isinstance(v, dict)):
					# Convert to structure
					data[k] = RFT_Structure(v)


			# Set new object data
			object.__setattr__(self, "__data__", data)
			# ~~~~~~~~~~~~~~~~~~~~~~~~


		elif (isinstance(newStruct, RFT_Object) or (isinstance(newStruct, type) and issubclass(newStruct, RFT_Object))):
			# ~~~~~~~~ Object ~~~~~~~~
			# New dictionary
			data = dict()

			if (isinstance(newStruct, type)):
				obj = newStruct.copy(newStruct)

			else:
				obj = newStruct.copy()

			# Iterate through attributes
			for k in obj.__dict__.keys():
				if (showMagic or not (k.startswith("__") and k.endswith("__"))):
					data[k] = getattr(obj, k)


			# Set new object data
			object.__setattr__(self, "__data__", data)
			# ~~~~~~~~~~~~~~~~~~~~~~~~


		else:
			# ~~~~ Unknown Object ~~~~
			# New dictionary
			data = dict()

			for k in newStruct.__dict__.keys():
				if (showMagic or not (k.startswith("__") and k.endswith("__"))):
					v = getattr(newStruct, k)

					if (not isinstance(v, int | float | complex | str | list | tuple | range | set | bool | bytes | bytearray | memoryview)):
						data[k] = RFT_Structure(v)

					else:
						data[k] = v

			# Set new object data
			object.__setattr__(self, "__data__", data)
			# ~~~~~~~~~~~~~~~~~~~~~~~~




	# ~~~~~~~~ Attr Assignment ~~~~~~~
	def __getattr__(self, attr:str):
		if (self.getEvent(attr)):
			# Get dict data
			v = self.data()

			# Return value
			return v[attr]



	def __setattr__(self, attr:str, value):
		if (not self.readonly()):
			if (self.setEvent(attr)):
				# Get dict data
				v = self.data()

				# Convert value to structure
				if (isinstance(value, dict)):
					value_ = RFT_Structure(value)
				else:
					value_ = value

				# Set value
				v[attr] = value_

		else:
			raise RFT_Exception("Structure is readonly", RFT_Exception.ERROR)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~ Item Assignment ~~~~~~~
	def __getitem__(self, path:tuple | list | str):
		if (not isinstance(path, (list, tuple))):
			path = [path]


		if (len(path) > 1):
			# Get final attribute
			attr = path[-1]

			# Get parent
			parent = self.parent(path)

			# If parent found
			if (parent != None):
				return RFT_Structure.__getattr__(parent, attr)


		else:
			attr = str(path[0])

			return self.__getattr__(attr)



	def __setitem__(self, path:tuple | list | str, value):
		if (not isinstance(path, (list, tuple))):
			path = [path]


		if (len(path) > 1):
			# Get final attribute
			attr = path[-1]

			# Get parent
			parent = self.parent(path)

			# If parent found
			if (parent != None):
				return RFT_Structure.__setattr__(parent, attr, value)


		else:
			attr = str(path[0])

			self.__setattr__(attr, value)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
	def getEvent(self, attr:str):
		return True

	def assignGetEvent(self, func):
		object.__setattr__(self, "getEvent", func)



	def setEvent(self, attr:str):
		return True

	def assignSetEvent(self, func):
		object.__setattr__(self, "setEvent", func)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	def __len__(self):
		return len(
			self.keys()
		)


	def __add__(self, value):
		value_ = RFT_Structure(value)
		self.default(value_)

		return self


	def __mul__(self, value):
		value_ = RFT_Structure(value)
		for k, v in value_.items():
			self[k] = v

		return self


	def __str__(self, *, showMagic:bool = False, indent:int = 0, found:list = [], ignore:list = []):
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
		return RFT_Structure(self)


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


	# ~~~~~ Wait for key ~~~~~
	def waitFor(self, attr:str | list | tuple, *, timeout:int | float = -1):
		start = time.time()

		while True:
			if (self.contains(attr)):
				return self[attr]

			else:
				if (timeout > 0):
					if (time.time() - start > timeout):
						return None

				time.sleep(0.01)


	# ~~~~~~ If readonly ~~~~~
	def readonly(self):
		return self.__dict__["__readonly__"]

	def setReadonly(self, value:bool):
		object.__setattr__(self, "__readonly__", bool(value))
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



	# ~~~~~ Contains Inst ~~~~
	def containsInst(self, attr:str | list | tuple, type_:type):
		l = []

		if (isinstance(attr, str)):
			attr = (attr,)

		for a in attr:
			if (self.contains(a)):
				l.append(
					isinstance(self[a], type_)
				)

			else:
				l.append(False)
					

		return all(l)



	# ~~~~~~~~~~ All ~~~~~~~~~
	def all(self):
		vals = []

		for k, v in self.items():
			vals.append(bool(v))

		return vals.all()



	# ~~~~~~~~~~ Any ~~~~~~~~~
	def any(self):
		vals = []

		for k, v in self.items():
			vals.append(bool(v))

		return vals.any()
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


	# ~~~~~~~~~~ Remove Data ~~~~~~~~~
	# ~~~~~~~~~~ Pop ~~~~~~~~~
	def pop(self, attr:str):
		if (not self.readonly()):
			d = self.data()

			return d.pop(attr)

		else:
			raise RFT_Exception("Structure is readonly", RFT_Exception.ERROR)



	# ~~~~~~~~~ Clear ~~~~~~~~
	def clear(self):
		if (not self.readonly()):
			d = self.data()

			d.clear()

		else:
			raise RFT_Exception("Structure is readonly", RFT_Exception.ERROR)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Allocate Data ~~~~~~~~
	# ~~~~~~~~ Default ~~~~~~~
	def default(self, struct):
		for k, v in struct.items():
			if (not self.contains(k)):
				self[k] = v

		return self



	# ~~~~~ Default Inst ~~~~~
	def defaultInst(self, attr:str, value, type_:type):
		if (not self.containsInst(attr, type_)):
			self[attr] = value

		return self



	# ~~~~~~~~ Parent ~~~~~~~~
	# Gets parent structure of given path
	def parent(self, path:tuple | list | str):
		if (not isinstance(path, (list, tuple))):
			path = [path]


		# Default parent
		parent = None


		if (len(path) > 0):
			# Set parent
			parent = self
			
			for i,a in enumerate(path[:-1]):
				# Get value in namespace
				val = parent[a]

				if (isinstance(val, RFT_Structure)):
					# Set new parent
					parent = val

				else:
					# Doesn't exist or invalid value
					parent = None
					break


		return parent



	# ~~~~~~~ Allocate ~~~~~~~
	def allocate(self, path:tuple | list | str):
		if (not isinstance(path, (list, tuple))):
			path = [path]


		parent = self

		for p in path:
			if (parent.contains(p)):
				v = parent[p]

				if (isinstance(v, RFT_Structure)):
					parent = v

				else:
					return None

			else:
				v = RFT_Structure()

				parent[p] = v
				parent = v


		return parent
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Convert Data ~~~~~~~~~
	# ~~~~~ To Dictionary ~~~~
	def toDict(self):
		out = {}

		for k,v in self.data().items():
			if (isinstance(v, RFT_Object)):
				if (hasattr(v, "toDict")):
					out[k] = v.toDict()

				else:
					out[k] = v
			else:
				out[k] = v

		return out
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




