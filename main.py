from RFTLib.Require import *
from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Database import *
from RFTLib.Database.Client import *
from RFTLib.Serialize import *




s=RFT_Database(9999)
s["FUCK_ME"]=False



c=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
c.connect(("127.0.0.1",s.port))



c.send(b"\x00")
d=c.recv(s.chunkSize)
print(d)





