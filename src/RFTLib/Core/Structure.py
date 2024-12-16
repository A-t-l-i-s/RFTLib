from RFTLib.Require import *

from .Object import *
from .Exception import *





__all__ = ("RFT_Structure",)





class RFT_Structure(RFT_Object):
	def __init__(self, struct:dict = None, *, defaults:dict = {}, readonly:bool = False):
		# Create new dict
		if (struct == None):
			struct = dict()


		# Convert struct to dict
		if (isinstance(struct, RFT_Structure)):
			newStruct = struct.data()
		else:
			newStruct = struct


		# Convert defaults to dict
		if (isinstance(defaults, RFT_Structure)):
			newDefaults = defaults.data()
		else:
			newDefaults = defaults



		# If newStruct is a dictionary
		if (isinstance(newStruct, dict)):
			# Copy dictionary
			data = copy.deepcopy(newDefaults)
			data.update(newStruct)


			# Iterate keys
			for k in data.keys():
				v = data[k]

				if (isinstance(v, dict)):
					# Convert to structure
					v = RFT_Structure(v)
					data[k] = v


			object.__setattr__(self, "__data__", data)
			object.__setattr__(self, "__readonly__", readonly)

		else:
			raise TypeError





	# ~~~~~~~~ Attr Assignment ~~~~~~~
	def __getattr__(self, attr:str):
		if (self.getEvent(attr)):
			# Get dict data
			v = self.data()

			# Return value
			return v[attr]



	def __setattr__(self, attr:str, value):
		if (not self.__readonly__):
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
		if (isinstance(value, (dict, RFT_Structure))):
			self.default(value)

		return self
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Retrieve Data ~~~~~~~~
	# ~~~~~ Get Raw Data ~~~~~
	def data(self):
		return self.__dict__["__data__"]


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


	# ~~~~~~ If readonly ~~~~~
	def readonly(self):
		return self.__dict__["__readonly__"]
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Contains Data ~~~~~~~~
	# ~~~~~~~ Contains ~~~~~~~
	def contains(self, attr:tuple | list | str):
		d = self.data()
		k = d.keys()

		if (isinstance(attr, (list, tuple))):
			return all(
				[a in k for a in attr]
			)

		else:
			return attr in k



	# ~~~~~ Contains Inst ~~~~
	def containsInst(self, attr:str, type_:type):
		if (self.contains(attr)):
			if (isinstance(self[attr], type_)):
				return True

		return False



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



	# ~~~~~~~~~~ Remove Data ~~~~~~~~~
	# ~~~~~~~~~~ Pop ~~~~~~~~~
	def pop(self, attr:str):
		d = self.data()

		return d.pop(attr)



	# ~~~~~~~~~ Clear ~~~~~~~~
	def clear(self):
		d = self.data()

		d.clear()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Allocate Data ~~~~~~~~
	# ~~~~~~~~ Default ~~~~~~~
	def default(self, struct):
		for k, v in struct.items():
			if (not self.contains(k)):
				self[k] = v



	# ~~~~~ Default Inst ~~~~~
	def defaultInst(self, attr:str, value, type_:type):
		if (not self.containsInst(attr, type_)):
			self[attr] = value



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

				if (isinstance(val,RFT_Structure)):
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

				if (isinstance(v,RFT_Structure)):
					parent = v

				else:
					return None

			else:
				v = RFT_Structure({})

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




