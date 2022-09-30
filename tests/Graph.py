from RFTLib.Require import *
from RFTLib.Graph import *
from RFTLib.Graph.Window import *
from RFTLib.Core.Graphics.Text import *
from RFTLib.Core.Graphics.Color import *

from RFTLib.Core.Geometry.Null import *
from RFTLib.Core.Geometry.Point import *
from RFTLib.Core.Geometry.Velocity import *





if (__name__=="__main__"):
	graph=Graph(800,800)


	win=Window(width=800,height=800,graph=graph)
	win.show()


	pos=Point()
	velocity=Velocity(0.75,0.2)



	while win.running:
		for i in range(1000):

			pos.update(velocity)

			if (pos.x>=graph.width or pos.x<0):
				velocity.xVelocity=-velocity.xVelocity


			if (pos.y>=graph.height or pos.y<0):
				velocity.yVelocity=-velocity.yVelocity



			graph[pos]=Color(i%255,(i//2)%255,(i//2)%255,255)


		win.update()




