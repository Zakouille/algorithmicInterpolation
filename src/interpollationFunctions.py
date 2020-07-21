import sympy.polys.polyfuncs
import sympy
import matplotlib.pyplot as plt
import numpy as np


def Lagrange(ListeAbscisse, ListeOrdonnée):
    X = sympy.symbols('X')
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
    y = np.array(echelle)
    x = eval(expression)
    plt.plot(x, y)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    ListeAbscisse = [1, -1, 2]
    ListeOrdonnée = [3, 2, -1]


    result=sympy.simplify(Lagrange(ListeAbscisse, ListeOrdonnée))
    print(result)

    DessinerGraphe(str(result), range(-10,10), ListeAbscisse, ListeOrdonnée)
