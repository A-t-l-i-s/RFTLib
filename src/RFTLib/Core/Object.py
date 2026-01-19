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

		return self
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~ Normalize ~~~~~~
	def normalize(self) -> object:
		return None
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Context ~~~~~~~~~~~
	def __enter__(self) -> object:
		return self

	def __exit__(self, excType:object, excValue:object, excTraceback:object) -> bool:
		return False
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	def __str_function__(self, obj:object, *, key:str = None) -> str:
		funcName = getattr(obj, "__name__", key)
		out = ""


		try:
			# Get function signature
			details = inspect.signature(obj)
		
		except:
			out = f"{funcName}()"

		else:
			# Get returned out
			returnedOut = self.__str_type__(
				details.return_annotation
			)

			# Get function parameters
			params = dict(details.parameters)
			args = []

			for k, param in params.items():
				# Append to type names list
				args.append(
					f"{k}: " + self.__str_type__(
						param.annotation
					)
				)

			# Join type names into string
			paramsOut = ", ".join(args)


			# Create line output
			out = f"{funcName}({paramsOut}) -> {returnedOut}"

		finally:
			return out

	def __str_type__(self, obj:object) -> str:
		if (not isinstance(obj, tuple | list)):
			obj = [obj]

		# Define items
		items = []

		for v in obj:
			if (v in (inspect._empty, types.NoneType, typing.NoReturn)):
				# Argument type is void
				name = "None"

			elif (isinstance(v, types.GenericAlias)):
				name = str(v)

			elif (isinstance(v, list | tuple | types.UnionType)):
				if (isinstance(v, types.UnionType)):
					l = v.__args__
				else:
					l = v

				# Repeat call on list
				name = self.__str_type__(
					l
				)

			else:
				# Get argument type name
				name = getattr(v, "__name__", "None")

			# Append name
			items.append(f"{name}")


		# Append to type names list
		return " | ".join(items)

	def __str__(self, *, indent:int = 0, found:list | tuple = [], showMagic:bool = False, tab:str = "\t", newline:str = "\n", blockStart:str = "{", blockEnd:str = "}") -> str:
		found = list(found)

		lines = [blockStart]

		# Define longest key and value
		longestKey = 0
		longestType = 0

		# Clear found
		if (indent == 0):
			found.clear()


		# Add self to found list
		found.append(
			id(self)
		)

		# Define items
		items = {}

		for k in dir(self):
			try:
				# Get value
				v = self.getattr(k)

			except:
				# Failed to retrieve value for some reason
				v = None
				t = type(v)

			else:
				# Get type
				t = type(v)

			finally:
				# If key is blacklisted
				if (k in ("__class__", "__module__", "__dict__", "getattr", "setattr", "hasattr", "normalize")):
					...

				# If value is blacklisted
				elif (isinstance(v, types.BuiltinFunctionType | types.BuiltinMethodType | types.MethodWrapperType)):
					...

				# Ignore magic functions
				elif (not showMagic and (k.startswith("__") and k.endswith("__"))):
					...

				else:
					# Determine longest var name
					if ((lk := len(k)) > longestKey):
						longestKey = lk

					# Determine longest type name
					if ((lt := len(t.__name__)) > longestType):
						longestType = lt


					if (isinstance(v, dict | tuple | list | RFT_Object)):
						# Get uid
						uid = id(v)

						# If uid already displayed
						if (uid in found):
							v = hex(uid)

						else:
							# Add uid to found
							found.append(uid)


					# Add list to items
					if (t not in items):
						items[t] = []

					# Append key and value to items
					items[t].append((k, v))


		# Iter through filtered items
		for type_, values in items.items():
			for k, v in values:
				n = f"<{type_.__name__}> {k}: "


				if (isinstance(v, RFT_Object)):
					# Repeat operation on same class type
					l = n + v.__str__(
						indent = indent + 1,
						found = found,
						showMagic = showMagic
					)

				elif (isinstance(v, dict)):
					# Display dictionary
					o = RFT_Object()
					o.__dict__ = v

					l = n + o.__str__(
						indent = indent + 1,
						found = found,
						showMagic = showMagic
					)

				elif (isinstance(v, list | tuple)):
					# Display list
					o = RFT_Object()

					for i, x in enumerate(v):
						o.__dict__[f"{i}"] = x

					l = n + o.__str__(
						indent = indent + 1,
						found = found,
						showMagic = showMagic,
						blockStart = "[",
						blockEnd = "]"
					)

				elif (issubclass(type_, type)):
					# Display type
					l = n + v.__name__

				elif (issubclass(type_, typing.Callable)):
					# Display function
					l = f"<{type_.__name__}> {self.__str_function__(v, key = k)}"

				elif (issubclass(type_, str)):
					l = f"{n}\"{v}\""

				elif (issubclass(type_, bytes | bytearray | memoryview)):
					l = f"{n}b\"{str(v, 'utf-8', 'ignore')}\""

				else:
					l = f"{n}{v}"

				# Add line to list
				lines.append(l)


		return (newline + (tab * (indent + 1))).join(lines) + newline + (tab * indent) + blockEnd

	def __repr__(self) -> str:
		return self.__str__()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


