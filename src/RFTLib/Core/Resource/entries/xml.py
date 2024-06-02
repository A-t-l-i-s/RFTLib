from RFTLib.Require import *
from RFTLib.Core.Structure import *





__all__ = ("Entry",)





class Entry:
	def init(self):
		# Import module
		import xml.etree.ElementTree as ET

		self.ET = ET



	def load(self, path):
		# Create soup object
		data = self.ET.parse(path)

		root = data.getroot()


		# Return data
		return root


