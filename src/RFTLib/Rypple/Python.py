from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *





__all__ = ("RFT_Rypple_Python",)






class RFT_Rypple_Python(RFT_Object):
	file_:str = None
	bytecode_:bool = False
	buffered_:bool = False

	args_:list = []

	if (sys.platform == "win32"):
		exe_:str = "py"

	else:
		exe_:str = "python3"



	@classmethod
	def file(self, file:str):
		self.file_ = file
		return self


	@classmethod
	def bytecode(self, value:bool = True):
		self.bytecode_ = value
		return self

	@classmethod
	def buffered(self, value:bool = True):
		self.buffered_ = value
		return self


	@classmethod
	def add(self, name:str):
		self.args_.append(name)
		return self


	@classmethod
	def args(self):
		args = [self.exe_]

		if (not self.bytecode_):
			args.append("-B")

		if (not self.buffered_):
			args.append("-u")

		if (self.file_):
			args.append(self.file_)

		return args + self.args_


	@classmethod
	def done(self):
		return self.scope.run(
			*self.args()
		)


