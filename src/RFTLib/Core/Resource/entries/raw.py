from RFTLib.Require import *
from RFTLib.Core.Buffer import *





__all__ = ("Entry",)





class Entry:
	def load(self, path):
		# Read json file
		with path.open("rb") as file:
			data = RFT_Buffer()

			# Read file in chunks
			while True:
				c = file.read(1024)

				# If not eof
				if (c):
					data += c
				else:
					break


		# Return data
		return data


