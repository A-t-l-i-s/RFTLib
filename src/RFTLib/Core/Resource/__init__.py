from RFTLib.Require import *

from ..Object import *
from ..Exception import *
from ..Structure import *

from .entries.json import Entry as RFT_Resource_JSON
from .entries.yaml import Entry as RFT_Resource_YAML
from .entries.toml import Entry as RFT_Resource_TOML

from .entries.raw import Entry as RFT_Resource_RAW
from .entries.text import Entry as RFT_Resource_TEXT

from .entries.qt.qicon import Entry as RFT_Resource_QT_QICON
from .entries.qt.qimage import Entry as RFT_Resource_QT_QIMAGE
from .entries.qt.qpixmap import Entry as RFT_Resource_QT_QPIXMAP





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
	def load(self):
		# Create structure
		data = RFT_Structure({})


		# Initialize entry
		for ex, en in self.entries.items():
			if (hasattr(en, "init")):
				try:
					en.init(en)

				except:
					RFT_Exception.Traceback().print()


		# Resolve path
		path = self.path.resolve()


		if (path.exists()):
			if (path.is_file()):
				with zipfile.ZipFile(path, "r") as zfile:
					for f in zfile.infolist():
						if (not f.is_dir()):
							# Create path
							p = Path(f.filename)

							# Get attributes
							attr, ext = self.getAttr(p)

							# Open and Process file
							with zfile.open(f.filename, "r") as file:
								self.processFile(
									attr, ext, file, data
								)


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
						attr, ext = self.getAttr(child)

						# Open and Process file
						with f.open("rb") as file:
							self.processFile(
								attr, ext, file, data
							)


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
		# End path
		attrEnd = attr.pop(-1)


		# Iterate through all entries
		for ex, en in self.entries.items():
			if (re.fullmatch(ex, ext)):
				if (hasattr(en, "load")):
					try:
						d = en.load(en, file)

					except:
						RFT_Exception.Traceback().print()

					else:
						# If any parent attributes then allocate some
						parent = data.allocate(attr)

						# Set value inside the parent
						parent[attrEnd] = d
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



