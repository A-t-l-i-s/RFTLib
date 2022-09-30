from RFTLib.Require import *
from RFTLib.Core.Geometry.Null import *
from RFTLib.Core.Graphics.Text import *
from RFTLib.Core.Graphics.Color import *
from RFTLib.Core.Base.BaseGeometry import *





__all__=["Graph"]





class Graph:
	def __init__(self,width:int,height:int):
		self.width=width
		self.height=height

		self.canvas=np.zeros((self.height,self.width,4),np.uint8)

		self.flipXAxis=False
		self.flipYAxis=True

		self.prevMax=10
		self.prevActions=collections.deque(maxlen=self.prevMax)

		self.prevClear()





	def toQImage(self):
		canvas=QImage(
			self.canvas,
			self.width,
			self.height,
			self.width*4,
			QImage.Format_RGBA8888,
		)

		return canvas





	# ~~~~~~~ Previous Actions ~~~~~~~
	@property
	def first(self):
		return self.prevActions[-1]



	@first.setter
	def first(self,value):
		self.prevActions[-1]=value





	@property
	def last(self):
		return self.prevActions[0]



	@last.setter
	def last(self,value):
		self.prevActions[0]=value



	def prevClear(self):
		for i in range(self.prevMax):
			self.prevActions.append(Null())

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





	def fill(self,value):
		self.canvas[:]=value





	def clear(self):
		self.canvas[:]=0





	def reset(self):
		self.clear()
		self.prevClear()





	def shift(self,amount:int,axis:int=0):
		self.canvas[:]=np.roll(
			self.canvas,
			amount,
			axis,
		)





	def save(self,path:str):
		img=cv2.cvtColor(self.canvas,cv2.COLOR_RGBA2BGRA)

		if (self.flipYAxis):
			img=cv2.flip(img,0)

		cv2.imwrite(path,img)





	def __getitem__(self,pos):
		return self.canvas[pos]





	def __setitem__(self,pos,color:Color):
		if (not isinstance(pos,tuple)):
			pos=(pos,)



		for v in pos:
			if (isinstance(v,BaseGeometry)):
				v.draw(self.canvas,color)
				self.prevActions.append(v)

			else:
				raise ValueError(f"Invalid type \"{type(v).__name__}\"")


