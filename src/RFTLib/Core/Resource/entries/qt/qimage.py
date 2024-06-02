from RFTLib.Require import *





__all__ = ("Entry",)





class Entry:
	def init(self):
		# Import module
		from PyQt6.QtGui import QImage

		self.QImage = QImage



	def load(self, path):
		# Load image
		try:
			data = self.QImage(
				path.resolve().as_posix()
			)
		except:
			data = None


		# Return data
		return data


