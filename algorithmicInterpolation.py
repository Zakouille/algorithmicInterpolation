import random
from ast import literal_eval
import argparse
import MySortingAlgorithms
import MyInterpolationFunctions
import sympy
from huepy import *

def parserInput():
    parser = argparse.ArgumentParser()

    parser.add_argument("methode", help="Merci de préciser la méthode souhaitée")

    parser.add_argument("data", help="Nuage de points nécessaire pour exécuter le programme."
                                     "Assurez-vous de respecter le format décrit dans la documentation.")

    parser.add_argument("-p", "--pointNewton", help="Point à interpoler en utilisant Newton", type=float, default=2)

    args = parser.parse_args()
    return args

def traiterInput(input):
    pointsFormatString = literal_eval(input.data)
    temp1 = pointsFormatString.replace('(', '')
    temp2 = temp1.replace(')', '')
    ListePoints = temp2.split(';')

    NombreColonnes = 2
    NombreLignes = len(ListePoints)
    resultat = [[0] * NombreColonnes for _ in range(NombreLignes)]

    i = 0
    j = 0
    for couple in ListePoints:
        array = couple.split(',')
        resultat[i][j] = int(array[0])
        resultat[i][j + 1] = int(array[1])
        i = i + 1

    return resultat

def executerLagrange(ListeAbscisse, ListeOrdonnee):
    print("Résultat en utilisant l'interpollation de Lagrange :\n")

    print("Expression complète de l'interpollation de Lagrange: ")
    lagrangeInterpollation = MyInterpolationFunctions.Lagrange(ListeAbscisse, ListeOrdonnee)
    print(lagrangeInterpollation)

    print("\nExpression simplifiée de l'interpollation de Lagrange : ")
    equationDroite = sympy.simplify(lagrangeInterpollation)
    print(green(equationDroite))

    MyInterpolationFunctions.DessinerGraphe(str(equationDroite), range(ListeAbscisse[0], 10), ListeAbscisse, ListeOrdonnee)

def executerNewton(ListeAbscisse, ListeOrdonnee):
    print("Utilisation de l'interpolation de Newton : ")

    polynomiale = MyInterpolationFunctions.Newton(ListeAbscisse, ListeOrdonnee)

    print("\nPolynomiale non simplifiée :", polynomiale)

    equationSimplifiée = sympy.simplify(polynomiale)

    print("\nLa polynomiale déduite est : ")
    print(green(equationSimplifiée))

    MyInterpolationFunctions.DessinerGraphe(str(equationSimplifiée), range(ListeAbscisse[0], 10), ListeAbscisse, ListeOrdonnee)

def executerMoindresCarres(ListeAbscisse, ListeOrdonnee):
    print("Utilisation de la méthode des moindres carrées : ")

    result = MyInterpolationFunctions.moindresCarres(ListeAbscisse, ListeOrdonnee)

    equation = sympy.simplify(result)

    print("\nPour un modèle 'ax + b', l'équation linéaire résultante est : ")
    print(green(equation))

    MyInterpolationFunctions.DessinerGraphe(str(equation), range(ListeAbscisse[0], 10), ListeAbscisse, ListeOrdonnee)

def executerTrapeze(fonction, ListeAbscisse, range):
    print("Résultat en utilisant la méthode des trapèzes :\n")
    result = MyInterpolationFunctions.trapeze(fonction, ListeAbscisse[0], ListeAbscisse[-1], range)
    print("Valeur de l'intégrale allant de x =", ListeAbscisse[0], " à x =", ListeAbscisse[-1], " :")
    print(green(result))

def executerSimpson(fonction, ListeAbscisse, range):
    print("Résultat en utilisant la méthode de Simpson :\n")
    result = MyInterpolationFunctions.simpson(fonction, ListeAbscisse[0], ListeAbscisse[-1], range)
    print("Valeur de l'intégrale allant de x =", ListeAbscisse[0], " à x =", ListeAbscisse[-1], " :")
    print(green(result))


if __name__ == "__main__":
    input = parserInput()
    inputConforme = traiterInput(input)

    algosDeTri = [MySortingAlgorithms.TriInsertion, MySortingAlgorithms.TriBulle,
                  MySortingAlgorithms.TriSelection, MySortingAlgorithms.TriRapide]

    donneesTriees = random.choice(algosDeTri)(inputConforme, 0, len(inputConforme)-1, 'true')
    print("Liste des points triées : ", blue(donneesTriees), "\n")

    ListeAbscisse = []
    ListeOrdonnee = []

    for couple in donneesTriees:
        ListeAbscisse.append(couple[0])
        ListeOrdonnee.append(couple[1])

    if (input.methode == "lagrange"):
        executerLagrange(ListeAbscisse, ListeOrdonnee)
    elif (input.methode == "newton"):
        executerNewton(ListeAbscisse, ListeOrdonnee)
    elif (input.methode == "carres"):
        executerMoindresCarres(ListeAbscisse, ListeOrdonnee)
    elif (input.methode == "trapeze"):
        equationFonction = sympy.simplify(MyInterpolationFunctions.Lagrange(ListeAbscisse, ListeOrdonnee))
        executerTrapeze(equationFonction, ListeAbscisse, 10)
    elif (input.methode == "simpson"):
        equationFonction = sympy.simplify(MyInterpolationFunctions.Lagrange(ListeAbscisse, ListeOrdonnee))
        executerSimpson(equationFonction, ListeAbscisse, 10)




    # TODO : joli output fichier + test assertion avec lib

    # TODO : test install requirements


    # print("Début de l'output :\n")

    # print("\nFin de l'output")
