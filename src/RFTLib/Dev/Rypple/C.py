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
		self.scope = RFT_Structure({
			"inFile": None,
			"outFile": None,
			
			"isStatic": False,
			"isShared": False,
			"isWindow": False,
			
			"includePath": [],
			"libraryPath": [],
			
			"library": [],
			
			"version": None,
			"bit": None,
			"compression": None,
			
			"define": {},

			"args": [],
			"executable": "gcc",
		})



	@RFT_Decorator.configure()
	def executable(self, path:str):
		self.scope.executable = path
		return self


	@RFT_Decorator.configure()
	def inFile(self, path:str):
		self.scope.inFile = path
		return self

	@RFT_Decorator.configure()
	def outFile(self, path:str):
		self.scope.outFile = path
		return self


	@RFT_Decorator.configure()
	def isStatic(self, value:bool = True):
		self.scope.isStatic = value
		return self

	@RFT_Decorator.configure()
	def isShared(self, value:bool = True):
		self.scope.shared = value
		return self

	@RFT_Decorator.configure()
	def isWindow(self, value:bool = True):
		self.scope.isWindow = value
		return self

	@RFT_Decorator.configure()
	def includePath(self, path:str):
		self.scope.includePath.append(path)
		return self

	@RFT_Decorator.configure()
	def libraryPath(self, path:str):
		self.scope.libraryPath.append(path)
		return self

	@RFT_Decorator.configure()
	def library(self, name:str):
		self.scope.library.append(name)
		return self


	@RFT_Decorator.configure()
	def version(self, value:str):
		self.scope.version = value
		return self

	@RFT_Decorator.configure()
	def bit(self, value:int):
		self.scope.bit = value
		return self

	@RFT_Decorator.configure()
	def compression(self, value:int):
		self.scope.compression = value
		return self


	@RFT_Decorator.configure()
	def define(self, key:str, value:object = None):
		self.scope.define[key] = value
		return self

	@RFT_Decorator.configure()
	def defineRemove(self, key:str):
		if (self.scope.define.contains(key)):
			self.scope.define.pop(key)
		return self


	@RFT_Decorator.configure()
	def args(self, *args:str | tuple | list):
		self.scope.args += args
		return self


	@RFT_Decorator.configure()
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



