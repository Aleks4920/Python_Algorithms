# O = n^2 or O = (n)log(n) complexity
#Accending order

def QuickSort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence;
    else:
        pivot = sequence.pop()
    ItemsGreater = []
    ItemsLower = []

    for item in sequence:
        if item > pivot:
            ItemsGreater.append(item)
        else:
            ItemsLower.append(item)
    return QuickSort(ItemsLower) + [pivot] + QuickSort(ItemsGreater)

#provid input and print output
print(QuickSort([5,7,8,6,2,4,9,4,6,2,3,6,9,1]))
