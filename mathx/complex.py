''' A class Complex that evaluates operations of complex numbers'''


'''def conv(self):
        #Checks for cases where
        other is not a complex number#
        if isinstance(other, (float, int)):
            other = Complex(other)
        else:
            return False'''


class Complex:

    def __init__(self, rl=0, img=0.0):
        self.rl = rl
        self.img = img

    def __add__(self, other):
        '''modifies the __add__ method to control
        the sum of two complex numbers'''
        if isinstance(other, int):
            return Complex(self.rl + other, self.img)
        elif isinstance(other, float):
            return Complex(self.rl + other, self.img)
        else:
            return Complex(self.rl + other.rl,
                           self.img + other.img)

    def __sub__(self, other):
        '''modifies the __sub__ method to control
        the division of two complex numbers'''

        if isinstance(other, int):
            return Complex(self.rl - other, self.img)
        elif isinstance(other, float):
            return Complex(self.rl - other, self.img)
        else:
            return Complex(self.rl - other.rl,
                           self.img - other.img)

    def __div__(self, other):
        '''modifies the __add__ method to control
        the result  of dividing two complex numbers'''
        if isinstance(other, int):
            return Complex(self.rl / other, self.img / other)
        elif isinstance(other, float):
            return Complex(self.rl / other, self.img / other)
        else:
            s = other.rl ** 2 + other.img ** 2
            return Complex(self.rl * other.rl - self.rl * other.img/s
                           + self.rl * other.rl + self.img * other.img/s)

    def __mul__(self, other):
        '''modify the __mul__ method to control
        the product of two or more complex numbers'''
        if isinstance(other, int):
            return Complex(self.rl * other, self.img * other)
        elif isinstance(other, float):
            return Complex(self.rl * other, self.img * other)
        else:
            return Complex(self.rl * other.rl + self.rl
                           * other.rl + self.img *
                           other.rl + self.img * other.img)

    def __str__(self):
        '''returns a printable string of the variables in an object '''
        return '(%g, %g)' % (self.rl, self.img)
