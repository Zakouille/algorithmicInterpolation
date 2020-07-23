import numpy as np
import MyInterpollationFunctions
import sympy
import unittest
from sympy.polys.polyfuncs import interpolate


class interpollationTesting(unittest.TestCase):

    def testLagrange(self):
        ListeAbscisse=[1,2,3]
        ListeOrdonnée=[1,8,27]
        x = sympy.symbols('x')
        assert MyInterpollationFunctions.Lagrange(ListeAbscisse, ListeOrdonnée) == interpolate(zip(ListeAbscisse, ListeOrdonnée), x)

if __name__ == "__main__":
    unittest.main()
