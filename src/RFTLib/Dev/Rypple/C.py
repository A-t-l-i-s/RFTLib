from RFTLib.Require import *
from RFTLib.Dev.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *

from RFTLib.Dev.Decorator import *



__all__ = ("RFT_Rypple_C",)



class RFT_Rypple_C(RFT_Object):
	def __init__(self, parent):
		self.parent = parent
		self.scope = RFT_Structure()

		self.scope.inFile:str = None
		self.scope.outFile:str = None

		self.scope.isStatic:bool = False
		self.scope.isShared:bool = False
		self.scope.isWindow:bool = False

		self.scope.includePath:list = []
		self.scope.libraryPath:list = []

		self.scope.library:list = []
		self.scope.version:str = None

		self.scope.bit:int = None
		self.scope.compression:int = None

		self.scope.define:RFT_Structure = RFT_Structure()

		self.scope.args:list = []
		self.scope.executable:str = "gcc"



	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def executable(self, path:str):
		self.scope.executable = path
		return self


	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def inFile(self, path:str):
		self.scope.inFile = path
		return self

	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def outFile(self, path:str):
		self.scope.outFile = path
		return self


	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def isStatic(self, value:bool = True):
		self.scope.isStatic = value
		return self

	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def isShared(self, value:bool = True):
		self.scope.shared = value
		return self

	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def isWindow(self, value:bool = True):
		self.scope.isWindow = value
		return self

	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def includePath(self, path:str):
		self.scope.includePath.append(path)
		return self

	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def libraryPath(self, path:str):
		self.scope.libraryPath.append(path)
		return self

	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def library(self, name:str):
		self.scope.library.append(name)
		return self


	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def version(self, value:str):
		self.scope.version = value
		return self

	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def bit(self, value:int):
		self.scope.bit = value
		return self

	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def compression(self, value:int):
		self.scope.compression = value
		return self


	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def define(self, key:str, value:object = None):
		self.scope.define[key] = value
		return self

	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def defineRemove(self, key:str):
		self.scope.define.pop(key)
		return self


	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def args(self, *args:str | tuple | list):
		self.scope.args += args
		return self


	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def done(self):
		args = [self.scope.executable]


		if (self.scope.inFile):
			args.append(self.scope.inFile)

		if (self.scope.outFile):
			args.append(f"-o{self.scope.outFile}")


		if (self.scope.isStatic):
			args.append("-static")

		if (self.scope.isShared):
			args.append("-shared")

		if (self.scope.isWindow):
			args.append("-mwindows")


		for v in self.scope.includePath:
			args.append(f"-I{v}")

		for v in self.scope.libraryPath:
			args.append(f"-L{v}")

		for v in self.scope.library:
			args.append(f"-l{v}")


		if (self.scope.version):
			args.append(f"--std={self.scope.version}")

		if (self.scope.bit):
			args.append(f"-m{self.scope.bit}")

		if (self.scope.compression):
			args.append(f"-O{self.scope.compression}")


		for k, v in self.scope.define.items():
			if (v is None):
				args.append(f"-D {k}")

			else:
				args.append(f"-D {k}={v}")


		args += self.scope.args


		return self.parent.Process.run(*args)



