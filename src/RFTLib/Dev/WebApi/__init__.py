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

import socket
import waitress
import mimetypes

from http import HTTPStatus

from flask import (
	Flask,
	request as FlaskRequest,
	Response as FlaskResponse,
	redirect as FlaskRedirect,
	abort as FlaskAbort
)

from werkzeug.exceptions import HTTPException
from werkzeug.middleware.proxy_fix import ProxyFix



__all__ = ("RFT_WebApi",)



class RFT_WebApi(RFT_Object):
	# ~~~~~~~ Variables ~~~~~~
	app = None
	config = RFT_Structure()

	logger = RFT_Logging()

	rules = RFT_Structure()
	rulesInst = RFT_Resource({
		r"py": RFT_Resource.PYTHON_Entry
	})
	# ~~~~~~~~~~~~~~~~~~~~~~~~


	def __init__(self):
		raise RFT_Exception("Class is strictly static.")


	@RFT_Decorator.configure(static = True)
	def init(self, config:RFT_Structure):
		if (self.app is None):
			# Create App
			self.app = Flask(config.name)
			self.app.config.update(config.config)

			self.app.errorhandler(HTTPException)(self.errorHandler)

			# Log that server is good
			self.logger.log("Initialized Server")

			# Fix proxy
			self.app.wsgi_app = ProxyFix(self.app.wsgi_app)

			# Log that proxy is good
			self.logger.log("Initialized Proxy")

			# Override config
			self.config *= config


	@RFT_Decorator.configure(static = True)
	def run(self):
		if (self.app is not None):
			# Log that server is running
			self.logger.log(
				f"Listening on {self.config.host}:{self.config.port}"
			)

			if (self.config.production):
				# Run app in a production server
				waitress.serve(
					self.app,
					host = self.config.host,
					port = self.config.port,
					threads = self.config.threads
				)

			else:
				# Run app in a development server
				self.app.run(
					host = self.config.host,
					port = self.config.port,
					debug = True,
					threaded = True,
					use_reloader = False
				)


	@RFT_Decorator.configure(static = True)
	def load(self, path:str):
		if (self.app is not None):
			for attr, value in self.rulesInst.iterDir(path):
				uid = ".".join(attr)

				# Log error
				log = RFT_Exception(
					"Failed",
					uid
				)

				if (not isinstance(value, RFT_Exception)):
					if (value.contains("Main")):
						main = value.Main

						attrEnd = attr.pop(-1)
						parent = self.rules.allocate(attr)
						parent[attrEnd] = main

						if (issubclass(main, RFT_Object)):
							main.uid = (*attr, attrEnd)

							try:
								# Call init function
								main.init()

								# Wrap function
								func = self.wrapEvent(main.event, uid)

							except:
								# Log error
								self.logger.log(
									RFT_Exception.Traceback(
										(RFT_Exception.ERROR, uid)
									)
								)

							else:
								try:
									# Add rule to app
									self.app.add_url_rule(
										main.path,
										endpoint = main.path,
										view_func = func,
										methods = main.methods
									)

								except:
									# Log error
									self.logger.log(
										RFT_Exception.Traceback(
											(RFT_Exception.ERROR, uid)
										)
									)

								else:
									# Everything works
									log.text = "Success"

				else:
					# Assign log text to exception
					self.logger.log(
						RFT_Exception(
							value,
							uid
						)
					)

				# Print log to console
				self.logger.log(log)


	@RFT_Decorator.configure(static = True)
	def wrapEvent(self, func:object, uid:str):
		def wrapper(*args, **kwargs):
			start = time.time()


			with RFT_Structure({"status": HTTPStatus.OK}) as model:
				response = FlaskResponse()
				response.code = HTTPStatus.OK
				response.headers["Content-Type"] = "application/json; charset=utf-8"
				response.headers["Server"] = f"{self.config.name}/{self.config.version}"

				# Assign log status
				logStatus = (FlaskRequest.remote_addr, uid)

				try:
					# Call function
					c = func(
						model,
						FlaskRequest,
						**kwargs
					)

				except:
					model.status = HTTPStatus.INTERNAL_SERVER_ERROR

					# Log error
					self.logger.log(
						RFT_Exception.Traceback(
							(RFT_Exception.ERROR, *logStatus)
						)
					)

				else:
					if (isinstance(c, int)):
						model.status = c

				finally:
					with RFT_Buffer() as buf:
						try:
							buf += model

						except:
							buf += {
								"status": HTTPStatus.INTERNAL_SERVER_ERROR
							}

							# Log error
							self.logger.log(
								RFT_Exception.Traceback(
									(RFT_Exception.ERROR, *logStatus)
								)
							)


						finally:
							response.set_data(
								buf.toStr()
							)


					# Update log
					self.logger.log(
						RFT_Exception(
							f"{FlaskRequest.endpoint} -> {model.status} [{response.content_length}][{time.time() - start:.2f}ms]",
							logStatus
						)
					)

					# Return response
					return response

		return wrapper


	@RFT_Decorator.configure(static = True)
	def errorHandler(self, event:object):
		with RFT_Structure({"status": event.code}) as model:
			response = FlaskResponse()
			response.code = HTTPStatus.OK
			response.headers["Content-Type"] = "application/json; charset=utf-8"
			response.headers["Server"] = f"{self.config.name}/{self.config.version}"

			with RFT_Buffer() as buf:
				buf += model

				response.set_data(
					buf.toStr()
				)


				# Update log
				self.logger.log(
					RFT_Exception(
						f"{model.status}",
						FlaskRequest.remote_addr
					)
				)

				# Return response
				return response


