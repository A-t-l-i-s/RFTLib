from ..Require import *

from PyQt6.QtGui import QPixmap, QIcon, QImage

from .loader import *
from ..Core.Types import *
from ..Core.Structure import *





__all__ = ("RFT_Config_QT_PIXMAP", "RFT_Config_QT_IMAGE", "RFT_Config_QT_ICON")





class RFT_Config_QT_PIXMAP(RFT_Config_Loader):
	exts = (
		"bmp",
		"png",
		"gif",
		"jpg", "jpeg",
		"pbm", "pgm", "ppm", "xbm", "xpm",
	)



	def load(cls, path:RFT_Typing.Path):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()


		# Read file
		data = QPixmap(str(path))


		# Return data
		return data





class RFT_Config_QT_IMAGE(RFT_Config_Loader):
	exts = RFT_Config_QT_PIXMAP.exts



	def load(cls, path:RFT_Typing.Path):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()


		# Read file
		data = QImage(str(path))


		# Return data
		return data





class RFT_Config_QT_ICON(RFT_Config_Loader):
	exts = RFT_Config_QT_PIXMAP.exts



	def load(cls, path:RFT_Typing.Path):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()


		# Read file
		data = QIcon(str(path))


		# Return data
		return data
		



