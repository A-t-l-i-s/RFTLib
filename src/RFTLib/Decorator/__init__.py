from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Exception import *
from RFTLib.Core.Structure import *



__all__ = ("RFT_Decorator",)



class RFT_Decorator(RFT_Object):
	def __init__(self, func:object):
		self.inst = None
		self.func = None
		self.events = []


		if (isinstance(func, classmethod)):
			self.inst = func.__func__

		else:
			self.func = func
		


	def __get__(self, instance, owner = None):
		if (self.inst is not None):
			self.func = classmethod(self.inst).__get__(instance, owner)

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
		o.inst = self.inst
		o.func = self.func
		o.events = self.events

		return o.__str__(
			showMagic = showMagic,
			indent = indent,
			found = found,
			ignore = dir(RFT_Object) + ignore
		)



