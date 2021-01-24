
def Recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2

        if target == data[mid]:
            return True
        elif target < data[mid]:
            return Recursive(data, target, low, mid-1)
        else:
            return Recursive(data, target, mid+1, high)


print(Recursive([1,2,4,5,6,7,8,9,10], 4, 1, 10))
