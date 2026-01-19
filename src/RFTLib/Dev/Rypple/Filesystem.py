from RFTLib.Require import *
from RFTLib.Dev.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *

from RFTLib.Dev.Decorator import *



__all__ = ("RFT_Rypple_Filesystem",)



class RFT_Rypple_Filesystem(RFT_Object):
	def __init__(self, parent):
		self.parent = parent
		self.scope = RFT_Structure({
			"path": pathlib.Path(".")
		})



	@RFT_Decorator.configure()
	def path(self, path:str):
		self.scope.path = pathlib.Path(path)
		return self


	@RFT_Decorator.configure()
	def touch(self):
		self.scope.path.touch()
		return self


	@RFT_Decorator.configure()
	def write(self, buf:RFT_Buffer):
		buf = RFT_Buffer(buf)

		with self.scope.path.open("ab") as file:
			file.write(buf.data)

		return self


	@RFT_Decorator.configure()
	def remove(self):
		if (self.scope.path.is_file()):
			os.remove(self.scope.path)

		return self


	@RFT_Decorator.configure()
	def chdir(self, path:str = None):
		if (path == None):
			path = self.scope.path

		else:
			path = pathlib.Path(path)

		if (path.is_file()):
			path = path.parent

		os.chdir(path)

		return self







