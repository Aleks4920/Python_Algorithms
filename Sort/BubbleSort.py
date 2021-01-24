
def bubble(list):
    indexeingLength = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexeingLength):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
    return list

print(bubble([5,8,6,2,4,9,4,6,2,3,6,1,7]))
