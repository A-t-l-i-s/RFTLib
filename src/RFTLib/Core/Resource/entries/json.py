from RFTLib.Require import *
from RFTLib.Core.Structure import *





__all__ = ("Entry",)





class Entry:
	def init(self):
		# Import module
		import json

		self.json = json



	def load(self, path):
		# Read json file
		with path.open("rb") as file:
			try:
				# Read file
				data_ = self.json.load(file)
			
			except:
				# Default
				data_ = {}

			finally:
				# Convert to struct
				data = RFT_Structure(data_)


		# Return data
		return data


