from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Structure import *

from .entries.xml import Entry as RFT_Resource_XML
from .entries.json import Entry as RFT_Resource_JSON
from .entries.yaml import Entry as RFT_Resource_YAML
from .entries.toml import Entry as RFT_Resource_TOML

from .entries.raw import Entry as RFT_Resource_RAW
from .entries.text import Entry as RFT_Resource_TEXT
from .entries.python import Entry as RFT_Resource_PYTHON

from .entries.qt.qicon import Entry as RFT_Resource_QT_QICON
from .entries.qt.qimage import Entry as RFT_Resource_QT_QIMAGE
from .entries.qt.qpixmap import Entry as RFT_Resource_QT_QPIXMAP





__all__ = (
	"RFT_Resource",

	"RFT_Resource_XML",
	"RFT_Resource_JSON",
	"RFT_Resource_YAML",
	"RFT_Resource_TOML",

	"RFT_Resource_RAW",
	"RFT_Resource_TEXT",
	"RFT_Resource_PYTHON",

	"RFT_Resource_QT_QICON",
	"RFT_Resource_QT_QIMAGE",
	"RFT_Resource_QT_QPIXMAP",
)





class RFT_Resource(RFT_Object):
	def __init__(self, path:str, entries:dict):
		self.path = Path(path)

		self.entries = entries



	def load(self):
		# Create structure
		data = RFT_Structure({})


		# Initialize entry
		for ex, en in self.entries.items():
			if (hasattr(en, "init")):
				try:
					en.init(en)

				except:
					print(traceback.format_exc())


		# Resolve path
		path = self.path.resolve()


		if (path.exists() and path.is_dir()):
			for f in path.glob("**/*.*"):
				if (f.is_file()):
					# Format path and file to correct object structure naming
					# Resolve file path
					f = f.resolve()
					
					# Get parent/child path
					parent = f.parent.as_posix()
					child = parent.replace(path.as_posix(), "")

					# Create attributes from path
					p = child.replace("/", ".").strip(".")


					# Parse path parent dir to file name
					structName = ""
					for c in f.stem:
						if (c not in "\\/:*?<>|."):
							structName += c
						else:
							structName += "_"

					p += "." + structName
					p = p.strip(".")


					# Split path into tuple
					attr = p.split(".")

					# End path
					attrEnd = attr.pop(-1)

					# Get extension
					ext = f.suffix.lower().strip(".")


					# Iterate through all entries
					for ex, en in self.entries.items():
						if (re.fullmatch(ex, ext)):
							if (hasattr(en, "load")):
								try:
									d = en.load(en, f)

								except:
									print(traceback.format_exc())

								else:
									# If any parent attributes then allocate some
									if (len(p) > 0):
										parent = data.allocate(attr)
									else:
										parent = data.data()


									# Set value inside the parent
									parent[attrEnd] = d


		# Return structure data
		return data






