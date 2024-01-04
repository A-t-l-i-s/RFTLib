from ..Require import *

from ..Core.Buffer import *
from ..Core.Object import *
from ..Core.Parser import *
from ..Core.Structure import *





__all__ = ("RFT_Tables",)





class RFT_Tables(RFT_Object):
	def __init__(self, path:str):
		self.path = Path(path)

		self.updating = False
		self.running = False

		self.data = RFT_Structure({})
		self.data.assignGetEvent(self.getEvent)
		self.data.assignSetEvent(self.setEvent)





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





	def wait(self):
		while self.updating:
			time.sleep(0.001)





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





	def readFile(self, attr:str):
		# Touch file
		path = self.touchFile(attr)

		# Start Updating
		self.updating = True

		# Read file data
		with path.open("rb") as file:
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





	def writeFile(self, attr:str):
		# Touch file
		path = self.touchFile(attr)

		# Gut data
		data = self.data[attr]


		# Start Updating
		self.updating = True

		with path.open("wb") as file:
			try:
				buf = RFT_Buffer(data)

				file.write(buf.data)
			except:
				file.write(b"{}")

		# End Updating
		self.updating = False





	def saveAll(self):
		for k in self.data.keys():
			self.writeFile(k)





	def saveEvery(self, secs):
		def call():
			while self.running:
				# Save all tables
				self.saveAll()

				# Delay in seconds
				time.sleep(secs)


		self.running = True
		threading._start_new_thread(call, (), {})







