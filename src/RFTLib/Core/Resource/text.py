from RFTLib.Require import *
from RFTLib.Core.Buffer import *





__all__ = ("Entry",)





class Entry:
	def load(self, file):
		buf = RFT_Buffer()

		# Read entire file
		buf.read(file, -1)

		return buf.toStr()


