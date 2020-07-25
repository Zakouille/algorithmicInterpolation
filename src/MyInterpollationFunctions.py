import sympy.polys.polyfuncs
import sympy
import matplotlib.pyplot as plt
import numpy as np
import sortingAlgorithms


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


def afficherDifferencesDivisees(tableDiff):
    print("Tableau des différences divisées :")
    print(tableDiff)

    nombreLigne = (len(tableDiff))
    nombreColonne = (len(tableDiff[0]))

    coefficients = []
    for i in range(nombreLigne - 1):
        for j in range(nombreColonne - 1):
            if (tableDiff[i][j] != 0 and tableDiff[i][j + 1] == 0):
                coefficients.append(tableDiff[i][j])
    coefficients.append(tableDiff[nombreLigne - 1][nombreColonne - 1])

    print("\nNos coefficients sont donc la diagonale du tableau : ", coefficients)


def newtonPolynomiale(ListeAbscisse, ListeOrdonnée, tableDiff):
    nombreLigne = (len(tableDiff))
    nombreColonne = (len(tableDiff[0]))

    coefficients = []
    for i in range(nombreLigne - 1):
        for j in range(nombreColonne - 1):
            if (tableDiff[i][j] != 0 and tableDiff[i][j + 1] == 0):
                coefficients.append(tableDiff[i][j])
    coefficients.append(tableDiff[nombreLigne - 1][nombreColonne - 1])

    X = sympy.symbols('x')
    produit = 1
    produitsAbscisse = []
    for i in range(len(ListeAbscisse)):
        produit *= (X - ListeAbscisse[i])
        produitsAbscisse.append(produit)

    j = 0
    polynomiale = ListeOrdonnée[0]
    for coeff in coefficients[1:]:
        polynomiale += produitsAbscisse[j] * coeff
        j = j + 1
    print(polynomiale)
    return str(sympy.simplify(polynomiale))


def newtonInterpolation(ListeAbscisse, ListeOrdonnée, xi):
    tableDiff = np.zeros([len(ListeAbscisse), len(ListeAbscisse) + 1], dtype=float)

    for i in range(len(ListeAbscisse)):
        tableDiff[i][0] = ListeAbscisse[i]
        tableDiff[i][1] = ListeOrdonnée[i]

    for i in range(2, len(tableDiff[1])):
        for j in range(i - 1, len(tableDiff[0]) - 1):
            tableDiff[j][i] = (tableDiff[j][i - 1] - tableDiff[j - 1][i - 1]) / (ListeAbscisse[j] - ListeAbscisse[j - i + 1])

    afficherDifferencesDivisees(tableDiff)

    polynomial = newtonPolynomiale(ListeAbscisse, ListeOrdonnée, tableDiff)

    imageDeXi = 0
    for i in range(len(tableDiff[0]) - 1):
        tmp = tableDiff[i][i + 1]
        for j in range(i):
            tmp *= (xi - ListeAbscisse[j])
        imageDeXi += tmp
    return imageDeXi, polynomial


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
    plt.title(str(expression).replace("**", "^"))
    for x, y in zip(ListeAbscisse, ListeOrdonnée):
        plt.text(x, y, ' ({}, {})'.format(x, y))
    plt.show()
