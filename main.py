from RFTLib.Config import *
from RFTLib.Config.qt import *
from RFTLib.Config.cv2 import *
from RFTLib.Config.json import *
from RFTLib.Config.text import *
from RFTLib.Config.toml import *
from RFTLib.Config.yaml import *
from RFTLib.Config.pillow import *
from RFTLib.Config.rypple import *

from RFTLib.Core.Types import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Object import *
from RFTLib.Core.Structure import *

from RFTLib.Saves import *







if (__name__ == "__main__"):
	c = RFT_Config()


	c.scan("./tests/")


	print(c.toDict())




