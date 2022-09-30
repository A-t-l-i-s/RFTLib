from RFTLib.Require import *
from RFTLib.Core.Object import *

from .Block import *





__all__=["RFT_Volume"]





class RFT_Volume(RFT_Object):



	uuid=None
	stream=None

	blockSize=512

	systemBlock=0
	mappingBlock=1



	def __init__(self,uuid):
		self.uuid=uuid





	def open(self):
		p=f"\\\\?\\Volume{{{self.uuid}}}"


		self.close()
		self.stream=None


		if (ntpath.exists(p)):
			try:
				self.stream=open(p,"rb+")
			except:
				...





	def close(self):
		if (self.isOpen()):
			self.stream.close()





	def isOpen(self):
		if (self.stream!=None and not self.stream.closed):
			return True

		else:
			return False





	def seek(self,count,offset):
		if (self.isOpen()):
			try:
				self.stream.seek(
					count,
					offset
				)

				return True
			except:
				...
		

		return False





	def tell(self):
		if (self.isOpen()):
			pos=self.stream.tell()

		else:
			pos=0

		return pos





	def seekBlock(self,pos):
		return self.seek(
			pos * self.blockSize,
			os.SEEK_SET
		)





	def tellBlock(self):
		return math.floor(
			self.tell() / self.blockSize
		)





	def nextBlock(self):
		return self.seek(
			self.blockSize,
			os.SEEK_CUR
		)





	def prevBlock(self):
		return self.seek(
			-self.blockSize,
			os.SEEK_CUR
		)





	def readBlock(self):
		block=None

		if (self.isOpen()):
			data=self.stream.read(self.blockSize)

			block=RFT_Block(data)


		return block





	def writeBlock(self,block):
		if (self.isOpen()):
			self.stream.write(block.data)






