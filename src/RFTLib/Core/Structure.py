from ..Require import *

from .Types import *
from .Object import *





__all__ = ("RFT_Structure",)





class RFT_Structure(RFT_Object):
	def __init__(self, struct:RFT_Typing.Dictionary, *, defaults:RFT_Typing.Dictionary = {}):
		# If struct is an RFT_Structure
		if (isinstance(struct, RFT_Structure)):
			newStruct = struct.data()
		else:
			newStruct = struct


		# If defaults is an RFT_Structure
		if (isinstance(defaults, RFT_Structure)):
			newDefaults = defaults.data()
		else:
			newDefaults = defaults



		# If newStruct is a dictionary
		if (isinstance(newStruct, dict)):
			# Copy dictionary
			data = copy.deepcopy(newDefaults)
			data.update(newStruct)


			for k in data.keys():
				v = data[k]

				if (isinstance(v, dict)):
					v = RFT_Structure(v)
					data[k] = v


			object.__setattr__(self, "__data__", data)

		else:
			raise TypeError





	# ~~~~~~~~ Attr Assignment ~~~~~~~
	def __getattr__(self, attr:str):
		self.getEvent(attr) # Call get event

		v = self.data() # Get dict data

		return v[attr]



	def __setattr__(self, attr:str, val:RFT_Typing.Any):
		self.setEvent(attr) # Call set event

		v = self.data() # Get dict data
		
		v[attr] = val
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~ Item Assignment ~~~~~~~
	def __getitem__(self, path:RFT_Typing.Array | str):
		# If path is string then split into array
		if (isinstance(path, str)):
			path = path.split(".")

		elif (not isinstance(path, (list, tuple))):
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
			# Create attribute string
			attr = ""
			for i, p in enumerate(path):
				attr += str(p)

				if (i < len(path) - 1):
					attr += "."

			return self.__getattr__(attr)



	def __setitem__(self, path:RFT_Typing.Array | str, value:RFT_Typing.Any):
		# If path is string then split into array
		if (isinstance(path, str)):
			path = path.split(".")

		elif (not isinstance(path, (list, tuple))):
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
			# Create attribute string
			attr = ""
			for i, p in enumerate(path):
				attr += str(p)

				if (i < len(path) - 1):
					attr += "."

			self.__setattr__(attr, value)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
	def getEvent(self, attr:str):
		...

	def assignGetEvent(self, func):
		object.__setattr__(self, "getEvent", func)



	def setEvent(self, attr:str):
		...

	def assignSetEvent(self, func):
		object.__setattr__(self, "setEvent", func)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	def __len__(self):
		return len(
			self.keys()
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Methods ~~~~~~~~~~~
	def data(self):
		d = self.__dict__
		v = d["__data__"]

		return v




	def get(self, key, default = None):
		if (self.contains(key)):
			return self[key]

		else:
			return default




	def keys(self):
		d = self.data()

		return d.keys()



	def items(self):
		d = self.data()

		return d.items()





	def contains(self, attr:RFT_Typing.Array | str):
		d = self.data()

		if (isinstance(attr, (list, tuple))):
			return all(
				[a in d.keys() for a in attr]
			)

		else:
			return attr in d.keys()





	def pop(self, attr:str):
		d = self.data()

		return d.pop(attr)





	def clear(self):
		d = self.data()

		d.clear()




	def copy(self):
		newStruct = RFT_Structure(
			self.data()
		)

		return newStruct





	# Gets parent structure of given path
	def parent(self, path:RFT_Typing.Array | str):
		# If path is string then split into array
		if (isinstance(path, str)):
			path = path.split(".")

		elif (not isinstance(path, (list, tuple))):
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





	def allocate(self, path:RFT_Typing.Array | str):
		# If path is string then split into array
		if (isinstance(path,str)):
			path = path.split(".")

		elif (not isinstance(path, (list, tuple))):
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






	def toDict(self):
		out = {}

		for k,v in self.data().items():
			if (isinstance(v, RFT_Structure)):
				out[k] = v.toDict()
			else:
				out[k] = v

		return out
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




