from RFTLib.Require import *
from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *

from RFTLib.Core.Graphic.Text import *
from RFTLib.Core.Graphic.Color import *

from RFTLib.Core.Geometric import *
from RFTLib.Core.Geometric.Circle import *
from RFTLib.Core.Geometric.Ellipse import *
from RFTLib.Core.Geometric.Line import *
from RFTLib.Core.Geometric.Nan import *
from RFTLib.Core.Geometric.Point import *
from RFTLib.Core.Geometric.Polygon import *
from RFTLib.Core.Geometric.Rectangle import *

import cv2
import numpy as np





__all__ = ("RFT_Graph",)





class RFT_Graph(RFT_Object):
	def __init__(self, width:int, height:int):
		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.width = width
		self.height = height
		self.channels = 4

		self.flipXAxis = False
		self.flipYAxis = True

		self.data = np.zeros(
			(self.height, self.width, self.channels),
			np.uint8
		)

		self.recentMax = 10
		self.recent = collections.deque(
			maxlen = self.recentMax
		)

		self.reset()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Recent Actions ~~~~~~~~
	@property
	def first(self):
		return self.recent[-1]

	@first.setter
	def first(self,value):
		self.recent[-1] = value



	@property
	def last(self):
		return self.recent[0]

	@last.setter
	def last(self,value):
		self.recent[0] = value
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Methods ~~~~~~~~~~~
	# ~~~~~~~~~ Fill ~~~~~~~~~
	def fill(self, color:RFT_Color):
		self.data[:] = color.toRGBA()

		return self



	# ~~~~~~~~~ Clear ~~~~~~~~
	def clear(self):
		self.data[:] = 0

		return self

	# ~~~~~~~~~ Reset ~~~~~~~~
	def reset(self):
		self.recent += [RFT_Nan()] * self.recentMax
		self.clear()



	# ~~~~~~~~~ Shift ~~~~~~~~
	def shiftX(self, amount:int):
		self.data[:] = np.roll(
			self.data,
			amount,
			True
		)

		return self


	def shiftY(self, amount:int):
		self.data[:] = np.roll(
			self.data,
			amount,
			False
		)

		return self



	# ~~~~~~~~ Random ~~~~~~~~
	def randomX(self):
		return random.randint(0, self.width)


	def randomY(self):
		return random.randint(0, self.height)


	def randomPos(self):
		return RFT_Point((self.randomX(), self.randomY()))
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Drawing ~~~~~~~~~~~
	def drawCircle(self, pos:RFT_Circle, color:RFT_Color):
		self.recent.append(pos)

		cv2.circle(
			self.data,
			(
				round(pos.center.x),
				round(pos.center.y)
			),
			round(pos.radius),
			color.toRGBA(),
			color.thickness
		)


	def drawEllipse(self, pos:RFT_Ellipse, color:RFT_Color):
		self.recent.append(pos)

		cv2.ellipse(
			self.data,
			(
				round(pos.center.x),
				round(pos.center.y)
			),
			(
				round(pos.axis.x),
				round(pos.axis.y)
			),
			round(pos.angle),
			round(pos.startAngle),
			round(pos.endAngle),
			color.toRGBA(),
			color.thickness
		)


	def drawLine(self, pos:RFT_Line, color:RFT_Color):
		self.recent.append(pos)

		cv2.line(
			self.data,
			(
				round(pos.begin.x),
				round(pos.begin.y)
			),
			(
				round(pos.end.x),
				round(pos.end.y)
			),
			color.toRGBA(),
			color.thickness
		)


	def drawPolygon(self, pos:RFT_Polygon, color:RFT_Color):
		self.recent.append(pos)

		if (len(pos.fields) > 0):
			first = pos.fields[0]
			last = pos.fields[-1]

			prev = first

			for k in pos.fields:
				self.drawLine(
					RFT_Line(pos[prev], pos[k]),
					color
				)
				prev = k

			self.drawLine(
				RFT_Line(pos[first], pos[last]),
				color
			)


	def drawRectangle(self, pos:RFT_Rectangle, color:RFT_Color):
		self.recent.append(pos)

		cv2.rectangle(
			self.data,
			(
				round(pos.begin.x),
				round(pos.begin.y)
			),
			(
				round(pos.end.x),
				round(pos.end.y)
			),
			color.toRGBA(),
			color.thickness
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Get/Set Item ~~~~~~~~~
	def __getitem__(self, pos):
		return self.data[pos]



	def __setitem__(self, pos, color:RFT_Color):
		if (isinstance(color, RFT_Color)):
			# If value isnt a tuple then make it one
			if (not isinstance(pos, tuple)):
				pos = (pos,)



			for v in pos:
				if (isinstance(v, RFT_Geometric)):
					if (isinstance(v, RFT_Circle)):
						# Draw circle
						self.drawCircle(v, color)


					elif (isinstance(v, RFT_Ellipse)):
						# Draw ellipse
						self.drawEllipse(v, color)


					elif (isinstance(v, RFT_Line)):
						# Draw line
						self.drawLine(v, color)


					elif (isinstance(v, RFT_Nan)):
						...
						# Draw nothing


					elif (isinstance(v, RFT_Point)):
						# Draw point
						self.data[pos.y, pos.x] = color.toRGBA()


					elif (isinstance(v, RFT_Polygon)):
						# Draw polygon
						self.drawPolygon(v, color)


					elif (isinstance(v, RFT_Rectangle)):
						# Draw rectangle
						self.drawRectangle(v, color)


				else:
					# If not geometry then assume its another method of editing the data
					self.data[v] = color.toRGBA()
		
		else:
			raise TypeError
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



