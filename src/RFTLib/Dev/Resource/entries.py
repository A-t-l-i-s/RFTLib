from RFTLib.Require import *
from RFTLib.Dev.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Exception import *
from RFTLib.Core.Structure import *

from RFTLib.Dev.Decorator import *



__all__ = ("RFT_Resource_Entries",)



class RFT_Resource_Entries(RFT_Object):
	@RFT_Decorator.configure(static = True)
	def JSON(self, file:object) -> RFT_Object:
		# Read file
		dataRaw = json.load(file)

		if (dataRaw is None or isinstance(dataRaw, dict)):
			# Convert to struct
			data = RFT_Structure(dataRaw)

		else:
			data = dataRaw

		# Return data
		return data


	@RFT_Decorator.configure(static = True)
	def YAML(self, file:object) -> RFT_Object:
		import yaml

		# Read file
		dataRaw = yaml.load(
			file,
			Loader = yaml.FullLoader
		)

		if (dataRaw is None or isinstance(dataRaw, dict)):
			# Convert to struct
			data = RFT_Structure(dataRaw)

		else:
			data = dataRaw


		# Return data
		return data


	@RFT_Decorator.configure(static = True)
	def TOML(self, file:object) -> RFT_Object:
		import tomllib

		# Read file
		dataRaw = tomllib.load(file)

		if (dataRaw is None or isinstance(dataRaw, dict)):
			# Convert to struct
			data = RFT_Structure(dataRaw)

		else:
			data = dataRaw


		# Return data
		return data


	@RFT_Decorator.configure(static = True)
	def STRING(self, file:object) -> str:
		# Allocate buffer
		with RFT_Buffer() as buf:
			# Read entire file
			buf += file.read()

			# Return data
			return buf.toStr()


	@RFT_Decorator.configure(static = True)
	def BUFFER(self, file:object) -> RFT_Object:
		# Allocate buffer
		buf = RFT_Buffer()

		# Read entire file
		buf += file.read()

		# Return data
		return buf


	@RFT_Decorator.configure(static = True)
	def PYTHON(self, file:object) -> RFT_Object:
		# Allocate buffer
		buf = RFT_Buffer()
		buf += file.read()

		with RFT_Structure() as struct:
			# Create empty module spec
			spec = importlib.util.spec_from_loader(f"PYTHON_Entry.{uuid.uuid4().hex}", loader = None)

			# Get module
			mod = importlib.util.module_from_spec(spec)

			# Compile module
			exec(buf.data, mod.__dict__)

			# Module dict to scope
			struct += mod.__dict__

		# Return data
		return struct


	@RFT_Decorator.configure(static = True)
	def QT_QIMAGE(self, file:object) -> object:
		from PyQt6.QtGui import QImage

		# Read entire file
		data = file.read()

		# Load as qimage
		img = QImage.fromData(data)

		# Return data
		return img


	@RFT_Decorator.configure(static = True)
	def QT_QPIXMAP(self, file:object) -> object:
		from PyQt6.QtGui import QImage, QPixmap

		# Read entire file
		data = file.read()

		# Load as qimage
		img = QImage.fromData(data)
		pix = QPixmap.fromImage(img)

		# Return data
		return pix


	@RFT_Decorator.configure(static = True)
	def QT_QICON(self, file:object) -> object:
		from PyQt6.QtGui import QImage, QPixmap, QIcon

		# Read entire file
		data = file.read()

		# Allocate icon
		ico = QIcon()

		# Load as qimage
		img = QImage.fromData(data)
		pix = QPixmap.fromImage(img)

		# Add pixmap
		ico.addPixmap(pix)

		# Return data
		return ico


	@RFT_Decorator.configure(static = True)
	def QT_QFONT(self, file:object) -> object:
		from PyQt6.QtGui import QFont, QFontDatabase

		# Read entire file
		data = file.read()

		# Load font data
		uid = QFontDatabase.addApplicationFontFromData(data)

		# Get families
		families = QFontDatabase.applicationFontFamilies(uid)

		return QFont(
			families[0],
			12
		)



