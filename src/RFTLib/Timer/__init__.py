from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Structure import *
from RFTLib.Core.Exception import *



__all__ = ("RFT_Timer",)



class RFT_Timer(RFT_Object):
	def __init__(self, timestamp:int | float = None):
		self.timestamp = 0.0

		self.update(timestamp)


	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	# ~~~~~~~ Operators ~~~~~~
	def __add__(self, obj:int | float | RFT_Object) -> RFT_Object:
		if (isinstance(obj, RFT_Timer)):
			self.timestamp += obj.timestamp

		else:
			self.timestamp += obj

		return self

	def __sub__(self, obj:int | float | RFT_Object) -> RFT_Object:
		if (isinstance(obj, RFT_Timer)):
			self.timestamp -= obj.timestamp

		else:
			self.timestamp -= obj
		
		return self

	def __mul__(self, obj:int | float | RFT_Object) -> RFT_Object:
		if (isinstance(obj, RFT_Timer)):
			self.timestamp *= obj.timestamp

		else:
			self.timestamp *= obj

		return self

	def __eq__(self, obj:int | float | RFT_Object) -> bool:
		if (isinstance(obj, RFT_Timer)):
			return obj.timestamp == self.timestamp

		else:
			return obj == self.timestamp


	# ~~~~~~ Converters ~~~~~~
	def __bool__(self) -> bool:
		return self.timestamp > 0.0
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~ Update Timestamp ~~~~~~~
	def update(self, timestamp:int | float = None):
		if (timestamp is None):
			self.timestamp = time.time()

		else:
			if (isinstance(timestamp, int | float)):
				self.timestamp = timestamp

			else:
				raise RFT_Exception.TypeError(type(timestamp))
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~ Retrieve Timestamp ~~~~~~
	def secs(self) -> int | float:
		return time.time() - self.timestamp


	def msecs(self) -> int | float:
		return self.secs() * 1000


	def dif(self, timestamp:int | float) -> int | float:
		return timestamp - self.timestamp
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


