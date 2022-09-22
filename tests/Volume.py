import time




p1="\\\\?\\Volume{3b18842b-0000-0000-0000-d01200000000}" # temp
p2="\\\\?\\Volume{3b18842b-0000-0000-0000-101900000000}" # data


file=open(p1,"rb+")



blockSize=512
pos=0

start=time.time()

while (True):
	try:
		d=file.read(blockSize)

		attr=d[0]
		size=int.from_bytes(d[1:3],"big")
		block_pointer=int.from_bytes(d[3:7],"big")
	except:
		break


print(time.time()-start)






"""
512 byte block size

1 byte = attributes
2 bytes = size
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




