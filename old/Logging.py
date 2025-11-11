from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Exception import *
from RFTLib.Core.Structure import *



__all__ = ("RFT_Logging",)



class RFT_Logging(RFT_Object):
	def __init__(self):
		self.streams = RFT_Structure()



	# ~~~~~~~~ Logging ~~~~~~~
	def logRaw(self, text:str | RFT_Object, category:str = "default"):
		streams = self.getCategory(category)
		buffer = RFT_Buffer(text)

		for k, v in streams.items():
			# Grab stream object
			s = v.stream

			# Create context that ignores any exceptions
			with buffer.context(ignore = True) as buf:
				if (v.binary):
					s.write(buf.data)

				else:
					s.write(buf.toStr())


	def log(self, text:str, category:str = "default"):
		if (isinstance(text, RFT_Exception)):
			# Combine cetegory and exception level
			categoryN = f"{category} | {text.level}"

		else:
			# Normalize category
			categoryN = "_".join(self.streams.formatAttr(category))


		# Get current datetime
		timestamp = datetime.datetime.now()

		self.logRaw(
			f"[{timestamp.hour:>2}:{timestamp.minute:>2}:{str(timestamp.second) + '.' + str(timestamp.microsecond)[:4]:<7}]({categoryN}): {str(text)}\n",
			category
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~ Management ~~~~~~
	def close(self, category:str = "default"):
		streams = self.getCategory(category)

		for k, v in streams.items():
			s = v.stream

			if (hasattr(s, "close")):
				s.close()


	def clear(self, category:str = "default"):
		streams = self.getCategory(category)

		# Clear category
		streams.clear()


	def getCategory(self, category:str) -> RFT_Object:
		category = "_".join(self.streams.formatAttr(category))

		if ((streams := self.streams.get(category)) is not None):
			return streams

		else:
			raise RFT_Exception("Category doesn't exist", RFT_Exception.ERROR)
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Streams ~~~~~~~
	def addStream(self, uid:str, stream:object, category:str = "default"):
		uid = "_".join(self.streams.formatAttr(uid))
		category = "_".join(self.streams.formatAttr(category))

		if (hasattr(stream, "mode") and hasattr(stream, "write")):
			m = stream.mode.lower()

			parent, key = self.streams.parent(category, allocate = True, child = True)

			if ("w" in m or "a" in m):

				parent[key][uid] = {
					"stream": stream,
					"binary": "b" in m
				}

			else:
				raise RFT_Exception("Stream isn't writable", RFT_Exception.ERROR)
		else:
			raise RFT_Exception.TypeError(type(stream))


	def addFile(self, uid:str, path:str, category:str = "default", *, clear:bool = False):
		path = pathlib.Path(path)

		if (clear):
			# Open and clear file
			stream = path.open("wb")

		else:
			# Open and append file
			stream = path.open("ab")

		# Add file to stream list
		self.addStream(
			uid,
			stream,
			category
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~


