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

def afficherDifferencesDivisees(table):
    print("Tableau des différences divisées :")
    print(table)

    coefficients = []
    for coeff in table[len(table) - 1]:
        coefficients.append(coeff)

    print("\nNos coefficients sont donc la dernière ligne de notre tableau : ", coefficients)

def newton(ListeAbscisse, ListeOrdonnée, xi):
    table = np.zeros([len(ListeAbscisse), len(ListeAbscisse) + 1], dtype=float)

    for i in range(len(ListeAbscisse)):
        table[i][0] = ListeAbscisse[i]
        table[i][1] = ListeOrdonnée[i]

    for i in range(2, len(table[1])):
        for j in range(i - 1, len(table[0])-1):
            table[j][i] = (table[j][i - 1] - table[j - 1][i - 1]) / (ListeAbscisse[j] - ListeAbscisse[j - i + 1])

    afficherDifferencesDivisees(table)

    imageDeXi = 0
    for i in range(len(table[0])-1):
        tmp = table[i][i + 1]
        for j in range(i):
            tmp *= (xi - ListeAbscisse[j])
        imageDeXi += tmp
    return imageDeXi


def moindresCarres(ListeAbscisse, ListeOrdonnée):
    taille = len(ListeAbscisse)
    moyenneAbscisse = sum(ListeAbscisse) / taille
    moyenneOrdonnée = sum(ListeOrdonnée) / taille

    variance_x, covariance_x = 0, 0
    for x, y in zip(ListeAbscisse, ListeOrdonnée):
        temp = x - moyenneAbscisse
        variance_x += temp ** 2
        covariance_x += temp * (y - moyenneOrdonnée)

    a = covariance_x / variance_x
    b = moyenneOrdonnée - a * moyenneAbscisse
    return (a, b)

def DessinerGraphe(expression, echelle, ListeAbscisse, ListeOrdonnée):
    plt.scatter(ListeAbscisse, ListeOrdonnée, c='k')
    x = np.array(echelle)
    y = eval(expression)
    plt.plot(x, y, linestyle=':')
    plt.title(str(expression).replace("**","^"))
    for x, y in zip(ListeAbscisse, ListeOrdonnée):
        plt.text(x, y, ' ({}, {})'.format(x, y))
    plt.show()
