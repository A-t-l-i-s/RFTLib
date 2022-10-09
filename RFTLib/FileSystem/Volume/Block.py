from RFTLib.Require import *
from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *





__all__=["RFT_Block"]





class RFT_Block(RFT_Object):



	buffer:np.ndarray=None

	_system:bool=False
	_mapping:bool=False
	_hidden:bool=False
	_encrypted:bool=False
	_compressed:bool=False
	_readonly:bool=False
	_head:bool=False
	_unknown:bool=False



	# ~~~~~~~~~~~~~ Init ~~~~~~~~~~~~~
	def __init__(self,buffer:Union[str,bytes,bytearray]):
		self.buffer=np.fromstring(
			buffer,
			dtype=np.uint8
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~~ Data ~~~~~~~~~~~~~
	@property
	def data(self):
		return self.buffer[5:]



	@data.setter
	def data(self,value):
		self.buffer[5:]=value
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~ Attributes ~~~~~~~~~~
	@property
	def attributes(self):
		# Get block bits
		bits=self.buffer[0]


		# Set attrs
		attrs={
			"system":			(bits & (1 << 0))!=0,
			"mapping":			(bits & (1 << 1))!=0,
			"hidden":			(bits & (1 << 2))!=0,
			"encrypted":		(bits & (1 << 3))!=0,
			"compressed":		(bits & (1 << 4))!=0,
			"readonly":			(bits & (1 << 5))!=0,
			"head":				(bits & (1 << 6))!=0,
			"unknown":			(bits & (1 << 7))!=0,
		}


		return attrs



	@attributes.setter
	def attributes(self,attrs):
		# 0 bits 
		bits=0b00000000


		# Update attrs list by getting current attributes and adding the missing values to attrs
		for k,v in self.attributes.items():
			if (k not in attrs):
				attrs[k]=v


		bits+=(attrs["system"] 			<< 0)
		bits+=(attrs["mapping"] 		<< 1)
		bits+=(attrs["hidden"] 			<< 2)
		bits+=(attrs["encrypted"] 		<< 3)
		bits+=(attrs["compressed"] 		<< 4)
		bits+=(attrs["readonly"] 		<< 5)
		bits+=(attrs["head"] 			<< 6)
		bits+=(attrs["unknown"] 		<< 7)

		self.buffer[0]=bits


	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~ Pointer ~~~~~~~~~~~~
	@property
	def pointer(self):
		return RFT_Buffer.intFromBytes(self.buffer[1:5])



	@pointer.setter
	def pointer(self,value):
		self.buffer[1:5]=RFT_Buffer.intToBytes(value,4)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~ Representation ~~~~~~~~
	def __repr__(self)->repr:
		return repr(self.__str__())



	def __str__(self)->str:
		return "\n".join((
			f"System - {self.system}",
			f"Mapping - {self.mapping}",
			f"Hidden - {self.hidden}",
			f"Encrypted - {self.encrypted}",
			f"Compressed - {self.compressed}",
			f"Read Only - {self.readonly}",
			f"Head - {self.head}",
			f"Unknown - {self.unknown}",
		))
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~









