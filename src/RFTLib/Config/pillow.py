from ..Require import *

from PIL import Image

from .loader import *

from ..Core.Structure import *





__all__ = ("RFT_Config_PILLOW",)





class RFT_Config_PILLOW(RFT_Config_Loader):
	exts = (
		"blp", "bmp", "dib",
		"bufr", "cur", "pcx",
		"dcx", "dds", "ps",
		"eps", "fit", "fits",
		"fli", "flc", "ftc",
		"ftu", "gbr", "gif",
		"grib", "h5", "hdf",
		"png", "apng", "jp2",
		"j2k", "jpc", "jpf",
		"jpx", "j2c", "icns",
		"ico", "im", "iim",
		"jfif", "jpe", "jpg",
		"jpeg", "mpg", "mpeg",
		"tif", "tiff", "mpo",
		"msp", "palm", "pcd",
		"pdf", "pxr", "pbm",
		"pgm", "ppm", "pnm",
		"psd", "qoi", "bw",
		"rgb", "rgba", "sgi",
		"ras", "tga", "icb",
		"vda", "vst", "webp",
		"wmf", "emf", "xbm",
		"xpm"
	)



	def import_(cls, path:str):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()


		# Read file
		data = Image.open(path)


		# Return data
		return data

		



