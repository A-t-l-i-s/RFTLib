from RFTLib.Require import *





__all__ = ("Entry",)





class Entry:
	def init(self):
		# Import module
		from PyQt6.QtGui import QImage, QPixmap, QIcon

		self.QImage = QImage
		self.QPixmap = QPixmap
		self.QIcon = QIcon



	def load(self, file):
		# Read entire file
		data = file.read()

		# Allocate icon
		ico = self.QIcon()

		try:
			# Load as qimage
			img = self.QImage.fromData(data)
			pix = self.QPixmap.fromImage(img)

			# Add pixmap
			ico.addPixmap(pix)

		except:
			...

		# Return data
		return ico


