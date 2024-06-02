from RFTLib.Require import *





__all__ = ("Entry",)





class Entry:
	def init(self):
		# Import module
		import importlib
		import importlib.util

		self.importlib = importlib



	def load(self, path):
		# Import module spec
		spec = self.importlib.util.spec_from_file_location("script", path)

		# Get module
		mod = self.importlib.util.module_from_spec(spec)

		# Compile module
		spec.loader.exec_module(mod)


		# Return data
		return mod


