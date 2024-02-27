from RFTLib.Require import *

from . import *





__all__ = ("RFT_Nan",)





class RFT_Nan(RFT_Geometric):
	# ~~~~~~~~~~~ Variables ~~~~~~~~~~
	fields = ()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def __init__(self, *args, **kwargs):
		...

	def __getattr__(self, attr):
		return 0




