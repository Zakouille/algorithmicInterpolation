import sympy
import matplotlib.pyplot as plt
import numpy as np
import MySortingAlgorithms


def Lagrange(ListeAbscisse, ListeOrdonnee):
    X = sympy.symbols('x')
    expression = 0
    for k in range(len(ListeAbscisse)):
        terme = 1
        for j in range(len(ListeAbscisse)):
            if j != k:
                terme = terme * ((X - ListeAbscisse[j]) / (ListeAbscisse[k] - ListeAbscisse[j]))
        expression += terme * ListeOrdonnee[k]
    return expression


def afficherDifferencesDivisees(tableDiff):
    print("\nTableau des différences divisées :")
    print(tableDiff)

    nombreLigne = (len(tableDiff))
    nombreColonne = (len(tableDiff[0]))

    coefficients = []
    j = 1
    for i in range(0, nombreLigne - 1):
        coefficients.append(tableDiff[i][j])
        j += 1
    coefficients.append(tableDiff[nombreLigne - 1][nombreColonne - 1])

    print("\nNos coefficients sont donc la diagonale du tableau (avant les zéros) : ", coefficients)


def newtonPolynomiale(ListeAbscisse, ListeOrdonnee, tableDiff):
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
    polynomiale = ListeOrdonnee[0]
    for coeff in coefficients[1:]:
        polynomiale += produitsAbscisse[j] * coeff
        j = j + 1

    return polynomiale


def Newton(ListeAbscisse, ListeOrdonnee):
    tableDiff = np.zeros([len(ListeAbscisse), len(ListeAbscisse) + 1], dtype=float)

    for i in range(len(ListeAbscisse)):
        tableDiff[i][0] = ListeAbscisse[i]
        tableDiff[i][1] = ListeOrdonnee[i]

    for i in range(2, len(tableDiff[1])):
        for j in range(i - 1, len(tableDiff[0]) - 1):
            tableDiff[j][i] = (tableDiff[j][i - 1] - tableDiff[j - 1][i - 1]) / (
                    ListeAbscisse[j] - ListeAbscisse[j - i + 1])

    afficherDifferencesDivisees(tableDiff)

    polynomial = newtonPolynomiale(ListeAbscisse, ListeOrdonnee, tableDiff)

    return polynomial


def moindresCarres(ListeAbscisse, ListeOrdonnee):
    taille = len(ListeAbscisse)
    moyenneAbscisse = MySortingAlgorithms.Somme(ListeAbscisse) / taille
    moyenneOrdonnee = MySortingAlgorithms.Somme(ListeOrdonnee) / taille

    variance_x, covariance_x = 0, 0
    for x, y in MySortingAlgorithms.Zip(ListeAbscisse, ListeOrdonnee):
        temp = x - moyenneAbscisse
        variance_x += temp ** 2
        covariance_x += temp * (y - moyenneOrdonnee)

    print("\nCovariance = ", covariance_x, " , Variance = ", variance_x)

    a = covariance_x / variance_x
    print("\na =  covariance / variance = ", covariance_x, " / ", variance_x, " = ", a)
    b = moyenneOrdonnee - a * moyenneAbscisse
    print("\nb = moyenneOrdonnee - a * moyenneAbscisse = ", b)

    X = sympy.symbols('x')
    expression = a * X + b
    return expression


def trapeze(fonction, pointDepart, pointFin, subintervales):
    x = sympy.symbols('x')
    h = float(pointFin - pointDepart) / subintervales
    result = 0.5 * fonction.evalf(subs={x: pointDepart}) + 0.5 * fonction.evalf(subs={x: pointFin})
    for i in range(1, subintervales):
        result += fonction.evalf(subs={x: (pointDepart + i * h)})
    result *= h
    return result


def simpson(fonction, pointDepart, pointFin, subintervales):
    x = sympy.symbols('x')

    h = (pointFin - pointDepart) / subintervales
    s = fonction.evalf(subs={x: pointDepart}) + fonction.evalf(subs={x: pointFin})

    for i in range(1, subintervales, 2):
        s += 4 * fonction.evalf(subs={x: (pointDepart + i * h)})
    for i in range(2, subintervales - 1, 2):
        s += 2 * fonction.evalf(subs={x: (pointDepart + i * h)})

    return s * h / 3


def DessinerGraphe(expression, echelle, ListeAbscisse, ListeOrdonnee):
    plt.scatter(ListeAbscisse, ListeOrdonnee, c='k')
    x = np.array(echelle)
    y = eval(expression)
    plt.plot(x, y, linestyle=':')
    plt.title(str(expression).replace("**", "^"))
    for x, y in zip(ListeAbscisse, ListeOrdonnee):
        plt.text(x, y, ' ({}, {})'.format(x, y))
    plt.show()
