from RFTLib.Require import *

from RFTLib.Core.Json import *
from RFTLib.Core.Math import *
from RFTLib.Core.Types import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Object import *
from RFTLib.Core.Structure import *

from RFTLib.Core.Gui.Text import *
from RFTLib.Core.Gui.Color import *

from RFTLib.Core.Decorators.Label import *
from RFTLib.Core.Decorators.Structure import *
from RFTLib.Core.Decorators.Threading import *

from RFTLib.Config import *
from RFTLib.Config.qt import *
from RFTLib.Config.cv2 import *
from RFTLib.Config.json import *
from RFTLib.Config.text import *
from RFTLib.Config.toml import *
from RFTLib.Config.yaml import *
from RFTLib.Config.pillow import *
from RFTLib.Config.rypple import *

from RFTLib.Saves import *

from RFTLib.Graph import *
from RFTLib.Graph.nan import *
from RFTLib.Graph.line import *
from RFTLib.Graph.point import *
from RFTLib.Graph.circle import *
from RFTLib.Graph.ellipse import *
from RFTLib.Graph.velocity import *
from RFTLib.Graph.rectangle import *

from RFTLib.Graph.Window import *

from RFTLib.Core.Exceptions import *
from RFTLib.Core.Exceptions.Info import *
from RFTLib.Core.Exceptions.Error import *
from RFTLib.Core.Exceptions.Warning import *
from RFTLib.Core.Exceptions.Critical import *

from RFTLib.Console.Color import *






if (__name__ == "__main__"):
	RFT_Console_Color.init()

	try:
		raise RFT_Exception("UwU")
	except RFT_Exception as e:
		print(e)






