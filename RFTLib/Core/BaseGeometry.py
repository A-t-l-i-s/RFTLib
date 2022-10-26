from RFTLib.Require import *
from RFTLib.Core.Object import *
from RFTLib.Core.Graphics.Color import *





__all__=["RFT_BaseGeometry"]





class RFT_BaseGeometry(RFT_Object):
	def __init__(self,*args,**kwargs):
		raise NotImplementedError



	def draw(self,canvas:np.ndarray,color:Color):
		raise NotImplementedError



	def update(self,obj:Any):
		raise NotImplementedError



