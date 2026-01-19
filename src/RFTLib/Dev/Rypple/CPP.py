from RFTLib.Require import *
from RFTLib.Dev.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *

from RFTLib.Dev.Decorator import *

from .C import *



__all__ = ("RFT_Rypple_CPP",)



class RFT_Rypple_CPP(RFT_Object):
	def __init__(self, parent):
		self.parent = parent
		self.scope = self.parent.C.scope

		self.parent.C.executable("g++")

		self.executable = self.parent.C.executable
		self.inFile = self.parent.C.inFile
		self.outFile = self.parent.C.outFile
		self.isStatic = self.parent.C.isStatic
		self.isShared = self.parent.C.isShared
		self.isWindow = self.parent.C.isWindow
		self.includePath = self.parent.C.includePath
		self.libraryPath = self.parent.C.libraryPath
		self.library = self.parent.C.library
		self.version = self.parent.C.version
		self.bit = self.parent.C.bit
		self.compression = self.parent.C.compression
		self.define = self.parent.C.define
		self.defineRemove = self.parent.C.defineRemove
		self.args = self.parent.C.args



	@RFT_Decorator.configure()
	def done(self):
		return self.parent.C.done()


