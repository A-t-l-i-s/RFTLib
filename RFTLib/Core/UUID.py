from RFTLib.Require import *
from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *





__all__=["RFT_UUID"]





class RFT_UUID(RFT_Object):
	# https://docs.python.org/3/library/uuid.html



	timeLow:int=0
	timeMid:int=0
	timeHigh:int=0
	clockSeqHigh:int=0
	clockSeqLow:int=0
	address:int=0



	# ~~~~~~~~~~~~~ Init ~~~~~~~~~~~~~
	def __init__(self,timeLow,timeMid,timeHigh,clockSeqHigh,clockSeqLow,address):
		self.timeLow=timeLow
		self.timeMid=timeMid
		self.timeHigh=timeHigh
		self.clockSeqHigh=clockSeqHigh
		self.clockSeqLow=clockSeqLow
		self.address=address
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~ Functions ~~~~~~~~~~
	def create(address=None):
		temp=uuid.uuid1(address)

		new=RFT_UUID(
			temp.time_low,
			temp.time_mid,
			temp.time_hi_version,
			temp.clock_seq_hi_variant,
			temp.clock_seq_low,
			temp.node
		)

		return new
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




	# ~~~~~~~~ Representation ~~~~~~~~
	def __repr__(self)->repr:
		return repr(self.__str__())



	def __str__(self):
		tl=RFT_Buffer.intToHex(self.timeLow,4)
		tm=RFT_Buffer.intToHex(self.timeMid,2)
		th=RFT_Buffer.intToHex(self.timeHigh,2)

		cqh=RFT_Buffer.intToHex(self.clockSeqHigh,1)
		cql=RFT_Buffer.intToHex(self.clockSeqLow,1)

		ad=RFT_Buffer.intToHex(self.address,6)

		return f"{tl}-{tm}-{th}-{cqh}{cql}-{ad}"
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

