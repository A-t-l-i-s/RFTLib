from RFTLib.Require import *
from RFTLib.Dev.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *

from RFTLib.Dev.Decorator import *



__all__ = ("RFT_Rypple_Python",)




class RFT_Rypple_Python(RFT_Object):
	def __init__(self, parent):
		self.parent = parent
		self.scope = RFT_Structure()

		self.scope.file:str = None

		self.scope.bytecode:bool = False
		self.scope.buffered:bool = False

		self.scope.args:list = []
		self.scope.executable:str = "python"



	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def executable(self, path:str):
		self.scope.executable = path
		return self


	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def file(self, file:str):
		self.scope.file = file
		return self


	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def bytecode(self, value:bool = True):
		self.scope.bytecode = value
		return self

	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def buffered(self, value:bool = True):
		self.scope.buffered = value
		return self


	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def args(self, *args:str | tuple | list):
		self.scope.args += args
		return self


	@RFT_Decorator.configure(static = True, eventsMax = 30)
	def done(self):
		args = [self.scope.executable]

		if (not self.scope.bytecode):
			args.append("-B")

		if (not self.scope.buffered):
			args.append("-u")

		if (self.scope.file):
			args.append(self.scope.file)


		args += self.scope.args


		return self.parent.Process.run(*args)

