from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Exception import *
from RFTLib.Core.Structure import *



__all__ = ("RFT_Table",)



class RFT_Table(RFT_Object):
	def __init__(self, path:str, struct:dict | RFT_Object = None, *, default:str | bytes | dict | RFT_Object = {}, indent:bool = False):
		self.path = pathlib.Path(path)

		self.updating = False
		self.running = False
		self.indent = indent
		self.thread = None

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


	# ~~~~~~~~~~ RFT Methods ~~~~~~~~~
	def __rft_clear__(self):
		self.data.clear()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
	def touchFile(self, attr:str):
		path = self.path / (attr + ".table")

		# Allocate new structure if needed
		if (not self.data.containsInst(attr, RFT_Structure)):
			struct = RFT_Structure(
				getEvent = self.tableGetEvent,
				setEvent = self.tableSetEvent
			)
			
			self.data[attr] = struct


		# Allocate new file if needed
		if (not path.exists()):
			with path.open("wb") as file:
				self.default.write(file)

		return path

	# ~~~~~~~ Read File ~~~~~~
	def readFile(self, attr:str):
		# Touch file
		path = self.touchFile(attr)

		# Start Updating
		self.updating = True

		with RFT_Buffer() as buf:
			# Read file data
			with path.open("r") as file:
				buf.read(file)

				try:
					data = RFT_Structure(
						buf,
						getEvent = self.tableGetEvent,
						setEvent = self.tableSetEvent
					)

				except:
					data = {}

					# Backup file
					with path.with_suffix(".error").open("wb") as errFile:
						buf.write(errFile)

				finally:
					self.data[attr] = data

		# End Updating
		self.updating = False

	# ~~~~~~ Write File ~~~~~~
	def writeFile(self, attr:str):
		# Touch file
		path = self.touchFile(attr)

		# Get data
		data = self.data[attr]


		# Start Updating
		self.updating = True

		with path.open("w") as file:
			try:
				# Convert to python dict
				dataOut = data.normalize()

				# Dump json data to file
				json.dump(
					dataOut,
					file,
					skipkeys = False,
					default = lambda o: None,
					indent = (
						"\t" if (self.indent) else None
					)
				)
			
			except:
				file.write(self.default)

		# End Updating
		self.updating = False
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~ File Saving ~~~~~~~~~
	# ~~~~~~~ Save All ~~~~~~~
	def saveAll(self):
		for k in self.data.keys():
			self.writeFile(k)


	# ~~~~~~ Save Every ~~~~~~
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
	def saveEvery_(self, secs:int | float):
		# Reset running flag
		self.running = True

		while self.running:
			# Delay in seconds
			time.sleep(secs)

			# Save all tables
			self.saveAll()
	# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


