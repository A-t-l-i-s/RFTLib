from RFTLib.Require import *
from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Serialize import *





__all__=["RFT_Database"]





class RFT_Database(RFT_Object):



	ip:str="127.0.0.1"
	chunkSize:int=0xffff

	dataTimeout:float=6.0
	connectTimeout:float=3.0
	clientTimeout:float=600.0

	CODE_FAILED=b"\x00"
	CODE_SUCCESS=b"\x01"
	CODE_SET=b"\x02"
	CODE_GET=b"\x03"



	def __init__(self,port:int):
		# Type check
		if (not isinstance(port,int)):
			raise TypeError()
		


		# Assign variables
		self.data={}
		self.clients={}

		self.port=port
		self.open=True



		# Create socket
		self.socket=socket.socket(
			socket.AF_INET,
			socket.SOCK_STREAM,
			0
		)

		# Assign socket timeout
		self.socket.settimeout(self.connectTimeout)

		# Bind socket
		self.socket.bind((self.ip,self.port))
		self.socket.listen(1)



		# Start accept client loop
		t=threading.Thread(
			target=self.loop,
			args=(),
			kwargs={},
			daemon=True
		)

		t.start()





	def close(self):
		self.socket.close()
		self.open=False





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

				# Set options for client
				client.settimeout(self.clientTimeout)
				addrInfo["client"]=client

				self.clients[addrId]=addrInfo





	def accept(self,addrId:str):
		while (self.open):
			if (addrId in self.clients):
				# Get currently connected client
				client=self.clients[addrId]["client"]

				try:
					# Receive client data
					data=client.recv(self.chunkSize)

				except:
					# Set client as disconnected
					self.clients[addrId]["connected"]=False

				else:
					if (data):
						# Do stuff with data
						print(data)



			else:
				time.sleep(0.1)






	def __getitem__(self,attr:str):
		if (isinstance(attr,str)):
			data=self.data.get(attr,{})
			
			obj=data.get("value")
			
			if (obj!=None):
				value=RFT_Serialize.deserialize(obj)
			
			return value

		else:
			raise TypeError()



	def __setitem__(self,attr,value):
		if (isinstance(attr,str)):
			value=RFT_Serialize.serialize(value)
			
			data=self.data.get(attr,{})

			data["value"]=value
			data["changed"]=time.time()

			self.data[attr]=data

		else:
			raise TypeError()

