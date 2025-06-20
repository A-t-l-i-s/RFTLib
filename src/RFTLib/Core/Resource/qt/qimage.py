from RFTLib.Require import *
from RFTLib.Core.Exception import *





__all__ = ("Entry",)





class Entry:
	def init(self):
		# Import module
		from PyQt6.QtGui import QImage

		self.QImage = QImage



	def load(self, file):
		# Read entire file
		data = file.read()

		# Load as qimage
		img = self.QImage.fromData(data)

		# Return data
		return img


