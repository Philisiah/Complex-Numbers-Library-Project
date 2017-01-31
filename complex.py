import unittest
class Complex(object):
	def __init__(self, real, imag=0.0):
		self.real = real
		self.imag = imag

	def __add__(self, other):
		if isinstance(other, (float, int)):
			other = Complex(other)
		elif not (hasattr(other, 'real') and \
			hasattr(other, 'imag')):
			raise TypeError('other must have real and imag attr.')
		return Complex(self.real + other.real, self.imag + other.imag)

	def __radd__(self, other):
		return self.__add__(other)

	def __sub__(self, other):
		print 'in sub, self=%s, other=%s' % (self, other)
		if isinstance(other, (float, int)):
			other = Complex(other)
		return Complex(self.real - other.real,\
		 self.imag - other.imag)	
	
	def __rsub__(self, other):
		print 'in rsub, self=%s, other=%s' % (self, other)
		if isinstance(other, (float, int)):
			other = Complex(other)
		return other.__sub__(self)

	def __mul__(self, other):
		return Complex(self.real * other.real,\
		 self.imag * other.imag)
	
	def __div__(self, other):
		sr, si, orr, oi = self.real, self.imag, \
		other.real, other.imag
		r = float(orr**2 + oi **2)
		return Complex((sr*orr + si*oi)/r, (si+orr - sr*oi)/r)

	def __abs__(self):
		return sqrt(self.real **2 + self.imag **2)

	def __neg__(self):
		return Complex(-self.real, -self.imag)

	def __eq__(self, other):
		return Complex(self.real == other.real\
		 and self.imag == other.imag)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __str__(self):
		return '(%g, %g)' % (self.real, self.imag)

	def __repr__(self):
		return 'Complex' + str(self)

	def __pow__ (self, power):
		raise NotImplementedError\
			('self ** poweris not yet implemanted for complex')	

	def _illegal(self, op):
		print 'illegal operation "%s" for complex numbers' %op
	
	def __gt__(self, other):
		self._illegal('>')

	def __ge__(self, other):
		self._illegal('>=')

	def __lt__(self, other):
		self._illegal('<')

	def __le__(self, other):
		self._illegal('<=')

	print 'ready for use'
#checklist functions
# ['__abs__', '__add__', '__class__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__eq__',
# '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__'
# , '__init__', '__int__', '__le__', '__long__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__',
# '__nonzero__', '__pos__', '__pow__', '__radd__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__r
# epr__', '__rfloordiv__', '__rmod__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__size
# of__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 'conjugate', 'imag', 'real']