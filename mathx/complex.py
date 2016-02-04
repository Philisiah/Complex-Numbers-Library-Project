''' A class Complex that evaluates operations of complex numbers'''


class Complex(object):

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
    __radd__ = __add__  # reverse add remains the same for

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
    __rsub__ = __sub__

    def __div__(self, other):
        '''modifies the __add__ method to control
        the result  of dividing two complex numbers'''
        if isinstance(other, int):
            return Complex(self.rl / other, self.img / other)
        elif isinstance(other, float):
            return Complex(self.rl / other, self.img / other)
        else:
            s = float(other.rl ** 2 + other.img ** 2)
        return Complex((self.rl * other.rl + self.img * other.img) / s,
                       (self.img * other.rl - self.rl * other.img) / s)

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
    __rmul__ = __mul__  # reverse product remains the same

    def __neg__(self):
        '''this function handles
         computations where one operand is negative'''
        return Complex(-self.rl, -self.img)

    def __ne__(self, other):
        '''this specifies that conditions for which != will apply'''
        return Complex(self.rl != other.rl, self.img != other.img)

    def __str__(self):
        '''returns a printable string of the variables in an object to user'''
        return '(%g, %g)' % (self.rl, self.img)
