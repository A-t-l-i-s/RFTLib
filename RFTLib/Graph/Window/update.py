from RFTLib.Require import *
from RFTLib.Graph import *
from RFTLib.Core.Graphics.Text import *
from RFTLib.Core.Graphics.Color import *





__all__=["update"]





def update(self,texts:Dict[Any,Text]={},graphs:Dict[Any,Graph]={},*,skipRepaint=False,skipPause:bool=False):


	# set texts
	self.texts.update(texts)
	

	# set graphs
	self.graphs.update(graphs)




	current=time.time() # get current time

	self.fpsFrames.append(current) # append current time

	last=self.fpsFrames[-1] # get last frame
	first=self.fpsFrames[0] # get first frame
	dif=last-first
	
	if (dif):
		self.fps=len(self.fpsFrames)/(last-first) # get difference between frame the first and final frame



	QtApp.processEvents(QEventLoop.AllEvents)

	if (not skipRepaint):
		self.widget.repaint()



	if (not skipPause):
		while self.pause:
			self.update(skipPause=True)



