from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Structure import *
from RFTLib.Core.Exception import *



__all__ = ("RFT_Timer",)



class RFT_Timer(RFT_Object):
	def __init__(self, timestamp:int | float | RFT_Object = None):
		self.timestamp = 0.0

		self.update(timestamp)


	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	# ~~~~~~~ Operators ~~~~~~
	def __add__(self, obj:int | float | RFT_Object) -> RFT_Object:
		self.timestamp += float(obj)
		return self

	def __sub__(self, obj:int | float | RFT_Object) -> RFT_Object:
		self.timestamp -= float(obj)
		return self

	def __mul__(self, obj:int | float | RFT_Object) -> RFT_Object:
		self.timestamp *= float(obj)
		return self

	def __truediv__(self, obj:int | float | RFT_Object) -> RFT_Object:
		self.timestamp /= float(obj)
		return self

	def __floordiv__(self, obj:int | float | RFT_Object) -> RFT_Object:
		self.timestamp //= float(obj)
		return self


	# ~~~~~~ Conditions ~~~~~~
	def __eq__(self, obj:int | float | RFT_Object) -> bool:
		return float(obj) == self.timestamp

	def __lt__(self, obj:int | float | RFT_Object) -> bool:
		return float(obj) > self.timestamp

	def __le__(self, obj:int | float | RFT_Object) -> bool:
		return float(obj) >= self.timestamp

	def __gt__(self, obj:int | float | RFT_Object) -> bool:
		return float(obj) < self.timestamp

	def __ge__(self, obj:int | float | RFT_Object) -> bool:
		return float(obj) <= self.timestamp


	# ~~~~~~ Converters ~~~~~~
	def __int__(self) -> int:
		return int(self.timestamp)

	def __float__(self) -> float:
		return float(self.timestamp)

	def __complex__(self) -> complex:
		return complex(self.timestamp)

	def __bool__(self) -> bool:
		return self.timestamp > 0.0
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~ Normalize ~~~~~~~~~~
	def normalize(self) -> float:
		return self.timestamp
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~ Update Timestamp ~~~~~~~
	def update(self, timestamp:int | float | RFT_Object = None):
		if (timestamp is None):
			self.timestamp = time.time()

		else:
			if (isinstance(timestamp, int | float | RFT_Object)):
				self.timestamp = float(timestamp)

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


	# ~~~~~~~~~~~ Add Time ~~~~~~~~~~~
	def addMSecs(self, n:int | float | RFT_Object):
		return self + (n / 1000)

	def addSecs(self, n:int | float | RFT_Object):
		return self + n

	def addMins(self, n:int | float | RFT_Object):
		return self + (n * 60)

	def addHours(self, n:int | float | RFT_Object):
		return self + (n * 60 * 60)

	def addDays(self, n:int | float | RFT_Object):
		return self + (n * 60 * 60 * 24)

	def addWeeks(self, n:int | float | RFT_Object):
		return self + (n * 60 * 60 * 24 * 7)

	def addMonths(self, n:int | float | RFT_Object):
		return self + (n * 60 * 60 * 24 * 30)

	def addYears(self, n:int | float | RFT_Object):
		return self + (n * 60 * 60 * 24 * 365)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


