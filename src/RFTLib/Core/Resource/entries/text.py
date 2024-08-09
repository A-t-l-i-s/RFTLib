from RFTLib.Require import *





__all__ = ("Entry",)





class Entry:
	def load(self, file):
		# Read entire file
		data = file.read()

		# Convert to utf-8
		dataStr = str(data, "utf-8")

		return dataStr


