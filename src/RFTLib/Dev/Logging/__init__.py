from RFTLib.Require import *
from RFTLib.Dev.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Enum import *
from RFTLib.Core.Exception import *
from RFTLib.Core.Structure import *



__all__ = ("RFT_Logging",)



class RFT_Logging(RFT_Object):
	TYPES = RFT_Enum((
		"STREAM",
		"FUNCTION",
		"LOGGER"
	))


	def __init__(self, streams:dict | RFT_Structure = {}):
		self.streams = RFT_Structure()

		# Add streams to instance
		for k, v in streams.items():
			self.add(v, k)



	# ~~~~~~~~ Logging ~~~~~~~
	def logRaw(self, obj:str, uid:str = RFT_Exception.WILDCARD, *, end:str = "\n", forced:bool = False):
		if (self.streams):
			if (uid is RFT_Exception.WILDCARD):
				# If no uid present then recall with all streams available
				for u in self.streams.keys():
					self.logRaw(obj, u)

			else:
				# Get stream wrapped object
				stream = self.streams.get(uid)

				if (stream is not None):
					if (stream.type == RFT_Logging.TYPES.STREAM):
						# ~~~~~~~~~ Write ~~~~~~~~
						if (stream.binary):
							# Write as binary
							stream.obj.write(
								bytearray(obj, stream.encoding) + bytearray(end, stream.encoding)
							)

						else:
							# Write as text
							stream.obj.write(
								str(obj) + str(end)
							)
						# ~~~~~~~~~~~~~~~~~~~~~~~~


					elif (stream.type == RFT_Logging.TYPES.FUNCTION):
						# ~~~ Callback Function ~~
						if (not forced):
							try:
								# Call function
								stream.obj(
									self,
									obj,
									uid
								)

							except Exception as exc:
								# Log function exception but dont call function again
								self.logRaw(
									RFT_Exception(exc, uid).message(),
									uid,
									end = end,
									forced = True
								)
						# ~~~~~~~~~~~~~~~~~~~~~~~~


					elif (stream.type == RFT_Logging.TYPES.LOGGER):
						# ~~~~~~~~ Logger ~~~~~~~~
						stream.obj.logRaw(
							RFT_Exception(obj, uid),
							end = True,
							forced = forced
						)
						# ~~~~~~~~~~~~~~~~~~~~~~~~


					else:
						raise RFT_Exception.TypeError(type(stream.obj))

				else:
					raise RFT_Exception(f"Stream \"{uid}\" doesn't exist", RFT_Exception.ERROR)


	def log(self, obj:str | RFT_Exception, uid:str = RFT_Exception.WILDCARD, *, end:str = "\n"):
		if (self.streams):
			# Log text
			self.logRaw(
				RFT_Exception(obj, uid).message(),
				uid,
				end = end
			)
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~ Management ~~~~~~
	def close(self, uid:str = RFT_Exception.WILDCARD):
		if (uid is RFT_Exception.WILDCARD):
			# If no uid present then recall with all streams available
			for u in self.streams.keys():
				self.close(u)

		else:
			# Get stream wrapped object
			obj = self.streams.pop(uid)

			if (hasattr(obj.stream, "close")):
				obj.stream.close()
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Streams ~~~~~~~
	def add(self, obj:object, uid:str):
		if (isinstance(obj, io.IOBase)):
			self.addStream(obj, uid)

		elif (isinstance(obj, str)):
			self.addFile(obj, uid)

		elif (isinstance(obj, typing.Callable)):
			self.addFunction(obj, uid)

		elif (isinstance(obj, RFT_Logging)):
			self.addLogger(obj, uid)

		else:
			raise RFT_Exception.TypeError(type(obj))


	def addStream(self, stream:object, uid:str):
		if (hasattr(stream, "write") and stream.writable()):
			self.streams[uid] = {
				"obj": stream,
				"encoding": getattr(stream, "encoding", "utf-8"),
				"binary": not isinstance(stream, io.TextIOBase),
				"type": RFT_Logging.TYPES.STREAM
			}

		else:
			raise RFT_Exception.TypeError(type(stream))


	def addFile(self, path:str, uid:str, *, clear:bool = False):
		# Create path object
		path = pathlib.Path(path)

		# Open stream
		stream = path.open("wb" if clear else "ab")

		# Add file to stream list
		self.addStream(
			stream,
			uid
		)


	def addLogFile(self, path:str):
		# Create path object
		path = pathlib.Path(path)

		# Get current datetime
		timestamp = datetime.datetime.now()

		uid = f"{timestamp.month:>02}-{timestamp.day:>02}-{timestamp.year:>04}"
		path /= (uid + ".log")

		self.addFile(
			path,
			uid,
			clear = False
		)


	def addFunction(self, func:object, uid:str):
		self.streams[uid] = {
			"obj": func,
			"encoding": None,
			"binary": None,
			"type": RFT_Logging.TYPES.FUNCTION
		}


	def addLogger(self, obj:RFT_Object, uid:str):
		if (isinstance(obj, RFT_Logging)):
			if (obj is not self):
				self.streams[uid] = {
					"obj": obj,
					"encoding": None,
					"binary": None,
					"type": RFT_Logging.TYPES.LOGGER
				}

			else:
				raise RFT_Exception("Can't add logger due to recursion issues", RFT_Exception.ERROR)
		else:
			raise RFT_Exception.TypeError(type(obj))
	# ~~~~~~~~~~~~~~~~~~~~~~~~


