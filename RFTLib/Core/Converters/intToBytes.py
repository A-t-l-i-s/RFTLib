from RFTLib.Require import *
from RFTLib.Core.Object import *





__all__=["intToBytes"]





def intToBytes(value,size):
	arr=[]

	for i in range(size):
		arr.insert(0,(value >> (((size - 1) - i) * 8)) & 0xff)

	return arr




