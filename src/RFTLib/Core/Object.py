from RFTLib.Require import *





__all__ = ("RFT_Object",)





class RFT_Object(object):
	# ~~~~~~~~~~~~ Globals ~~~~~~~~~~~
	# ~~~~~~~~~ Lift ~~~~~~~~~
	def lift(self, name:str):
		setattr(
			builtins,
			name,
			self
		)


	# ~~~~~~~~~ Drop ~~~~~~~~~
	def drop(self, name:str):
		# If had attribute
		if (hasattr(builtins, name)):
			# Get value
			v = getattr(builtins, name)

			if (v == self):
				# Delete attribute
				delattr(
					builtins,
					name
				)


	# ~~~~~~~~~ Copy ~~~~~~~~~
	def copy(self):
		return copy.deepcopy(self)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~ Attributes ~~~~~~~~~~
	def tryattr(self, attr, ret = None):
		if (hasattr(self, attr)):
			return getattr(self, attr)

		else:
			return ret


	def hasattr(self, attr):
		return hasattr(self, attr)


	def getattr(self, attr):
		return getattr(self, attr)


	def setattr(self, attr, value):
		setattr(self, attr, value)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	def __str__(self, showMagic:bool = False, indent:int = 0, found = []):
		# Variables
		lines = []

		varis = sorted(dir(self))
		items = {}

		longest = 0
		longestType = 0

		removed = []

		# Clear found
		if (indent == 0):
			found.clear()

		found.append(self)


		for k in varis:
			try:
				# Get value
				v = getattr(self, k)
			except:
				...

			else:
				# If key is blacklisted
				if (k in ("__class__", "__module__", "__dict__")):
					removed.append(k)

				# If value is blacklisted
				elif (isinstance(v, (types.BuiltinFunctionType, types.BuiltinMethodType, types.MethodWrapperType))):
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
		lines.append("{")

		last = None

		for t, i in items.items():
			for k, v in i:
				if (isinstance(v, RFT_Object)):
					if (v not in found):
						# Add newline
						lines.append("")

						found.append(v)
						
						try:
							# Covert RFT object to string
							o = v.__str__(showMagic = showMagic, indent = indent + 1, found = found)
						
						except:
							o = "<error>"

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
						for k_,v_ in params.items():
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
						


							# Join types to form name
							name = " | ".join(types_)

							# Append to type names list
							typeNames.append(f"{k_}: {name}")


						# Join type names into string
						typeNamesStr = ", ".join(typeNames)
						
						# Create line output
						o = f"({typeNamesStr}) -> {retName}"


				else:
					# Get value repr
					o = str(v)



				# If value type is none
				if (isinstance(v, (inspect._empty, types.NoneType))):
					n = "void"
				else:
					n = type(v).__name__




				# Format type string
				typeStr = f"<{n}>"
				typeStr = typeStr.ljust(longestType + len(typeStr) - len(n) + 3)


				nameStr = k.ljust(longest + 3)


				# Combine all into single line
				l = "   " + typeStr + nameStr + o


				# Add a newline of previous value is an object and current isn't
				if (isinstance(last, RFT_Object)):
					if (not isinstance(v, RFT_Object)):
						if (last not in found):
							lines.append("")


				# Append new line
				lines.append(l)

				# Add last
				last = v



		# Close structure
		lines.append("}")


		# Join lines into string
		out = ("\n" + ("   " * indent)).join(lines)

		# Return string
		return out
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

