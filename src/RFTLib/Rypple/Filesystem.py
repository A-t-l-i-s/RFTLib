from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *





__all__ = ("RFT_Rypple_Filesystem",)





class RFT_Rypple_Filesystem(RFT_Object):
	path_ = Path("file")


	@classmethod
	def path(self, path:str | Path):
		self.path_ = Path(path)

		return self


	@classmethod
	def touch(self):
		self.path_.touch()
		return self


	@classmethod
	def write(self, buf: RFT_Buffer):
		buf = RFT_Buffer(buf)

		with self.path_.open("ab") as file:
			file.write(buf.data)

		return self


	@classmethod
	def remove(self):
		if (self.path_.is_file()):
			os.remove(self.path_)

		return self


	@classmethod
	def isFile(self):
		return self.path_.is_file()

	@classmethod
	def isDir(self):
		return self.path_.is_dir()


	@classmethod
	def chdir(self, path:str | Path = None):
		if (path == None):
			path = self.path_

		else:
			path = Path(path)

		if (path.is_file()):
			path = path.parent

		os.chdir(path)







