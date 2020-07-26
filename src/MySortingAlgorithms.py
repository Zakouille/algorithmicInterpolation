def TriInsertion(tableau):
    print('Algorithme utilisé pour trié le nuage de point : Tri par insersion\n')
    for i in range(1, len(tableau)):
        j = i - 1
        prochainElement = tableau[i]

        # On compare l'élément actuel avec le prochain
        while (tableau[j] > prochainElement) and (j >= 0):
            tableau[j + 1] = tableau[j]
            j = j - 1
        tableau[j + 1] = prochainElement
    return tableau

def TriBulle(tableau):
    print('Algorithme utilisé pour trié le nuage de point : Tri par bulle\n')

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

def TriSelection(tableau):
    print('Algorithme utilisé pour trié le nuage de point : Tri par sélection\n')

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

def reverse(data_list):
    length = len(data_list)
    s = length

    new_list = [None]*length

    for item in data_list:
        s = s - 1
        new_list[s] = item
    return new_list