from RFTLib.Require import *
from RFTLib.Core.Structure import *





__all__ = ("Entry",)





class Entry:
	def init(self):
		# Import module
		import tomllib

		self.tomllib = tomllib



	def load(self, path):
		# Read json file
		with path.open("rb") as file:
			try:
				# Read file
				data_ = self.tomllib.load(file)
			
			except:
				print(traceback.format_exc())
				# Default
				data_ = {}

			finally:
				# Convert to struct
				data = RFT_Structure(data_)


		# Return data
		return data


