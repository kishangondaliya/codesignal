def missingNumber(arr):
    arr = sorted(arr)
    i = 0
    for e in arr:
        if e != i:
            return e - 1
        i += 1
    return len(arr)
