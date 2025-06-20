from RFTLib.Require import *

from .Buffer import *
from .Object import *
from .Structure import *





__all__ = ("RFT_Table",)





class RFT_Table(RFT_Object):
	def __init__(self, path:str):
		self.path = Path(path)

		self.updating = False
		self.running = False
		self.indent = False

		self.thread = None

		self.data = RFT_Structure()
		self.data.assignGetEvent(self.getEvent)
		self.data.assignSetEvent(self.setEvent)

		# Verify path
		self.path.mkdir(
			parents = True,
			exist_ok = True
		)




	# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
	def getEvent(self, attr:str):
		self.wait()

		if (not self.data.contains(attr)):
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



	# ~~~~~~~ File Input/Output ~~~~~~
	# ~~~~~~ Touch File ~~~~~~
	def touchFile(self, attr:str):
		path = self.path / (attr + ".table")

		# Get attr data
		data = self.data.get(attr)

		if (not isinstance(data, RFT_Structure)):
			struct = RFT_Structure({})
			struct.assignGetEvent(self.tableGetEvent)
			struct.assignSetEvent(self.tableSetEvent)
			
			self.data[attr] = struct


		# Allocate new file if needed
		if (not path.exists()):
			with path.open("wb") as file:
				file.write(b"{}")


		return path



	# ~~~~~~~ Read File ~~~~~~
	def readFile(self, attr:str):
		# Touch file
		path = self.touchFile(attr)

		# Start Updating
		self.updating = True

		# Read file data
		with path.open("r") as file:
			try:
				data = json.load(file)
			except:
				data = {}


		# Convert to structure
		struct = RFT_Structure(data)
		struct.assignGetEvent(self.tableGetEvent)
		struct.assignSetEvent(self.tableSetEvent)
		
		# Set value
		self.data[attr] = struct

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
				data_ = data.toDict()

				# Dump json data to file
				json.dump(
					data_,
					file,
					skipkeys = False,
					default = lambda o: None,
					indent = (
						"\t" if (self.indent) else None
					)
				)
			
			except:
				file.write("{}")

		# End Updating
		self.updating = False
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~ File Saving ~~~~~~~~~
	# ~~~~~~~ Save All ~~~~~~~
	def saveAll(self):
		try:
			for k in self.data.keys():
				self.writeFile(k)
		
		except:
			raise RFT_Exception.Traceback()



	# ~~~~~~ Save Every ~~~~~~
	def saveEvery(self, secs:int | float):
		self.running = True

		if (self.thread is not None):
			self.running = False
			self.thread.join()

		self.thread = threading.Thread(
			target = self.saveEvery_,
			args = (secs,),
			kwargs = {},
			daemon = True
		)

		self.thread.start()



	# ~~~~~~~~ Thread ~~~~~~~~
	def saveEvery_(self, secs:int | float):
		while self.running:
			# Delay in seconds
			time.sleep(secs)

			# Save all tables
			self.saveAll()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Safety ~~~~~~~~~~~~
	# ~~~~~~~~~ Wait ~~~~~~~~~
	def wait(self):
		while self.updating:
			time.sleep(0.01)


	# ~~~~~~~~~ Clear ~~~~~~~~
	def clear(self, stop:bool = False):
		self.running = not stop

		for f in self.path.iterdir():
			p = Path(f)
			
			if (p.is_file()):
				os.remove(p)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






