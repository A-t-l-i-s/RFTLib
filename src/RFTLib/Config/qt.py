from ..Require import *

from PyQt6.QtGui import QPixmap, QIcon, QImage

from .loader import *

from ..Core.Structure import *





__all__ = ("RFT_Config_QT_PIXMAP", "RFT_Config_QT_IMAGE", "RFT_Config_QT_ICON", "RFT_Config_QT_QSS")





class RFT_Config_QT_PIXMAP(RFT_Config_Loader):
	exts = (
		"bmp",
		"png",
		"gif",
		"jpg", "jpeg",
		"pbm", "pgm", "ppm", "xbm", "xpm",
		"ico"
	)



	def import_(cls, path:str):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()


		try:
			data = QPixmap(str(path))
		except:
			data = None


		# Return data
		return data





class RFT_Config_QT_IMAGE(RFT_Config_Loader):
	exts = RFT_Config_QT_PIXMAP.exts



	def import_(cls, path:str):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()


		try:
			data = QImage(str(path))
		except:
			data = None


		# Return data
		return data





class RFT_Config_QT_ICON(RFT_Config_Loader):
	exts = RFT_Config_QT_PIXMAP.exts



	def import_(cls, path:str):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()


		try:
			data = QIcon(str(path))
		except:
			data = None


		# Return data
		return data





class RFT_Config_QT_QSS(RFT_Config_Loader):
	exts = ("qss", "css")



	def import_(cls, path:str):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()


		with path.open("r") as file:
			data = file.read()


		# Return data
		return data
		



