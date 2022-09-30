import time
import random




p1="\\\\?\\Volume{3b18842b-0000-0000-0000-d01200000000}" # temp
p2="\\\\?\\Volume{3b18842b-0000-0000-0000-101900000000}" # data


file=open(p1,"rb+")
file.seek(0,0)


start=time.time()


data=None
while (True):
	try:
		data=file.read(512)
		attr=data[0]
		ptr=int.from_bytes(data[1:5],"big")
	except:
		break


print(time.time()-start)



"""
512 byte block size

1 byte = attributes
4 bytes = next chunk, 0 means means eoc

Available bytes per block 505


■ = used block
□ = empty block
● = last block


┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│□   0│□    │□    │□    │□    │□    │□    │□    │□    │□    │
│    0│     │     │     │     │     │     │     │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│□    │□    │□    │□    │□    │□    │□    │□    │□    │□    │
│     │     │     │     │     │     │     │     │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│□    │□    │□    │□    │□    │□    │□    │□    │□    │□    │
│     │     │     │     │     │     │     │     │     │     │
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
"""




