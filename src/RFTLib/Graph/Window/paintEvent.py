from RFTLib.Require import *

from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter, QColor, QPen, QFont, QImage





__all__ = ("paintEvent",)





def paintEvent(self, event):
	painter = QPainter(self.widget)

	painter.fillRect(
		0, 0,
		self.width, self.height,
		QColor(*self.backgroundColor.toRGBA())
	)



	for g in self.graphs:
		# Convert to QImage
		img = QImage(
			g.data,
			g.width,
			g.height,
			g.width * g.data.shape[2],
			QImage.Format.Format_RGBA8888
		)



		# Define transformation mode
		trans = Qt.TransformationMode.FastTransformation
		if (self.smoothing):
			trans = Qt.TransformationMode.SmoothTransformation


		# Resize image
		img = img.scaled(
			self.width,
			self.height,
			Qt.AspectRatioMode.KeepAspectRatio,
			trans
		)


		# Position offset
		x = abs(img.width() - self.width) // 2
		y = abs(img.height() - self.height) // 2


		# Flip axis
		if (g.flipXAxis):
			painter.translate(self.width, 0)
			painter.scale(-1, 1)

		if (g.flipYAxis):
			painter.translate(0, self.height)
			painter.scale(1, -1)


		# Draw image on canvas
		painter.drawImage(x, y, img)


		# Reset transformation
		painter.resetTransform()





	if (self.displayText):
		for v in self.texts:
			# Pen object
			pen = QPen()

			# Pen foreground color
			pen.setColor(
				QColor(
					*v.color.toRGBA()
				)
			)

			# Add pen to painter
			painter.setPen(pen)



			# Create font object
			font = QFont()

			# Set font and font size
			font.setFamily(v.font)
			font.setPointSize(v.fontSize)

			# Set font style
			font.setBold(v.isBold)
			font.setItalic(v.isItalic)
			font.setStrikeOut(v.isStrikeOut)
			font.setOverline(v.isOverline)
			font.setUnderline(v.isUnderline)

			# Set painter font
			painter.setFont(font)



			# Draw text to painter object
			painter.drawText(
				round(v.pos.x), round(v.pos.y),
				round(self.width - v.pos.x), round(self.height - v.pos.y),

				Qt.AlignmentFlag.AlignLeft,
				v.text
			)





		if (self.displayFPS):
			# Pen object
			pen = QPen()
			pen.setColor(QColor(255, 255, 255))
			painter.setPen(pen)

			# Font object
			font = QFont()
			font.setFamily("Arial")
			font.setPointSize(14)
			font.setBold(True)
			painter.setFont(font)

			# Draw text to painter
			painter.drawText(
				0, 0,
				self.width, 30,
				Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
				str(
					round(self.fpsCurrent, 2)
				)
			)



