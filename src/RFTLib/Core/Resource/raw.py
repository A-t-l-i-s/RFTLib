from RFTLib.Require import *
from RFTLib.Core.Buffer import *





__all__ = ("Entry",)





class Entry:
	def load(self, file):
		# Allocate buffer
		buf = RFT_Buffer()

		# Read entire file
		buf.read(file)

		# Return data
		return buf


