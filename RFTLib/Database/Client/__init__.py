from RFTLib.Require import *
from RFTLib.Core.Object import *
from RFTLib.Database import *
from RFTLib.Serialize import *





__all__=["RFT_Database_Client"]





class RFT_Database_Client(RFT_Object):



	ip:str="127.0.0.1"
	chunkSize:int=0xffff



	def __init__(self,port:int):
		# Type check
		if (not isinstance(port,int)):
			raise TypeError()



		# Assign variables
		self.port=port
		self.open=True
		self.connected=False



		# Create socket client
		self.socket=socket.socket(
			socket.AF_INET,
			socket.SOCK_STREAM,
			0
		)



		# Start loop
		t=threading.Thread(
			target=self.loop,
			args=(),
			kwargs={},
			daemon=True
		)

		t.start()





	def loop(self):
		while (self.open):
			if (not self.connected):
				self.socket.settimeout(RFT_Database.connectTimeout)

				try:
					self.socket.connect((self.ip,self.port))
					self.connected=True
				except:
					self.connected=False


			else:
				time.sleep(0.1)





	def send(self,data):
		self.socket.settimeout(RFT_Database.dataTimeout)


		try:
			self.socket.send(data)

		except (ConnectionRefusedError,ConnectionResetError):
			self.disconnect()
			return None

		except (TimeoutError):
			return None



		try:
			value=self.socket.recv(RFT_Database.chunkSize)

		except (ConnectionRefusedError,ConnectionResetError):
			self.disconnect()
			return None

		except (TimeoutError):
			return None



		return value





	def disconnect(self):
		self.socket.close()
		self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
		self.connected=False





	def close(self):
		self.socket.close()
		self.open=False




