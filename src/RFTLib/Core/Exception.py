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
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	def __init__(self, obj:str | RFT_Object, level:str = INFO):
		# Set text and level
		self.text = str(obj)
		self.level = level


	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	# ~~~~~~~ Operators ~~~~~~
	def __eq__(self, obj:object) -> bool:
		if (isinstance(obj, RFT_Exception)):
			return obj.text == self.text and obj.level == self.level

		else:
			return obj == self.text


	# ~~~~~~ Containers ~~~~~~
	def __iter__(self) -> iter:
		msg = self.message(extra = False)
		msg = msg.strip()
		return iter(msg.split("\n"))


	# ~~~~~~ Converters ~~~~~~
	def __bool__(self) -> bool:
		return len(self.text) > 0

	def __str__(self, *args, **kwargs) -> str:
		return self.message()

	def __repr__(self) -> str:
		return RFT_Object.__str__(self)

	def __format__(self, fmt:str) -> str:
		return self.text
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Message ~~~~~~~~~~~
	def message(self, *, extra:bool = True) -> str:
		# Get current datetime
		timestamp = datetime.datetime.now()

		# Add extra info to msg
		if (extra):
			msg = f"[{timestamp.hour:>2}:{timestamp.minute:>2}:{str(timestamp.second) + '.' + str(timestamp.microsecond)[:4]:<7}]({self.level}): {self.text}"

		else:
			# Set msg to text
			msg = str(self.text)

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
	def TypeError(cls, type_:type, level:str = ERROR) -> RFT_Object:
		return RFT_Exception(
			f"Invalid type '{type_.__name__}'",
			level
		)


	@classmethod
	def NoValue(cls, level:str = ERROR) -> RFT_Object:
		return RFT_Exception(
			"No value provided",
			level
		)


	@classmethod
	def HasValue(cls, level:str = ERROR) -> RFT_Object:
		return RFT_Exception(
			"Values are not needed",
			level
		)


	@classmethod
	def AttributeError(cls, type_:type, attr:str, level:str = ERROR) -> RFT_Object:
		return RFT_Exception(
			f"'{type_.__name__}' doesn't contain attribute '{attr}'",
			level
		)


	@classmethod
	def IndexError(cls, index:int, level:str = ERROR) -> RFT_Object:
		return RFT_Exception(
			f"Index out of range: {index}",
			level
		)


	@classmethod
	def Traceback(cls, level:str = WARNING) -> RFT_Object:
		return RFT_Exception(
			"\n" + traceback.format_exc().strip(),
			level
		)


	@classmethod
	def NotImplemented(cls, level:str = WARNING) -> RFT_Object:
		return RFT_Exception(
			"Not Implemented",
			level
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~











