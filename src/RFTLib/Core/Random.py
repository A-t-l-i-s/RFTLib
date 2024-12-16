from RFTLib.Require import *

from .Object import *
from .Buffer import *
from .Exception import *





__all__ = ("RFT_Random",)





class RFT_Random(RFT_Object):
	def __init__(self, seed:int = None):
		self.seed = seed
		self.inst = random.Random(self.seed)


	def range(self, min_:int = 0, max_:int = 1, decimal:int = 0):
		if (decimal > 0):
			return self.inst.randint(
				min_ * (10 ** decimal),
				max_ * (10 ** decimal)
			) / (10 ** decimal)

		else:
			return self.inst.randint(
				min_,
				max_
			)


	def array(self, min_:int = 0, max_:int = 1):
		a = list(range(min_, max_))
		self.shuffle(a)

		return a


	def shuffle(self, array:list):
		self.inst.shuffle(array)


	def bytes(self, n:int = 1):
		return self.inst.randbytes(n)

	def buffer(self, n:int = 1):
		return RFT_Buffer(self.bytes(n))





