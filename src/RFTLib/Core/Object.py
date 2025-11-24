from RFTLib.Require import *



__all__ = ("RFT_Object",)



class RFT_Object(object):
	# ~~~~~~~~~~ Attributes ~~~~~~~~~~
	def hasattr(self, attr:str) -> bool:
		return hasattr(self, attr)

	def getattr(self, attr:str, default:object = None) -> object:
		return getattr(self, attr, default)

	def setattr(self, attr:str, obj:object):
		object.__setattr__(self, attr, obj)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Context ~~~~~~~~~~~
	def __enter__(self) -> object:
		return self

	def __exit__(self, excType:object, excValue:object, excTraceback:object) -> bool:
		return False
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	def __str__(self, *, showMagic:bool = False, indent:int = 0, found:list = [], ignore:list = [], listOnly:bool = False) -> str:
		# Variables
		lines = []

		varis = dir(self)
		items = {}

		longest = 0
		longestType = 0

		removed = []

		# Clear found
		if (indent == 0):
			found.clear()

		found.append(id(self))


		for k in varis:
			try:
				# Get value
				v = self.getattr(k)

			except:
				...

			else:
				# If key is blacklisted
				if (k in ("__class__", "__module__", "__dict__")):
					removed.append(k)

				# If value is blacklisted
				elif (isinstance(v, (types.BuiltinFunctionType, types.BuiltinMethodType, types.MethodWrapperType))):
					removed.append(k)


				# If key in ignore list
				elif (k in ignore):
					removed.append(k)


				# Ignore magic functions
				elif (not showMagic and k.startswith("__") and k.endswith("__")):
					removed.append(k)


				else:
					# Determine longest var name
					l = len(k)
					if (l > longest):
						longest = l


					# Determine longest type name
					l = len(type(v).__name__)
					if (l > longestType):
						longestType = l


					# Get value type
					t = type(v)

					# Add list to items
					if (t not in items):
						items[t] = []

					# Append key and value to items
					items[t].append((k, v))



		# Remove all blacklisted vars
		for k in removed:
			varis.remove(k)

		# Opening structure
		if (listOnly):
			lines.append("[")

		else:
			lines.append("{")

		last = None

		for t, i in items.items():
			for k, v in i:
				id_ = id(v)

				if (isinstance(v, RFT_Object)):
					if (id_ not in found):
						# if (len(found) > 1):
						# 	# Add newline
						# 	lines.append("")

						found.append(id_)

						# Covert RFT object to string
						o = v.__str__(
							showMagic = showMagic,
							indent = indent + 1,
							found = found
						)

					else:
						o = "<...>"


				elif (isinstance(v, typing.Callable)):
					try:
						# Get function signature
						sig = inspect.signature(v)
					except:
						o = "void"

					else:
						# Get function parameters
						params = dict(sig.parameters)

						# Get function return type
						ret = sig.return_annotation


						# Return type is void
						if (ret in (inspect._empty, types.NoneType, typing.NoReturn, None)):
							retName = "void"

						else:
							# Get return type name
							retName = ret.__name__


						typeNames = []
						for k_, v_ in params.items():
							types_ = []
							
							# Get parameter annotations
							anno = v_.annotation

							# Convert annoatation to tuple
							if (isinstance(anno, types.UnionType)):
								annoL = anno.__args__

							elif (isinstance(anno, tuple | list)):
								annoL = tuple(anno)

							else:
								annoL = (anno,)


							for t in annoL:
								# If argument type is void
								if (t in (inspect._empty, types.NoneType, typing.NoReturn)):
									t_ = "void"

								else:
									# Get argument type name
									t_ = t.__name__

								types_.append(t_)


							# Append to type names list
							typeNames.append(f"{k_}: " + " | ".join(types_))


						# Join type names into string
						typeNamesStr = ", ".join(typeNames)
						
						# Create line output
						o = f"({typeNamesStr}) -> {retName}"


				elif (isinstance(v, tuple | list)):
					struct = {}

					for i, v in enumerate(v):
						struct[str(i)] = v

					obj = RFT_Object()
					obj.__dict__ = struct

					o = obj.__str__(
						showMagic = showMagic,
						indent = indent + 1,
						found = found,
						ignore = dir(RFT_Object),
						listOnly = True
					)

				else:
					# Get value repr
					o = str(v)


				# If value type is none
				if (isinstance(v, (inspect._empty, types.NoneType))):
					n = "void"
				
				else:
					n = type(v).__name__


				if (listOnly):
					l = f"\t{o}"

				else:
					# Format type string
					typeStr = f"<{n}>"


					if (isinstance(v, RFT_Object)):
						# Combine all into single line
						l = f"\t{typeStr} {k} {o}"

					else:
						l = f"\t{typeStr} {k}: {o}"



				# Add a newline of previous value is an object and current isn't
				if (isinstance(last, RFT_Object)):
					if (not isinstance(v, RFT_Object)):
						if (id(last) not in found):
							lines.append("")


				# Append new line
				lines.append(l)

				# Add last
				last = v


		# Close structure
		if (listOnly):
			lines.append("]")

		else:
			lines.append("}")

		# Return string
		return ("\n" + ("\t" * indent)).join(lines)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

