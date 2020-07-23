# def quickSort1(arrayToSort):
#     if len(arrayToSort) <= 1:
#         return arrayToSort
#     else:
#         return quickSort1([x for x in arrayToSort[1:] if x < arrayToSort[0]]) + \
#                [arrayToSort[0]] + \
#                quickSort1([x for x in arrayToSort[1:] if x >= arrayToSort[0]])
#
# def quickSort(arrayToSort):
#      if len(arrayToSort) < 2:
#       return arrayToSort
#      else:
#       pivot = arrayToSort[0]
#
#      lesserThan = [i for i in arrayToSort[1:] if i <= pivot]
#      greaterThan = [i for i in arrayToSort[1:] if i > pivot]
#      return quickSort(lesserThan) + [pivot] + quickSort(greaterThan)


def selectionSort(arrayToSort):
    lenght = len(arrayToSort)
    for i in range(lenght):
        # Pour la première itération, on assume que le premier élément est le plus petit du tableau non-trié.
        minimum = i

        for j in range(i + 1, lenght):
            if (arrayToSort[j] < arrayToSort[minimum]):
                # Mettre à jour la position de l'élément connu le plus petit si un élément inférieur a été trouvé.
                minimum = j

        # Inverser le plus petit élément avec le premier élément de la partie non-triée.
        temp = arrayToSort[i]
        arrayToSort[i] = arrayToSort[minimum]
        arrayToSort[minimum] = temp

    return arrayToSort