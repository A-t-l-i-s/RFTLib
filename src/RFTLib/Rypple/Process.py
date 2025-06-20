from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *
from RFTLib.Core.Exception import *





__all__ = ("RFT_Rypple_Process",)





class RFT_Rypple_Process(RFT_Object):
	popout_:bool = False
	processes_:list = []


	@classmethod
	def run(self, *args:tuple | list):
		if (len(args) == 1):
			args = shlex.split(args[0])

		try:
			# Create new subprocess attached to main process
			process = subprocess.Popen(
				args,
				creationflags = subprocess.CREATE_NEW_CONSOLE if self.popout_ else 0x00
			)
		except:
			RFT_Exception.Traceback(RFT_Exception.ERROR).print()

		else:
			self.processes_.append(
				process
			)

		return self


	@classmethod
	def capture(self, *args:tuple | list, split = False):
		if (len(args) == 1):
			args = shlex.split(args[0])


		try:
			result = subprocess.run(
				args,
				creationflags = subprocess.CREATE_NEW_CONSOLE if self.popout_ else 0x00,
				capture_output = True,
				text = True
			)

		except:
			RFT_Exception.Traceback(RFT_Exception.ERROR).print()

		else:
			if (result.returncode == 0):
				text = result.stdout

				if (text):
					text = text.strip()

					if (split):
						return shlex.split(text)

					else:
						return text


	@classmethod
	def wait(self):
		for p in self.processes_:
			p.wait()

		self.processes_.clear()
		return self


	@classmethod
	def kill(self):
		for p in self.processes_:
			p.kill()
			p.wait()

		self.processes_.clear()
		return self


	@classmethod
	def popout(self, value:bool = True):
		self.popout_ = value
		return self


