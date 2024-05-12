from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Structure import *
from RFTLib.Core.Exception import *

import simplepyble





__all__ = ("RFT_BLE_Characteristic",)





class RFT_BLE_Characteristic(RFT_Object):
	peripheral: RFT_Object = None

	service: str = None
	uuid: str = None
	methods: tuple = None




