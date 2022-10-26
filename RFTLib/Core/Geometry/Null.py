from RFTLib.Require import *
from RFTLib.Core.BaseGeometry import *
from RFTLib.Core.Graphics.Color import *




__all__=["Null"]





class Null(RFT_BaseGeometry):
	def __init__(cls,*args:Tuple[Any],**kwargs:Dict[str,Any]):
		...



	def __getattr__(self,attr:str):
		return 0



	def draw(self,canvas:np.array,color:Color):
		...

