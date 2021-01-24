
def selection(list):
    indexingLength = range(0, len(list)-1)

    for i in indexingLength:
        minValue = i

        for j in range(i+1, len(list)):
            if list[j] < list[minValue]:
                minValue = j

        if minValue != i:
            list[minValue], list[i] = list[i], list[minValue]

    return list

print(selection([5,8,6,2,4,9,4,6,2,3,6,1,7]))
