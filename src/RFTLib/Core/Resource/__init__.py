from RFTLib.Require import *

from ..Object import *
from ..Exception import *
from ..Structure import *

from .json import Entry as RFT_Resource_JSON
from .yaml import Entry as RFT_Resource_YAML
from .toml import Entry as RFT_Resource_TOML

from .raw import Entry as RFT_Resource_RAW
from .text import Entry as RFT_Resource_TEXT

from .qt.qicon import Entry as RFT_Resource_QT_QICON
from .qt.qimage import Entry as RFT_Resource_QT_QIMAGE
from .qt.qpixmap import Entry as RFT_Resource_QT_QPIXMAP





__all__ = (
	"RFT_Resource",

	"RFT_Resource_JSON",
	"RFT_Resource_YAML",
	"RFT_Resource_TOML",

	"RFT_Resource_RAW",
	"RFT_Resource_TEXT",

	"RFT_Resource_QT_QICON",
	"RFT_Resource_QT_QIMAGE",
	"RFT_Resource_QT_QPIXMAP",
)





class RFT_Resource(RFT_Object):
	def __init__(self, path:str, entries:dict):
		self.path = Path(path)

		self.entries = entries

		if (not self.path.is_file()):
			# Verify path
			self.path.mkdir(
				parents = True,
				exist_ok = True
			)


	# ~~~~~~~~~~~~~ Load ~~~~~~~~~~~~~
	def load(self, callback = None):
		# Create structure
		data = RFT_Structure({})


		# Initialize entry
		for ex, en in self.entries.items():
			if (hasattr(en, "init")):
				try:
					en.init(en)

				except:
					...


		# Resolve path
		path = self.path.resolve()


		if (path.exists()):
			if (path.is_file()):
				with zipfile.ZipFile(path, "r") as zfile:
					for f in zfile.infolist():
						if (not f.is_dir()):
							name = f.filename

							# Create path
							p = Path(name)

							# Get attributes
							attr, ext = self.getAttr(p)

							# Open and Process file
							while True:
								retry = False
								
								with zfile.open(name, "r") as file:
									try:
										self.processFile(
											attr, ext, file, data
										)

									except:
										exc = RFT_Exception(f"Failed to load file \"{name}\"")

										if (callback is not None):
											retry = callback(exc, p)

										else:
											raise exc

									finally:
										if (not retry):
											break



			else:
				for f in self.path.glob("**/*"):
					if (not f.is_dir()):
						# Format path and file to correct object structure naming
						# Resolve file path
						f_ = f.resolve()
						
						# Get parent/child path
						parent = f_.as_posix()
						child = Path(parent.replace(path.as_posix(), ""))

						name = Path(child.as_posix().strip("/"))

						# Get attribute
						attr, ext = self.getAttr(child)

						# Open and Process file
						while True:
							retry = False
							
							with f.open("rb") as file:
								try:
									self.processFile(
										attr, ext, file, data
									)

								except:
									exc = RFT_Exception(f"Failed to load file \"{name}\"")

									if (callback is not None):
										retry = callback(exc, name)

									else:
										raise exc

								finally:
									if (not retry):
										break


		# Return structure data
		return data
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	@classmethod
	def getAttr(self, path):
		# Get parent
		parent = path.parent.as_posix()

		# Create attributes from path
		p = parent.replace("/", ".").strip(".")

		# Verify stem chars
		name = ""
		for c in path.stem:
			if (c not in "\\/:*?<>|."):
				name += c
			else:
				name += "_"

		# Add file stem
		p += "." + name
		p = p.strip(".")

		# Split path into tuple
		attr = p.split(".")

		# Get extension
		ext = path.suffix.lower().strip(".")

		return attr, ext



	def processFile(self, attr, ext, file, data):
		attr = list(attr)

		# End path
		attrEnd = attr.pop(-1)


		# Iterate through all entries
		for ex, en in self.entries.items():
			if (re.fullmatch(ex, ext)):
				if (hasattr(en, "load")):
					try:
						d = en.load(en, file)

					except:
						raise RFT_Exception.Traceback()

					else:
						# If any parent attributes then allocate some
						parent = data.allocate(attr)

						if (parent.containsInst(attrEnd, RFT_Structure)):
							# Default value
							parent[attrEnd].default(d)

						else:
							# Set value inside the parent
							parent[attrEnd] = d
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



