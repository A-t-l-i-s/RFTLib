from RFTLib.Require import *

from .Object import *
from .Resource import *
from .Structure import *
from .Exception import *





__all__ = ("RFT_Script",)





class RFT_Script(RFT_Object):
	def __init__(self, path:str):
		self.path = Path(path)
		
		# Verify path
		self.path.mkdir(
			parents = True,
			exist_ok = True
		)



	# ~~~~~~~~~~~~~ Load ~~~~~~~~~~~~~
	def load(self):
		# Create structure
		data = RFT_Structure({})


		# Resolve path
		path = self.path.resolve()


		if (path.exists()):
			if (path.is_file()):
				# Zip archive
				with zipfile.ZipFile(path, "r") as zfile:
					for f in zfile.infolist():
						if (not f.is_dir()):
							# Create path
							p = Path(f.filename)

							# Get attributes
							attr, ext = RFT_Resource.getAttr(p)
							attrEnd = attr.pop(-1)

							if (ext in ("py", "pyc")):
								with zfile.open(f.filename, "r") as file:
									# Read file
									fileData = file.read()

									# Allocate scope
									scope = RFT_Structure()

									try:
										# Execute code
										exec(fileData, scope.data())
									
									except:
										RFT_Exception.Traceback().print()

									else:
										# If any parent attributes then allocate some
										parent = data.allocate(attr)

										# Set value inside the parent
										parent[attrEnd] = scope



			else:
				for f in path.glob("**/*"):
					if (not f.is_dir()):
						# Format path and file to correct object structure naming
						# Resolve file path
						f = f.resolve()
						
						# Get parent/child path
						parent = f.as_posix()
						child = Path(parent.replace(path.as_posix(), ""))

						# Get attribute
						attr, ext = RFT_Resource.getAttr(child)
						attrEnd = attr.pop(-1)

						if (ext in ("py", "pyc")):
							try:
								# Import module spec
								spec = importlib.util.spec_from_file_location("script", f)

								# Get module
								mod = importlib.util.module_from_spec(spec)

								# Compile module
								spec.loader.exec_module(mod)

								# Module dict to scope
								scope = RFT_Structure(mod.__dict__)

							except:
								RFT_Exception.Traceback().print()

							else:
								# If any parent attributes then allocate some
								parent = data.allocate(attr)

								# Set value inside the parent
								parent[attrEnd] = scope


		# Return structure data
		return data
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






