from ..Require import *

from .loader import *

from ..Core.Types import *
from ..Core.Object import *
from ..Core.Parser import *
from ..Core.Structure import *





__all__ = ("RFT_Config",)





class RFT_Config(RFT_Structure):
	def __init__(self):
		super().__init__({})






	"""
		path: Source file path location
		loaders: All loaders to sift through while loading file
		attr: Attribute location inside the structure
	"""
	def load(self, path:RFT_Typing.Path, loaders:RFT_Typing.Group, attr:str, hideErrors:bool = True):
		# Convert to pathlike
		path = Path(path)



		# Parse group into tuple
		loaders = RFT_Parser.parseGroup(loaders)



		# Split path
		p = attr.split(".")

		# End path
		end = p.pop(-1)

		# Get extension
		ext = path.suffix.lower().strip(".")



		# Iterate through all loaders
		for l in loaders:
			if (ext in l.exts):
				try:
					d = l.load(l, path)
				
				except:
					if (not hideErrors):
						print(traceback.format_exc())

				else:
					# If any parent attributes then allocate some
					if (len(p) > 0):
						parent = self.allocate(p)
					else:
						parent = self.data()


					# Set value inside the parent
					parent[end] = d





	"""
		path: Directory of configurations to iterate through
		loaders: All loaders to sift through while loading file
	"""
	def scan(self, path:RFT_Typing.Path, loaders:RFT_Typing.Group = (), hideErrors:bool = True):
		# Convert to pathlike
		path = Path(path)



		if (path.exists() and path.is_dir()):
			for f in path.glob("**/*.*"):
				if (f.is_file()):
					# Format path and file to correct object structure naming
					p = str(f.resolve().parent) \
						.replace(str(path.resolve()),"") \
						.replace("\\","/").replace("/",".") \
						.strip(".")
					

					# Parse path parent dir to file name
					p = f"{p}.{f.stem}" \
						.strip(".")


					# Remove all incorrect characters and replace them with underscores
					p_ = ""
					for c in p:
						if (c not in (string.ascii_letters + string.digits + "_.")):
							p_ += "_"
						else:
							p_ += c


					# Load file into structure
					self.load(f, loaders, p_, hideErrors = hideErrors)









