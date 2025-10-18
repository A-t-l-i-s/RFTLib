from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *
from RFTLib.Core.Exception import *





__all__ = ("RFT_Rypple_Process",)





class RFT_Rypple_Process(RFT_Object):
	def __init__(self, parent):
		self.parent = parent
		self.scope = RFT_Structure()
		
		self.scope.latest:list[object, list] = [None, []]
		self.scope.popout:bool = False
		self.scope.processes:list = []



	def run(self, *args:tuple | list):
		args = shlex.split(shlex.join(args))

		self.scope.latest[0] = self.run
		self.scope.latest[1] = args

		self.scope.processes.append(
			subprocess.Popen(
				args,
				creationflags = subprocess.CREATE_NEW_CONSOLE if self.scope.popout else 0x00
			)
		)

		return self


	def capture(self, *args:tuple | list):
		args = shlex.split(shlex.join(args))

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


	def again(self):
		self.scope.latest[0](*self.scope.latest[1])
		return self


	def wait(self):
		for p in self.scope.processes:
			p.wait()

		self.scope.processes.clear()
		return self


	def kill(self):
		for p in self.scope.processes:
			p.kill()
			p.wait()

		self.scope.processes.clear()
		return self


	def popout(self, value:bool = True):
		self.scope.popout = value
		return self


