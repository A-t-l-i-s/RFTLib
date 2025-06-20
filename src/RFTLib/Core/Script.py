from RFTLib.Require import *

from .Object import *
from .Resource import *
from .Structure import *
from .Exception import *





__all__ = ("RFT_Script",)





class RFT_Script(RFT_Object):
	def __init__(self, path:str | Path):
		self.path = Path(path)
		
		if (not self.path.is_file()):
			# Verify path
			self.path.mkdir(
				parents = True,
				exist_ok = True
			)



	# ~~~~~~~~~~~~~ Load ~~~~~~~~~~~~~
	def load(self, *, callback = None):
		# Create structure
		data = RFT_Structure()

		# Resolve path
		path = self.path.resolve()

		if (path.exists()):
			if (path.is_file()):
				# Zip archive
				with zipfile.ZipFile(path, "r") as zfile:
					for f in zfile.infolist():
						if (not f.is_dir()):
							name = f.filename

							# Create path
							p = Path(name)

							# Get attributes
							attr, ext = RFT_Resource.getAttr(p)
							attrEnd = attr.pop(-1)

							if (ext in ("py", "pyc")):
								while True:
									retry = False

									with zfile.open(name, "r") as file:
										# Read file
										fileData = file.read()

										try:
											# Create empty module spec
											spec = importlib.util.spec_from_loader("__RFTScript__", loader = None)

											# Get module
											mod = importlib.util.module_from_spec(spec)

											# Execute code
											exec(fileData, mod.__dict__)
											
											# Allocate scope
											scope = RFT_Structure(mod.__dict__)
										
										except:
											exc = RFT_Exception.Traceback()
											
											if (callback is not None):
												retry = callback(exc, p)

											else:
												raise exc

										else:
											# If any parent attributes then allocate some
											parent = data.allocate(attr)

											# Set value inside the parent
											parent[attrEnd] = scope

										finally:
											if (not retry):
												break



			else:
				for f in path.glob("**/*"):
					if (not f.is_dir()):
						# Format path and file to correct object structure naming
						# Resolve file path
						f = f.resolve()
						
						# Get parent/child path
						parent = f.as_posix()
						child = Path(parent.replace(path.resolve().as_posix(), ""))

						name = child.as_posix().strip("/")

						# Get attribute
						attr, ext = RFT_Resource.getAttr(child)
						attrEnd = attr.pop(-1)

						if (ext in ("py", "pyc")):
							while True:
								retry = False

								try:
									# Import module spec
									spec = importlib.util.spec_from_file_location("__RFTScript__", f)

									# Get module
									mod = importlib.util.module_from_spec(spec)

									# Compile module
									spec.loader.exec_module(mod)

									# Module dict to scope
									scope = RFT_Structure(mod.__dict__)

								except:
									exc = RFT_Exception.Traceback()
											
									if (callback is not None):
										retry = callback(exc, name)

									else:
										raise exc

								else:
									# If any parent attributes then allocate some
									parent = data.allocate(attr)

									# Set value inside the parent
									parent[attrEnd] = scope

								finally:
									if (not retry):
										break


		# Return structure data
		return data
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






