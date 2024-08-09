from RFTLib.Require import *

from ..Object import *





__all__ = ("RFT_Geometric",)





class RFT_Geometric(RFT_Object):
	# ~~~~~~~~~~~ Variables ~~~~~~~~~~
	fields = ()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~ Magic Methods ~~~~~~~~
	def __add__(self, val):
		for k in self.fields:
			self[k] = self[k] + val

		return self

	def __radd__(self, val):
		for k in self.fields:
			self[k] = val + self[k]

		return self



	def __sub__(self, val):
		for k in self.fields:
			self[k] = self[k] - val

		return self

	def __rsub__(self, val):
		for k in self.fields:
			self[k] = val - self[k]

		return self



	def __mul__(self, val):
		for k in self.fields:
			self[k] = self[k] * val

		return self

	def __rmul__(self, val):
		for k in self.fields:
			self[k] = val * self[k]

		return self



	def __truediv__(self, val):
		for k in self.fields:
			self[k] = self[k] / val

		return self

	def __rtruediv__(self, val):
		for k in self.fields:
			self[k] = val / self[k]

		return self



	def __floordiv__(self, val):
		for k in self.fields:
			self[k] = self[k] // val

		return self

	def __rfloordiv__(self, val):
		for k in self.fields:
			self[k] = val // self[k]

		return self



	def __mod__(self, val):
		for k in self.fields:
			self[k] = self[k] % val

		return self

	def __rmod__(self, val):
		for k in self.fields:
			self[k] = val % self[k]

		return self



	def __pow__(self, val):
		for k in self.fields:
			self[k] = self[k] ** val

		return self

	def __rpow__(self, val):
		for k in self.fields:
			self[k] = val ** self[k]

		return self



	def __neg__(self):
		for k in self.fields:
			self[k] = -self[k]

		return self

	def __pos__(self):
		for k in self.fields:
			self[k] = +self[k]

		return self



	def __lt__(self, val):
		eqs = []

		for k in self.fields:
			eqs.append(
				self[k] < val
			)

		return all(eqs)

	def __le__(self, val):
		eqs = []

		for k in self.fields:
			eqs.append(
				self[k] <= val
			)

		return all(eqs)

	def __eq__(self, val):
		eqs = []

		for k in self.fields:
			eqs.append(
				self[k] == val
			)

		return all(eqs)

	def __ne__(self, val):
		eqs = []

		for k in self.fields:
			eqs.append(
				self[k] != val
			)

		return all(eqs)

	def __ge__(self, val):
		eqs = []

		for k in self.fields:
			eqs.append(
				self[k] >= val
			)

		return all(eqs)

	def __gt__(self, val):
		eqs = []

		for k in self.fields:
			eqs.append(
				self[k] > val
			)

		return all(eqs)



	def __and__(self, val):
		for k in self.fields:
			self[k] = self[k] & val

		return self

	def __rand__(self, val):
		for k in self.fields:
			self[k] = val & self[k]

		return self



	def __or__(self, val):
		for k in self.fields:
			self[k] = self[k] | val

		return self

	def __ror__(self, val):
		for k in self.fields:
			self[k] = val | self[k]

		return self



	def __xor__(self, val):
		for k in self.fields:
			self[k] = self[k] ^ val

		return self

	def __rxor__(self, val):
		for k in self.fields:
			self[k] = val ^ self[k]

		return self



	def __lshift__(self, val):
		for k in self.fields:
			self[k] = self[k] << val

		return self

	def __rlshift__(self, val):
		for k in self.fields:
			self[k] = val << self[k]

		return self



	def __rshift__(self, val):
		for k in self.fields:
			self[k] = self[k] >> val

		return self

	def __rrshift__(self, val):
		for k in self.fields:
			self[k] = val >> self[k]

		return self



	def __invert__(self):
		for k in self.fields:
			self[k] = ~self[k]

		return self



	def __getitem__(self, key):
		return getattr(self, key)

	def __setitem__(self, key, val):
		return setattr(self, key, val)



	def __len__(self):
		return len(self.fields)

	def __contains__(self, key):
		return (key in self.fields)



	def __iter__(self):
		v = []

		for k in self.fields:
			v.append(
				self[k]
			)

		return iter(v)




	def __round__(self, val = 0):
		for k in self.fields:
			self[k] = round(self[k], val)

		return self
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




