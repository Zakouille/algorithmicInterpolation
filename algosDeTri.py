from huepy import *

# Complexité = O(n^2)
def TriInsertion(tableau, *args):
    print('Algorithme utilisé pour trier le nuage de point : ', green("Tri par insertion\n"))
    for i in range(1, len(tableau)):
        j = i - 1
        prochainElement = tableau[i]

        # On compare l'élément actuel avec le prochain
        while (tableau[j] > prochainElement) and (j >= 0):
            tableau[j + 1] = tableau[j]
            j = j - 1
        tableau[j + 1] = prochainElement
    return tableau

# Complexité = O(n^2)
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

# Complexité = O(n^2)
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

# Complexité = O(n log(n))
def TriFusion(tableau, premiereIteration, *args):
    if (premiereIteration == 'true'):
        print('Algorithme utilisé pour trier le nuage de point : ', green("Tri par fusion\n"))

    #print('Tri Fusion du tableau : ',tableau)

    if len(tableau) > 1:
        milieu = len(tableau) // 2
        gauche = tableau[:milieu]
        droite = tableau[milieu:]

        # On fait un appel récursif sur chaque partie du tableau
        TriFusion(gauche, 'false')
        TriFusion(droite, 'false')

        # Deux itérateurs pour traverser respectivement les deux parties du tableau
        i = 0
        j = 0

        # Itérateur pour l'objet tableau principal (Le tableau complet)
        k = 0

        while i < len(gauche) and j < len(droite):
            if gauche[i] < droite[j]:
                # On prend la valeur du tableau gauche
                tableau[k] = gauche[i]
                # On passe à l'élément suivant pour le tableau gauche
                i += 1
            else:
                # On prend la valeur du tableau de droite
                tableau[k] = droite[j]
                # On passe à l'élément suivant pour le tableau de droite
                j += 1
            # On passe à la prochaine case du tableau principal
            k += 1

        # For all the remaining values
        while i < len(gauche):
            tableau[k] = gauche[i]
            i += 1
            k += 1

        while j < len(droite):
            tableau[k] = droite[j]
            j += 1
            k += 1

    return tableau

# Complexité = O(n)
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

# Complexité = O(n^2) ou Theta(n log(n))
def TriRapide(tableau, premiereIteration, debut, fin):
    if (premiereIteration == 'true'):
        print('Algorithme utilisé pour trier le nuage de point : ', green("Tri rapide\n"))

    if debut < fin:
        indexPartition = Partition(tableau, debut, fin)

        # Trier récursivement les éléments du coté droit et gauche et la partition
        TriRapide(tableau, 'false', debut, indexPartition - 1)
        TriRapide(tableau, 'false', indexPartition + 1, fin)
        return tableau

# Complexité = O(n)
def Somme(liste):
    # équivalent de la fonction built-in : sum()
    somme = 0
    for index in range(0, len(liste)):
        somme += liste[index]
    return somme

# Complexité = O(n)
def Zip(x, y):
    # équivalent de la fonction built-in : zip()
    zip = []
    for i in range(len(x)):
        zip.append((x[i], y[i]))
    return zip
