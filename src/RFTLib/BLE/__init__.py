from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Structure import *
from RFTLib.Core.Exception import *

import simplepyble

from .peripheral import *
from .characteristic import *





__all__ = ("RFT_BLE", "RFT_BLE_Peripheral", "RFT_BLE_Characteristic")





class RFT_BLE(RFT_Object):
	def __init__(self, address = None):
		self.adapter = None
		self.peripherals = []


		if (simplepyble.Adapter.bluetooth_enabled()):
			for a in simplepyble.Adapter.get_adapters():
				# Get adapter address
				addr = a.address().lower()

				if (addr == str(address).lower() or address == None):
					# Set adapter
					self.adapter = a
					break


			if (self.adapter == None):
				raise RFT_Exception(
					"No adapters available",
					RFT_Exception.ERROR
				)

		else:
			raise RFT_Exception(
				"Bluetooth not enabled",
				RFT_Exception.WARNING
			)


		self.adapter.set_callback_on_scan_start(self._onStart)
		self.adapter.set_callback_on_scan_stop(self._onStop)
		self.adapter.set_callback_on_scan_found(self._onFound)



	# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
	def _onStart(self):
		try:
			self.onStart()
		except:
			...

	def _onStop(self):
		try:
			self.onStop()
		except:
			...

	def _onFound(self, peripheral):
		# Add device to list
		self.peripherals.append(
			peripheral
		)
		
		try:
			self.onFound(peripheral)
		except:
			...



	def onStart(self):
		...

	def onStop(self):
		...

	def onFound(self, peripheral):
		...
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~ Scanning ~~~~~~~~~~~
	def scanStart(self):
		self.adapter.scan_start()


	def scanStop(self):
		self.adapter.scan_stop()


	def scanFor(self, timeout:int):
		self.adapter.scan_for(
			timeout
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



