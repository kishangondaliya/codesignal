def sortByHeight(a):
    arr = []
    for i,e in enumerate(a):
        if e == -1:
            arr.append(i)
    a = sorted(a)
    a = a[len(arr):]
    for e in arr:
        a.insert(e, -1)
    return a
