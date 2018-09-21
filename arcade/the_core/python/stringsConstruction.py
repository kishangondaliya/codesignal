
def stringsConstruction(a, b):
    arr = []
    for i in range(len(a)):
        if a[i] in b:
            arr.append(b.count(a[i])//a.count(a[i]))
        else:
            return 0
    return min(arr)
