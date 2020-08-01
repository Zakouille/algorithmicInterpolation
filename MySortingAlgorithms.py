from huepy import *


def TriInsertion(tableau, *args):
    print('Algorithme utilisé pour trier le nuage de point : ', green("Tri par insersion\n"))
    for i in range(1, len(tableau)):
        j = i - 1
        prochainElement = tableau[i]

        # On compare l'élément actuel avec le prochain
        while (tableau[j] > prochainElement) and (j >= 0):
            tableau[j + 1] = tableau[j]
            j = j - 1
        tableau[j + 1] = prochainElement
    return tableau


def TriBulle(tableau, *args):
    print('Algorithme utilisé pour trier le nuage de point : ', green("Tri par bulle\n"))

    taille = len(tableau)

    # Parcourir tous les éléments du tableau
    # range(taille) marchera dans la première boucle mais avec le -1 on économise une itération qui n'est pas nécessaire
    for i in range(taille - 1):
        for j in range(0, taille - i - 1):

            # Parcourir le tableau de 0 à taille-i-1
            # Swap si l'élément est plus grand que le prochain
            if tableau[j] > tableau[j + 1]:
                tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]
    return tableau


def TriSelection(tableau, *args):
    print('Algorithme utilisé pour trier le nuage de point : ', green("Tri par sélection\n"))

    taille = len(tableau)
    for i in range(taille):
        # Pour la première itération, on assume que le premier élément est le plus petit du tableau non-trié.
        minimum = i

        for j in range(i + 1, taille):
            if (tableau[j] < tableau[minimum]):
                # Mettre à jour la position de l'élément connu le plus petit si un élément inférieur a été trouvé.
                minimum = j

        # Inverser le plus petit élément avec le premier élément de la partie non-triée.
        temp = tableau[i]
        tableau[i] = tableau[minimum]
        tableau[minimum] = temp

    return tableau


def Partition(tableau, debut, fin):
    i = (debut - 1)  # index du plus petit élément
    pivot = tableau[fin]

    for j in range(debut, fin):

        # Si l'élément actuel est plus petit ou égal au pivot
        if tableau[j] <= pivot:
            # On incrémente l'index du plus petit élément
            i += 1
            tableau[i], tableau[j] = tableau[j], tableau[i]

    tableau[i + 1], tableau[fin] = tableau[fin], tableau[i + 1]
    return (i + 1)


def TriRapide(tableau, debut, fin, premiereIteration):
    if (premiereIteration == 'true'):
        print('Algorithme utilisé pour trier le nuage de point : ', green("Tri rapide\n"))
    if debut < fin:
        indexPartition = Partition(tableau, debut, fin)

        # Trier récursivement les éléments du coté droit et gauche et la partition
        TriRapide(tableau, debut, indexPartition - 1, 'false')
        TriRapide(tableau, indexPartition + 1, fin, 'false')
        return tableau
