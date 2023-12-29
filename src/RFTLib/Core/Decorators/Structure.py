from ...Require import *
from ..Structure import *





__all__ = ("RFT_ToStructure", "RFT_JoinStructure")





def RFT_ToStructure(obj):
	# Create structure
	struct = RFT_Structure({})
	

	# Iterate through attributes
	for d in dir(obj):
		if (not (d.startswith("__") and d.endswith("__"))):
			struct[d] = getattr(obj, d)


	return struct





class RFT_JoinStructure:
	def __init__(self, struct):
		self.struct = struct


	def __call__(self, obj):
		for k,v in self.struct.items():
			setattr(obj, k, v)

		return obj






