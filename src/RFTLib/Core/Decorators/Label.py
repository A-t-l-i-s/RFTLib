from ...Require import *





__all__ = ("RFT_Name", "RFT_Description", "RFT_Enabled")





class RFT_Name:
	def __init__(self, value):
		self.value = value


	def __call__(self, obj):
		obj.name = self.value

		return obj





class RFT_Description:
	def __init__(self, value):
		self.value = value


	def __call__(self, obj):
		obj.description = self.value

		return obj





class RFT_Enabled:
	def __init__(self, value):
		self.value = value



	def __call__(self, obj):
		obj.enabled = self.value

		return obj




