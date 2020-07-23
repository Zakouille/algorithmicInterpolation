import numpy as np
import MyInterpollationFunctions
import sympy
import unittest
from sympy.polys.polyfuncs import interpolate


class interpollationTesting(unittest.TestCase):

    def testLagrange1(self):
        ListeAbscisse=[1,2,3]
        ListeOrdonnée=[1,4,9]
        x = sympy.symbols('x')

        assert sympy.simplify(MyInterpollationFunctions.Lagrange(ListeAbscisse, ListeOrdonnée)) == x**2
        assert sympy.simplify(MyInterpollationFunctions.Lagrange(ListeAbscisse, ListeOrdonnée)) == interpolate([(1,1), (2,4), (3,9)], x)


if __name__ == "__main__":
    unittest.main()
