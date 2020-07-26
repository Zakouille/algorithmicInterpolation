import numpy as np
import MyInterpollationFunctions
import sympy
import unittest
from sympy.polys.polyfuncs import interpolate


class interpollationTesting(unittest.TestCase):

    def testLagrange(self):
        x = sympy.symbols('x')

        assert sympy.simplify(MyInterpollationFunctions.Lagrange([1,2,3], [1,4,9])) == x**2
        assert sympy.simplify(MyInterpollationFunctions.Lagrange([1,2,3], [1,4,9])) == interpolate([(1,1), (2,4), (3,9)], x)

    def testNewton(self):
        x = sympy.symbols('x')

        assert sympy.simplify(MyInterpollationFunctions.Newton([3,5,7], [-11,5,37])) == 2.0*x**2 - 8.0*x - 5.0


if __name__ == "__main__":
    unittest.main()
