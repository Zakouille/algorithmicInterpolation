import random
import argparse
import algosDeTri
import fonctionsInterpolation
import sympy
from huepy import *

def parserInput():
    parser = argparse.ArgumentParser()

    parser.add_argument("methode", help="Merci de préciser la méthode souhaitée")

    parser.add_argument("data", help="Nuage de points nécessaire pour exécuter le programme."
                                     "Assurez-vous de respecter le format décrit dans la documentation.")

    args = parser.parse_args()
    return args

def traiterInput(input):
    pointsFormatString = input.data.replace('(', '').replace(')', '').replace('"','').replace("'","")
    ListePoints = pointsFormatString.split(';')

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
    lagrangeInterpollation = fonctionsInterpolation.Lagrange(ListeAbscisse, ListeOrdonnee)
    print(lagrangeInterpollation)

    print("\nExpression simplifiée de l'interpollation de Lagrange : ")
    equationDroite = sympy.simplify(lagrangeInterpollation)
    print(green(equationDroite))

    fonctionsInterpolation.DessinerGraphe(str(equationDroite), range(ListeAbscisse[0], 10), ListeAbscisse, ListeOrdonnee)

def executerNewton(ListeAbscisse, ListeOrdonnee):
    print("Utilisation de l'interpolation de Newton : ")

    polynomiale = fonctionsInterpolation.Newton(ListeAbscisse, ListeOrdonnee)

    print("\nPolynomiale non simplifiée :", polynomiale)

    equationSimplifiee = sympy.simplify(polynomiale)

    print("\nLa polynomiale déduite est : ")
    print(green(equationSimplifiee))

    fonctionsInterpolation.DessinerGraphe(str(equationSimplifiee), range(ListeAbscisse[0], 10), ListeAbscisse, ListeOrdonnee)

def executerMoindresCarres(ListeAbscisse, ListeOrdonnee):
    print("Utilisation de la méthode des moindres carrées : ")

    result = fonctionsInterpolation.moindresCarres(ListeAbscisse, ListeOrdonnee)

    equation = sympy.simplify(result)

    print("\nPour un modèle 'ax + b', l'équation linéaire résultante est : ")
    print(green(equation))

    fonctionsInterpolation.DessinerGraphe(str(equation), range(ListeAbscisse[0], 10), ListeAbscisse, ListeOrdonnee)

def executerTrapeze(fonction, ListeAbscisse, range):
    print("Résultat en utilisant la méthode des trapèzes :\n")
    result = fonctionsInterpolation.trapeze(fonction, ListeAbscisse[0], ListeAbscisse[-1], range)
    print("Valeur de l'intégrale allant de x =", ListeAbscisse[0], " à x =", ListeAbscisse[-1], " :")
    print(green(result))

def executerSimpson(fonction, ListeAbscisse, range):
    print("Résultat en utilisant la méthode de Simpson :\n")
    result = fonctionsInterpolation.simpson(fonction, ListeAbscisse[0], ListeAbscisse[-1], range)
    print("Valeur de l'intégrale allant de x =", ListeAbscisse[0], " à x =", ListeAbscisse[-1], " :")
    print(green(result))


if __name__ == "__main__":
    input = parserInput()
    inputConforme = traiterInput(input)

    algosDeTri = [algosDeTri.TriInsertion, algosDeTri.TriBulle,
                  algosDeTri.TriSelection, algosDeTri.TriFusion, algosDeTri.TriRapide]

    donneesTriees = random.choice(algosDeTri)(inputConforme, 'true', 0, len(inputConforme)-1)
    print("Liste des points triée : ", blue(donneesTriees), "\n")

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
        equationFonction = sympy.simplify(fonctionsInterpolation.Lagrange(ListeAbscisse, ListeOrdonnee))
        executerTrapeze(equationFonction, ListeAbscisse, 10)
    elif (input.methode == "simpson"):
        equationFonction = sympy.simplify(fonctionsInterpolation.Lagrange(ListeAbscisse, ListeOrdonnee))
        executerSimpson(equationFonction, ListeAbscisse, 10)
