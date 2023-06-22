from ...Require import *
from ...Console.Color import *





__all__ = ("RFT_Exception",)





class RFT_Exception(BaseException):
	def __init__(self, text = ""):
		self.text = text
		self.type = "Exception"





	def message(self):
		# Get current datetime
		now = datetime.datetime.now()

		tmpstmp = f"{now.hour:>2}:{now.minute:>2}:{str(now.second) + '.' + str(now.microsecond)[:4]:<7}"
		msg = "{fg.white}[{fg.reset}{fg.light_cyan}{tmpstmp}{fg.reset}{fg.white}]({fg.reset}{fg.light_blue}{type}{fg.reset}{fg.white}):{fg.reset} {fg.light_white}{text}{fg.reset}".format(
			tmpstmp = tmpstmp,
			type = self.type,
			text = self.text,
			fg = RFT_Console_Color.foreground
		)

		return msg




	def __str__(self):
		return self.message()











