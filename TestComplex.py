import unittest
import complex

class TestComplex(unittest.TestCase):
	def testconversion(self):
		u = complex.Complex(2,-1)
		v = complex.Complex(1)
		self.assertEquals(u, 2-1j)
		self.assertEquals(v, 1 + 0j)

	def test_addition(self):
		u = complex.Complex(3,-1)
		v = complex.Complex(2)
		w = u + v
		print w
		self.assertEquals(w, 5 - 1j)
	def test_subtraction(self):
		u = complex.Complex(4,-3)
		v = complex.Complex(2, 5)
		w = u - v
		self.assertEquals(w, 2 - 8j)

if __name__ == '__main__':
	unittest.main()