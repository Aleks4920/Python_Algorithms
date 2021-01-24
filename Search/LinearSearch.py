

def Linear(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


print(Linear([5,8,6,2,4,9,4,6,2,3,6,1,7], 10))
