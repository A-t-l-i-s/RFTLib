from ..Require import *

from ..Core.Buffer import *
from ..Core.Object import *
from ..Core.Parser import *
from ..Core.Structure import *





__all__ = ("RFT_Saves",)





class RFT_Saves(RFT_Object):
	def __init__(self, path:str, ext:str = "sav"):
		self.path = Path(path)
		self.ext = ext

		self.data = RFT_Structure({})
		self.data.assignSetEvent(self.setEvent)

		self.updating = False
		self.autoUpdate = True





	def read(self, name:str):
		path = self.path / (RFT_Parser.verifyPath(name) + f".{self.ext}")



		if (not path.exists()):
			with path.open("wb") as file:
				# Write to file
				file.write(zlib.compress(b"{}"))



		with open(path, "rb") as file:
			data = file.read()

			try:
				buf = RFT_Buffer(data)
				buf = buf.decompress()

				out_ = json.loads(buf.data)
				out = RFT_Structure(out_)

			except:
				out = RFT_Structure({})


			out.assignSetEvent(self.setEvent)
			self.data[name] = out

			return out




	def write(self, name:str):
		path = self.path / (RFT_Parser.verifyPath(name) + f".{self.ext}")


		if (not path.exists()):
			self.read(name)


		with open(path, "ab+") as file:
			try:
				struct = self.data[name]

				buf = RFT_Buffer(struct)
				buf = buf.compress()


				file.truncate(0)
				file.seek(0)


				file.write(buf.data)

			except:
				...




	def autoUpdater(self, secs:int | float):
		def update():
			while self.autoUpdate:
				# Wait for timer
				time.sleep(secs)

				# Set status to updating
				self.updating = True

				for k in self.data.keys():
					self.write(k)

				time.sleep(0.01)
				self.updating = False



		t = threading.Thread(
			target = update,
			daemon = True
		); t.start()




	def wait(self):
		while self.updating:
			time.sleep(0.001)



	def setEvent(self, attr:str):
		self.wait()






