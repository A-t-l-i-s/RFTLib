from RFTLib.Require import *
from RFTLib.Core.Object import *





__all__=["intFromBytes"]





def intFromBytes(data):
	value=0

	for i,b in enumerate(data):
		value+=(int(b) << (i*8))

	return value




