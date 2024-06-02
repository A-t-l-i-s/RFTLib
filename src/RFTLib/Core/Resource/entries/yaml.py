from RFTLib.Require import *
from RFTLib.Core.Structure import *





__all__ = ("Entry",)





class Entry:
	def init(self):
		# Import module
		import yaml

		self.yaml = yaml



	def load(self, path):
		# Read json file
		with path.open("rb") as file:
			try:
				# Read file
				data_ = self.yaml.load(
					file,
					Loader = self.yaml.FullLoader
				)

				if (data_ == None):
					data_ = {}
			
			except:
				# Default
				data_ = {}

			finally:
				# Convert to struct
				data = RFT_Structure(data_)


		# Return data
		return data


