import sys
import math
import time
import random

sys.path.append("..")

from RFTLib.RFT_Graph import *




graph=Graph(256*3,256*2)

window=Window(width=graph.width,height=graph.height,graph=graph)
window.show()




while window.running:


	lo=random.randint(-1800,1800)/10
	la=random.randint(-1800,1800)/10
	

	seed=pairing(lo,la)


	graph.reset()
	window.clearTexts()



	defaultData=list(range(256))
	size=len(defaultData)



	for i,c in enumerate(defaultData):

		shift=math.floor(math.sin((i+1+size)*seed)*256)
		
		h=(c+shift) & 0xFF
		d=(h-shift) & 0xFF


		x=i*(graph.width//size)
		y=h*(graph.height//size)


		if (not isinstance(graph.first,Line)):
			graph.first=Line(x,y)
		

		graph[Line(graph.first.x2,graph.first.y2,x,y)]=Color(i%256+200,100,i%256)


		# window.texts[i]=Text(x,graph.height-y,f"{i}:{h}",Color(100,255,100),"Consolas",8)


		if (not i%5):

			labelColor=Color(255,120,120)
			valueColor=Color(170,120,255)


			window.update(
				{
					"longitude":Text(0,16,"Longitude",labelColor,Text.Arial,16,isBold=True),
					"latitude":Text(0,36,"Latitude",labelColor,Text.Arial,16,isBold=True),
					"seed":Text(0,56,"Seed",labelColor,Text.Arial,16,isBold=True),
					"byte":Text(0,76,"Byte",labelColor,Text.Arial,16,isBold=True),
					"index":Text(0,96,"Index",labelColor,Text.Arial,16,isBold=True),

					"longitude_v":Text(120,16,str(round(lo,2)),valueColor,Text.Arial,16,isBold=True),
					"latitude_v":Text(120,36,str(round(la,2)),valueColor,Text.Arial,16,isBold=True),
					"seed_v":Text(120,56,str(round(seed,2)),valueColor,Text.Arial,16,isBold=True),
					"byte_v":Text(120,76,hex(h),valueColor,Text.Arial,16,isBold=True),
					"index_v":Text(120,96,str(i),valueColor,Text.Arial,16,isBold=True),
				}
			)

	window.pause=True
	window.update()







