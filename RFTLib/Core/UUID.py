from RFTLib.Require import *
from RFTLib.Core.Object import *





__all__=["RFT_UUID"]





class RFT_UUID(RFT_Object):
	# https://docs.python.org/3/library/uuid.html



	timeLow:int=0
	timeMid:int=0
	timeHigh:int=0
	clockSeqHigh:int=0
	clockSeqLow:int=0
	address:int=0



	def __init__(self,timeLow,timeMid,timeHigh,clockSeqHigh,clockSeqLow,address):
		self.timeLow=timeLow
		self.timeMid=timeMid
		self.timeHigh=timeHigh
		self.clockSeqHigh=clockSeqHigh
		self.clockSeqLow=clockSeqLow
		self.address=address





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





	def __str__(self):
		tl=int.to_bytes(self.timeLow,4,"big").hex()
		tm=int.to_bytes(self.timeMid,2,"big").hex()
		th=int.to_bytes(self.timeHigh,2,"big").hex()

		cqh=int.to_bytes(self.clockSeqHigh,1,"big").hex()
		cql=int.to_bytes(self.clockSeqLow,1,"big").hex()

		ad=int.to_bytes(self.address,6,"big").hex()

		return f"{tl}-{tm}-{th}-{cqh}{cql}-{ad}"

