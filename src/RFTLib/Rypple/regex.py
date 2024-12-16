from RFTLib.Require import *
from RFTLib.Core.Object import *
from RFTLib.Core.Structure import *





__all__ = ("RFT_Rypple_Regex",)





class RFT_Rypple_Regex(RFT_Object):
	statementRegex = re.compile(r"^\s*(?P<command>[\w_]+[\w\d_]*)?\s*:\s*(?P<variable>[\w_]+[\w\d_]*)?\s*:\s*(?P<value>.+)?$")


	@classmethod
	def readStatement(self, line):
		if (line):
			if (not line.strip().startswith("#")):
				m = self.statementRegex.match(line)
				
				if (m):
					# Convert to py dict
					d = m.groupdict()

					# Convert to RFT Structure
					statement = RFT_Structure(d)

					return statement




