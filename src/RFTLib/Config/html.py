from ..Require import *

from .loader import *





__all__ = ("RFT_Config_HTML",)





class RFT_Config_HTML(RFT_Config_Loader):
	exts = ("html", "htm", "php", "css", "js")



	def import_(cls, path:str):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()
		

		# Read file
		with path.open("r") as file:
			data = file.read()


		# Return data
		return data

		



