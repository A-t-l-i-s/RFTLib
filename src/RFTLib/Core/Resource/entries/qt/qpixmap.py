from RFTLib.Require import *





__all__ = ("Entry",)





class Entry:
	def init(self):
		# Import module
		from PyQt6.QtGui import QPixmap

		self.QPixmap = QPixmap



	def load(self, path):
		# Load image
		try:
			data = self.QPixmap(
				path.resolve().as_posix()
			)
		except:
			data = None


		# Return data
		return data


