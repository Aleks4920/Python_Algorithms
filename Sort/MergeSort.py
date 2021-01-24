def merge(a,b):
    c=[]
    IndexA,IndexB = 0,0
    while IndexA<len(a) and IndexB<len(b):
        if a[IndexA]<b[IndexB]:
            c.append(a[IndexA])
            IndexA += 1
        else:
            c.append(b[IndexB])
            IndexB += 1
    if IndexA==len(a):
         c.extend(b[IndexB:])
    else: c.extend(a[IndexA:])
    return c



def MergeSort(a):
    if len(a)<=1:
        return a
    left, right = MergeSort(a[:len(a)/2]), MergeSort(a[len(a)/2:])
    return merge(left,right)

print(MergeSort([1,3,4,5,8,9,3,2,6,5,9,1,2]))
