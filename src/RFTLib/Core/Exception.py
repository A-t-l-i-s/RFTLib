from RFTLib.Require import *





__all__ = ("RFT_Exception",)





class RFT_Exception(BaseException):
	# ~~~~~~~~~~~ Variables ~~~~~~~~~~
	INFO:int = 					0
	WARNING:int = 				1
	ERROR:int = 				2
	CRITICAL:int = 				3

	# Alert Status Types
	ALERT_OK:int = 				0
	ALERT_CANCEL:int = 			1

	ALERT_YES:int = 			2
	ALERT_NO:int = 				3

	ALERT_IGNORE:int = 			4
	ALERT_ABORT:int = 			5
	ALERT_RETRY:int = 			6

	# Alert Window Types
	ALERT_WINDOW_OK:int = 		0
	ALERT_WINDOW_INPUT:int = 	1
	ALERT_WINDOW_CANCEL:int =	2
	ALERT_WINDOW_RETRY:int =	3
	ALERT_WINDOW_SCRIPT:int = 	4
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def __init__(self,
			text = "",
			level = INFO
		):

		self.text = str(text)
		self.level = level



	# ~~~~~~~~~~~~ Message ~~~~~~~~~~~
	def message(self, *, extra:bool = True):
		# Get current datetime
		timestamp = datetime.datetime.now()


		# No threat
		if (self.level <= self.INFO):
			type_ = "Info"


		# Be aware
		elif (self.level == self.WARNING):
			type_ = "Warning"


		# Is a problem
		elif (self.level == self.ERROR):
			type_ = "Error"


		# Panic everything is wrong! (Critical)
		else:
			type_ = "Critical"



		# Add extra info to msg
		if (extra):
			msg = f"[{timestamp.hour:>2}:{timestamp.minute:>2}:{str(timestamp.second) + '.' + str(timestamp.microsecond)[:4]:<7}]({type_}): {self.text}"

		else:
			# Set msg to text
			msg = self.text


		return msg
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~~ Print ~~~~~~~~~~~~
	def print(self, *, end = "\n"):
		print(self.message(), end = end)
		
		return self

	def printErr(self, *, end = "\n"):
		print(self.message(), end = end, file = sys.stderr)
		
		return self


	def __str__(self):
		return self.message()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~~ Alert ~~~~~~~~~~~~
	def alert(self, title:str = "RFT_Exception", type:int = ALERT_WINDOW_OK):
		# Print to console
		self.print()

		if (sys.platform == "win32"):
			if (type == self.ALERT_WINDOW_OK):
				# Create window with one button Ok
				match ctypes.windll.user32.MessageBoxW(None, self.message(extra = False), title, 0x00000000):
					case 1:
						return self.ALERT_OK

					case 0:
						return self.ALERT_CANCEL


			elif (type == self.ALERT_WINDOW_INPUT):
				# Create window with two buttons Yes and No
				match ctypes.windll.user32.MessageBoxW(None, self.message(extra = False), title, 0x00000004):
					case 6:
						return self.ALERT_YES

					case 7:
						return self.ALERT_NO


			elif (type == self.ALERT_WINDOW_CANCEL):
				# Create window with two buttons Ok and Cancel
				match ctypes.windll.user32.MessageBoxW(None, self.message(extra = False), title, 0x00000001):
					case 1:
						return self.ALERT_OK

					case 2:
						return self.ALERT_CANCEL


			elif (type == self.ALERT_WINDOW_RETRY):
				# Create window with two buttons Retry and Cancel
				match ctypes.windll.user32.MessageBoxW(None, self.message(extra = False), title, 0x00000005):
					case 4:
						return self.ALERT_RETRY

					case 2:
						return self.ALERT_CANCEL


			elif (type == self.ALERT_WINDOW_SCRIPT):
				# Create window with three buttons Abort, Rety, and Ignore
				match ctypes.windll.user32.MessageBoxW(None, self.message(extra = False), title, 0x00000002):
					case 3:
						return self.ALERT_ABORT

					case 4:
						return self.ALERT_RETRY

					case 5:
						return self.ALERT_IGNORE


		return self.ALERT_CANCEL
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~~ Wait ~~~~~~~~~~~~~
	def wait(self, *, secs = None):
		if (secs != None):
			time.sleep(secs)

		else:
			input()

		return self
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Class Methods ~~~~~~~~
	@classmethod
	def TypeError(cls, t:type, level:int = ERROR):
		return RFT_Exception(
			f"Invalid type '{t.__name__}'",
			level
		)


	@classmethod
	def NoValue(cls, level:int = ERROR):
		return RFT_Exception(
			"No value provided",
			level
		)


	@classmethod
	def HasValue(cls, level:int = ERROR):
		return RFT_Exception(
			"Values are not needed",
			level
		)


	@classmethod
	def Traceback(cls, level:int = WARNING):
		return RFT_Exception(
			"\n" + traceback.format_exc().strip(),
			level
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~











