from ..Require import *





__all__ = ("RFT_Console_Color",)





class RFT_Console_Color:
	initialized:bool = False


	class foreground:
		black = ""
		red = ""
		green = ""
		yellow = ""
		blue = ""
		magenta = ""
		cyan = ""
		white = ""
		reset = ""
		light_black = ""
		light_red = ""
		light_green = ""
		light_yellow = ""
		light_blue = ""
		light_magenta = ""
		light_cyan = ""
		light_white = ""



	class background:
		black = ""
		red = ""
		green = ""
		yellow = ""
		blue = ""
		magenta = ""
		cyan = ""
		white = ""
		reset = ""
		light_black = ""
		light_red = ""
		light_green = ""
		light_yellow = ""
		light_blue = ""
		light_magenta = ""
		light_cyan = ""
		light_white = ""





	@classmethod
	def init(cls):
		if (not cls.initialized):
			# Import colorama
			import colorama

			# Initialize colorama
			colorama.init()


			cls.foreground.black = colorama.Fore.BLACK
			cls.foreground.red = colorama.Fore.RED
			cls.foreground.green = colorama.Fore.GREEN
			cls.foreground.yellow = colorama.Fore.YELLOW
			cls.foreground.blue = colorama.Fore.BLUE
			cls.foreground.magenta = colorama.Fore.MAGENTA
			cls.foreground.cyan = colorama.Fore.CYAN
			cls.foreground.white = colorama.Fore.WHITE
			cls.foreground.reset = colorama.Fore.RESET
			cls.foreground.light_black = colorama.Fore.LIGHTBLACK_EX
			cls.foreground.light_red = colorama.Fore.LIGHTRED_EX
			cls.foreground.light_green = colorama.Fore.LIGHTGREEN_EX
			cls.foreground.light_yellow = colorama.Fore.LIGHTYELLOW_EX
			cls.foreground.light_blue = colorama.Fore.LIGHTBLUE_EX
			cls.foreground.light_magenta = colorama.Fore.LIGHTMAGENTA_EX
			cls.foreground.light_cyan = colorama.Fore.LIGHTCYAN_EX
			cls.foreground.light_white = colorama.Fore.LIGHTWHITE_EX

			cls.background.black = colorama.Back.BLACK
			cls.background.red = colorama.Back.RED
			cls.background.green = colorama.Back.GREEN
			cls.background.yellow = colorama.Back.YELLOW
			cls.background.blue = colorama.Back.BLUE
			cls.background.magenta = colorama.Back.MAGENTA
			cls.background.cyan = colorama.Back.CYAN
			cls.background.white = colorama.Back.WHITE
			cls.background.reset = colorama.Back.RESET
			cls.background.light_black = colorama.Back.LIGHTBLACK_EX
			cls.background.light_red = colorama.Back.LIGHTRED_EX
			cls.background.light_green = colorama.Back.LIGHTGREEN_EX
			cls.background.light_yellow = colorama.Back.LIGHTYELLOW_EX
			cls.background.light_blue = colorama.Back.LIGHTBLUE_EX
			cls.background.light_magenta = colorama.Back.LIGHTMAGENTA_EX
			cls.background.light_cyan = colorama.Back.LIGHTCYAN_EX
			cls.background.light_white = colorama.Back.LIGHTWHITE_EX


			cls.initialized = True





	@classmethod
	def deinit(cls):
		if (cls.initialized):
			colorama.deinit()


			cls.foreground.black = ""
			cls.foreground.red = ""
			cls.foreground.green = ""
			cls.foreground.yellow = ""
			cls.foreground.blue = ""
			cls.foreground.magenta = ""
			cls.foreground.cyan = ""
			cls.foreground.white = ""
			cls.foreground.reset = ""
			cls.foreground.light_black = ""
			cls.foreground.light_red = ""
			cls.foreground.light_green = ""
			cls.foreground.light_yellow = ""
			cls.foreground.light_blue = ""
			cls.foreground.light_magenta = ""
			cls.foreground.light_cyan = ""
			cls.foreground.light_white = ""

			cls.background.black = ""
			cls.background.red = ""
			cls.background.green = ""
			cls.background.yellow = ""
			cls.background.blue = ""
			cls.background.magenta = ""
			cls.background.cyan = ""
			cls.background.white = ""
			cls.background.reset = ""
			cls.background.light_black = ""
			cls.background.light_red = ""
			cls.background.light_green = ""
			cls.background.light_yellow = ""
			cls.background.light_blue = ""
			cls.background.light_magenta = ""
			cls.background.light_cyan = ""
			cls.background.light_white = ""


			cls.initialized = False





	@classmethod
	def format(cls, text:str):
		return text.format(
			foreground = cls.foreground,
			background = cls.background
		)






