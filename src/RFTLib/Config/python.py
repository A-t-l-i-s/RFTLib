from ..Require import *

import importlib

from .loader import *
from ..Core.Types import *
from ..Core.Structure import *





__all__ = ("RFT_Config_PYTHON",)





class RFT_Config_PYTHON(RFT_Config_Loader):
	exts = ("py",)



	def load(cls, path:RFT_Typing.Path):
		# Convert to pathlib
		path = Path(path)
		path = path.resolve()


		# Import module spec
		spec = importlib.util.spec_from_file_location("dummy", path)

		# Get module
		module = importlib.util.module_from_spec(spec)


		try:
			# Compile module
			spec.loader.exec_module(module)

		except:
			module = None


		# Return data
		return module

		



