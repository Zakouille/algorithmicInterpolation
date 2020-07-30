import MyInterpollationFunctions
import sympy
import unittest
from sympy.polys.polyfuncs import interpolate


class interpollationTesting(unittest.TestCase):

    def testLagrange(self):
        x = sympy.symbols('x')

        assert sympy.simplify(MyInterpollationFunctions.Lagrange([1, 2, 3], [1, 4, 9])) == x ** 2
        assert sympy.simplify(MyInterpollationFunctions.Lagrange([1, 2, 3], [1, 4, 9])) == interpolate(
            [(1, 1), (2, 4), (3, 9)], x)

    def testNewton(self):
        x = sympy.symbols('x')

        assert sympy.simplify(MyInterpollationFunctions.Newton([3, 5, 7], [-11, 5, 37])) == 2.0 * x ** 2 - 8.0 * x - 5.0

    def testCarres(self):
        x = sympy.symbols('x')

        assert sympy.simplify(MyInterpollationFunctions.moindresCarres([3, 6, 7], [19, 31, 35])) == 4.0 * x + 7.0

    def testTrapeze(self):
        x = sympy.symbols('x')

        assert int(MyInterpollationFunctions.trapeze(x ** 2, 1, 4, 10)) == 21

    def testSimpson(self):
        x = sympy.symbols('x')

        assert int(MyInterpollationFunctions.simpson(x ** 2, 1, 4, 10)) == 21


if __name__ == "__main__":
    unittest.main()
