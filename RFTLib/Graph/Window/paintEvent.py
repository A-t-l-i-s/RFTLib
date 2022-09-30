from RFTLib.Require import *
from RFTLib.Graph import *
from RFTLib.Core.Graphics.Text import *
from RFTLib.Core.Graphics.Color import *





__all__=["paintEvent"]







def drawGraph(self,graph:Graph,painter:QPainter):
	canvas=graph.toQImage()

	trans=Qt.FastTransformation
	if (self.smooth):
		trans=Qt.SmoothTransformation


	canvas=canvas.scaled(self.width,self.height,Qt.KeepAspectRatio,trans)

	x=abs(canvas.width()-self.width)//2
	y=abs(canvas.height()-self.height)//2


	# reverse x axis
	if (graph.flipXAxis):
		painter.translate(self.width,0)
		painter.scale(-1,1)


	# reverse y axis
	if (graph.flipYAxis):
		painter.translate(0,self.height)
		painter.scale(1,-1)


	painter.drawImage(x,y,canvas)


	# reset transform
	painter.resetTransform()











def paintEvent(self,event):
	painter=QPainter(self.widget)





	painter.fillRect(0,0,self.width,self.height,self.backgroundColor.toQColor()) # fill background



	if (self.graph!=None):
		drawGraph(self,self.graph,painter)





	for k,g in self.graphs.items():
		drawGraph(self,g,painter)





	for k,t in self.texts.items():

		pen=QPen()

		pen.setColor(t.color.toQColor())

		painter.setPen(pen)



		font=QFont()

		font.setFamily(t.font)
		font.setPointSize(t.size)

		font.setBold(t.isBold)
		font.setItalic(t.isItalic)
		font.setStrikeOut(t.isStrikeOut)
		font.setOverline(t.isOverline)
		font.setUnderline(t.isUnderline)
		font.setKerning(t.isKerning)
		font.setFixedPitch(t.isFixedPitch)

		font.setLetterSpacing(QFont.AbsoluteSpacing,t.letterSpacing)
		font.setWordSpacing(t.wordSpacing)

		painter.setFont(font)



		painter.drawText(t.x,t.y,t.text)







	if (self.displayFPS):
		pen=QPen()
		pen.setColor(QColor(255,255,255))
		painter.setPen(pen)

		font=QFont()

		font.setFamily("Arial")
		font.setPointSize(20)

		font.setBold(True)

		painter.setFont(font)

		painter.drawText(QRect(0,0,self.width,30),str(round(self.fps,2)),Qt.AlignRight | Qt.AlignVCenter)





	painter.end()

