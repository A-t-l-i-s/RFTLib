from ..Require import *

from .loader import *

from ..Core.Object import *
from ..Core.Parser import *
from ..Core.Structure import *





__all__ = ("RFT_Config",)





class RFT_Config(RFT_Object):
	def __init__(self, path:tuple, loaders:tuple = None, showErrors:bool = False):
		self.path = path

		self.data = RFT_Structure({})

		if (loaders != None):
			self.load(loaders, showErrors)




	def load(self, loaders:tuple, showErrors:bool = False):
		# Convert to pathlike
		path = Path(self.path)


		# Parse group into tuple
		loaders = RFT_Parser.parseGroup(loaders)


		if (path.exists() and path.is_dir()):
			for f in path.glob("**/*.*"):
				if (f.is_file()):
					# Format path and file to correct object structure naming
					parent = Path(f.resolve().parent).as_posix()
					child = parent.replace(path.resolve().as_posix(), "")
					p = child.replace("/", ".").strip(".")


					# Parse path parent dir to file name
					structName = RFT_Parser.verifyPath(f.stem, "\\/:*?<>|.")
					p += "." + structName
					p = p.strip(".")


					# Remove all incorrect characters and replace them with underscores
					p = RFT_Parser.verifyPath(p)


					# Split path into tuple
					attr = p.split(".")

					# End path
					attrEnd = attr.pop(-1)

					# Get extension
					ext = f.suffix.lower().strip(".")


					# Iterate through all loaders
					for l in loaders:
						if (ext in l.exts):
							try:
								d = l.import_(l, f)

							except:
								if (showErrors):
									print(traceback.format_exc())

							else:
								# If any parent attributes then allocate some
								if (len(p) > 0):
									parent = self.data.allocate(attr)
								else:
									parent = self.data.data()


								# Set value inside the parent
								parent[attrEnd] = d









