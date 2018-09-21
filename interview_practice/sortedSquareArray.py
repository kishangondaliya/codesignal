def sortedSquaredArray(array):
    arr = []
    for a in array:
        arr.append(a**2)
    arr = sorted(arr)
    return arr

