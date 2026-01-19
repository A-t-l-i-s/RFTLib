from RFTLib.Require import *
from RFTLib.Dev.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Exception import *
from RFTLib.Core.Structure import *

from RFTLib.Timer import *

from RFTLib.Dev.Logging import *
from RFTLib.Dev.Decorator import *

from .entries import *



__all__ = ("RFT_Resource", "RFT_Resource_Entries")



class RFT_Resource(RFT_Object):
	"""
	If a filename extension matchs a key then call that keys function.

	{
		r"json": RFT_Resource_Entries.JSON_Entry,
		r"yaml|yml": RFT_Resource_Entries.YAML_Entry
	}

	"""
	def __init__(self, path:str, entries:dict[str, object] | RFT_Object):
		# Assign entries
		self.path = pathlib.Path(path)
		self.entries = RFT_Structure(entries)

		# Allocate timestamps
		self.timestamps = RFT_Structure()

		# Create logger
		self.logger = RFT_Logging()


	# ~~~~~~ Verify Dir ~~~~~~
	def verify(self):
		# Check if path is a file
		if (not self.path.exists()):
			try:
				# Verify integrity of path
				self.path.mkdir(
					parents = True,
					exist_ok = True
				)

				# Log success
				self.logger.log(
					f"Created directory: \"{self.path.as_posix()}\"",
				)

			except:
				# Log failure
				self.logger.log(
					f"Failed to create directory: \"{self.path.as_posix()}\"",
				)
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Iter Resources ~~~~~~~~
	def iter(self, *, onlyUpdated:bool = False) -> tuple[str, object]:
		if (self.path.exists()):
			if (self.path.is_dir()):
				# Iter directory
				for attr, value in self.iterDir(onlyUpdated = onlyUpdated):
					yield (attr, value)

			else:
				# Iter zip file
				for attr, value in self.iterZip(onlyUpdated = onlyUpdated):
					yield (attr, value)

		else:
			raise RFT_Exception("Directory doesn't exist")


	def iterDir(self, *, onlyUpdated:bool = False) -> tuple[str, object]:
		if (self.path.exists()):
			if (self.path.is_dir()):
				for file in self.path.rglob("*.*"):
					if (file.is_file()):
						# Get path relative to current path
						rel = file.relative_to(self.path)

						# Get entry
						entry = self.getEntry(rel)

						if (entry is not None):
							# Create attribute for structure
							attr = self.formatAttr(
								rel.parent.as_posix().replace("/", "."),
								rel.stem.replace(".", "_")
							)

							# Get uid
							uid = "-".join(attr).replace(".", "-")

							# Get stat
							stat = file.stat()
							timestamp = stat.st_mtime
							update = True

							# Check if already loaded and if file was edited after that
							if (self.timestamps.contains(uid)):
								if (self.timestamps[uid] >= timestamp):
									update = False


							if (onlyUpdated):
								# Yield only attribute to signify update
								yield (
									attr,
									update
								)

							else:
								if (update):
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

											# Update timestamp
											self.timestamps[uid] = timestamp

										finally:
											yield (
												attr,
												v
											)

			else:
				raise RFT_Exception("Directory is file")
		else:
			raise RFT_Exception("Directory doesn't exist")


	def iterZip(self, *, onlyUpdated:bool = False) -> tuple[str, object]:
		if (self.path.exists()):
			if (self.path.is_file()):
					with zipfile.ZipFile(self.path, "r") as zfile:
						for file in zfile.infolist():
							if (not file.is_dir()):
								# Get filename
								name = file.filename

								# Create path
								rel = pathlib.Path(name)

								# Get entry
								entry = self.getEntry(rel)

								if (entry is not None):
									# Create attribute for structure
									attr = self.formatAttr(
										rel.parent.as_posix().replace("/", "."),
										rel.stem.replace(".", "_")
									)

									# Get uid
									uid = "-".join(attr).replace(".", "-")

									# Get stat
									stat = datetime.datetime(*file.date_time)
									timestamp = stat.timestamp()
									update = True

									# Check if already loaded and if file was edited after that
									if (self.timestamps.contains(uid)):
										if (self.timestamps[uid] >= timestamp):
											update = False


									if (onlyUpdated):
										# Yield only attribute to signify update
										yield (
											attr,
											update
										)

									else:
										if (update):
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

													# Update timestamp
													self.timestamps[uid] = timestamp

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
	def load(self, struct:RFT_Object = None, *, single:bool = False, errEvent:object = None) -> RFT_Object:
		if (struct is None):
			# Create new structure
			structOut = RFT_Structure(struct)

		else:
			# Assign structure
			structOut = struct


		# Iterate through all content
		for attr, value in self.iter():
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
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~ Get Entry ~~~~~~
	def getEntry(self, path:str) -> RFT_Object:
		path = pathlib.Path(path)
		ext = path.name.split(".")[-1]

		# Iterate through all entries
		for pattern, entry in self.entries.items():
			if (re.fullmatch(pattern, ext, flags = re.IGNORECASE)):
				return entry


	# ~~~~~~ Format Attr ~~~~~
	def formatAttr(self, *text:tuple | list) -> list[str]:
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

