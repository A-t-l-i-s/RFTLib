from RFTLib.Require import *





__all__ = ("Entry",)





class Entry:
	def init(self):
		# Import module
		from PyQt6.QtGui import QImage, QPixmap

		self.QImage = QImage
		self.QPixmap = QPixmap



	def load(self, file):
		# Read entire file
		data = file.read()

		try:
			# Load as qimage
			img = self.QImage.fromData(data)
			pix = self.QPixmap.fromImage(img)

		except:
			pix = self.QPixmap()

		# Return data
		return pix


