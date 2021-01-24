
def insertion(list):
    indexingLength = range(1, len(list))

    for i in indexingLength:
        valueToSort = list[i]

        while list[i-1] > valueToSort and i > 0:
            list[i], list[i-1] = list[i-1], list[i]
            i = i - 1

    return list

print(insertion([5,8,6,2,4,9,4,6,2,3,6,1,7]))
