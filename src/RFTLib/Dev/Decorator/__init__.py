from RFTLib.Require import *
from RFTLib.Dev.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Exception import *
from RFTLib.Core.Structure import *
from RFTLib.Core.Enum import *

from RFTLib.Dev.Logging import *



__all__ = ("RFT_Decorator",)



class RFT_Decorator(RFT_Object):
	def __init__(self, func:object, *, log:bool = False, logBefore:bool = False, logStreams:dict | RFT_Structure = {}, ignore:bool = False, static:bool = False, eventsMax:int = -1):
		self.inst = None
		self.func = func
		self.events = []
		self.eventsLen = 0

		self.log = log
		self.logBefore = logBefore
		self.ignore = ignore
		self.static = static
		self.eventsMax = eventsMax

		self.logger = RFT_Logging(logStreams)

		self.__name__ = func.__name__


	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	# ~~~~~~~ Operators ~~~~~~
	def __eq__(self, obj:object) -> bool:
		return obj == self.func


	# ~~~~~~ Converters ~~~~~~
	def __bool__(self) -> bool:
		return len(self.events) > 0

	def __str__(self, **kwargs:dict) -> str:
		o = RFT_Object()
		o.func = self.func
		o.events = self.events
		o.eventsLen = self.eventsLen

		o.log = self.log
		o.logBefore = self.logBefore
		o.ignore = self.ignore
		o.static = self.static
		o.eventsMax = self.eventsMax

		o.logger = self.logger

		return o.__str__(
			**kwargs
		)

	def __repr__(self) -> str:
		return self.__str__()

	def __format__(self, fmt:str) -> str:
		return self.__str__()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~ Configure ~~~~~~~~~~
	"""
		Call whenever you need to change keyword arguments when used as a property

		@RFT_Decorator.configure(log = True, logBefore = True, static = True)
	"""
	@classmethod
	def configure(self, **kwargs:dict) -> object:
		def wrapper(func:object):
			return self(func, **kwargs)

		return wrapper
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~ Get Instance Owner ~~~~~~
	def __get__(self, instance:object, owner:object = None) -> RFT_Object:
		# Static Class Method
		if (self.static):
			self.inst = owner

		# Class Method
		if (instance is not None):
			self.inst = instance

		return self
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Call Function ~~~~~~~~
	def __call__(self, *args:tuple, **kwargs:dict) -> object:
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


		# If function is static add instance to first argument
		if (self.inst is not None):
			args = (
				self.inst,
				*args
			)


		# If function should log that it's about to be called
		if (self.logBefore):
			o = RFT_Object()
			o.__dict__["start"] = event.start
			o.__dict__["args"] = event.args
			o.__dict__["kwargs"] = event.kwargs

			self.logger.log(
				RFT_Exception(
					str(o),
					o.__str_function__(self.func)
				)
			)


		try:
			# Call function
			v = self.func(
				*args,
				**kwargs
			)

		except:
			# Update error and end time
			event.error = RFT_Exception.Traceback()

		else:
			# Update returned value and end time
			event.returned = v

		finally:
			event.end = time.time()

			if (self.log):
				o = RFT_Object()

				if (not self.logBefore):
					o.__dict__["args"] = event.args
					o.__dict__["kwargs"] = event.kwargs

				o.__dict__["start"] = event.start
				o.__dict__["end"] = event.end
				o.__dict__["error"] = event.error
				o.__dict__["returned"] = event.returned
				o.__dict__["took"] = f"{(event.end - event.start) * 1000:.2f}ms"

				# Log after function is called and everything is settled
				self.logger.log(
					RFT_Exception(
						str(o),
						o.__str_function__(self.func)
					)
				)


		if (event.error is not None):
			if (not self.ignore):
				# Raise error like usual
				raise event.error

		else:
			# Return value
			return event.returned
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



