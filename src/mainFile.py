from ast import literal_eval
import argparse
import sortingAlgorithms
import MyInterpollationFunctions
import sympy


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

    print("Expression simplifiée de l'interpollation de Lagrange : ")
    equationDroite = sympy.simplify(lagrangeInterpollation)
    print(equationDroite)

    MyInterpollationFunctions.DessinerGraphe(str(equationDroite), range(0, 10), ListeAbscisse, ListeOrdonnée)

def executerNewton(ListeAbscisse, ListeOrdonnée, point_a_interpoler):
    imagePoint, polynomiale = MyInterpollationFunctions.newtonInterpolation(ListeAbscisse, ListeOrdonnée, point_a_interpoler)
    print("Utilisation de l'interpolation de Newton : ")

    print("La polynomiale déduite est : ", polynomiale)

    print("\nL'image de ", point_a_interpoler, ' est ', imagePoint)

def executerMoindresCarres(ListeAbscisse, ListeOrdonnée):
    result = MyInterpollationFunctions.moindresCarres(ListeAbscisse, ListeOrdonnée)

    print("Utilisation de la méthode des moindres carrées : ")

    equation = str(str(result[0]) + "*x + " + str(result[1]))

    print("\nL'équation linéaire résultante est : ",equation)

    MyInterpollationFunctions.DessinerGraphe(str(equation), (0,10), ListeAbscisse, ListeOrdonnée)

if __name__ == "__main__":
    input = parserInput()
    inputConforme = traiterInput(input)

    donneesTriee = sortingAlgorithms.selectionSort(inputConforme)

    ListeAbscisse = []
    ListeOrdonnée = []

    for couple in donneesTriee:
        ListeAbscisse.append(couple[0])
        ListeOrdonnée.append(couple[1])

    if (input.methode == "lagrange"):
        executerLagrange(ListeAbscisse, ListeOrdonnée)
    elif (input.methode == "newton"):
        executerNewton(ListeAbscisse, ListeOrdonnée, input.pointNewton)
    elif (input.methode == "carres"):
        executerMoindresCarres(ListeAbscisse, ListeOrdonnée)




    # TODO : joli output fichier + test assertion
    # déduire l'équation avec newton

    # print("Début de l'output :\n")

    # print("\nFin de l'output")
