from RFTLib.Require import *





__all__ = ("Entry",)





class Entry:
	def init(self):
		# Import module
		from PyQt6.QtGui import QImage

		self.QImage = QImage



	def load(self, file):
		# Read entire file
		data = file.read()

		try:
			# Load as qimage
			img = self.QImage.fromData(data)

		except:
			img = self.QImage()

		# Return data
		return img


