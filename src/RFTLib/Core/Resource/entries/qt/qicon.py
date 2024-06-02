from RFTLib.Require import *





__all__ = ("Entry",)





class Entry:
	def init(self):
		# Import module
		from PyQt6.QtGui import QIcon

		self.QIcon = QIcon



	def load(self, path):
		# Load image
		try:
			data = self.QIcon(
				path.resolve().as_posix()
			)
		except:
			data = None


		# Return data
		return data


