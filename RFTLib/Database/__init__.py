from RFTLib.Require import *
from RFTLib.Core.Object import *
from RFTLib.Core.Serialize import *
from RFTLib.Core.Decorators.call_until import *





__all__=["RFT_Database"]





class RFT_Database(RFT_Object):
	def __init__(self,port):

		# Assign variables
		self.data={}
		self.clients={}

		self.port=port
		self.open=True



		# Create socket
		self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

		# Assign socket timeout
		self.socket.settimeout(1.0)

		# Bind socket
		self.socket.bind(("127.0.0.1",self.port))
		self.socket.listen(1)



		# Start accept client loop
		t=threading.Thread(
			target=self.loop,
			args=(),
			kwargs={},
			daemon=True
		)

		t.start()





	def loop(self):
		while (self.open):
			try:
				# Accept connecting clients
				client,address=self.socket.accept()

			except:
				# Server failed to find new client
				...

			else:
				# Create client id
				addrId=address[0]+":"+str(address[1])
				
				# Get client info
				addrInfo=self.clients.get(addrId,{"connected":False,"address":None,"client":None})


				# If client already connected
				if (addrInfo.get("connected",False)):
					conClient=addrInfo.get("client")

					if (conClient!=None):
						conClient.close()

				else:
					# Temp address info
					self.clients[addrId]=addrInfo


					# Start individual client thread
					t=threading.Thread(
						target=self.accept,
						args=(addrId,),
						kwargs={},
						daemon=True
					)

					t.start()


				# Assign new client info
				addrInfo["connected"]=True
				addrInfo["address"]=address
				addrInfo["client"]=client

				self.clients[addrId]=addrInfo






	def accept(self,addrId):
		while (self.open):
			if (self.clients[addrId].get("connected")):
				...

			else:
				time.sleep(1.0)




