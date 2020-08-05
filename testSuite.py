#-- coding: utf-8 --

import fonctionsInterpolation
import sympy
import unittest
from sympy.polys.polyfuncs import interpolate
from scipy import integrate




class interpolationTesting(unittest.TestCase):

    def testLagrange(self):
        x = sympy.symbols('x')

        assert sympy.simplify(fonctionsInterpolation.Lagrange([1, 2, 3], [1, 4, 9])) == x ** 2
        assert sympy.simplify(fonctionsInterpolation.Lagrange([1, 2, 3], [1, 4, 9])) == interpolate(
            [(1, 1), (2, 4), (3, 9)], x)

    def testNewton(self):
        x = sympy.symbols('x')

        assert sympy.simplify(fonctionsInterpolation.Newton([3, 5, 7], [-11, 5, 37])) == 2.0 * x ** 2 - 8.0 * x - 5.0

    def testCarres(self):
        x = sympy.symbols('x')

        assert sympy.simplify(fonctionsInterpolation.moindresCarres([3, 6, 7], [19, 31, 35])) == 4.0 * x + 7.0

    def testTrapeze(self):
        x = sympy.symbols('x')

        assert int(fonctionsInterpolation.trapeze(x ** 2, 1, 4, 10)) == 21

    def testSimpson(self):
        x = sympy.symbols('x')

        assert int(fonctionsInterpolation.simpson(x ** 2, 1, 4, 10)) == 21


if __name__ == "__main__":
    unittest.main()
