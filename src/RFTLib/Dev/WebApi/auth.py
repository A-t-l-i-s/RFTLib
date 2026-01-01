from RFTLib.Require import *
from RFTLib.Dev.Require import *

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Exception import *
from RFTLib.Core.Structure import *

from RFTLib.Timer import *

from RFTLib.Dev.Logging import *
from RFTLib.Dev.Resource import *
from RFTLib.Dev.Decorator import *

import secrets

from http import HTTPStatus



__all__ = ("RFT_WebApi_Auth",)



class RFT_WebApi_Auth(RFT_Object):
	# ~~~~~~~ Variables ~~~~~~
	tokens = RFT_Structure()

	logger = RFT_Logging()
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	@RFT_Decorator.configure(static = True)
	def newToken(self, *, expires:int | float = None, owner:str = None, length:int = 8):
		token = secrets.token_hex(length)

		self.tokens[token] = RFT_Structure({
			"expires": expires,
			"owner": owner,
			"length": length
		})

		return token


	@RFT_Decorator.configure(static = True)
	def getToken(self, token:str):
		if (self.tokens.contains(token)):
			with self.tokens[token] as struct:
				if (struct.expires is not None):
					if (struct.expires > time.time()):
						return struct

				else:
					return struct


	@RFT_Decorator.configure(static = True)
	def verify(self, model:RFT_Object, request:object):
		if ("token" in request.args):
			# Retrieve token from args
			token = request.args["token"]

			if (token is not None):
				# Convert to string and lowercase it
				token = str(token).lower()

				if (len(token) > 0):
					# Retrieve token (return None is doesn't exist or expired)
					struct = self.getToken(token)

					if (struct is not None):
						# Mark as ok
						model.status = HTTPStatus.OK

						return True

					else:
						model.status = HTTPStatus.UNAUTHORIZED
				else:
					model.status = HTTPStatus.BAD_REQUEST
			else:
				model.status = HTTPStatus.BAD_REQUEST
		else:
			model.status = HTTPStatus.BAD_REQUEST


		return False



