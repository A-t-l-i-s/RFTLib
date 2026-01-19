from RFTLib.Require import *
from RFTLib.Dev.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *
from RFTLib.Core.Exception import *

from RFTLib.Dev.Decorator import *



__all__ = ("RFT_Rypple_Process",)



class RFT_Rypple_Process(RFT_Object):
	def __init__(self, parent):
		self.parent = parent
		self.scope = RFT_Structure({
			"latest": [None, []],
			"popout": False,
			"processes": []
		})



	@RFT_Decorator.configure()
	def run(self, *args:tuple | list):
		args = shlex.split(" ".join(args))

		self.scope.latest[0] = self.run
		self.scope.latest[1] = args

		self.scope.processes.append(
			subprocess.Popen(
				args,
				creationflags = subprocess.CREATE_NEW_CONSOLE if self.scope.popout else 0x00
			)
		)

		return self


	@RFT_Decorator.configure()
	def capture(self, *args:tuple | list):
		args = shlex.split(" ".join(args))

		self.scope.latest[0] = self.capture
		self.scope.latest[1] = args

		result = subprocess.run(
			args,
			text = True,
			capture_output = True,
			creationflags = subprocess.CREATE_NEW_CONSOLE if self.scope.popout else 0x00
		)

		text = ""

		if (result.returncode == 0):
			text += result.stdout.strip()

		return text


	@RFT_Decorator.configure()
	def again(self):
		self.scope.latest[0](*self.scope.latest[1])
		return self


	@RFT_Decorator.configure()
	def wait(self):
		for p in self.scope.processes:
			p.wait()

		self.scope.processes.clear()
		return self


	@RFT_Decorator.configure()
	def kill(self):
		for p in self.scope.processes:
			p.kill()
			p.wait()

		self.scope.processes.clear()
		return self


	@RFT_Decorator.configure()
	def popout(self, value:bool = True):
		self.scope.popout = value
		return self


