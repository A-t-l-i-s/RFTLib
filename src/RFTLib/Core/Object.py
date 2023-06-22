from ..Require import *
from ..Console.Color import *





__all__ = ("RFT_Object",)





blacklistedVars = ("__class__", "__module__", "__dict__")
blacklistedTypes = (types.BuiltinFunctionType, types.BuiltinMethodType, types.MethodWrapperType)





class RFT_Object(object):
	def __str__(self, showMagic:bool = False, indent:int = 0) -> str:
		# Variables
		lines = []

		varis = sorted(dir(self))
		items = []

		longest = 0
		longestType = 0

		removed = []



		for k in varis:
			# Get value
			v = getattr(self, k)

			# If key is blacklisted
			if (k in blacklistedVars):
				removed.append(k)

			# If value is blacklisted
			elif (isinstance(v, blacklistedTypes)):
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

				# Append key and value to items
				items.append((k,v))



		# Remove all blacklisted vars
		for k in removed:
			varis.remove(k)



		# Opening structure
		lines.append("(")


		for k,v in items:
			if (isinstance(v, RFT_Object)):
				# Covert RFT object to string
				o = v.__str__(showMagic = showMagic, indent = indent + 1)


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
						if (isinstance(anno,types.UnionType)):
							annoL = anno.__args__
						elif (isinstance(anno,tuple | list)):
							annoL = tuple(anno)
						else:
							annoL = (anno,)


						for t in annoL:
							# If argument type is void
							if (t in (inspect._empty, types.NoneType, typing.NoReturn)):
								types_.append("void")

							else:
								# Get argument type name
								types_.append(t.__name__)
						

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
			if (isinstance(v,(inspect._empty,types.NoneType))):
				n = "void"
			else:
				n = type(v).__name__


			# Format type string
			typeStr = f"<{n}>"
			typeStr = typeStr.ljust(longestType + len(typeStr) - len(n) + 3)


			nameStr = k.ljust(longest + 3)


			# Combine all into single line
			l = "   " + typeStr + nameStr + o


			# Append new line
			lines.append(l)


		# Close structure
		lines.append(")")


		# Join lines into string
		out = ("\n" + ("   " * indent)).join(lines)


		# Return string
		return out




