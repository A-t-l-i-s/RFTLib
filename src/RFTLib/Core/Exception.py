from RFTLib.Require import *

from .Object import *



__all__ = ("RFT_Exception",)



class RFT_Exception(BaseException, RFT_Object):
	# ~~~~~~~~~~ Error Types ~~~~~~~~~
	LOG = "Log"
	INFO = "Info"
	WARNING = "Warning"
	ERROR = "Error"
	CRITICAL = "Critical"
	WILDCARD = "*"

	FORMAT = "[{timestamp}]({status}): {text}"
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	def __init__(self, obj:str | RFT_Object, status:str | tuple[str] | list[str] = WILDCARD):
		# Set text and status
		self.text = str(obj)

		if (isinstance(status, list | tuple)):
			self.status = " | ".join(status)

		else:
			self.status = str(status)

		# If RFT_Exception passed
		if (isinstance(obj, RFT_Exception)):
			self.status += f" | {obj.status}"



	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	# ~~~~~~~ Operators ~~~~~~
	def __eq__(self, obj:object) -> bool:
		if (isinstance(obj, RFT_Exception)):
			return obj.text == self.text and obj.status == self.status

		else:
			return obj == self.text


	# ~~~~~~ Containers ~~~~~~
	def __iter__(self) -> iter:
		return iter(self.text.split("\n"))


	# ~~~~~~ Converters ~~~~~~
	def __bool__(self) -> bool:
		return len(self.text) > 0

	def __str__(self, **kwargs:dict) -> str:
		return str(self.text)

	def __format__(self, fmt:str) -> str:
		return self.__str__()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~ Normalize ~~~~~~~~~~
	def normalize(self) -> str:
		return self.message()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Message ~~~~~~~~~~~
	def message(self) -> str:
		# Get current datetime
		timestamp = datetime.datetime.now()

		# Format message
		msg = RFT_Exception.FORMAT.format(
			timestamp = f"{timestamp.hour:>2}:{timestamp.minute:>2}:{str(timestamp.second) + '.' + str(timestamp.microsecond)[:4]:<7}",
			status = self.status,
			text = self.text
		)

		return msg
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~~ Print ~~~~~~~~~~~~
	def print(self, *, end:str = "\n") -> RFT_Object:
		print(self.message(), end = end)
		return self

	def printErr(self, *, end:str = "\n") -> RFT_Object:
		print(self.message(), end = end, file = sys.stderr)
		return self
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Class Methods ~~~~~~~~
	@classmethod
	def TypeError(cls, type_:type, status:str = ERROR) -> RFT_Object:
		return RFT_Exception(
			f"Invalid type '{type_.__name__}'",
			status
		)


	@classmethod
	def NoValue(cls, status:str = ERROR) -> RFT_Object:
		return RFT_Exception(
			"No value provided",
			status
		)


	@classmethod
	def HasValue(cls, status:str = ERROR) -> RFT_Object:
		return RFT_Exception(
			"Values are not needed",
			status
		)


	@classmethod
	def AttributeError(cls, type_:type, attr:str, status:str = ERROR) -> RFT_Object:
		return RFT_Exception(
			f"'{type_.__name__}' doesn't contain attribute '{attr}'",
			status
		)


	@classmethod
	def IndexError(cls, index:int, status:str = ERROR) -> RFT_Object:
		return RFT_Exception(
			f"Index out of range: {index}",
			status
		)


	@classmethod
	def Traceback(cls, status:str = WARNING) -> RFT_Object:
		return RFT_Exception(
			"\n" + traceback.format_exc().strip(),
			status
		)


	@classmethod
	def NotImplemented(cls, status:str = WARNING) -> RFT_Object:
		return RFT_Exception(
			"Not Implemented",
			status
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~











