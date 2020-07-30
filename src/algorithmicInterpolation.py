import random
from ast import literal_eval
import argparse
import MySortingAlgorithms
import MyInterpollationFunctions
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

def executerLagrange(ListeAbscisse, ListeOrdonnée):
    print("Résultat en utilisant l'interpollation de Lagrange :\n")

    print("Expression complète de l'interpollation de Lagrange: ")
    lagrangeInterpollation = MyInterpollationFunctions.Lagrange(ListeAbscisse, ListeOrdonnée)
    print(lagrangeInterpollation)

    print("\nExpression simplifiée de l'interpollation de Lagrange : ")
    equationDroite = sympy.simplify(lagrangeInterpollation)
    print(green(equationDroite))

    MyInterpollationFunctions.DessinerGraphe(str(equationDroite), range(ListeAbscisse[0], 10), ListeAbscisse, ListeOrdonnée)

def executerNewton(ListeAbscisse, ListeOrdonnée):
    print("Utilisation de l'interpolation de Newton : ")

    polynomiale = MyInterpollationFunctions.Newton(ListeAbscisse, ListeOrdonnée)

    print("\nPolynomiale non simplifiée :", polynomiale)

    equationSimplifiée = sympy.simplify(polynomiale)

    print("\nLa polynomiale déduite est : ")
    print(green(equationSimplifiée))

    MyInterpollationFunctions.DessinerGraphe(str(equationSimplifiée), range(ListeAbscisse[0], 10), ListeAbscisse, ListeOrdonnée)

def executerMoindresCarres(ListeAbscisse, ListeOrdonnée):
    print("Utilisation de la méthode des moindres carrées : ")

    result = MyInterpollationFunctions.moindresCarres(ListeAbscisse, ListeOrdonnée)

    equation = sympy.simplify(result)

    print("\nPour un modèle 'ax + b', l'équation linéaire résultante est : ")
    print(green(equation))

    MyInterpollationFunctions.DessinerGraphe(str(equation), range(ListeAbscisse[0], 10), ListeAbscisse, ListeOrdonnée)

def executerTrapeze(fonction, ListeAbscisse, range):
    print("Résultat en utilisant la méthode des trapèzes :\n")
    result = MyInterpollationFunctions.trapeze(fonction, ListeAbscisse[0], ListeAbscisse[-1], range)
    print("Valeur de l'intégrale allant de x =", ListeAbscisse[0], " à x =", ListeAbscisse[-1], " :")
    print(green(result))

def executerSimpson(fonction, ListeAbscisse, range):
    print("Résultat en utilisant la méthode de Simpson :\n")
    result = MyInterpollationFunctions.simpson(fonction, ListeAbscisse[0], ListeAbscisse[-1], range)
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
    ListeOrdonnée = []

    for couple in donneesTriees:
        ListeAbscisse.append(couple[0])
        ListeOrdonnée.append(couple[1])

    if (input.methode == "lagrange"):
        executerLagrange(ListeAbscisse, ListeOrdonnée)
    elif (input.methode == "newton"):
        executerNewton(ListeAbscisse, ListeOrdonnée)
    elif (input.methode == "carres"):
        executerMoindresCarres(ListeAbscisse, ListeOrdonnée)
    elif (input.methode == "trapeze"):
        equationFonction = sympy.simplify(MyInterpollationFunctions.Lagrange(ListeAbscisse, ListeOrdonnée))
        executerTrapeze(equationFonction, ListeAbscisse, 10)
    elif (input.methode == "simpson"):
        equationFonction = sympy.simplify(MyInterpollationFunctions.Lagrange(ListeAbscisse, ListeOrdonnée))
        executerSimpson(equationFonction, ListeAbscisse, 10)




    # TODO : joli output fichier + test assertion avec lib

    # TODO : test install requirements


    # print("Début de l'output :\n")

    # print("\nFin de l'output")
