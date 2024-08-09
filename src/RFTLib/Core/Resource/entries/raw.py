from RFTLib.Require import *
from RFTLib.Core.Buffer import *





__all__ = ("Entry",)





class Entry:
	def load(self, file):
		# Allocate buffer
		data = RFT_Buffer()

		# Read entire file
		data += file.read()

		# Return data
		return data


