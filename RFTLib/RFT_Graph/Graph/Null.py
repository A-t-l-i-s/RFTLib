from ..Require import *
from ..Utils.Color import *

from .BaseGeometry import *




__all__=["Null"]





class Null(BaseGeometry):
	def __new__(cls,*args:Tuple[Any],**kwargs:Dict[str,Any]):
		self=object.__new__(cls)

		return self



	def __getattr__(self,attr:str):
		return 0



	def draw(self,canvas:np.array,color:Color):
		...

