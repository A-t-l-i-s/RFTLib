from ...Require import *





__all__ = ("RFT_RunIn", "RFT_RunEvery")





def RFT_RunIn(*, milliseconds = 0, seconds = 0, minutes = 0, hours = 0):
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
				func()
			except:
				...


		# Start new thread
		threading._start_new_thread(call, (), {})



		def wrapper(*args, **kwargs):
			return func(*args, *kwargs)


		return wrapper
	return decorator





def RFT_RunEvery(*, milliseconds = 0, seconds = 0, minutes = 0, hours = 0, loop = 0):
	total = \
			(milliseconds / 1000) +\
			(seconds) +\
			(minutes * 60) +\
			(hours * (60 ** 2))



	def decorator(func):
		def call():
			loops = 0

			while True:
				# If loop count exceeds
				if (loops >= loop and loop > 0):
					break


				# Delay
				time.sleep(total)


				# Call function
				try:
					func()
				except:
					...


				# Increment loop count
				loops += 1


		# Start new thread
		threading._start_new_thread(call, (), {})



		def wrapper(*args, **kwargs):
			return func(*args, *kwargs)


		return wrapper
	return decorator








