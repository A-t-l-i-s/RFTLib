from RFTLib.Require import *
from RFTLib.Graph import *
from RFTLib.Graph.Window import *

from RFTLib.Core.Graphics.Color import *

from RFTLib.Core.Geometry.Rectangle import *

import pyaudio





audio=pyaudio.PyAudio()
stream=audio.open(
	format=pyaudio.paInt16,
	channels=1,
	rate=44100,
	input=True,
	frames_per_buffer=1024,
)



graph=Graph(256*4,256*2)

window=Window(width=graph.width,height=graph.height,graph=graph)
window.show()



spacing=graph.width/256
i=0



while window.running:

	data_=stream.read(1024)
	data=np.frombuffer(data_,np.uint16)
	data=np.resize(data,256)


	for i,c in enumerate(data):
		x=spacing*i
		y=c/32


		if (c>=2**16/2):
			y=0


		graph[Rectangle(x,0,x+spacing,y)]=Color(((i*2)+100) & 0xFF,round(c) & 0xFF,255)


		# window.update(skipRepaint=True)




	graph.first.x2=0
	graph.first.y2=0

	window.update()
	graph.clear()






