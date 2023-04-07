import cv2
import traceback

from pathlib import Path

from .loader import *
from ..Core.Types import *





__all__ = ("RFT_Config_CV2_IMAGE", "RFT_Config_CV2_VIDEO")





class RFT_Config_CV2_IMAGE(RFT_Config_Loader):
	exts = (
		"bmp", "dib",
		"jpeg", "jpg", "jpe", "jp2",
		"png",
		"webp",
		"pbm", "pgm", "ppm", "pxm", "pnm",
		"pfm",
		"sr", "ras",
		"tiff", "tif",
		"exr",
		"hdr", "pic",
	)



	def load(cls,path):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()

		# Read file
		data = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)

		# Return data
		return data







class RFT_Config_CV2_VIDEO(RFT_Config_Loader):
	exts = (
		"mp4",
		"avi",
	)



	def load(cls,path):
		# Convert to pathlib
		path = Path(path)

		# Read file
		data = cv2.VideoCapture(str(path))

		# Return data
		return data

		



