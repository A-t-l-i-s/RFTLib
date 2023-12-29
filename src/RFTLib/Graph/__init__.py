from ..Require import *

import cv2
import numpy as np

from .nan import *
from .geometry import *

from ..Core.Buffer import *
from ..Core.Object import *
from ..Core.Structure import *

from ..Core.Gui.Color import *





__all__ = ("RFT_Graph",)





class RFT_Graph(RFT_Object):
	def __init__(self, width:int, height:int):
		self.width, self.height = width, height

		self.canvas = np.zeros((self.height, self.width, 4), np.uint8)

		self.flipXAxis = False
		self.flipYAxis = True

		self.prevMax = 10
		self.prevActions = collections.deque(maxlen = self.prevMax)

		self.prevClear()





	# ~~~~~~~ Previous Actions ~~~~~~~
	@property
	def first(self):
		return self.prevActions[-1]

	@first.setter
	def first(self,value):
		self.prevActions[-1] = value



	@property
	def last(self):
		return self.prevActions[0]

	@last.setter
	def last(self,value):
		self.prevActions[0] = value



	def prevClear(self):
		for i in range(self.prevMax):
			self.prevActions.append(
				RFT_Graph_NAN()
			)


		return self
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Methods ~~~~~~~~~~~
	def fill(self, color:RFT_Color):
		self.canvas[:] = color.toRGBA()

		return self



	def clear(self):
		self.canvas[:] = 0

		return self



	def reset(self):
		self.clear()
		self.prevClear()

		return self



	def shift(self, amount:int, xAxis:bool = True):
		self.canvas[:] = np.roll(
			self.canvas,
			amount,
			xAxis
		)


		return self




	def randomX(self):
		return random.randint(0, self.width)

	def randomY(self):
		return random.randint(0, self.height)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	def __getitem__(self, pos):
		return self.canvas[pos]



	def __setitem__(self, pos, color:RFT_Color):
		# If value isnt a tuple then make it one
		if (not isinstance(pos, tuple)):
			pos = (pos,)



		for v in pos:
			if (isinstance(v, RFT_Graph_Geometry)):
				try:
					v.draw(self.canvas, color) # Draw on canvas
				
				except NotImplementedError:
					...
				
				else:
					self.prevActions.append(v) # Add action to list of actions

			else:
				# If not geometry then assume its another method of changing canvas
				self.canvas[v] = color
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


