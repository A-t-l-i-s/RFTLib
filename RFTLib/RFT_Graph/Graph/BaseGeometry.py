from ..Require import *
from ..Utils.Color import *





__all__=["BaseGeometry"]





class BaseGeometry:
	def __new__(cls,*args,**kwargs):
		raise NotImplementedError



	def draw(self,canvas:np.ndarray,color:Color):
		raise NotImplementedError



	def update(self,obj:Any):
		raise NotImplementedError



