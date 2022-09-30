from RFTLib.Require import *
from RFTLib.Core.Object import *
from RFTLib.Core.UUID import *
from RFTLib.FileSystem.Volume import *
from RFTLib.FileSystem.Volume.Block import *





vol=RFT_Volume(RFT_UUID(0x3b18842b,0x0000,0x0000,0x00,0x00,0xd01200000000))
vol.open()



block=vol.readBlock()


print(block.attributes)

block.pointer=0xffffffff
print(block.pointer)


vol.writeBlock(block)



