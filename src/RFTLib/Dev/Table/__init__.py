from RFTLib.Require import *
from RFTLib.Dev.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Exception import *
from RFTLib.Core.Structure import *

from RFTLib.Dev.Logging import *
from RFTLib.Dev.Decorator import *



__all__ = ("RFT_Table",)



class RFT_Table(RFT_Object):
	def __init__(self, path:str, struct:dict | RFT_Object = None, *, default:str | bytes | dict | RFT_Object = {}, indent:bool = False):
		self.path = pathlib.Path(path)

		self.updating = False
		self.running = False
		self.indent = indent
		self.thread = None

		self.logger = RFT_Logging()

		# Allocate data
		self.data = RFT_Structure(
			struct,
			getEvent = self.getEvent,
			setEvent = self.setEvent
		)

		# Set default buffer
		self.default = RFT_Buffer(default)


		# Check if path is a file
		if (self.path.is_file()):
			raise RFT_Exception("Directory is file")

		else:
			# Verify integrity of path
			self.path.mkdir(
				parents = True,
				exist_ok = True
			)


	# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
	def getEvent(self, attr:str):
		self.wait()

		if (attr not in self.data):
	 		self.readFile(attr)
	
		return True

	def setEvent(self, attr:str):
		return True


	def tableGetEvent(self, attr:str):
		self.wait()
		return True

	def tableSetEvent(self, attr:str):
		self.wait()
		return True
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Wait ~~~~~~~~~
	def wait(self):
		while self.updating:
			time.sleep(0.01)


	# ~~~~~~~ File Input/Output ~~~~~~
	# ~~~~~~ Touch File ~~~~~~
	@RFT_Decorator.configure(eventsMax = 120)
	def touchFile(self, attr:str):
		path = self.path / (attr + ".table")

		# Allocate new structure if needed
		if (not self.data.containsInst(RFT_Structure, attr)):
			struct = RFT_Structure()
			
			self.data[attr] = struct


		# Allocate new file if needed
		if (not path.exists()):
			with path.open("wb") as file:
				file.write(self.default.data)

			# Log file creation
			self.logger.log(
				RFT_Exception(
					f"Created \"{path.as_posix()}\"",
					attr
				)
			)

		return path


	# ~~~~~~~ Read File ~~~~~~
	@RFT_Decorator.configure(eventsMax = 120)
	def readFile(self, attr:str):
		# Touch file
		path = self.touchFile(attr)

		# Start Updating
		self.updating = True

		with RFT_Structure() as struct:
			with RFT_Buffer() as buf:
				# Read file data
				with path.open("r") as file:
					buf.readFile(file)
					
					try:
						struct *= json.loads(buf.data)

					except:
						# Backup file
						with path.with_suffix(".error").open("wb") as errFile:
							errFile.write(buf.data)


						# Log reading error
						self.logger.log(
							RFT_Exception.Traceback(
								attr
							)
						)

					else:
						# Log file reading
						self.logger.log(
							RFT_Exception(
								f"Loaded \"{path.as_posix()}\"",
								attr
							)
						)

					finally:
						self.data[attr] = struct

		# End Updating
		self.updating = False


	# ~~~~~~ Write File ~~~~~~
	@RFT_Decorator.configure(eventsMax = 120)
	def writeFile(self, attr:str):
		# Touch file
		path = self.touchFile(attr)

		# Get structure
		struct = self.data[attr]

		# Start Updating
		self.updating = True

		with path.open("wb") as file:
			try:
				# Dump json data to file
				file.write(
					json.dumps(
						struct.toDict(), # Convert to python dict
						skipkeys = False,
						default = lambda o: None,
						indent = (
							"\t" if (self.indent) else None
						)
					).encode("utf-8")
				)
			
			except:
				file.write(self.default.data)

				# Log writing error
				self.logger.log(
					RFT_Exception.Traceback(
						attr
					)
				)

			else:
				# Log successful write
				self.logger.log(
					RFT_Exception(
						f"Saved \"{path.as_posix()}\"",
						attr
					)
				)

		# End Updating
		self.updating = False
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~ File Saving ~~~~~~~~~
	# ~~~~~~~ Save All ~~~~~~~
	@RFT_Decorator.configure(eventsMax = 10)
	def saveAll(self):
		for k in self.data.keys():
			self.writeFile(k)


	# ~~~~~~ Save Every ~~~~~~
	@RFT_Decorator.configure(eventsMax = 10)
	def saveEvery(self, secs:int | float):
		# If thread is already running then wait for it to exit
		if (self.thread is not None):
			self.running = False
			self.thread.join()

		# Create new thread
		self.thread = threading.Thread(
			target = self.saveEvery_,
			args = (secs,),
			kwargs = {},
			daemon = True
		)

		# Start thread
		self.thread.start()

	# ~~~~~~~~ Thread ~~~~~~~~
	@RFT_Decorator.configure(eventsMax = 10)
	def saveEvery_(self, secs:int | float):
		# Reset running flag
		self.running = True

		while self.running:
			# Delay in seconds
			time.sleep(secs)

			# Save all tables
			self.saveAll()
	# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


