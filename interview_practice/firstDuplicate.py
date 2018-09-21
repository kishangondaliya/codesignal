def firstDuplicate(a):
    i = 0
    while i < len(a):
        if a[i] > len(a):
            return -1
        if a[abs(a[i])-1] < 0:
            return abs(a[i])
        else:
            a[abs(a[i])-1] = a[abs(a[i])-1] * -1
        i+=1
    return -1
