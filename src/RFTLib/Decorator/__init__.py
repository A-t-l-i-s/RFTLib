from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Exception import *
from RFTLib.Core.Structure import *



__all__ = ("RFT_Decorator",)



class RFT_Decorator(RFT_Object):
	def __init__(self, func:object, *, nested:bool = False):
		self.inst = None
		self.func = func
		self.nested = nested
		self.events = []



	@classmethod
	def nested(self, func:object):
		return self(func, nested = True)



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

			return v



	def __str__(self, *, showMagic:bool = False, indent:int = 0, found:list = [], ignore:list = []) -> str:
		o = RFT_Object()
		o.func = self.func
		o.nested = self.nested
		o.events = self.events

		return o.__str__(
			showMagic = showMagic,
			indent = indent,
			found = found,
			ignore = dir(RFT_Object) + ignore
		)



