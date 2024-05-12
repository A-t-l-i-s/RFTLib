from RFTLib.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *
from RFTLib.Core.Exception import *

import simplepyble

from .characteristic import *





__all__ = ("RFT_BLE_Peripheral",)





class RFT_BLE_Peripheral(RFT_Object):
	def __init__(self, inst:RFT_Object, address:str = None, timeout:int = 3000):
		# Create variables
		self.inst = inst
		self.device = None
		self.timeout = timeout

		self.running = True


		# Correct address value type
		if (address == None):
			self.address = ""

		elif (isinstance(address, str)):
			self.address = address

		else:
			raise RFT_Exception.TypeError(
				type(self.address)
			)



	# ~~~~~~~~~~ Connection ~~~~~~~~~~
	def connect(self, retries = 1):
		for i in range(retries):
			# Just search for known devices
			if (self.device == None):
				self.find()

			# Then scan for new devices and find again
			if (self.device == None):
				self.inst.scanFor(self.timeout)
				self.find()


			if (self.device != None):
				if (not self.connected()):
					try:
						# Connect to peripheral
						self.device.connect()

						try:
							# Call event
							self.onConnect(self)
						except:
							print(
								RFT_Exception(
									traceback.format_exc(),
									RFT_Exception.INFO
								)
							)

						return True
					except:
						...


			# Wait
			time.sleep(0.1)

		return False



	def connectLoop(self):
		def call():
			while self.running:
				# Connect to device
				self.connect()

		# Start new thread
		threading._start_new_thread(
			call,
			(),
			{}
		)



	def connected(self):
		if (self.device != None):
			return self.device.is_connected()

		return False



	def disconnect(self):
		if (self.device != None):
			self.device.disconnect()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~ Discover ~~~~~~~~~~~
	def find(self):
		for p in self.inst.peripherals:
			if (self.address):
				if (p.address().lower() == self.address.lower() or p.identifier() == self.address):
					self.device = p
					return True

		return False



	def setAddress(self, address):
		# Set new address
		self.address = address

		# Disconnect device
		self.disconnect()

		# Remove device
		self.device = None
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~ Services ~~~~~~~~~~~
	def characteristics(self):
		if (self.connected()):
			for s in self.device.services():
				for c in s.characteristics():
					# Create new char
					char = RFT_BLE_Characteristic()

					# Add peripheral
					char.peripheral = self

					# Add service and char uuid's
					char.service = s.uuid().lower()
					char.uuid = c.uuid().lower()
					char.methods = c.capabilities()

					# Yield new char
					yield char

		return ()



	def addNotify(self, char, callback):
		if (self.connected()):
			if ("notify" in char.methods):
				# Add notif callback to peripheral
				self.device.notify(
					char.service,
					char.uuid,
					callback
				)


			else:
				raise RFT_Exception(
					"Characteristic doesn't support notify",
					RFT_Exception.ERROR
				)
		
		else:
			raise RFT_Exception(
				"No peripheral connected",
				RFT_Exception.ERROR
			)



	def read(self, char):
		if (self.connected()):
			return self.device.read(
				char.service,
				char.uuid
			)

		return None


	def write(self, char, buf:RFT_Buffer):
		if (self.connected()):
			self.device.write_request(
				char.service,
				char.uuid,
				buf.data
			)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
	def onConnect(self, peripheral):
		...
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




