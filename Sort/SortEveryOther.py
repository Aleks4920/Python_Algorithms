


def insertion(list):
    listA = list[::2]
    indexingLength = range(1, len(listA))

    for i in indexingLength:
        valueToSort = listA[i]

        while listA[i-1] > valueToSort and i > 0:
            listA[i], list[i-1] = listA[i-1], listA[i]
            i = i - 1

    return listA




print(insertion([5,8,6,2,4,9,4,6,2,3,6,1,7]))
