def absoluteValuesSumMinimization(a):
    arr = []
    for e in a:
        val = e
        tmp = []
        for j in a:
            tmp.append(abs(val - j))
        arr.append(sum(tmp)) 
    return a[arr.index(min(arr))]
