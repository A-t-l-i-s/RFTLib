from ..Require import *

from .Types import *
from .Object import *
from .Structure import *





__all__ = ("RFT_Json",)





class RFT_Json(RFT_Object):
	class Encoder(json.JSONEncoder):
		def default(self, obj:RFT_Typing.Any) -> dict:
			if (isinstance(obj, RFT_Structure)):
				out = obj.toDict()

			else:
				out = json.JSONEncoder.default(self, obj)


			return out




	class Decoder(json.JSONDecoder):
		def decode(self, obj:RFT_Typing.Any) -> RFT_Typing.Any:
			out = json.JSONDecoder.decode(self, obj)


			return out







	@classmethod
	def dumps(cls, data, **kwargs):
		out = json.dumps(
			data,
			cls = cls.Encoder,
			**kwargs
		)

		buf = out.encode("utf-8")
		return buf



	@classmethod
	def loads(cls, data, **kwargs):
		out = json.loads(
			data,
			cls = RFT_Json.Decoder,
			**kwargs
		)

		struct = RFT_Structure(out)
		return struct










