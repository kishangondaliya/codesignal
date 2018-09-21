def areIsomorphic(array1, array2):
    if len(array1) == len(array2):
        arr1 = [len(i) for i in array1]
        arr2 = [len(i) for i in array2]
        return arr1 == arr2
    return False
