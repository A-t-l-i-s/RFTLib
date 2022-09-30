from RFTLib.Require import *





__all__=["RFT_Object"]





class RFT_Object(object):
	def __new__(cls,*args,**kwargs):
		self=object.__new__(cls)

		self.__created__=time.time()
		
		return self



