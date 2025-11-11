from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Exception import *
from RFTLib.Core.Structure import *



__all__ = ("RFT_Decorator",)



class RFT_Decorator(RFT_Object):
	def __init__(self, func:object, *, log:bool = False, nested:bool = False, eventsMax:int = -1):
		self.inst = None
		self.func = func
		self.events = []
		self.eventsLen = 0

		self.log = log
		self.nested = nested
		self.eventsMax = eventsMax



	@classmethod
	def configure(self, **kwargs:dict):
		def wrapper(func:object):
			return self(func, **kwargs)

		return wrapper



	def __get__(self, instance, owner = None):
		if (self.nested):
			self.inst = owner

		return self



	def __call__(self, *args, **kwargs):
		# Create new event
		event = RFT_Structure({
			"start": 0.0,
			"end": 0.0,
			"error": None,
			"returned": None,
			"args": args,
			"kwargs": kwargs
		})

		# Add to events list
		self.events.append(event)
		self.eventsLen += 1

		# Manage limited logs
		if (self.eventsMax > -1):
			if (self.eventsLen > self.eventsMax):
				self.events.pop(0)
				self.eventsLen -= 1


		# Update start time
		event.start = time.time()

		try:
			if (self.nested):
				# Call function
				v = self.func(
					self.inst,
					*args,
					**kwargs
				)

			else:
				# Call function
				v = self.func(
					*args,
					**kwargs
				)


		except Exception as exc:
			# Update error and end time
			event.error = exc
			event.end = time.time()

			# Raise error like usual
			raise exc

		else:
			# Update returned value and end time
			event.returned = v
			event.end = time.time()

			if (self.log):
				RFT_Exception(f"{self.func.__name__} -> {v} ({(event.end - event.start) * 1000:.2f}ms)", RFT_Exception.INFO).print()

			return v



	def __str__(self, *, showMagic:bool = False, indent:int = 0, found:list = [], ignore:list = []) -> str:
		o = RFT_Object()
		o.func = self.func
		o.events = self.events
		o.eventsLen = self.eventsLen

		o.nested = self.nested
		o.eventsMax = self.eventsMax

		return o.__str__(
			showMagic = showMagic,
			indent = indent,
			found = found,
			ignore = dir(RFT_Object) + ignore
		)



