from RFTLib.Require import *
from RFTLib.Core.Object import *
from RFTLib.Core.Decorators.call_until import *





__all__=["RFT_Database_Client"]





class RFT_Database_Client(RFT_Object):
	def __init__(self,port):
		self.port=port




