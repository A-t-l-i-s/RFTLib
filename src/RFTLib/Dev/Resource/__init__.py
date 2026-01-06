from RFTLib.Require import *
from RFTLib.Dev.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Exception import *
from RFTLib.Core.Structure import *

from RFTLib.Dev.Logging import *
from RFTLib.Dev.Decorator import *



__all__ = ("RFT_Resource",)



class RFT_Resource(RFT_Object):
	"""
	If a filename extension matchs a key then call that keys function.

	{
		r"json": RFT_Resource.JSON_Entry,
		r"yaml|yml": RFT_Resource.YAML_Entry
	}

	"""
	def __init__(self, entries:dict[str, object] | RFT_Object):
		# Assign entries
		self.entries = RFT_Structure(entries)
		self.timestamps = RFT_Structure()

		# Create logger
		self.logger = RFT_Logging()



	# ~~~~~~~~ Iter Resources ~~~~~~~~
	@RFT_Decorator
	def iterDir(self, path:str) -> tuple[str, object]:
		# Create path object
		path = pathlib.Path(path)


		if (path.exists()):
			if (path.is_dir()):
				for file in path.rglob("*.*"):
					if (file.is_file()):
						# Get path relative to current path
						rel = file.relative_to(path)

						# Create attribute for structure
						attr = self.formatAttr(rel.parent.as_posix().replace("/", "."), rel.stem.replace(".", "_"))

						# Get entry
						entry = self.getEntry(rel)

						if (entry is not None):
							# Open file
							with file.open("rb") as fileIO:
								try:
									v = entry.__call__(fileIO)

								except:
									v = RFT_Exception.Traceback(
										(RFT_Exception.ERROR, entry.__name__, ".".join(attr))
									)

									# Log exception
									self.logger.log(v)

								else:
									# Log file found
									self.logger.log(
										RFT_Exception(
											f"Loaded \"{rel.as_posix()}\"",
											(entry.__name__, ".".join(attr))
										)
									)

								finally:
									yield (
										attr,
										v	
									)

			else:
				raise RFT_Exception("Directory is file")
		else:
			raise RFT_Exception("Directory doesn't exist")


	@RFT_Decorator
	def iterZip(self, path:str) -> tuple[str, object]:
		# Create path object
		path = pathlib.Path(path)


		if (path.exists()):
			if (path.is_file()):
				with zipfile.ZipFile(path, "r") as zfile:
					for file in zfile.infolist():
						if (not file.is_dir()):
							# Get filename
							name = file.filename

							# Create path
							rel = pathlib.Path(name)
							
							# Create attribute for structure
							attr = self.formatAttr(rel.parent.as_posix().replace("/", "."), rel.stem.replace(".", "_"))

							# Get entry
							entry = self.getEntry(rel)

							if (entry is not None):
								# Open file in zipfile
								with zfile.open(file, "r") as fileIO:
									try:
										v = entry.__call__(fileIO)

									except:
										v = RFT_Exception.Traceback(
											(RFT_Exception.ERROR, entry.__name__, ".".join(attr))
										)

										# Log exception
										self.logger.log(v)

									else:
										# Log file found
										self.logger.log(
											RFT_Exception(
												f"Loaded \"{rel.as_posix()}\"",
												(entry.__name__, ".".join(attr))
											)
										)

									finally:
										yield (
											attr,
											v	
										)

			else:
				raise RFT_Exception("File is directory")
		else:
			raise RFT_Exception("File doesn't exist")
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Load Resources ~~~~~~~~
	@RFT_Decorator
	def load(self, path:str, struct:RFT_Object = None, *, single:bool = False, errEvent:object = None) -> RFT_Object:
		# Create path object
		path = pathlib.Path(path)

		# Check if path exists
		if (path.exists()):
			if (struct is None):
				# Create new structure
				structOut = RFT_Structure(struct)

			else:
				# Assign structure
				structOut = struct


			if (path.is_dir()):
				# Load from directory
				loader = self.iterDir

			else:
				# Load from zip file
				loader = self.iterZip


			# Iterate through all content
			for attr, value in loader(path):
				# Check if any files raised an error
				if (isinstance(value, RFT_Exception)):
					if (errEvent is not None):
						try:
							# Call errEvent with attr and exception
							errEvent(attr, value)

						except:
							v = RFT_Exception.Traceback()

							# Log error
							self.logger.log(
								RFT_Exception(
									v,
									(".".join(attr), "errEvent")
								)
							)

							raise v

					else:
						raise value

				else:
					if (single):
						# Only a single namespace
						structOut[
							"_".join(attr).replace(".", "_")
						] = value

					else:
						# Get parent of attribute and assign the key to the value
						attrEnd = attr.pop(-1)
						parent = structOut.allocate(attr)
						parent[attrEnd] = value


			# Return structure at end
			return structOut

		else:
			raise RFT_Exception("Path doesn't exist")
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~ Get Entry ~~~~~~
	@RFT_Decorator
	def getEntry(self, path:str) -> RFT_Object:
		path = pathlib.Path(path)
		ext = path.name.split(".")[-1]

		# Iterate through all entries
		for pattern, entry in self.entries.items():
			if (re.fullmatch(pattern, ext, flags = re.IGNORECASE)):
				return entry


	# ~~~~~~ Format Attr ~~~~~
	@RFT_Decorator
	def formatAttr(self, *text:tuple | list) -> str:
		"""
		Forcefully replaces any whitelisted characters to '_'

		Parameters:
			<text> text: Text needed to convert

		--> tuple[list]: Forced converted text
		"""
		out = [""]

		for t in text:
			if (t):
				if (out[-1]):
					out.append("")

				for c in t:
					if (c == '.'):
						if (out[-1]):
							out.append("")

					elif (c not in string.ascii_letters + string.digits + "_"):
						out[-1] += '_'

					else:
						out[-1] += c

		return out


	# ~~~~~~~~~~~~ Entries ~~~~~~~~~~~
	@RFT_Decorator.configure(static = True)
	def JSON_Entry(self, file:object) -> RFT_Object:
		# Read file
		dataRaw = json.load(file)

		if (dataRaw is None or isinstance(dataRaw, dict)):
			# Convert to struct
			data = RFT_Structure(dataRaw)

		else:
			data = dataRaw

		# Return data
		return data


	@RFT_Decorator.configure(static = True)
	def YAML_Entry(self, file:object) -> RFT_Object:
		import yaml

		# Read file
		dataRaw = yaml.load(
			file,
			Loader = yaml.FullLoader
		)

		if (dataRaw is None or isinstance(dataRaw, dict)):
			# Convert to struct
			data = RFT_Structure(dataRaw)

		else:
			data = dataRaw


		# Return data
		return data


	@RFT_Decorator.configure(static = True)
	def TOML_Entry(self, file:object) -> RFT_Object:
		import tomllib

		# Read file
		dataRaw = tomllib.load(file)

		if (dataRaw is None or isinstance(dataRaw, dict)):
			# Convert to struct
			data = RFT_Structure(dataRaw)

		else:
			data = dataRaw


		# Return data
		return data


	@RFT_Decorator.configure(static = True)
	def STRING_Entry(self, file:object) -> str:
		# Allocate buffer
		with RFT_Buffer() as buf:
			# Read entire file
			buf += file.read()

			# Return data
			return buf.toStr()


	@RFT_Decorator.configure(static = True)
	def BUFFER_Entry(self, file:object) -> RFT_Object:
		# Allocate buffer
		buf = RFT_Buffer()

		# Read entire file
		buf += file.read()

		# Return data
		return buf


	@RFT_Decorator.configure(static = True)
	def PYTHON_Entry(self, file:object) -> RFT_Object:
		# Allocate buffer
		buf = RFT_Buffer()
		buf += file.read()

		with RFT_Structure() as struct:
			# Create empty module spec
			spec = importlib.util.spec_from_loader(f"PYTHON_Entry.{uuid.uuid4().hex}", loader = None)

			# Get module
			mod = importlib.util.module_from_spec(spec)

			# Compile module
			exec(buf.data, mod.__dict__)

			# Module dict to scope
			struct += mod.__dict__

		# Return data
		return struct


	@RFT_Decorator.configure(static = True)
	def QT_QIMAGE_Entry(self, file:object) -> object:
		from PyQt6.QtGui import QImage

		# Read entire file
		data = file.read()

		# Load as qimage
		img = QImage.fromData(data)

		# Return data
		return img


	@RFT_Decorator.configure(static = True)
	def QT_QPIXMAP_Entry(self, file:object) -> object:
		from PyQt6.QtGui import QImage, QPixmap

		# Read entire file
		data = file.read()

		# Load as qimage
		img = QImage.fromData(data)
		pix = QPixmap.fromImage(img)

		# Return data
		return pix


	@RFT_Decorator.configure(static = True)
	def QT_QICON_Entry(self, file:object) -> object:
		from PyQt6.QtGui import QImage, QPixmap, QIcon

		# Read entire file
		data = file.read()

		# Allocate icon
		ico = QIcon()

		# Load as qimage
		img = QImage.fromData(data)
		pix = QPixmap.fromImage(img)

		# Add pixmap
		ico.addPixmap(pix)

		# Return data
		return ico
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

