from RFTLib.Require import *





__all__=["call_until"]





def call_until(*,milliseconds=0,seconds=0,minutes=0,hours=0,loopFor=0):

	total=(milliseconds/1000)+(seconds)+(minutes*60)+(hours*(60**2))


	def decorator(func):
		def loop():
			count=0
			while True:
				time.sleep(total)

				if (loopFor>0):
					if (loopFor<=count):
						return

					count+=1

				try:
					func()
				except:
					sys.stderr.write(traceback.format_exc())


		threading._start_new_thread(loop,(),{})


		def wrapper(*args,**kwargs):
			return func(*args,**kwargs)


		return wrapper
	return decorator



