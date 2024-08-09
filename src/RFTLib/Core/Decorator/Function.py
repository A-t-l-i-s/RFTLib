from RFTLib.Require import *

from RFTLib.Core.Exception import *





__all__ = ("RFT_RunIn", "RFT_RunEvery", "RFT_RunEveryAfter", "RFT_RunAfter")





# ~~~~~~~~~~~~ Run In ~~~~~~~~~~~~
# Calls the function once after specified timer exceeds
def RFT_RunIn(*, milliseconds = 0, seconds = 0, minutes = 0, hours = 0, args = (), kwargs = {}):
	total = \
			(milliseconds / 1000) +\
			(seconds) +\
			(minutes * 60) +\
			(hours * (60 ** 2))



	def decorator(func):
		def call():
			# Delay
			time.sleep(total)


			# Call function
			try:
				func(*args, **kwargs)
			
			except:
				RFT_Exception.Traceback().print()


		# Start new thread
		threading._start_new_thread(call, (), {})



		def wrapper(*args, **kwargs):
			return func(*args, *kwargs)


		return wrapper
	return decorator





# ~~~~~~~~~~~ Run Every ~~~~~~~~~~
# Calls the function everytime after timer exceeds
def RFT_RunEvery(*, milliseconds = 0, seconds = 0, minutes = 0, hours = 0, loop = 0, args = (), kwargs = {}):
	total = \
			(milliseconds / 1000) +\
			(seconds) +\
			(minutes * 60) +\
			(hours * (60 ** 2))



	def decorator(func):
		func.loops = 0

		def call():
			while True:
				# If loop count exceeds
				if (func.loops >= loop and loop > 0):
					break


				# Delay
				time.sleep(total)


				# Call function
				try:
					func(*args, **kwargs)
				
				except:
					RFT_Exception.Traceback().print()


				# Increment loop count
				if (loop):
					func.loops += 1


		# Start new thread
		threading._start_new_thread(call, (), {})



		def wrapper(*args, **kwargs):
			return func(*args, *kwargs)


		return wrapper
	return decorator





# ~~~~~~~~ Run Every After ~~~~~~~
# Calls the function everytime after timer exceeds since last call
def RFT_RunEveryAfter(*, milliseconds = 0, seconds = 0, minutes = 0, hours = 0, loop = 0, args = (), kwargs = {}):
	total = \
			(milliseconds / 1000) +\
			(seconds) +\
			(minutes * 60) +\
			(hours * (60 ** 2))



	def decorator(func):
		func.loops = 0
		func.lastCall = time.time()

		def call():
			while True:
				# If loop count exceeds
				if (func.loops >= loop and loop > 0):
					break


				# Delay
				time.sleep(total)


				# Get current time
				t = time.time()
				
				if (t - func.lastCall >= total):
					func.lastCall = t

					# Call function
					try:
						func(*args, **kwargs)
					
					except:
						RFT_Exception.Traceback().print()


				# Increment loop count
				if (loop):
					func.loops += 1


		# Start new thread
		threading._start_new_thread(call, (), {})



		def wrapper(*args, **kwargs):
			func.lastCall = time.time()

			return func(*args, *kwargs)


		return wrapper
	return decorator





# ~~~~~~~~~~~ Run After ~~~~~~~~~~
# Only allows function to be called after the last function call
def RFT_RunAfter(*, milliseconds = 0, seconds = 0, minutes = 0, hours = 0):
	total = \
			(milliseconds / 1000) +\
			(seconds) +\
			(minutes * 60) +\
			(hours * (60 ** 2))



	def decorator(func):
		func.lastCall = time.time()

		def wrapper(*args, **kwargs):
			# Get current time
			t = time.time()
			
			if (t - func.lastCall >= total):
				func.lastCall = t
				
				return func(*args, *kwargs)


		return wrapper
	return decorator








