from .Object import *
from .Types import *





__all__ = ("RFT_Structure",)





class RFT_Structure(RFT_Object):
	def __init__(self, struct:RFT_Typing.Dictionary):
		if (isinstance(struct,RFT_Structure)):
			struct = struct.data()


		if (isinstance(struct,dict)):
			data = dict(struct)
			

			for k in struct.keys():
				v = struct[k]

				if (isinstance(v,dict)):
					v = RFT_Structure(v)
					struct[k] = v


			object.__setattr__(self,"__data__",struct)

		else:
			raise TypeError





	# ~~~~~~~~ Attr Assignment ~~~~~~~
	def __getattr__(self, attr:str):
		v = self.data()

		return v[attr]



	def __setattr__(self, attr:str, val:RFT_Typing.Any):
		v = self.data()
		
		v[attr] = val
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~ Item Assignment ~~~~~~~
	def __getitem__(self, path:RFT_Typing.Array | str):
		# If path is string then split into array
		if (isinstance(path,str)):
			path = path.split(".")


		if (len(path) > 1):
			# Get final attribute
			attr = path[-1]

			# Get parent
			parent = self.parent(path)

			# If parent found
			if (parent != None):
				return RFT_Structure.__getattr__(parent,attr)


		else:
			attr = ".".join(path)
			return self.__getattr__(attr)



	def __setitem__(self, path:RFT_Typing.Array | str, value:RFT_Typing.Any):
		# If path is string then split into array
		if (isinstance(path,str)):
			path = path.split(".")


		if (len(path) > 1):
			# Get final attribute
			attr = path[-1]

			# Get parent
			parent = self.parent(path)

			# If parent found
			if (parent != None):
				return RFT_Structure.__setattr__(parent,attr,value)


		else:
			attr = ".".join(path)
			self.__setattr__(attr,value)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





	def data(self):
		d = self.__dict__
		v = d["__data__"]

		return v




	def toDict(self):
		out = {}

		for k,v in self.data().items():
			if (isinstance(v,RFT_Structure)):
				out[k] = v.toDict()
			else:
				out[k] = v

		return out






	def keys(self):
		d = self.data()

		return tuple(d.keys())





	def contains(self, attr:str):
		d = self.data()

		return attr in d.keys()





	def pop(self, attr:str):
		d = self.data()

		return d.pop(attr)





	# Gets parent structure of given path
	def parent(self, path:RFT_Typing.Array | str):
		# If path is string then split into array
		if (isinstance(path,str)):
			path = path.split(".")


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




