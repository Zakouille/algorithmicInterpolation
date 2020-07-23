import sympy.polys.polyfuncs
import sympy
import matplotlib.pyplot as plt
import numpy as np


def Lagrange(ListeAbscisse, ListeOrdonnée):
    X = sympy.symbols('x')
    if len(ListeAbscisse) != len(ListeOrdonnée):
        print("Les listes d'abscisses et d'ordonnées en entrée n'ont pas la même longueur")
        return 1
    expression = 0
    for k in range(len(ListeAbscisse)):
        terme = 1
        for j in range(len(ListeAbscisse)):
            if j != k:
                terme = terme * ((X - ListeAbscisse[j]) / (ListeAbscisse[k] - ListeAbscisse[j]))
        expression += terme * ListeOrdonnée[k]
    return expression


def DessinerGraphe(expression, echelle, ListeAbscisse, ListeOrdonnée):
    plt.scatter(ListeAbscisse, ListeOrdonnée, c='k')
    x = np.array(echelle)
    y = eval(expression)
    plt.plot(x, y, linestyle=':')
    plt.show()

